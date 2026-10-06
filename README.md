# Pstack

Ship faster. Build better.

<img src="assets/pstack.jpeg" alt="Pstack potato builder and colorful crew" width="640">

Bring Pstack’s engineering workflows to ChatGPT and Codex. Faithfully adapted from [Lauren Tan’s original](https://github.com/cursor/plugins/tree/main/pstack), with upstream tracking and reviewed updates to keep pace with Pstack as it evolves. Investigate, design, build, review, and verify with a consistent set of engineering practices. Independently maintained by HellowLab.

This is not an official poteto, Cursor, or OpenAI release. Pstack uses only the tools and permissions available in the host. The 0.1.1 candidate is not released or fully host-qualified. The submitted 0.1.0-rc.5 package remains in review and unchanged.

The source is pinned to Pstack **0.15.15**, commit [`df58112`](https://github.com/cursor/plugins/tree/df581122cde17e6e27686b5a448bde23e4ad4318/pstack). The [generated coverage map](resources/coverage.md) exposes the pinned version, last checked revision, adaptation status, and every source file's disposition. The [upstream workflow](.github/workflows/upstream.yml) is on `main` and checks subtree changes daily at 08:17 UTC. It detects changes without a version bump and requires adaptation review. It never merges or publishes.

## What is included

All 51 registered skill entry points and 23 playbook routes are represented. Use `poteto-help` for a guide, `how` for runtime behavior, `why` for rationale, `architect` for design, `interrogate` for critique, and `poteto-mode` for the workflow router. Slash spellings are aliases; the host's skill picker may expose them differently. Explicit-only invocation semantics are retained, including when the host must enforce them from instructions rather than metadata.

## Compatibility limits

Inventory coverage does not mean full runtime parity. The Grok Bot UI and persistent orchestration/autopilot runtimes have explanatory entry points but are unsupported. Native Cursor agent registration, helper scripts, model defaults, and private transcript paths are not portable. [Design and fidelity decisions](docs/design.md) explain each difference. The package never invents a tool, reviewer, model panel, or external-action authorization. [Validation](docs/validation.md) separates installation and resource-access checks from actual model behavior. The initial private beta is merged. The first manual check passed with no subtree change. The [Oct 6 scheduled check](https://github.com/HellowLab/Pstack/actions/runs/37485323936) detected upstream 0.15.15 and opened [draft PR #4](https://github.com/HellowLab/Pstack/pull/4). Its expected review-gate failure required the adaptation in this candidate.

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

## Try the candidate locally

Stage the exact ZIP in a fresh disposable marketplace:

```sh
python3 scripts/stage_local.py /tmp/pstack-preview
```

The staging command does not install or alter user configuration. On a supported Codex installation, register that local source with `codex plugin marketplace add /tmp/pstack-preview`, then install with `codex plugin add pstack@pstack-preview`. These installation commands change local plugin configuration. In the desktop plugin directory, select the local source where available, install the candidate, and start a new chat. Local-source availability varies between ChatGPT and Codex surfaces. See [the host validation matrix](docs/validation.md) for what was actually tested and what remains blocked.

To remove a test installation, use `codex plugin remove pstack@pstack-preview` and `codex plugin marketplace remove pstack-preview` on a compatible CLI. Keep evidence before deleting the disposable staging directory. No public marketplace URL exists yet.

## Privacy and support

Pstack is offered free, with availability requested in all OpenAI-supported countries. See the [privacy policy](docs/privacy.md). Use [GitHub Issues](https://github.com/HellowLab/Pstack/issues) for general support and `me@seankudrna.com` for private support or privacy requests.

## Maintain and publish

Read [maintenance](docs/maintenance.md) for the daily check, the one-draft-PR update flow, the verified repository PR-creation permission and recovery behavior, and manual adaptation review. Read [publishing](docs/publishing.md) for verified-publisher requirements, actual host validation, review, and explicit publication steps. The initial private-beta implementation was squash-merged in [PR #1](https://github.com/HellowLab/Pstack/pull/1). Future maintenance updates remain draft PRs for human review.

Pstack is MIT licensed. Copyright (c) 2026 Lauren Tan. See [LICENSE](LICENSE).
