"""Update one bot-owned maintenance branch and draft PR using GITHUB_TOKEN."""

import argparse
import json
import os
from pathlib import Path
import subprocess

BRANCH = "maintenance/pstack-upstream"
BOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"


def run(*args):
    return subprocess.check_output(args, text=True).strip()


def previously_merged(repository, base, expected):
    merged_prs = json.loads(run(
        "gh", "pr", "list", "--repo", repository, "--head", BRANCH, "--base", base,
        "--state", "merged", "--limit", "100", "--json", "headRefOid,mergeCommit"))
    for pr in merged_prs:
        if pr["headRefOid"] != expected or not pr["mergeCommit"]:
            continue
        merged = pr["mergeCommit"]["oid"]
        try:
            run("git", "merge-base", "--is-ancestor", merged, "HEAD")
        except subprocess.CalledProcessError as error:
            if error.returncode == 1:
                continue
            raise
        if run("git", "rev-parse", f"{expected}^{{tree}}") == run("git", "rev-parse", f"{merged}^{{tree}}"):
            return True
    return False


def main(existing_only=False):
    repository = os.environ["GITHUB_REPOSITORY"]
    base = os.environ["DEFAULT_BRANCH"]
    prs = json.loads(run("gh", "pr", "list", "--repo", repository, "--head", BRANCH,
                         "--state", "open", "--json", "number,isDraft"))
    if len(prs) > 1:
        raise SystemExit("Multiple maintenance PRs exist. Resolve manually; no branch was changed.")
    if existing_only and prs:
        return
    if prs and not prs[0]["isDraft"]:
        raise SystemExit("Maintenance PR is under active review. Refusing to replace its branch.")
    remote = run("git", "ls-remote", "--heads", "origin", BRANCH)
    expected = remote.split()[0] if remote else ""
    if existing_only and not expected:
        return
    if expected:
        if run("git", "rev-parse", "--is-shallow-repository") == "true":
            run("git", "fetch", "--unshallow", "origin")
        run("git", "fetch", "origin", BRANCH)
        if run("git", "rev-parse", "FETCH_HEAD") != expected:
            raise SystemExit("Maintenance branch moved during inspection. Retry without changing it.")
        authors = run("git", "log", "--format=%ae", f"HEAD..{expected}").splitlines()
        same_tree = run("git", "rev-parse", f"{expected}^{{tree}}") == run("git", "rev-parse", "HEAD^{tree}")
        if any(author != BOT_EMAIL for author in authors):
            if prs or not (same_tree or previously_merged(repository, base, expected)):
                raise SystemExit("Maintenance branch has an unmerged human commit. Refusing to overwrite it.")
    if existing_only:
        report = run("git", "show", "FETCH_HEAD:docs/upstream-update.md")
    else:
        run("git", "config", "user.name", "github-actions[bot]")
        run("git", "config", "user.email", BOT_EMAIL)
        run("git", "switch", "-C", BRANCH)
        run("git", "add", "upstream", "skills", "resources/coverage.json", "resources/coverage.md",
            "dist", "docs/upstream-update.md")
        if not run("git", "diff", "--cached", "--name-only"):
            return
        run("git", "commit", "-m", "chore(upstream): stage Pstack update for adaptation review")
        if expected:
            run("git", "merge", "--strategy=ours", "--no-edit", expected)
        run("git", "push", "origin", f"HEAD:refs/heads/{BRANCH}")
        report = Path("docs/upstream-update.md").read_text()
    body = Path(".build/maintenance-pr.md")
    body.parent.mkdir(exist_ok=True)
    body.write_text(report +
                    "\nThe scheduled run executes validation directly because GITHUB_TOKEN pushes do not trigger ordinary push/PR workflows. Inspect its checks and artifacts. Adaptation review must pass before release qualification.\n")
    try:
        if prs:
            run("gh", "pr", "edit", str(prs[0]["number"]), "--repo", repository,
                "--title", "chore(upstream): review Pstack adaptation update", "--body-file", str(body))
        else:
            run("gh", "pr", "create", "--repo", repository, "--base", base, "--head", BRANCH,
                "--draft", "--title", "chore(upstream): review Pstack adaptation update", "--body-file", str(body))
    except subprocess.CalledProcessError as error:
        raise SystemExit("Maintenance branch pushed, but GitHub blocked the PR operation. Check repository/organization Actions PR policy. No credentials or security settings were changed.") from error


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--existing-only", action="store_true",
                        help="Recover a missing draft PR without changing its candidate branch")
    main(parser.parse_args().existing_only)
