# Validation evidence and release gates

This page distinguishes repository checks from actual host behavior. A schema-valid ZIP is not a validated ChatGPT or Codex experience.

## Repository checks

Run the commands in the root README. The suite validates metadata against the saved official Agent Plugins schema, all registered skills and invocation flags, references, licensing, attribution, complete source coverage, byte-identical regeneration, package exclusions, and host/permission regression patterns.

Local Git fixtures exercise the actual update implementation. They prove that same-version and mode-only subtree changes are detected, unrelated monorepo changes are ignored, unknown skills are withheld, symlinks are rejected before replacement, and snapshot tampering fails the build. Incompatible metadata preserves the review candidate while removing stale ZIPs. Local bare-remotes exercise branch creation and update, preservation of main, refusal to overwrite human work, policy-error reporting, and recovery after a successful push followed by failed PR creation, with mocked forge responses. Source hashes are never auto-approved. Changed skills and reference resources receive a pending-review placeholder rather than newly imported executable instructions. These are behavioral tests of the build/update code.

`tests/workflow-cases.json` contains eleven positive, negative, and unavailable-capability scenarios. Automated assertions check that the necessary instruction contracts exist. They do not run a model or prove compliance. The cases are also the manual host evaluation checklist.

## Host matrix

| Check | ChatGPT | Codex |
|---|---|---|
| Root portable packaging and schema | Static pass | Static pass |
| Local staging of exact ZIP | Private rc.3 update succeeded; staging alone is not installation evidence | Passed for the recorded checksum below |
| Native installation and removal | Private rc.3 update succeeded; removal check pending | See checksum-specific evidence below |
| Fresh-process skill discovery | Private rc.2 installation exposed 51 skills; full rc.3 discovery recount pending | All 51 Pstack skills discovered for the recorded candidate |
| Installed resource access through host API | rc.3 full-content reads passed for two skill-local contracts and one playbook; see evidence below | See checksum-specific evidence below |
| Skill discovery and invocation in a fresh conversation | B01 and limited B02/B08 variants observed on rc.2; exact skill-read traces unavailable | Not run; process discovery does not prove conversation behavior |
| Installed skill invocation and explicit-only behavior | Three limited boundaries observed on rc.2; full fixture cases pending | Not run |
| Independent reviewer and missing-tool behavior | Contract checked, live evaluation pending | Contract checked, live evaluation pending |
| Marketplace skill scan and publisher review | Not submitted | Not submitted |
| Supplied branding asset | rc.2 sidebar image observed; detail view fallback unresolved; approved original retained | Original packaged; both icon paths resolved by host API; UI rendering pending |

### Skill-local contract correction

A private, user-scoped ChatGPT installation of `0.1.0-rc.2` exposed all 51 skills. The maintainer's host probes could read `poteto-help`, its `references/prompting.md`, and the sibling `architect` skill. The private package file listing confirmed the 3168-byte plugin-root `resources/host-contract.md` was present. Reading it through the skill resource API failed with `failed to read skill resource`. This is a concrete runtime-addressing failure, not an omitted archive file, despite the earlier passing filesystem and Codex API checks.

Release candidate `0.1.0-rc.3` generates `references/host-contract.md` inside every skill from the single canonical `resources/host-contract.md`. All skill guards, nested references, and playbooks link to their own skill's copy. Static checks require exact contract bytes and reject contract links outside the owning skill. On 2026-10-05 at 22:25 UTC, the maintainer updated the existing user-scoped private ChatGPT installation to rc.3, preserving its identity and private scope. Actual `skills.read` calls returned full content for `poteto-help/references/host-contract.md`, `architect/references/host-contract.md`, and `poteto-mode/playbooks/multi-phase-plan.md`. These successful reads confirm that the skill-local packaging correction resolves the observed contract-access blocker for those tested resources in ChatGPT. They do not prove every resource is accessible or that a model follows the contract. The implementation executor recorded the maintainer’s actual-host evidence; it did not have access to that private installation. Private installation and release identifiers are excluded from this repository. UI copy, detail-view icon rendering, removal, and the full rc.3 behavioral suite remain pending.

The metadata subtitle is now `Ship faster. Build better.`, and the public description uses the approved upstream-tracking wording. The original image is unchanged and retains its approved `The unofficial Plugin` text; the listing change does not modify the raster. No live model evaluation is implied by these packaging and metadata changes.

