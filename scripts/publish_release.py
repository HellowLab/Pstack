"""Publish a validated stable package without rewriting tags or existing assets."""

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request

from build import ROOT, build, current_archive, read_json, review_gaps


VERSION = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)")


def version_tuple(version):
    if not VERSION.fullmatch(version):
        raise ValueError("GitHub releases require a stable major.minor.patch version")
    return tuple(map(int, version.split(".")))


def release_notes(changelog, version):
    headings = list(re.finditer(r"^## \[([^\]]+)\][^\n]*$", changelog, re.M))
    matches = [heading for heading in headings if heading[1] == version]
    if len(matches) != 1:
        raise ValueError(f"Require exactly one changelog section for {version}")
    match = matches[0]
    end = next((heading.start() for heading in headings if heading.start() > match.start()), len(changelog))
    body = changelog[match.end():end].strip()
    if not body or not re.search(r"^[-*] \S", body, re.M):
        raise ValueError(f"Changelog {version} requires nonempty release notes")
    return changelog[match.start():end].strip()


def tag_commit(api, tag):
    ref = api("GET", f"git/ref/tags/{tag}", optional=True)
    if ref is None:
        return None
    obj = ref["object"]
    for _ in range(10):
        if obj["type"] == "commit":
            return obj["sha"]
        if obj["type"] != "tag":
            break
        obj = api("GET", f"git/tags/{obj['sha']}")["object"]
    raise ValueError(f"Cannot resolve immutable tag {tag}")


def releases(api):
    result = []
    for page in range(1, 101):
        batch = api("GET", f"releases?per_page=100&page={page}")
        result.extend(batch)
        if len(batch) < 100:
            return result
    raise ValueError("Release listing incomplete; refusing publication")


def eligible(api, sha, version):
    if api("GET", "git/ref/heads/main")["object"]["sha"] != sha:
        return False
    for release in releases(api):
        if release["draft"] or release["prerelease"]:
            continue
        tag = release["tag_name"]
        if not tag.startswith("v"):
            raise ValueError(f"Cannot order published release {tag}")
        if version_tuple(tag[1:]) > version_tuple(version):
            return False
    return True


def publish(api, *, sha, version, notes, assets):
    version_tuple(version)
    if not re.fullmatch(r"[0-9a-f]{40}", sha) or not notes.strip() or not assets:
        raise ValueError("Missing exact source, notes, or assets")
    tag = "v" + version
    if not eligible(api, sha, version):
        return "Skipped stale source or version; Latest unchanged."
    commit = tag_commit(api, tag)
    if commit and commit != sha:
        return f"Skipped immutable {tag} at {commit}. Bump the version for new source; no release changed."
    matches = [release for release in releases(api) if release["tag_name"] == tag]
    if len(matches) > 1:
        raise ValueError(f"Multiple releases for {tag}")
    release = matches[0] if matches else None
    if release and (not commit or release["prerelease"]):
        raise ValueError("Existing release conflicts with a stable tagged package")
    if not commit:
        api("POST", "git/refs", {"ref": "refs/tags/" + tag, "sha": sha})
    if tag_commit(api, tag) != sha:
        raise ValueError("Tag changed during publication")
    if release is None:
        release = api("POST", "releases", {
            "tag_name": tag, "target_commitish": sha, "name": f"Pstack {tag}",
            "body": notes, "draft": True, "prerelease": False, "make_latest": "false",
        })
    release_id = release["id"]
    for name, data in assets.items():
        existing = [asset for asset in api("GET", f"releases/{release_id}")["assets"] if asset["name"] == name]
        if len(existing) > 1:
            raise ValueError(f"Duplicate release asset {name}")
        digest = "sha256:" + hashlib.sha256(data).hexdigest()
        if not existing:
            asset = api("POST", f"releases/{release_id}/assets?name={urllib.parse.quote(name)}", data, upload=True)
        else:
            asset = existing[0]
        if asset.get("state") != "uploaded" or asset.get("digest") != digest or asset.get("size") != len(data):
            raise ValueError(f"Release asset {name} conflicts with validated bytes; never overwritten")
    if not eligible(api, sha, version):
        return "Stopped stale publication after staging; existing tag/assets preserved, Latest unchanged."
    if tag_commit(api, tag) != sha:
        raise ValueError("Tag changed before publication")
    api("PATCH", f"releases/{release_id}", {
        "name": f"Pstack {tag}", "body": notes, "draft": False,
        "prerelease": False, "make_latest": "true",
    })
    verified = api("GET", f"releases/{release_id}")
    latest = api("GET", "releases/latest")
    if verified["draft"] or verified["prerelease"] or verified["body"] != notes or latest["id"] != release_id:
        raise ValueError("Published release readback did not match expected notes and Latest")
    return f"Published {tag} at {sha}; exact notes and Latest verified. {verified['html_url']}"


class GitHub:
    def __init__(self, repository, token):
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", repository) or not token:
            raise ValueError("Require repository identity and job-scoped token")
        self.repository = repository
        self.token = token

    def __call__(self, method, path, body=None, *, optional=False, upload=False):
        host = "uploads.github.com" if upload else "api.github.com"
        headers = {"Authorization": "Bearer " + self.token, "Accept": "application/vnd.github+json",
                   "X-GitHub-Api-Version": "2022-11-28", "Content-Type": "application/octet-stream" if upload else "application/json"}
        data = body if upload else (json.dumps(body).encode() if body is not None else None)
        request = urllib.request.Request(f"https://{host}/repos/{self.repository}/{path}", data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if optional and method == "GET" and error.code == 404:
                return None
            raise RuntimeError(f"GitHub {method} {path} failed with HTTP {error.code}") from None


def main():
    if (os.environ.get("GITHUB_EVENT_NAME") not in {"push", "workflow_dispatch"}
            or os.environ.get("GITHUB_REF") != "refs/heads/main"
            or os.environ.get("VALIDATION_RESULT") != "success"):
        raise ValueError("Release requires successful validation on main")
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    if sha != os.environ.get("GITHUB_SHA"):
        raise ValueError("Checkout differs from validated workflow source")
    version = read_json(ROOT / "plugin.json")["version"]
    version_tuple(version)
    notes = release_notes((ROOT / "CHANGELOG.md").read_text(), version)
    if review_gaps():
        raise ValueError("Pending upstream adaptation cannot be released")
    build(check=True)
    archive = ROOT / current_archive()
    assets = {path.name: path.read_bytes() for path in (archive, archive.with_suffix(".zip.sha256"))}
    summary = publish(GitHub(os.environ["GITHUB_REPOSITORY"], os.environ["GH_TOKEN"]),
                      sha=sha, version=version, notes=notes, assets=assets)
    print(summary)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as output:
            output.write(summary + "\n")


if __name__ == "__main__":
    main()
