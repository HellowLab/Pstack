# Reviewed upstream adaptation: 0.15.32

Previous snapshot: `8b3326d99fd4b993cb33a24dad8af03175c642c5`.
Reviewed snapshot: `9580c23696ac8d7abed0c166f2f9918800afb819`.
Reviewed subtree: `880564357e051d7c7802da1cb5d8df1d0b008299`.
[Upstream comparison](https://github.com/cursor/plugins/compare/8b3326d99fd4b993cb33a24dad8af03175c642c5...9580c23696ac8d7abed0c166f2f9918800afb819)

All 47 changed/added/deleted sources and subtree identity received static review. No vendored code was executed. No file mode changes were imported.

| Source | Review and disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Source-only upstream version metadata; portable package version remains adapter-owned. |
| `README.md` | Source-only discovery/update guidance; ketchup-video route adapted without importing Claude/Cursor update commands. |
| `docs/guide/10-recipes-and-pitfalls.md` | Source-only discovery/update guidance; ketchup-video route adapted without importing Claude/Cursor update commands. |
| `plugin.json` | Source-only upstream version metadata; portable package version remains adapter-owned. |
| `skills/create-formal-verification-skill/SKILL.md` | Adapted. Named statechart handoff with no copied commands or runtime promises. |
| `skills/ketchup-video/SKILL.md` | Adapted. New guarded video recap with capability checks, source artifacts, inspected frames and calls-only failure fallback. |
| `skills/poteto-help/SKILL.md` | Adapted. Discover guarded ketchup-video and broaden statechart routing. |
| `skills/poteto-mode/scripts/check-plan.mjs` | Source-only multi-backtick parsing correction; portable plan contract updated. |
| `skills/poteto-mode/scripts/check-plan.test.ts` | Source-only multi-backtick, following prose and unmatched delimiter cases. |
| `skills/poteto-mode/scripts/orch/orch.test.ts` | Source-only sole-open-PR preference and ambiguous-active rejection; portable stack guidance updated. |
| `skills/poteto-mode/scripts/orch/store.ts` | Source-only sole-open-PR preference and ambiguous-active rejection; portable stack guidance updated. |
| `skills/poteto-mode/scripts/watch-pr/github.test.ts` | Source-only repository-qualified stack identity and capped-deadline polling/types/tests; supported manual guidance updated. |
| `skills/poteto-mode/scripts/watch-pr/github.ts` | Source-only repository-qualified stack identity and capped-deadline polling/types/tests; supported manual guidance updated. |
| `skills/poteto-mode/scripts/watch-pr/policy.test.ts` | Source-only repository-qualified stack identity and capped-deadline polling/types/tests; supported manual guidance updated. |
| `skills/poteto-mode/scripts/watch-pr/policy.ts` | Source-only repository-qualified stack identity and capped-deadline polling/types/tests; supported manual guidance updated. |
| `skills/poteto-mode/scripts/watch-pr/types.ts` | Source-only repository-qualified stack identity and capped-deadline polling/types/tests; supported manual guidance updated. |
| `skills/poteto-mode/scripts/worktree-audit.sh` | Source-only GNU/BSD stat/date correction; private transcript scanning is not imported. |
| `skills/reflect/SKILL.md` | Adapted. Protect installed/cache files, show approved local-copy destination and prohibit implicit PR/push. |
| `skills/statechart/SKILL.md` | Adapted. Broaden to product/protocol/service/design; preserve rule/replay evidence and distinguish goals, omissions, mixed states and temporal limits. |
| `skills/statechart/scripts/bug-states.mjs` | Source-only unsupported. First failures, clean reachability and mixed/after statuses. |
| `skills/statechart/scripts/chart-edges.mjs` | Source-only unsupported. Numbered paths, divergence and reduced overview. |
| `skills/statechart/scripts/chart-parts.mjs` | Source-only unsupported. Shared edge IDs, guard labels and chart configuration. |
| `skills/statechart/scripts/chart-to-tla.mjs` | Source-only unsupported. CLI simplification and empty transition relation FALSE. |
| `skills/statechart/scripts/compare-charts.mjs` | Source-only unsupported. Self-loop comparison and explicit exclusions. |
| `skills/statechart/scripts/lib.mjs` | Source-only unsupported. Tuple identity, heuristic provenance/dependencies, PROPERTY interpretation and partial failures. |
| `skills/statechart/scripts/map-view.mjs` | Source-only unsupported. Tuple proxies and global structuredClone replacement. |
| `skills/statechart/scripts/model/OutputFolder.cfg` | Deletion reviewed; removed output-folder model is not retained as proof of current publishing. |
| `skills/statechart/scripts/model/OutputFolder.map.mjs` | Deletion reviewed; removed output-folder model is not retained as proof of current publishing. |
| `skills/statechart/scripts/model/OutputFolder.tla` | Deletion reviewed; removed output-folder model is not retained as proof of current publishing. |
| `skills/statechart/scripts/property-loop.mjs` | Source-only unsupported. Temporal loop/stuttering summaries. |
| `skills/statechart/scripts/read-check.mjs` | Source-only unsupported. Cross-model shape/type and missing-field checks. |
| `skills/statechart/scripts/regions-chart.mjs` | Source-only unsupported. Region reduction and bounded graph equivalence. |
| `skills/statechart/scripts/render.mjs` | Source-only unsupported. npm installation, native renderer/font dependencies and raster limits. |
| `skills/statechart/scripts/rule-book.mjs` | Source-only unsupported. EXTENDS/INSTANCE rule provenance and substitutions. |
| `skills/statechart/scripts/second-replay.mjs` | Source-only unsupported. Model-path replay and divergence; not real-code replay. |
| `skills/statechart/scripts/snapshot.mjs` | Source-only unsupported. Limited regex dependency discovery and input copies; not a complete frozen-input guarantee. |
| `skills/statechart/scripts/spec-text.mjs` | Source-only unsupported. Generated rule modules and mapping scaffolds. |
| `skills/statechart/scripts/statechart-help.mjs` | Source-only unsupported. Runtime command documentation and limitations. |
| `skills/statechart/scripts/statechart.mjs` | Source-only unsupported. Orchestration, checking, snapshots, rendering and output replacement. |
| `skills/statechart/scripts/test/band.mmd` | Source-only unsupported. Composite-boundary fixture. |
| `skills/statechart/scripts/test/regions.mmd` | Source-only unsupported. Parallel-region fixture. |
| `skills/statechart/scripts/test/statechart.test.mjs` | Source-only unsupported. Complete large test diff including rendering, config, mapping, graph and output safety cases; never executed. |
| `skills/statechart/scripts/tlc-to-chart-args.mjs` | Source-only unsupported. Extracted CLI parsing. |
| `skills/statechart/scripts/tlc-to-chart.mjs` | Source-only unsupported. Chart/status/story generation and helper integration. |
| `skills/statechart/scripts/tlc-tools.mjs` | Source-only unsupported. Automatic mise Java/TLC installation remains excluded. |
| `skills/statechart/scripts/ways-in.mjs` | Source-only unsupported. Entry-step counts versus shortest witnesses. |
| `skills/swarm/SKILL.md` | Adapted. Result-table wording; retain existing worker count, host model and isolation safeguards. |

All 26 remaining statechart support files are excluded from distribution. Automatic Java/TLC/mise/npm installation, executable live mappings, native rendering and runtime concurrency claims remain unsupported. Copy-based publication still has overlap limitations; dependency discovery is heuristic. Removed model files do not establish a proof of current code.

The initial 69-test run failed nine pending-adaptation checks. Those candidate placeholders are not released 0.1.11 regressions. The raw-outcome summary and final failure gate correctly reported an unqualified candidate; no checks or permissions were bypassed.

The package represents 58 skills and 23 routes. Static contract coverage checks new boundaries but does not qualify actual model behavior, video rendering, native installation, TLC or PNG inspection. Historical stable archives, attribution and host contracts are preserved.