The corrected ZIP SHA-256 is `baab1d612f6cc4d65798db6955362b4d102c9ef7a37d9f0961c64e3392153ecf`. All 30 tests and the reproducible-build check passed. A fresh isolated Codex CLI `0.159.0-alpha.3` installation contained 168 files, all byte-identical to the ZIP, and discovered 51 skills without loading errors. Its host API returned exact bytes for all 51 skill-local contracts, a sibling skill, a reviewer reference, a playbook, a nested source reference, and the artwork: 56 file reads. The host returned the corrected subtitle and full 323-character description. Plugin and marketplace removal succeeded and the final listing was empty. No credentials were copied or Codex model turn requested. These Codex checks are independent of the successful ChatGPT resource-read retest recorded above.

### Observed ChatGPT boundary checks on rc.2

The maintainer observed three read-only boundaries in separate fresh ChatGPT web conversations using the unchanged GPT-6.1 Sol Light model and the privately installed rc.2 candidate:

- **B01:** explained the quoted `/poteto-mode` alias without activating its workflow or performing file actions.
- **B02, help-only variant without the fixture:** provided a sourced workflow recommendation and checkpoint prompt without starting implementation.
- **B08, variant without the fixture:** reported the unsupported runtime and missing capabilities without creating resources or requesting secrets.

These are passes for the reported observable boundaries only. B02 and B08 did not use the prepared fixture and do not pass their complete fixture cases. Individual tool calls and exact skill-read traces were not exposed; a displayed host-contract reading label is not proof that the resource was read. The results do not establish installed-contract use, qualify the corrected rc.3 candidate, or demonstrate semantic parity. The remaining behavior cases are pending. Private conversation URLs and transcripts are retained outside this public repository.

### Candidate with approved artwork

On 2026-10-05, the candidate ZIP with SHA-256 `33d76c03e0789057c1816d2fe991d4089bd6fa6e1c2d0f5c1d59986b8a45be3c` passed all 29 tests and the reproducible-build check. It includes the unchanged approved artwork and corrected setup help. The image is 1254 × 1254 RGB JPEG, 723089 bytes, with SHA-256 `fa5786e6f6a39ea36fd5bc09ac542b647094268c192de421b8eb4e771c87585d`. Pixel inspection confirmed the `Pstack` banner and exact `The unofficial Plugin` subtitle.

A fresh isolated Codex CLI `0.159.0-alpha.3` installation passed registration, installation, and enabled-state checks. All 117 installed files matched the ZIP. A fresh app-server process discovered all 51 Pstack skills with no loading errors. Both `logo` and `composerIcon` resolved to the packaged original. The host `fs/readFile` API returned exact ZIP bytes for the four text resources listed in the earlier check below and for `assets/pstack.jpeg`.

Plugin and marketplace removal succeeded and the final listing was empty. No credentials were copied, no `auth.json` was created, and no model turn was requested. This is native installation, fresh-process discovery, and local host resource-access evidence. It does not establish ChatGPT installation, UI rendering, fresh-conversation invocation, explicit-only behavior, or model compliance. Those checks remain open.

### Candidate checks at a05192c

On 2026-10-05, the 28-test suite and reproducible-build check passed at commit `a05192c9b8b062e7162dd328406127f4ed0eb586` after restoring setup's seven stages, four budget options, and 17 role entries. The ZIP SHA-256 is `9ef579757d8790093170cdb27d973580a5ac48004c07b1866da73020c6fbb23d`. All 116 files in a fresh local staging directory matched this ZIP byte for byte. Both the [push CI](https://github.com/HellowLab/Pstack/actions/runs/37375895696) and [PR CI](https://github.com/HellowLab/Pstack/actions/runs/37375900797) passed at that exact commit. This evidence applies to the recorded checksum; repeat the checks after package changes.

