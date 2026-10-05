import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import maintenance_pr
from sync_upstream import candidate_tree


class MaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "work"
        self.root.mkdir()
        self.remote = Path(self.temp.name) / "remote.git"
        subprocess.run(["git", "init", "--bare", "-q", str(self.remote)], check=True)
        self.previous = Path.cwd()
        os.chdir(self.root)
        self.addCleanup(os.chdir, self.previous)
        self.real_run = maintenance_pr.run
        self.real_run("git", "init", "-q", "-b", "main")
        self.real_run("git", "config", "user.name", "Fixture")
        self.real_run("git", "config", "user.email", "fixture@example.invalid")
        for folder in ("upstream", "skills", "resources", "dist", "docs"):
            Path(folder).mkdir()
            Path(folder, "fixture").write_text("baseline")
        Path("resources/coverage.json").write_text("{}")
        Path("upstream/pstack").mkdir()
        Path("upstream/pstack/source.md").write_text("canonical source fixture")
        Path("resources/coverage.md").write_text("baseline")
        Path("docs/upstream-update.md").write_text("baseline")
        self.real_run("git", "add", ".")
        self.real_run("git", "commit", "-qm", "baseline")
        self.base = self.real_run("git", "rev-parse", "HEAD")
        self.real_run("git", "remote", "add", "origin", str(self.remote))
        self.real_run("git", "push", "-q", "origin", "main")
        self.prs = []
        self.calls = []
        self.block_create = False

    def command(self, *args):
        if args[0] != "gh":
            return self.real_run(*args)
        self.calls.append(args)
        if args[1:3] == ("pr", "list"):
            return json.dumps(self.prs)
        if args[1:3] == ("pr", "create"):
            if self.block_create:
                raise subprocess.CalledProcessError(1, args)
            self.prs = [{"number": 1, "isDraft": True}]
            return "https://example.invalid/pull/1"
        if args[1:3] == ("pr", "edit"):
            return "updated"
        raise AssertionError(args)

    def candidate(self, content):
        Path("upstream/fixture").write_text(content)
        Path("docs/upstream-update.md").write_text(content)

    def invoke(self, existing_only=False):
        with patch.dict(os.environ, {"GITHUB_REPOSITORY": "fixture/project", "DEFAULT_BRANCH": "main"}), patch.object(maintenance_pr, "run", side_effect=self.command):
            maintenance_pr.main(existing_only=existing_only)

    def test_failed_pr_creation_recovers_without_rewriting_candidate(self):
        self.block_create = True
        self.candidate("candidate report that must survive")
        with self.assertRaisesRegex(SystemExit, "GitHub blocked the PR operation"):
            self.invoke()
        first = self.real_run("git", "rev-parse", "HEAD")
        self.real_run("git", "switch", "main")
        self.block_create = False
        self.invoke(existing_only=True)
        self.assertEqual(self.prs, [{"number": 1, "isDraft": True}])
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/" + maintenance_pr.BRANCH).split()[0], first)
        self.assertEqual(self.real_run("git", "rev-parse", "HEAD"), self.base)
        self.assertIn("candidate report that must survive", Path(".build/maintenance-pr.md").read_text())
        self.invoke(existing_only=True)
        self.assertEqual(sum(call[1:3] == ("pr", "create") for call in self.calls), 2)
        self.assertEqual(sum(call[1:3] == ("pr", "edit") for call in self.calls), 0)

    def test_create_then_update_one_draft_and_preserve_main(self):
        self.candidate("first update")
        self.invoke()
        first = self.real_run("git", "rev-parse", "HEAD")
        self.real_run("git", "switch", "main")
        self.candidate("second update")
        self.invoke()
        second = self.real_run("git", "rev-parse", "HEAD")
        self.assertEqual(candidate_tree(self.root), self.real_run("git", "rev-parse", "HEAD:upstream/pstack"))
        self.assertNotEqual(first, second)
        self.assertEqual(sum(call[1:3] == ("pr", "create") for call in self.calls), 1)
        self.assertEqual(sum(call[1:3] == ("pr", "edit") for call in self.calls), 1)
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/main").split()[0], self.base)
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/" + maintenance_pr.BRANCH).split()[0], second)
        self.assertEqual(Path("docs/upstream-update.md").read_text(), "second update")

    def test_policy_block_keeps_branch_and_reports_error(self):
        self.block_create = True
        self.candidate("update needing manual PR")
        with self.assertRaisesRegex(SystemExit, "GitHub blocked the PR operation"):
            self.invoke()
        self.assertTrue(self.real_run("git", "ls-remote", "origin", "refs/heads/" + maintenance_pr.BRANCH))
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/main").split()[0], self.base)

    def test_ready_pr_is_not_overwritten(self):
        self.prs = [{"number": 1, "isDraft": False}]
        self.candidate("not pushed")
        with self.assertRaisesRegex(SystemExit, "active review"):
            self.invoke()
        self.assertFalse(self.real_run("git", "ls-remote", "origin", "refs/heads/" + maintenance_pr.BRANCH))

    def test_human_owned_branch_is_not_overwritten(self):
        self.real_run("git", "push", "-q", "origin", "HEAD:refs/heads/" + maintenance_pr.BRANCH)
        self.candidate("not pushed")
        with self.assertRaisesRegex(SystemExit, "human commit"):
            self.invoke()
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/" + maintenance_pr.BRANCH).split()[0], self.base)


if __name__ == "__main__":
    unittest.main()
