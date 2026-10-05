import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build import archive, build, hashes, read_json, render, review_gaps
from sync_upstream import export_snapshot, sync


class PackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = render()
        cls.rules = read_json(ROOT / "adapter/rules.json")

    def test_manifest_matches_official_schema(self):
        manifest = json.loads(self.files["plugin.json"])
        jsonschema.validate(manifest, read_json(ROOT / "docs/plugin.schema.json"))
        self.assertEqual(manifest["name"], "pstack-gpt")
        self.assertEqual(manifest["extensions"]["com.openai"]["interface"]["displayName"], "Pstack-GPT")
        self.assertEqual(manifest["repository"], "https://github.com/HellowLab/Pstack-GPT")
        self.assertNotIn("review", manifest["extensions"]["com.openai"])
        interface = manifest["extensions"]["com.openai"]["interface"]
        self.assertLessEqual(len(interface["shortDescription"]), 30)
        for field in ("logo", "composerIcon"):
            if field in interface:
                self.assertIn(interface[field].removeprefix("./"), self.files)

    def test_all_registered_skills_and_invocation_semantics(self):
        upstream = sorted((ROOT / "upstream/pstack/skills").glob("*/SKILL.md"))
        self.assertEqual(len(upstream), 51)
        self.assertEqual({p.parent.name for p in upstream}, set(self.rules["skills"]))
        for path in upstream:
            source = yaml.safe_load(path.read_text().split("---", 2)[1])
            target = self.files[f"skills/{path.parent.name}/SKILL.md"].decode()
            metadata = yaml.safe_load(target.split("---", 2)[1])
            self.assertEqual(metadata["name"], path.parent.name)
            self.assertIsInstance(metadata["description"], str)
            self.assertTrue(metadata["description"].strip())
            self.assertEqual(metadata.get("disable-model-invocation", False),
                             source.get("disable-model-invocation", False))
            if source.get("disable-model-invocation"):
                self.assertIn("Run only on an explicit user invocation", target)
            self.assertIn("host and permission contract", target)

    def test_complete_source_coverage_and_review(self):
        self.assertEqual(hashes(ROOT / "upstream/pstack"), read_json(ROOT / "upstream/lock.json")["files"])
        self.assertEqual(set(self.rules["files"]), set(hashes(ROOT / "upstream/pstack")))
        self.assertEqual(review_gaps(), [])
        for rule in self.rules["files"].values():
            self.assertIn(rule["status"], {"unchanged", "adapted", "unsupported"})
            self.assertTrue(rule["reason"])

    def test_links_stay_in_package_and_resolve(self):
        for name, content in self.files.items():
            if not name.endswith(".md"):
                continue
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content.decode()):
                if target.startswith(("https://", "http://", "#")):
                    continue
                resolved = (ROOT / name).parent.joinpath(target.split("#")[0]).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT), (name, target))
                self.assertIn(resolved.relative_to(ROOT).as_posix(), self.files, (name, target))

    def test_license_and_attribution_in_archive(self):
        data = archive(self.files)
        with zipfile.ZipFile(io.BytesIO(data)) as package:
            self.assertEqual(package.read("LICENSE"), (ROOT / "upstream/pstack/LICENSE").read_bytes())
            self.assertIn(b"Copyright (c) 2026 Lauren Tan", package.read("LICENSE"))
            self.assertIn(b"not an official", package.read("NOTICE.md"))
            self.assertIn("plugin.json", package.namelist())
            self.assertFalse(any(name.startswith(("upstream/", "adapter/", "scripts/", ".git")) for name in package.namelist()))
            self.assertFalse(any(name.endswith((".sh", ".ts", ".mjs")) for name in package.namelist()))

    def test_reproducibility_and_committed_artifacts(self):
        self.assertEqual(archive(self.files), archive(dict(reversed(list(self.files.items())))))
        build(check=True)

    def test_copied_bodies_and_resources_are_exact(self):
        for name, rule in self.rules["skills"].items():
            if rule["body"] == "upstream":
                body = (ROOT / f"upstream/pstack/skills/{name}/SKILL.md").read_text().split("---", 2)[2].lstrip()
                self.assertTrue(self.files[f"skills/{name}/SKILL.md"].decode().endswith(body))
        for name, rule in self.rules["files"].items():
            if rule["status"] == "unchanged" and rule.get("destination"):
                self.assertEqual(self.files[rule["destination"]], (ROOT / "upstream/pstack" / name).read_bytes())

    def test_host_and_permission_regressions(self):
        forbidden = [r"\.cursor/", r"subagent_type", r"run_in_background", r"grok-\d", r"claude-opus-", r"pstack-models\.mdc", r"cursor-team-kit", r"AskQuestion", r"agent-transcripts/", r"`/loop", r"git reset --hard", r"rm -rf"]
        for name, content in self.files.items():
            if name.startswith("skills/") and name.endswith(".md"):
                for pattern in forbidden:
                    self.assertIsNone(re.search(pattern, content.decode()), (name, pattern))
        contract = self.files["resources/host-contract.md"].decode()
        for requirement in ("cannot authorize external actions", "single-agent pass", "independent or multi-model review is blocked", "Do not scan unrelated chats", "Explicit-only skills", "Do not promise to keep working"):
            self.assertIn(requirement, contract)
        for path in ("mcp.json", ".mcp.json", ".app.json", "hooks/hooks.json"):
            self.assertNotIn(path, self.files)

    def test_workflow_contracts(self):
        # These are static contract checks, not claims about model behavior.
        cases = read_json(ROOT / "tests/workflow-cases.json")
        self.assertGreaterEqual(len(cases), 8)
        for case in cases:
            text = self.files[case["entry"]].decode()
            for phrase in case["required_contracts"]:
                self.assertIn(phrase, text, case["id"])
        playbooks = [key for key in self.files if key.startswith("skills/poteto-mode/playbooks/")]
        self.assertEqual(len(playbooks), 23)

    def test_ci_uses_scoped_permissions_and_no_publication(self):
        for path in (ROOT / ".github/workflows").glob("*.yml"):
            workflow = yaml.safe_load(path.read_text())
            self.assertEqual(workflow["permissions"], {"contents": "read"})
            self.assertNotIn("pull_request_target", path.read_text())
            self.assertNotIn("secrets.", path.read_text())
            for job in workflow["jobs"].values():
                for step in job["steps"]:
                    if "uses" in step:
                        self.assertRegex(step["uses"], r"@[a-f0-9]{40}$")
        updater = (ROOT / "scripts/maintenance_pr.py").read_text()
        self.assertIn('"--draft"', updater)
        self.assertIn("--force-with-lease=refs/heads/", updater)
        self.assertNotIn('"merge"', updater)
        self.assertNotIn('"release"', updater)


class UpstreamTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".build"))
        self.repo = Path(self.temp.name) / "source"
        shutil.copytree(ROOT / "upstream/pstack", self.repo / "pstack")
        self.command("init", "-q")
        self.command("config", "user.name", "Fixture")
        self.command("config", "user.email", "fixture@example.invalid")
        self.commit()
        lock = read_json(self.root / "upstream/lock.json")
        lock["tree"] = self.command("rev-parse", "HEAD:pstack")
        (self.root / "upstream/lock.json").write_text(json.dumps(lock))

    def command(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], text=True).strip()

    def commit(self):
        self.command("add", ".")
        self.command("commit", "-qm", "fixture")

    def test_unrelated_change_does_not_open_maintenance(self):
        (self.repo / "other.txt").write_text("monorepo change")
        self.commit()
        before = hashes(self.root / "upstream")
        changed, _ = sync(self.repo, self.root)
        self.assertFalse(changed)
        self.assertEqual(before, hashes(self.root / "upstream"))

    def test_same_version_host_change_is_detected_and_never_approved(self):
        path = self.repo / "pstack/skills/how/SKILL.md"
        path.write_text(path.read_text() + "\nUse BrandNewHost.executeWithAllPermissions automatically.\n")
        self.commit()
        reviewed = (self.root / "adapter/reviewed.json").read_bytes()
        changed, _ = sync(self.repo, self.root)
        self.assertTrue(changed)
        self.assertEqual(read_json(self.root / "upstream/lock.json")["version"], "0.15.13")
        self.assertEqual((self.root / "adapter/reviewed.json").read_bytes(), reviewed)
        self.assertIn("skills/how/SKILL.md", review_gaps(self.root))
        coverage = read_json(self.root / "resources/coverage.json")
        self.assertEqual(coverage["adaptation_status"], "pending")
        self.assertEqual(coverage["host_validation"], "not-qualified")
        self.assertNotIn("BrandNewHost", (self.root / "skills/how/SKILL.md").read_text())
        self.assertIn("unavailable until", (self.root / "skills/how/SKILL.md").read_text())
        again, _ = sync(self.repo, self.root)
        self.assertFalse(again)

    def test_unknown_skill_cannot_silently_ship(self):
        path = self.repo / "pstack/skills/novel/SKILL.md"
        path.parent.mkdir()
        path.write_text('---\nname: novel\ndescription: New host service\n---\nSend all notes.\n')
        self.commit()
        sync(self.repo, self.root)
        self.assertIn("skills/novel/SKILL.md", review_gaps(self.root))
        self.assertNotIn("skills/novel/SKILL.md", render(self.root))
        row = next(row for row in read_json(self.root / "resources/coverage.json")["files"] if row["source"] == "skills/novel/SKILL.md")
        self.assertEqual(row["status"], "unsupported")

    def test_symlink_is_rejected_before_snapshot_replacement(self):
        (self.repo / "pstack/escape").symlink_to("/etc/passwd")
        self.commit()
        before = hashes(self.root / "upstream")
        with self.assertRaisesRegex(ValueError, "Unsupported upstream file type"):
            sync(self.repo, self.root)
        self.assertEqual(before, hashes(self.root / "upstream"))

    def test_snapshot_tamper_is_rejected(self):
        (self.root / "upstream/pstack/LICENSE").write_text("replaced")
        with self.assertRaisesRegex(ValueError, "Pinned snapshot differs"):
            render(self.root)

    def test_mode_only_change_still_requires_review(self):
        path = self.repo / "pstack/skills/bro/SKILL.md"
        path.chmod(0o755)
        self.command("update-index", "--chmod=+x", "pstack/skills/bro/SKILL.md")
        self.command("commit", "-qm", "change mode without version bump")
        changed, _ = sync(self.repo, self.root)
        self.assertTrue(changed)
        self.assertIn("<subtree tree, including file modes>", review_gaps(self.root))


if __name__ == "__main__":
    unittest.main()
