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
        self.assertEqual(manifest["name"], "pstack")
        self.assertEqual(manifest["extensions"]["com.openai"]["interface"]["displayName"], "Pstack")
        self.assertEqual(manifest["repository"], "https://github.com/HellowLab/Pstack")
        self.assertNotIn("review", manifest["extensions"]["com.openai"])
        interface = manifest["extensions"]["com.openai"]["interface"]
        self.assertLessEqual(len(interface["shortDescription"]), 30)
        self.assertEqual(interface["shortDescription"], "Ship faster. Build better.")
        self.assertLessEqual(len(interface["longDescription"]), 4000)
        self.assertIn("with upstream tracking and reviewed updates", interface["longDescription"])
        self.assertIn("Independently maintained by HellowLab.", interface["longDescription"])
        for field in ("logo", "composerIcon"):
            self.assertEqual(interface[field], "./assets/pstack.jpeg")
            self.assertIn(interface[field].removeprefix("./"), self.files)

    def test_approved_artwork_is_packaged_without_changes(self):
        original = (ROOT / "assets/pstack.jpeg").read_bytes()
        self.assertEqual(len(original), 723089)
        self.assertEqual(hashlib.sha256(original).hexdigest(),
                         "fa5786e6f6a39ea36fd5bc09ac542b647094268c192de421b8eb4e771c87585d")
        with zipfile.ZipFile(io.BytesIO(archive(self.files))) as package:
            self.assertEqual(package.read("assets/pstack.jpeg"), original)

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

    def test_codex_compatibility_manifest_has_one_metadata_source(self):
        portable = json.loads(self.files["plugin.json"])
        compatibility = json.loads(self.files[".codex-plugin/plugin.json"])
        for field in ("name", "version", "description", "author", "license", "repository"):
            self.assertEqual(compatibility[field], portable[field])
        self.assertEqual(compatibility["skills"], "./skills/")
        expected = dict(portable["extensions"]["com.openai"]["interface"])
        expected.pop("supportURL", None)
        self.assertEqual(compatibility["interface"], expected)
        self.assertNotIn("mcpServers", compatibility)
        self.assertNotIn("apps", compatibility)

    def test_host_contract_is_accessible_within_each_skill(self):
        canonical = self.files["resources/host-contract.md"]
        for skill in self.rules["skills"]:
            resource = f"skills/{skill}/references/host-contract.md"
            self.assertEqual(self.files[resource], canonical, skill)
            entry = self.files[f"skills/{skill}/SKILL.md"].decode()
            self.assertIn(
                "[the host and permission contract](references/host-contract.md)", entry)
        for name, content in self.files.items():
            if not name.startswith("skills/") or not name.endswith(".md"):
                continue
            skill = Path(name).parts[1]
            expected = (ROOT / f"skills/{skill}/references/host-contract.md").resolve()
            for target in re.findall(r"\[[^\]]*\]\(([^)]*host-contract\.md)\)", content.decode()):
                resolved = (ROOT / name).parent.joinpath(target).resolve()
                self.assertEqual(resolved, expected, (name, target))

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
                if name == "skills/why/references/synthesizer-prompt.md" and target == "url":
                    continue  # Upstream output-template slot, not a package resource.
                resolved = (ROOT / name).parent.joinpath(target.split("#")[0]).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT), (name, target))
                self.assertTrue(resolved.relative_to(ROOT).as_posix() in self.files, (name, target))

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

    def test_submitted_rc5_archive_remains_unchanged(self):
        name = "pstack-0.1.0-rc.5.zip"
        digest = "26415a9643c42ecd8c83a79788446b858d90ad88c68ff315296b725325de9cdc"
        self.assertEqual(hashlib.sha256((ROOT / "dist" / name).read_bytes()).hexdigest(), digest)
        self.assertEqual((ROOT / "dist" / (name + ".sha256")).read_text(),
                         f"{digest}  {name}\n")

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

    def test_portable_reference_inventory_and_workflow_structure(self):
        # Preserve complete role/rubric/template resources, not just entrypoint names.
        source = ROOT / "upstream/pstack/skills"
        for path in source.glob("*/references/**/*"):
            if path.is_file():
                destination = "skills/" + path.relative_to(source).as_posix()
                self.assertTrue(destination in self.files, destination)
        restored = ("architect", "arena", "automate-me", "blast-radius",
                    "create-verification-skill", "figure-it-out", "how", "interrogate",
                    "maintain-verification-skill", "poteto-mode", "recall", "reflect",
                    "show-me-your-work", "swarm", "why")
        for name in restored:
            original = (source / name / "SKILL.md").read_text()
            adapted = self.files[f"skills/{name}/SKILL.md"].decode()
            headings = re.findall(r"^#{2,3} .+$", original, re.MULTILINE)
            for heading in headings:
                self.assertIn(heading, adapted, name)

    def test_load_bearing_semantic_contracts(self):
        # Static preservation checks. Live model behavior is a separate release gate.
        contracts = {
            "architect/SKILL.md": ["Require at least two structurally distinct candidates",
                "Screen every candidate", "references/design-red-flags.md",
                "references/rationale-template.md", "Phase C: Agree (opt-in)",
                "The caller's usage is written first",
                "Before choosing a base or grafts, present a finding for every flag for each candidate",
                "Record any resulting revisions or rejection before writing the synthesis decision",
                "Claim a case is defined only when the sketch or rationale states its policy and outcome"],
            "architect/references/runner-prompt.md": [
                "findings against every flag", "design-red-flags.md",
                "with concrete reasons and any resulting revisions"],
            "interrogate/SKILL.md": ["references/reviewer-prompt.md",
                "references/rubric.md", "references/code-quality-review.md",
                "references/lead-judgment.md"],
            "why/SKILL.md": ["references/epistemics.md", "references/synthesizer-prompt.md"],
            "why/references/epistemics.md": ["### 1. Direct", "### 2. Supported",
                "### 3. Inferred", "### 4. Speculative", "### 5. Unknown",
                "## When Evidence Contradicts", "## Calibration Check Before Finalizing"],
            "reflect/SKILL.md": ["references/judgment-reviewer.md",
                "references/tooling-reviewer.md", "references/divergent-reviewer.md",
                "references/synthesizer.md", "Accepted / Rejected / Backlog"],
            "show-me-your-work/SKILL.md": ["Append-only", "Never edit or delete history",
                "first row has phase `start`", "audit never edits or removes a row",
                "Self-review is not a substitute"],
            "poteto-mode/playbooks/feature.md": ["Blocking first steps", "Independent workstreams",
                "Shared mutable state", "Smallest safe decomposition"],
            "poteto-mode/playbooks/refactoring.md": ["Pin the behavior contract first",
                "Type check and lint are not a pin", "If the diff does not lower reader load"],
            "poteto-mode/playbooks/multi-phase-plan.md": ["Regression lane against trunk",
                "Do not claim a ratio between unlike scenarios", "**Review gate.**"],
        }
        for path, clauses in contracts.items():
            text = self.files["skills/" + path].decode()
            for clause in clauses:
                self.assertTrue(clause in text, (path, clause))
        self.assertEqual(self.files["skills/show-me-your-work/references/decision-log-template.tsv"],
                         b"ts\tphase\tdecision\twhy\tevidence\tresult\n")

    def test_setup_preserves_roles_budget_and_confirmation_stages(self):
        original = (ROOT / "upstream/pstack/skills/setup-pstack/SKILL.md").read_text()
        adapted = self.files["skills/setup-pstack/SKILL.md"].decode()
        for heading in re.findall(r"^#{2,3} .+$", original, re.MULTILINE):
            self.assertIn(heading, adapted)
        source_table = re.search(r"^# budget: [^\n]+\n(.*?)^```", original,
                                 re.MULTILINE | re.DOTALL).group(1)
        target_table = adapted.split("```text\n", 1)[1].split("```", 1)[0]
        roles = lambda table: [line.split(":", 1)[0] for line in table.splitlines() if ":" in line]
        self.assertEqual(roles(source_table), roles(target_table))
        for label in ("unlimited — max reasoning", "large — xhigh reasoning",
                      "medium — high reasoning", "small — medium reasoning"):
            self.assertIn(label, adapted)
        for clause in ("Alias entries still count toward panel size",
                       "Do not derive a new identifier", "only when the user accepts it",
                       "Replace only the Pstack configuration section",
                       "Do not promise that a saved preference applies to new sessions"):
            self.assertIn(clause, adapted)
        self.assertIn("`max`, `xhigh`, `high`, or `medium`", adapted)
        self.assertIn("Inherited aliases keep the parent's settings", adapted)
        self.assertIn("Keep existing user-selected models and panel lists", adapted)
        for line in target_table.splitlines():
            role, choices = line.split(": ", 1)
            if role in {"arena runners", "arena cross-judge pool", "architect runners",
                        "interrogate reviewers"}:
                self.assertEqual(choices.split(", "), ["inherit-parent", "inherit-parent"])

    def test_help_offers_setup_without_discarding_existing_preferences(self):
        adapted = self.files["skills/poteto-help/SKILL.md"].decode()
        for clause in ("at most once per chat", "authorized project document",
                       "confirmed preferences", "answer the original question",
                       "inherited host settings"):
            self.assertIn(clause, adapted)

    def test_setup_host_contract_retains_role_settings(self):
        contract = self.files["resources/host-contract.md"].decode()
        self.assertIn("revalidate them against actual host capabilities", contract)
        self.assertIn("never pass those aliases as API identifiers", contract)
        for name in ("bug-fix", "feature", "refactoring", "hillclimb", "perf-issue"):
            playbook = self.files[f"skills/poteto-mode/playbooks/{name}.md"].decode()
            self.assertIn("role settings allowed by the host contract", playbook)
            self.assertNotIn("with inherited model settings", playbook)

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

    def test_restored_workflows_do_not_call_excluded_runtime_helpers(self):
        forbidden = (r"pstack/skills/", r"agent store", r"ready, never draft",
                     r"check-plan\.mjs", r"watcher.s four-column", r"allow_multiple",
                     r"/loop\b", r"hand (?:creation )?to `create-skill`")
        for name, content in self.files.items():
            if not name.startswith("skills/") or not name.endswith(".md"):
                continue
            for pattern in forbidden:
                self.assertIsNone(re.search(pattern, content.decode()), (name, pattern))
        plan = self.files["skills/poteto-mode/playbooks/multi-phase-plan.md"].decode()
        self.assertIn("../references/plan-validation.md", plan)
        self.assertIn("never as a script run", plan)
        contract = self.files["skills/poteto-mode/references/plan-validation.md"].decode()
        for obligation in ("introduction under ten", "PR block order", "exactly ten",
                           "1 through 10", "Metric, Probe, Baseline, and Rule",
                           "None gate", "screenshots, video, and operator review",
                           "all four appendices", "Fill every placeholder"):
            self.assertIn(obligation, contract)


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
        version = read_json(self.root / "upstream/lock.json")["version"]
        path = self.repo / "pstack/skills/how/SKILL.md"
        path.write_text(path.read_text() + "\nUse BrandNewHost.executeWithAllPermissions automatically.\n")
        self.commit()
        reviewed = (self.root / "adapter/reviewed.json").read_bytes()
        changed, _ = sync(self.repo, self.root)
        self.assertTrue(changed)
        self.assertEqual(read_json(self.root / "upstream/lock.json")["version"], version)
        self.assertEqual((self.root / "adapter/reviewed.json").read_bytes(), reviewed)
        self.assertIn("skills/how/SKILL.md", review_gaps(self.root))
        coverage = read_json(self.root / "resources/coverage.json")
        self.assertEqual(coverage["adaptation_status"], "pending")
        self.assertEqual(coverage["host_validation"], "not-qualified")
        self.assertNotIn("BrandNewHost", (self.root / "skills/how/SKILL.md").read_text())
        self.assertIn("unavailable until", (self.root / "skills/how/SKILL.md").read_text())
        again, _ = sync(self.repo, self.root)
        self.assertFalse(again)

    def test_version_bump_and_later_same_version_change_require_review(self):
        metadata = self.repo / "pstack/.cursor-plugin/plugin.json"
        manifest = read_json(metadata)
        manifest["version"] = "99.0.0"
        metadata.write_text(json.dumps(manifest))
        self.commit()
        reviewed = (self.root / "adapter/reviewed.json").read_bytes()
        changed, _ = sync(self.repo, self.root)
        self.assertTrue(changed)
        self.assertEqual(read_json(self.root / "upstream/lock.json")["version"], "99.0.0")
        self.assertEqual((self.root / "adapter/reviewed.json").read_bytes(), reviewed)
        self.assertIn(".cursor-plugin/plugin.json", review_gaps(self.root))
        self.assertIn("Source hashes were NOT approved", (self.root / "docs/upstream-update.md").read_text())
        self.assertEqual(read_json(self.root / "resources/coverage.json")["adaptation_status"], "pending")

        path = self.repo / "pstack/skills/how/SKILL.md"
        path.write_text(path.read_text() + "\nUse BrandNewHost.executeWithAllPermissions automatically.\n")
        self.commit()
        changed, _ = sync(self.repo, self.root)
        self.assertTrue(changed)
        self.assertEqual(read_json(self.root / "upstream/lock.json")["version"], "99.0.0")
        self.assertEqual((self.root / "adapter/reviewed.json").read_bytes(), reviewed)
        self.assertIn("skills/how/SKILL.md", review_gaps(self.root))
        coverage = read_json(self.root / "resources/coverage.json")
        self.assertEqual(coverage["adaptation_status"], "pending")
        self.assertEqual(coverage["host_validation"], "not-qualified")
        generated = (self.root / "skills/how/SKILL.md").read_text()
        self.assertNotIn("BrandNewHost", generated)
        self.assertIn("unavailable until", generated)

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

    def test_incompatible_metadata_keeps_candidate_without_stale_zip(self):
        manifest = read_json(self.root / "plugin.json")
        current = f"{manifest['name']}-{manifest['version']}.zip"
        previous = {name: digest for name, digest in hashes(self.root / "dist").items()
                    if name not in {current, current + ".sha256"}}
        path = self.repo / "pstack/skills/how/SKILL.md"
        path.write_text("New incompatible registration format")
        self.commit()
        changed, summary = sync(self.repo, self.root)
        self.assertTrue(changed)
        self.assertIn("Generation blocked", summary)
        self.assertFalse((self.root / "dist" / current).exists())
        self.assertFalse((self.root / "dist" / (current + ".sha256")).exists())
        self.assertEqual(hashes(self.root / "dist"), previous)
        self.assertIn("No current candidate ZIP is available", (self.root / "docs/upstream-update.md").read_text())
        self.assertIn("skills/how/SKILL.md", review_gaps(self.root))

    def test_existing_candidate_is_a_noop_even_from_older_default_branch(self):
        path = self.repo / "pstack/README.md"
        path.write_text(path.read_text() + "\nAnother source change.\n")
        self.commit()
        candidate = self.command("rev-parse", "HEAD:pstack")
        before = hashes(self.root / "upstream")
        changed, summary = sync(self.repo, self.root, existing_candidate_tree=candidate)
        self.assertFalse(changed)
        self.assertIn("already staged", summary)
        self.assertEqual(hashes(self.root / "upstream"), before)


if __name__ == "__main__":
    unittest.main()
