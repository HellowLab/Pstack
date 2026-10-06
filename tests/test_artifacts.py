import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build import ArchiveIntegrityError, build, current_archive, hashes, read_json
from sync_upstream import sync


class ArtifactTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        shutil.copytree(ROOT, self.root,
                        ignore=shutil.ignore_patterns(".git", "__pycache__", "dist"))
        self.set_version("0.0.0-fixture")
        build(self.root)
        self.retained = self.root / current_archive(self.root)
        self.checksum = self.retained.with_name(self.retained.name + ".sha256")
        self.retained_bytes = {path.name: path.read_bytes()
                               for path in (self.retained, self.checksum)}
        self.set_version("0.0.1-fixture")

    def set_version(self, version):
        path = self.root / "plugin.json"
        manifest = read_json(path)
        manifest["version"] = version
        path.write_text(json.dumps(manifest, indent=2) + "\n")

    def assert_retained_bytes(self):
        self.assertEqual({path.name: path.read_bytes()
                          for path in (self.retained, self.checksum)}, self.retained_bytes)

    def source_repo(self):
        repo = Path(self.temp.name) / "source"
        shutil.copytree(self.root / "upstream/pstack", repo / "pstack")

        def git(*args):
            return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()

        git("init", "-q")
        git("config", "user.name", "Fixture")
        git("config", "user.email", "fixture@example.invalid")
        git("add", ".")
        git("commit", "-qm", "fixture")
        lock_path = self.root / "upstream/lock.json"
        lock = read_json(lock_path)
        lock["tree"] = git("rev-parse", "HEAD:pstack")
        lock_path.write_text(json.dumps(lock))
        path = repo / "pstack/skills/how/SKILL.md"
        path.write_text("New incompatible registration format")
        git("add", ".")
        git("commit", "-qm", "incompatible fixture")
        return repo

    def test_version_bump_retains_prior_pair_and_regenerates_current_archive(self):
        zip_name, digest = build(self.root)
        current = self.root / zip_name
        self.assert_retained_bytes()
        self.assertNotEqual(current, self.retained)
        self.assertEqual(hashlib.sha256(current.read_bytes()).hexdigest(), digest)
        current_bytes = current.read_bytes()
        current.write_bytes(b"stale current preview")
        stale = self.root / "skills/removed/SKILL.md"
        stale.parent.mkdir()
        stale.write_text("obsolete generated skill")
        with self.assertRaisesRegex(ValueError, "Generated artifacts differ"):
            build(self.root, check=True)
        self.assertEqual(current.read_bytes(), b"stale current preview")
        self.assertTrue(stale.exists())
        build(self.root)
        self.assertEqual(current.read_bytes(), current_bytes)
        self.assertFalse(stale.exists())
        self.assert_retained_bytes()
        build(self.root, check=True)

    def test_corrupt_retained_pairs_block_build_and_check_before_writes(self):
        build(self.root)
        original = hashes(self.root)
        corruptions = (
            (self.retained, self.retained.read_bytes() + b"tampered"),
            (self.checksum, b"invalid checksum\n"),
            (self.checksum, self.checksum.read_bytes().replace(b"  ", b" ")),
        )
        for path, content in corruptions:
            with self.subTest(path=path.name, content=content[-20:]):
                path.write_bytes(content)
                before = hashes(self.root)
                for check in (False, True):
                    with self.assertRaisesRegex(ArchiveIntegrityError, "Retained archive checksum differs"):
                        build(self.root, check=check)
                    self.assertEqual(hashes(self.root), before)
                path.write_bytes(self.retained_bytes[path.name])
                self.assertEqual(hashes(self.root), original)

    def test_orphan_retained_files_block_build_and_check_without_writes(self):
        build(self.root)
        for path in (self.retained, self.checksum):
            with self.subTest(path=path.name):
                path.unlink()
                before = hashes(self.root)
                for check in (False, True):
                    with self.assertRaisesRegex(ArchiveIntegrityError, "pair is incomplete"):
                        build(self.root, check=check)
                    self.assertEqual(hashes(self.root), before)
                path.write_bytes(self.retained_bytes[path.name])

    def test_unowned_dist_entries_are_rejected_and_preserved(self):
        build(self.root)
        path = self.root / "dist/notes.txt"
        path.write_bytes(b"must not be deleted")
        before = hashes(self.root)
        for check in (False, True):
            with self.assertRaisesRegex(ArchiveIntegrityError, "Unexpected archive entry"):
                build(self.root, check=check)
            self.assertEqual(hashes(self.root), before)

    def test_symlink_current_archive_is_rejected_without_writing_target(self):
        target = Path(self.temp.name) / "external.zip"
        target.write_bytes(b"external bytes")
        current = self.root / current_archive(self.root)
        current.symlink_to(target)
        for check in (False, True):
            with self.assertRaisesRegex(ArchiveIntegrityError, "Unexpected archive entry"):
                build(self.root, check=check)
            self.assertTrue(current.is_symlink())
            self.assertEqual(target.read_bytes(), b"external bytes")
            self.assert_retained_bytes()

    def test_incompatible_sync_invalidates_only_current_archive(self):
        build(self.root)
        repo = self.source_repo()
        changed, summary = sync(repo, self.root)
        self.assertTrue(changed)
        self.assertIn("Generation blocked", summary)
        current = self.root / current_archive(self.root)
        self.assertFalse(current.exists())
        self.assertFalse(current.with_name(current.name + ".sha256").exists())
        self.assert_retained_bytes()
        self.assertIn("No current candidate ZIP is available",
                      (self.root / "docs/upstream-update.md").read_text())
        self.assertEqual((self.root / "upstream/pstack/skills/how/SKILL.md").read_text(),
                         "New incompatible registration format")

    def test_corrupt_retained_archive_blocks_sync_before_snapshot_replacement(self):
        build(self.root)
        repo = self.source_repo()
        self.checksum.write_bytes(b"invalid checksum\n")
        before = hashes(self.root)
        with self.assertRaisesRegex(ArchiveIntegrityError, "Retained archive checksum differs"):
            sync(repo, self.root)
        self.assertEqual(hashes(self.root), before)


if __name__ == "__main__":
    unittest.main()
