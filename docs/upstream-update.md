# Reviewed upstream adaptation: 0.15.30

Previous snapshot: `88d47514b82e7c44f00f2b2a72ff6dd12158038c`.
Reviewed snapshot: `eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10`.
Reviewed subtree: `d08bf3a76c8f3bdaeb9af65c98344c85a304fb63`.
[Upstream comparison](https://github.com/cursor/plugins/compare/88d47514b82e7c44f00f2b2a72ff6dd12158038c...eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10)

All 17 changed/new sources and subtree identity were statically reviewed. Upstream code was treated as source data, not executed.

| Source | Review and disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Version-only bump; source-only Cursor manifest. |
| `plugin.json` | Version-only bump; portable manifests remain adapter-owned. |
| `README.md` | Adds statechart discovery; adapted without claiming bundled tools. |
| `docs/guide/06-verify-and-ship.md` | Describes model/chart round trips and replay; source-only guide, with supported concepts adapted and tool limitations disclosed. |
| `skills/poteto-help/SKILL.md` | Adds guarded statechart routing; preserves setup consent and sharpen rewrite-only behavior. |
| `skills/statechart/SKILL.md` | Adapt explicit user-visible chart/model review, invariants, separate baseline/fix models, numbered counterexamples, real-code replay and bounded claims. Missing tooling yields unverified drafts. |
| `skills/statechart/scripts/statechart.mjs` | Source-only: invokes Java/TLC, dynamically imports mappings, replaces output folders, writes beside inputs and calls unpinned `npx -y @mermaid-js/mermaid-cli`. None is packaged or executed. |
| `skills/statechart/scripts/chart-to-tla.mjs` | Source-only: restricted Mermaid translation writing named TLA/config/mapping files. Manual drafts do not inherit its synchronization claims. |
| `skills/statechart/scripts/tlc-to-chart.mjs` | Source-only: executable mappings and bounded TLC graph/trace conversion to charts, stories and counts. No fabricated output artifacts. |
| `skills/statechart/scripts/lib.mjs` | Source-only parsing, reachable-state comparison, TLC completion checks and chart styling. |
| `skills/statechart/scripts/compare-charts.mjs` | Source-only reachable-state/transition comparison with exclusions including self-loops; not an exhaustive application-equivalence proof. |
| `skills/statechart/scripts/model/OutputFolder.tla` | Source-only safe-output/concurrency model, not proof about this adapter. |
| `skills/statechart/scripts/model/OutputFolder.cfg` | Source-only finite model configuration and invariants. |
| `skills/statechart/scripts/model/OutputFolder.map.mjs` | Source-only executable labels/mapping module. |
| `skills/statechart/scripts/test/statechart.test.mjs` | Source-only suite spawning Node/Java, compiling C interception shims, using LD_PRELOAD/Linux namespace attempts and filesystem/process races. Not run. |
| `skills/statechart/scripts/test/sync.mmd` | Source-only parallel-region fixture. |
| `skills/statechart/scripts/test/upload.mmd` | Source-only composite-transition fixture. |

All 11 helper/model/test files stay out of the distributable ZIP. The portable skill retains code grounding, unchanged baseline specs, invariant agreement without weakening, actual-tool checks, honest replay/rendering gaps and evidence-backed counts. Existing license, attribution and host/permission contracts remain unchanged. No executable mode changes are imported.

The initial candidate's 67-test run had four failures: new skill inventory, missing source classification and two help assertions against a pending-review stub. These were candidate review gaps, not released 0.1.9 regressions. `continue-on-error` makes the validation step's conclusion look successful so a draft can be created; its raw outcome failed and the workflow's final adaptation gate correctly failed the run. The separate initial PR run was action-required with no validation evidence. Neither state is a passing qualification result.

Version 0.1.10 retains 23 routes and represents 57 skill entry points. Static contract and package tests do not establish native installation, model behavior, Java/TLC execution or PNG inspection. Those checks were not run.
