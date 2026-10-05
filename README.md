# Pstack-GPT

Independent HellowLab adaptation of [Lauren Tan's Pstack](https://github.com/cursor/plugins/tree/main/pstack) for ChatGPT and Codex. This is not an official poteto, Cursor, or OpenAI release.

Pstack-GPT provides skills for understanding code, designing changes, implementation, review, and verification. It uses only the tools and permissions available in the host. This initial release candidate is not marketplace-approved or host-qualified. No marketplace package has been submitted or published.

The source is pinned to Pstack **0.15.13**, commit [`2cbf585`](https://github.com/cursor/plugins/tree/2cbf58508f40de470d7490b55c51d71241928fa2/pstack). The [generated coverage map](resources/coverage.md) exposes the pinned version, last checked revision, adaptation status, and every source file's disposition. The [upstream workflow](.github/workflows/upstream.yml) checks subtree changes daily after it reaches the default branch. It detects changes without a version bump and requires adaptation review. It never merges or publishes.

## What is included

All 51 registered skill entry points and 23 playbook routes are represented. Use `poteto-help` for a guide, `how` for runtime behavior, `why` for rationale, `architect` for design, `interrogate` for critique, and `poteto-mode` for the workflow router. Slash spellings are aliases; the host's skill picker may expose them differently. Explicit-only invocation semantics are retained, including when the host must enforce them from instructions rather than metadata.

Inventory coverage does not mean full runtime parity. The Grok Bot UI and persistent orchestration/autopilot runtimes have explanatory entry points but are unsupported. Native Cursor agent registration, helper scripts, model defaults, and private transcript paths are not portable. [Design and fidelity decisions](docs/design.md) explain each difference. The package never invents a tool, reviewer, model panel, or external-action authorization.

## Build and validate

Use Python 3.11 or newer. The package build has no third-party dependencies.

```sh
python3 -m venv .build/venv
.build/venv/bin/python -m pip install -r requirements-dev.txt
python3 scripts/build.py
.build/venv/bin/python -m unittest discover -s tests -v
python3 scripts/build.py --check
```

The ZIP and SHA-256 file are in [dist](dist/). They contain root `plugin.json`, generated skills, resources, the full MIT license, and attribution. The supplied branding asset is not yet included because its transfer to the build environment failed. Icons and branding review remain release gates. The ZIP contains no upstream executable helpers, MCP configuration, hooks, secrets, or publisher agreements. Repeated builds from the same inputs are byte-identical.

Edit `adapter/overrides/`, `adapter/rules.json`, and authored metadata rather than generated skills. The complete untouched upstream subtree is retained under `upstream/pstack/` as review data. Do not install that subtree as this plugin.

## Try the candidate locally

Stage the exact ZIP in a fresh disposable marketplace:

```sh
python3 scripts/stage_local.py /tmp/pstack-gpt-preview
```

The staging command does not install or alter user configuration. On a supported Codex installation, register that local source with `codex plugin marketplace add /tmp/pstack-gpt-preview`, then install with `codex plugin add pstack-gpt@pstack-gpt-preview`. These installation commands change local plugin configuration. In the desktop plugin directory, select the local source where available, install the candidate, and start a new chat. Local-source availability varies between ChatGPT and Codex surfaces. See [the host validation matrix](docs/validation.md) for what was actually tested and what remains blocked.

To remove a test installation, use `codex plugin remove pstack-gpt@pstack-gpt-preview` and `codex plugin marketplace remove pstack-gpt-preview` on a compatible CLI. Keep evidence before deleting the disposable staging directory. No public marketplace URL exists yet.

## Maintain and publish

Read [maintenance](docs/maintenance.md) for the daily check, the one-draft-PR update flow, the current repository PR-creation permission blocker, and manual adaptation review. Read [publishing](docs/publishing.md) for verified-publisher requirements, actual host validation, review, and explicit publication steps. The initial implementation remains subject to human review and must not be merged automatically.

Pstack is MIT licensed. Copyright (c) 2026 Lauren Tan. See [LICENSE](LICENSE).
