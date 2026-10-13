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
        Path("docs/fixture").write_text("unmerged human work")
        self.real_run("git", "add", ".")
        self.real_run("git", "commit", "-qm", "human work")
        human = self.real_run("git", "rev-parse", "HEAD")
        self.real_run("git", "push", "-q", "origin", "HEAD:refs/heads/" + maintenance_pr.BRANCH)
        self.real_run("git", "switch", "--detach", self.base)
        self.candidate("not pushed")
        with self.assertRaisesRegex(SystemExit, "human commit"):
            self.invoke()
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/" + maintenance_pr.BRANCH).split()[0], human)


    def test_squash_merged_human_tree_is_preserved_as_ancestor(self):
        self.real_run("git", "switch", "-c", "human")
        Path("docs/fixture").write_text("reviewed work")
        self.real_run("git", "add", ".")
        self.real_run("git", "commit", "-qm", "human review")
        human = self.real_run("git", "rev-parse", "HEAD")
        self.real_run("git", "push", "-q", "origin", "HEAD:refs/heads/" + maintenance_pr.BRANCH)
        self.real_run("git", "switch", "main")
        self.real_run("git", "merge", "--squash", "human")
        self.real_run("git", "commit", "-qm", "squash reviewed work")
        main = self.real_run("git", "rev-parse", "HEAD")
        self.real_run("git", "push", "-q", "origin", "main")
        self.candidate("next candidate")
        self.invoke()
        self.real_run("git", "merge-base", "--is-ancestor", human, "HEAD")
        self.real_run("git", "merge-base", "--is-ancestor", main, "HEAD")
        self.assertEqual(Path("docs/fixture").read_text(), "reviewed work")
        self.assertEqual(Path("docs/upstream-update.md").read_text(), "next candidate")
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/main").split()[0], main)

    def test_bot_tip_cannot_hide_unmerged_human_work(self):
        Path("docs/fixture").write_text("human work")
        self.real_run("git", "add", ".")
        self.real_run("git", "commit", "-qm", "human change")
        self.real_run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        self.real_run("git", "commit", "--allow-empty", "-qm", "bot tip")
        tip = self.real_run("git", "rev-parse", "HEAD")
        self.real_run("git", "push", "-q", "origin", "HEAD:refs/heads/" + maintenance_pr.BRANCH)
        self.real_run("git", "switch", "--detach", self.base)
        self.candidate("not pushed")
        with self.assertRaisesRegex(SystemExit, "human commit"):
            self.invoke()
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/" + maintenance_pr.BRANCH).split()[0], tip)


    def test_concurrent_remote_commit_rejects_push_without_losing_work(self):
        self.candidate("first update")
        self.invoke()
        self.real_run("git", "switch", "main")
        self.candidate("second update")
        normal_command = self.command
        raced = []
        def race(*args):
            if args[:2] == ("git", "push"):
                old = self.real_run("git", "--git-dir", str(self.remote), "rev-parse", maintenance_pr.BRANCH)
                tree = self.real_run("git", "--git-dir", str(self.remote), "rev-parse", old + "^{tree}")
                new = self.real_run("git", "--git-dir", str(self.remote), "-c", "user.name=Human",
                                    "-c", "user.email=human@example.invalid", "commit-tree", tree,
                                    "-p", old, "-m", "concurrent human work")
                self.real_run("git", "--git-dir", str(self.remote), "update-ref", "refs/heads/" + maintenance_pr.BRANCH, new, old)
                raced.append(new)
            return normal_command(*args)
        with patch.dict(os.environ, {"GITHUB_REPOSITORY": "fixture/project", "DEFAULT_BRANCH": "main"}), patch.object(maintenance_pr, "run", side_effect=race):
            with self.assertRaises(subprocess.CalledProcessError):
                maintenance_pr.main()
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/" + maintenance_pr.BRANCH).split()[0], raced[0])
        self.assertEqual(sum(call[1:3] == ("pr", "edit") for call in self.calls), 0)

    def test_active_draft_preserves_human_commit_even_with_equivalent_tree(self):
        self.real_run("git", "commit", "--allow-empty", "-qm", "human review notes")
        human = self.real_run("git", "rev-parse", "HEAD")
        self.real_run("git", "push", "-q", "origin", "HEAD:refs/heads/" + maintenance_pr.BRANCH)
        self.real_run("git", "switch", "--detach", self.base)
        self.prs = [{"number": 1, "isDraft": True}]
        self.candidate("not pushed")
        with self.assertRaisesRegex(SystemExit, "human commit"):
            self.invoke()
        self.assertEqual(self.real_run("git", "ls-remote", "origin", "refs/heads/" + maintenance_pr.BRANCH).split()[0], human)

if __name__ == "__main__":
    unittest.main()