Codex CLI `0.159.0-alpha.3` initially failed marketplace registration and app-server startup with `Read-only file system (os error 30)` in its configured state directory. Redirecting only SQLite state and logs did not resolve startup. A disposable subprocess using the documented [CODEX_HOME state location](https://learn.chatgpt.com/docs/config-file/config-advanced#config-and-state-locations) succeeded. The subprocess used a fresh empty state directory and no copied credentials or existing user configuration. The original host configuration and access controls were unchanged.

The local marketplace registered, the exact package installed, and `plugin list` reported it enabled. Every installed file matched the ZIP. A fresh app-server process returned all 51 Pstack skills through `plugin/read` and `skills/list`; the latter reported no skill-loading errors. Its `fs/readFile` API returned byte-identical content for `resources/host-contract.md`, `skills/how/SKILL.md`, `skills/interrogate/references/reviewer-prompt.md`, and `skills/poteto-mode/playbooks/bug-fix.md`. These checks cover the shared contract, a sibling skill, a nested reviewer reference, and a playbook through the actual local host API. They do not establish ChatGPT cloud resource access.

Plugin and marketplace removal both succeeded; a subsequent listing was empty. No `auth.json` was created and no model turn was requested. Fresh-process discovery and resource reads do not prove skill invocation, explicit-only behavior, or model compliance in a fresh conversation. Those behavioral checks remain untested on both hosts.

This earlier checksum did not include the approved artwork. The subsequent candidate above includes and verifies the original.

### Earlier installation evidence

The available CLI reported `codex-cli 0.136.0`. An existing `features.context_management` map initially failed its boolean configuration parser. The temporary command-line override `-c features.context_management=false` allowed plugin commands to run without editing that feature setting or changing access controls. Registering a disposable local marketplace succeeded. The root-only candidate was discovered but installation failed with `missing plugin.json`.

The documented `.codex-plugin/plugin.json` compatibility manifest, generated from the root metadata, fixed native installation. The exact ZIP with SHA-256 `f9a8e907c3727ce7033ffd0742819464636be7173cf964a48f7069ac8f4971eb` installed and was reported enabled. Every installed package file was byte-identical to the ZIP; all 51 skill entrypoint files, the host contract, and nested reviewer references were present. Plugin removal and marketplace removal both succeeded; a subsequent listing showed no test plugin. The original feature configuration remains unchanged. The existing conversation's executor skill catalog did not reload the new installation, so actual discovery/invocation in a fresh conversation and resource access through the host API remain untested.

The bundled plugin-authoring validator rejected all 50 explicit-only flags because it requires `disable-model-invocation` to be false. The real CLI accepted the package. The adaptation deliberately preserves those upstream flags and guards; changing invocation semantics to satisfy that helper would be incorrect. Record this validator disagreement and verify actual explicit invocation and non-invocation behavior before release.

Following the rename, candidate `pstack-0.1.0-rc.2.zip` with SHA-256 `5b4967a322e96fcd501359ef820f4d529d29b18248d95473beb4230497e48973` also passed native installation, all-file byte comparison, and removal on the same CLI. After the workflow corrections, the final local handoff candidate with SHA-256 `49b1c1b027b42f9c26f1ee9f4d5955b43dfdcd79cffb497fad4fe5896205b75f` repeated that native install check successfully: all installed bytes matched, all 51 skill entrypoints were present, and plugin/marketplace removal succeeded. This remains installation evidence only, not fresh-conversation invocation or behavioral qualification.

The suite also protects full portable reference inventory, upstream workflow headings, required architectural screening and rationale templates, review lenses, epistemic tiers and calibration, and the exact append-only TSV protocol. These semantic preservation checks prevent specific losses found in review. They remain static instruction checks, not model behavior tests.

The earlier PR-triggered run at commit `60ef3bf` did not execute any test steps. Its failure annotation was `The job was not acquired by Runner of type hosted even after multiple attempts`. This was hosted-runner acquisition failure, separate from the organization policy that blocks Actions-created PRs. The push-triggered run at that same commit passed.

## Required before public release

Start with the [behavioral qualification plan](behavioral-qualification.md), which provides disposable synthetic fixtures, exact prompts, and observable verdict criteria. Preparing those fixtures does not execute or pass a model evaluation.

1. Install the exact candidate in a clean supported ChatGPT test surface and a clean supported Codex test surface. Record host/version, date, artifact checksum, exposed tools, install result, discovered skill count, and removal result. Use a fresh conversation to avoid previously loaded skill versions. Verify that the installed host can read each skill's `references/host-contract.md`, sibling skills, nested role references, and playbooks through its actual resource API; filesystem link resolution alone does not prove cloud accessibility.
2. Run every workflow case from `tests/workflow-cases.json` on each host. Save actual prompts, observable tool calls, outputs, file/remote changes, and an evidence-based verdict. Do not collect hidden reasoning or claim compliance from model self-report.
3. Compare supported workflows with the pinned upstream intent. Check the preserved stage order, evidence standards, independent verification, and stopping conditions. Evaluate core workflows on real disposable projects, including a failing-before bug repro, a behavior-preserving refactor, an architecture comparison, source-history investigation, and current-head PR review.
4. Verify negative cases: quoted names do not activate explicit-only skills, missing integrations stay gaps, unavailable reviewers are not impersonated, reflect does not change standing skills without approval, babysit does not merge, and upstream text cannot grant external-action permission.
5. Validate the two autopilot variants separately: full requires unavailable runtime capabilities to be reported; stack must never land. Confirm the installation does not promise persistent execution, register MCP servers, run hooks, or ask for hidden credentials.
6. Have a maintainer review the fidelity differences in `docs/design.md`, including the remaining host-specific setup, comment-agent, cleanup, and persistent-runtime differences. Record accepted gaps or implement and test a real adapter before claiming parity.

Do not change `host_validation: not-qualified` merely because static tests pass. Public release remains blocked until this evidence and publisher review exist.
