# Pstack

Ship faster. Build better.

<img src="assets/pstack.jpeg" alt="Pstack potato builder and colorful crew" width="640">

Bring Pstack’s engineering workflows to ChatGPT and Codex. Faithfully adapted from [Lauren Tan’s original](https://github.com/cursor/plugins/tree/main/pstack), with upstream tracking and reviewed updates to keep pace with Pstack as it evolves. Investigate, design, build, review, and verify with a consistent set of engineering practices. Independently maintained by HellowLab.

## Install Pstack

Choose the [latest qualified GitHub release](https://github.com/HellowLab/Pstack/releases/latest). It is our latest tested, supported adaptation of [Lauren Tan's upstream Pstack](https://github.com/cursor/plugins/tree/main/pstack). We check upstream daily and review changes before release. Pending branches and upstream HEAD are not installation targets.

Copy one prompt into an agent with access to the intended installation target. The agent must check its available tools and required permissions. These prompts do not guarantee support in every Codex client.

### On this computer

```text
Install Pstack on this computer only. Follow https://github.com/HellowLab/Pstack/blob/main/docs/install.md and use the latest qualified GitHub release with its verified checksum. Check native local-plugin support first. Reuse an existing Pstack installation, preserve settings, and avoid duplicates or downgrades. Ask for required permissions; stop if unsupported. Verify the installed version and new-session availability, and report anything you could not test.
```

A local marketplace and plugin cache belong to that computer. They do not synchronize through your account.

### In my private account

```text
Set up Pstack privately in my personal account using Plugin Creator and https://github.com/HellowLab/Pstack/blob/main/docs/install.md. Use the latest qualified GitHub release and verify its checksum. Confirm personal USER scope and PRIVATE visibility before writing; reuse my existing Pstack identity and preserve settings. If personal scope or tooling is unavailable, stop and explain, without creating a workspace or local substitute. Verify saving, installation or enabling, and new-session access separately.
```

This route requires Plugin Creator and the necessary permissions. Account availability depends on the client and account context; it does not promise access on every computer or Codex client. See the [scope and compatibility checks](docs/install.md#install-in-a-private-personal-account).

### Optional weekly updates

Copy this into a personal assistant such as dot only if you want it to create an update schedule:

```text
Set up weekly Pstack update checks following https://github.com/HellowLab/Pstack/blob/main/docs/install.md. Ask me to choose my existing private account install, a named computer install, or both, and a weekly time and timezone. Use a supported scheduler with access to those targets and verify schedule creation. Update only those existing targets when a newer qualified GitHub release is available; verify its checksum and installed result, preserve identity and settings, and never downgrade or duplicate. Ask for required permissions. Report updates or blockers concisely; keep no-op checks quiet.
```

A reminder alone cannot update a plugin. An offline computer or unavailable account tool is a blocker for that target, not permission to update another. The [installation guide](docs/install.md) covers updates, removal, and verification limits.

## Compatibility, review, and qualification

The public OpenAI marketplace submission is **in review**, last verified October 27, 2026. No public install link is available yet. Marketplace review can delay initial availability and later updates; there is no promised turnaround. Once published, we will add the verified public listing here as another installation option. GitHub installations also need update checks to stay current.

This is not an official poteto, Cursor, or OpenAI release. Pstack uses only the tools and permissions available in the host. Version 0.1.13 is distributed through GitHub releases and is not fully host-qualified. GitHub releases are separate from plugin marketplace approval. The submitted 0.1.0-rc.5 package is preserved; its verified state on October 27, 2026 was In review / Not published.

The source is pinned to Pstack **0.15.34**, commit [`519d36a`](https://github.com/cursor/plugins/tree/519d36aa98955bf680db01bcde5fdfba686dc901/pstack). The [generated coverage map](resources/coverage.md) exposes the pinned version, last checked revision, adaptation status, and every source file's disposition. The [upstream workflow](.github/workflows/upstream.yml) is on `main` and checks subtree changes daily at 08:17 UTC. It detects changes without a version bump and requires adaptation review. It never merges or publishes.

An isolated Linux test of Codex CLI `0.159.0-alpha.3` installed v0.1.13, matched all 183 cached files to the release ZIP, and discovered all 58 Pstack skills in a fresh process. Native removal left no test plugin or marketplace. Model smoke tests could not run without authentication in the isolated environment. This does not qualify every client or platform. See [the measured result and cleanup evidence](docs/validation.md#isolated-native-cli-check-for-0113).

### Included workflows

All 58 registered skill entry points and 23 playbook routes are represented. Use `poteto-help` for a guide, `how` for runtime behavior, `why` for rationale, `architect` for design, `interrogate` for critique, and `poteto-mode` for the workflow router. Slash spellings are aliases; the host's skill picker may expose them differently. Explicit-only invocation semantics are retained, including when the host must enforce them from instructions rather than metadata.

### Limits and platform support

Inventory coverage does not mean full runtime parity. The Grok Bot UI and persistent orchestration/autopilot runtimes have explanatory entry points but are unsupported. Native Cursor agent registration, helper scripts, model defaults, and private transcript paths are not portable. Upstream Claude Code harness mappings are retained as source-only documentation and do not add ChatGPT or Codex capabilities. [Design and fidelity decisions](docs/design.md) explain each difference. The package never invents a tool, reviewer, model panel, or external-action authorization. [Validation](docs/validation.md) separates installation and resource-access checks from actual model behavior. The initial private beta is merged. The first manual check passed with no subtree change. The [Oct 6 scheduled check](https://github.com/HellowLab/Pstack/actions/runs/37485323936) detected upstream 0.15.15 and opened [draft PR #4](https://github.com/HellowLab/Pstack/pull/4). Its expected review-gate failure required the adaptation in this candidate.

## Build and validate

Use Python 3.11 or newer. The package build has no third-party dependencies.

```sh
python3 -m venv .build/venv
.build/venv/bin/python -m pip install -r requirements-dev.txt
python3 scripts/build.py
.build/venv/bin/python -m unittest discover -s tests -v
python3 scripts/build.py --check
```

The current candidate ZIP and SHA-256 file are in [dist](dist/). Earlier archive pairs remain there with their original checksums, including the submitted rc.5 package. They contain root `plugin.json`, a generated Codex compatibility manifest, generated skills, resources, the approved original artwork, the full MIT license, and attribution. Both icon fields reference the unchanged [Pstack artwork](assets/pstack.jpeg). Its "Always up to date" chalkboard is artwork copy: the workflow is scheduled daily, and updates require review. Marketplace branding approval remains a release gate. The ZIP contains no upstream executable helpers, MCP configuration, hooks, secrets, or publisher agreements. Repeated builds from the same inputs are byte-identical.

Edit `adapter/overrides/`, `adapter/rules.json`, and authored metadata rather than generated skills. The complete untouched upstream subtree is retained under `upstream/pstack/` as review data. Do not install that subtree as this plugin.

## Test a release locally

Follow the [installation guide](docs/install.md#install-on-one-computer) to stage a verified release in a native local marketplace. Staging, installing, and checking behavior are separate steps. Pstack 0.1.13 passed repository tests, reproducible builds, and the isolated Linux CLI installation/discovery check above. Model-behavior qualification remains incomplete. See [validation evidence](docs/validation.md) for version-specific results.

## Privacy and support

Pstack is offered free, with availability requested in all OpenAI-supported countries. See the [privacy policy](docs/privacy.md). Use [GitHub Issues](https://github.com/HellowLab/Pstack/issues) for general support and `me@seankudrna.com` for private support or privacy requests.

## Maintain and publish

Read [maintenance](docs/maintenance.md) for the daily check, the one-draft-PR update flow, the verified repository PR-creation permission and recovery behavior, and manual adaptation review. Read [publishing](docs/publishing.md) for verified-publisher requirements, actual host validation, review, and explicit publication steps. The initial private-beta implementation was squash-merged in [PR #1](https://github.com/HellowLab/Pstack/pull/1). Future maintenance updates remain draft PRs for human review.

Pstack is MIT licensed. Copyright (c) 2026 Lauren Tan. See [LICENSE](LICENSE).

## GitHub releases

After a stable version reaches `main`, successful package validation publishes its `v<version>` GitHub release with the matching [changelog](CHANGELOG.md) section, ZIP, and checksum. The workflow verifies uploaded digests and marks the version Latest only when main and version checks are current. Existing tags and conflicting assets are never overwritten. See [release maintenance](docs/maintenance.md#github-release-publication) for retries and version rules.
