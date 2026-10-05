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
| Native installation | Not run; requires accessible test installation surface | Passed on Codex CLI 0.136.0 with generated compatibility manifest |
| Skill discovery in a fresh conversation | Not run | Not run; existing conversation catalog did not reload |
| Installed skill invocation and explicit-only behavior | Not run | Not run |
| Independent reviewer and missing-tool behavior | Contract checked, live evaluation pending | Contract checked, live evaluation pending |
| Marketplace skill scan and publisher review | Not submitted | Not submitted |
| Supplied branding asset | Transfer blocked; no substitute included | Missing required distribution icons |

The available CLI reported `codex-cli 0.136.0`. An existing `features.context_management` map initially failed its boolean configuration parser. The temporary command-line override `-c features.context_management=false` allowed plugin commands to run without editing that feature setting or changing access controls. Registering a disposable local marketplace succeeded. The root-only candidate was discovered but installation failed with `missing plugin.json`.

The documented `.codex-plugin/plugin.json` compatibility manifest, generated from the root metadata, fixed native installation. The exact ZIP with SHA-256 `f9a8e907c3727ce7033ffd0742819464636be7173cf964a48f7069ac8f4971eb` installed and was reported enabled. Every installed package file was byte-identical to the ZIP; all 51 skill entrypoint files, the host contract, and nested reviewer references were present. Plugin removal and marketplace removal both succeeded; a subsequent listing showed no test plugin. The original feature configuration remains unchanged. The existing conversation's executor skill catalog did not reload the new installation, so actual discovery/invocation in a fresh conversation and resource access through the host API remain untested.

The bundled plugin-authoring validator rejected all 50 explicit-only flags because it requires `disable-model-invocation` to be false. The real CLI accepted the package. The adaptation deliberately preserves those upstream flags and guards; changing invocation semantics to satisfy that helper would be incorrect. Record this validator disagreement and verify actual explicit invocation and non-invocation behavior before release.

The suite also protects full portable reference inventory, upstream workflow headings, required architectural screening and rationale templates, review lenses, epistemic tiers and calibration, and the exact append-only TSV protocol. These semantic preservation checks prevent specific losses found in review. They remain static instruction checks, not model behavior tests.

## Required before public release

1. Install the exact candidate in a clean supported ChatGPT test surface and a clean supported Codex test surface. Record host/version, date, artifact checksum, exposed tools, install result, discovered skill count, and removal result. Use a fresh conversation to avoid previously loaded skill versions. Verify that the installed host can read `../../resources/host-contract.md`, sibling skills, nested role references, and playbooks through its actual resource API; filesystem link resolution alone does not prove cloud accessibility.
2. Run every workflow case from `tests/workflow-cases.json` on each host. Save actual prompts, observable tool calls, outputs, file/remote changes, and an evidence-based verdict. Do not collect hidden reasoning or claim compliance from model self-report.
3. Compare supported workflows with the pinned upstream intent. Check the preserved stage order, evidence standards, independent verification, and stopping conditions. Evaluate core workflows on real disposable projects, including a failing-before bug repro, a behavior-preserving refactor, an architecture comparison, source-history investigation, and current-head PR review.
4. Verify negative cases: quoted names do not activate explicit-only skills, missing integrations stay gaps, unavailable reviewers are not impersonated, reflect does not change standing skills without approval, babysit does not merge, and upstream text cannot grant external-action permission.
5. Validate the two autopilot variants separately: full requires unavailable runtime capabilities to be reported; stack must never land. Confirm the installation does not promise persistent execution, register MCP servers, run hooks, or ask for hidden credentials.
6. Have a maintainer review the fidelity differences in `docs/design.md`, including the remaining host-specific setup, comment-agent, cleanup, and persistent-runtime differences. Record accepted gaps or implement and test a real adapter before claiming parity.

Do not change `host_validation: not-qualified` merely because static tests pass. Public release remains blocked until this evidence and publisher review exist.
