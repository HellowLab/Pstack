"""Fetch the public Pstack subtree without executing it or approving adaptation."""

import argparse
from datetime import datetime, timezone
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile

from build import ROOT, build, hashes, read_json, review_gaps
from maintenance_pr import BRANCH

UPSTREAM = "https://github.com/cursor/plugins.git"


def git(directory, *args):
    return subprocess.check_output(["git", "-C", str(directory), *args])


def export_snapshot(checkout, commit, destination):
    data = git(checkout, "archive", commit, "pstack")
    with tarfile.open(fileobj=io.BytesIO(data)) as archive:
        for member in archive:
            relative = Path(member.name)
            if relative.parts[0] != "pstack" or ".." in relative.parts or relative.is_absolute():
                raise ValueError(f"Unsafe upstream path: {member.name}")
            if member.isdir():
                continue
            if not member.isfile():
                raise ValueError(f"Unsupported upstream file type: {member.name}")
            target = destination.joinpath(*relative.parts[1:])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.extractfile(member).read())
            target.chmod(0o755 if member.mode & 0o111 else 0o644)


def candidate_tree(root=ROOT):
    remote = git(root, "ls-remote", "--heads", "origin", BRANCH).decode().strip()
    if not remote:
        return None
    git(root, "fetch", "--no-tags", "origin", BRANCH)
    return git(root, "rev-parse", "FETCH_HEAD:upstream/pstack").decode().strip()


def sync(checkout, root=ROOT, existing_candidate_tree=None):
    lock = read_json(root / "upstream/lock.json")
    latest = git(checkout, "rev-parse", "HEAD").decode().strip()
    tree = git(checkout, "rev-parse", "HEAD:pstack").decode().strip()
    summary = f"Checked cursor/plugins {latest}; pstack subtree {tree}."
    if tree == lock["tree"]:
        return False, summary + " No subtree change."
    if tree == existing_candidate_tree:
        return False, summary + " This subtree is already staged on the maintenance branch. Preserved its review and timestamps."
    with tempfile.TemporaryDirectory() as temp:
        staged = Path(temp) / "pstack"
        staged.mkdir()
        export_snapshot(checkout, latest, staged)
        try:
            version = read_json(staged / ".cursor-plugin/plugin.json")["version"]
        except (ValueError, KeyError, FileNotFoundError):
            version = "unknown; upstream metadata requires review"
        files = hashes(staged)
        changed = sorted(key for key in files.keys() | lock["files"].keys()
                         if files.get(key) != lock["files"].get(key))
        shutil.rmtree(root / "upstream/pstack")
        shutil.copytree(staged, root / "upstream/pstack")
    previous = lock["commit"]
    lock.update(commit=latest, tree=tree, version=version, files=files,
                latest_checked_commit=latest,
                checked_at=datetime.now(timezone.utc).date().isoformat())
    (root / "upstream/lock.json").write_text(json.dumps(lock, indent=2) + "\n")
    report = ["# Pending upstream adaptation", "", f"Previous snapshot: `{previous}`.",
              f"Candidate snapshot: `{latest}`. Version: {version}.",
              f"[Upstream comparison](https://github.com/cursor/plugins/compare/{previous}...{latest})", "",
              "The snapshot changed even if the version did not. Source hashes were NOT approved.",
              "Inspect the subtree diff in this PR, update adapters and tests, then deliberately update reviewed hashes.",
              "The generated ZIP is an unqualified preview. No auto-merge or publication.", "", "Changed files:", ""]
    report.extend(f"- `{path}`" for path in changed)
    (root / "docs/upstream-update.md").write_text("\n".join(report) + "\n")
    try:
        build(root)
    except (ValueError, KeyError, IndexError, FileNotFoundError) as error:
        for artifact in (root / "dist").glob("*"):
            if artifact.is_file():
                artifact.unlink()
        failure = "Generation blocked by incompatible upstream input. " + type(error).__name__
        with (root / "docs/upstream-update.md").open("a") as output:
            output.write("\n" + failure + ". No ZIP is available for this candidate. Inspect the source diff and rerun the build locally for diagnostics.\n")
        return True, summary + " " + failure
    return True, summary + f" {len(review_gaps(root))} files require adaptation review."


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, help="Local Git fixture or previously fetched canonical checkout")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as temp:
        checkout = args.checkout
        if checkout is None:
            checkout = Path(temp) / "source"
            subprocess.run(["git", "clone", "--depth=1", "--no-tags", UPSTREAM, str(checkout)], check=True)
        existing = candidate_tree()
        latest_tree = git(checkout, "rev-parse", "HEAD:pstack").decode().strip()
        changed, summary = sync(checkout, existing_candidate_tree=existing)
        recover_pr = (not changed and existing == latest_tree
                      and existing != read_json(ROOT / "upstream/lock.json")["tree"])
    print(summary)
    if os.getenv("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write(f"changed={str(changed).lower()}\n")
            output.write(f"recover_pr={str(recover_pr).lower()}\n")
    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as output:
            output.write(summary + "\n")


if __name__ == "__main__":
    main()
