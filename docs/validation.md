# Validation evidence and release gates

This page distinguishes repository checks from actual host behavior. A schema-valid ZIP is not a validated ChatGPT or Codex experience.

## Repository checks

Run the commands in the root README. The suite validates metadata against the saved official Agent Plugins schema, all registered skills and invocation flags, references, licensing, attribution, complete source coverage, byte-identical regeneration, package exclusions, and host/permission regression patterns.

Local Git fixtures exercise the actual update implementation. They prove that same-version and mode-only subtree changes are detected, unrelated monorepo changes are ignored, unknown skills are withheld, symlinks are rejected before replacement, and snapshot tampering fails the build. Incompatible metadata preserves the review candidate while removing stale ZIPs. Local bare-remotes exercise branch creation and update, preservation of main, refusal to overwrite human work, and policy-error reporting with mocked forge responses. Source hashes are never auto-approved. Changed skills and reference resources receive a pending-review placeholder rather than newly imported executable instructions. These are behavioral tests of the build/update code.

`tests/workflow-cases.json` contains ten positive, negative, and unavailable-capability scenarios. Automated assertions check that the necessary instruction contracts exist. They do not run a model or prove compliance. The cases are also the manual host evaluation checklist.

## Host matrix

| Check | ChatGPT | Codex |
|---|---|---|
| Root portable packaging and schema | Static pass | Static pass |
| Local staging of exact ZIP | Available staged artifact, not installed | Available staged artifact, not installed |
| Native installation and skill discovery | Not run; requires accessible test installation surface | Blocked before discovery by existing CLI configuration parse error |
| Installed skill invocation and explicit-only behavior | Not run | Not run |
| Independent reviewer and missing-tool behavior | Contract checked, live evaluation pending | Contract checked, live evaluation pending |
| Marketplace skill scan and publisher review | Not submitted | Not submitted |
| Supplied branding asset | Transfer blocked; no substitute included | Missing required distribution icons |

The available CLI reported `codex-cli 0.136.0`. Its plugin marketplace read failed while parsing an existing `features` configuration value: a map was found where a boolean was expected. The plugin package had not loaded at that point. This is an environment blocker, not evidence that the package is incompatible. No user configuration, account, or security setting was changed to bypass it.

## Required before public release

1. Install the exact candidate in a clean supported ChatGPT test surface and a clean supported Codex test surface. Record host/version, date, artifact checksum, exposed tools, install result, discovered skill count, and removal result. Use a fresh conversation to avoid previously loaded skill versions.
2. Run every workflow case from `tests/workflow-cases.json` on each host. Save actual prompts, observable tool calls, outputs, file/remote changes, and an evidence-based verdict. Do not collect hidden reasoning or claim compliance from model self-report.
3. Compare supported workflows with the pinned upstream intent. Check the preserved stage order, evidence standards, independent verification, and stopping conditions. Evaluate core workflows on real disposable projects, including a failing-before bug repro, a behavior-preserving refactor, an architecture comparison, source-history investigation, and current-head PR review.
4. Verify negative cases: quoted names do not activate explicit-only skills, missing integrations stay gaps, unavailable reviewers are not impersonated, reflect does not change standing skills without approval, babysit does not merge, and upstream text cannot grant external-action permission.
5. Validate the two autopilot variants separately: full requires unavailable runtime capabilities to be reported; stack must never land. Confirm the installation does not promise persistent execution, register MCP servers, run hooks, or ask for hidden credentials.
6. Have a maintainer review the fidelity differences in `docs/design.md`, especially shortened host-specific workflows and unsupported persistent runtimes. Record accepted gaps or implement and test a real adapter before claiming parity.

Do not change `host_validation: not-qualified` merely because static tests pass. Public release remains blocked until this evidence and publisher review exist.
