# Reviewed upstream adaptation: 0.15.30, revised statechart evidence

Previous snapshot: `eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10`.
Reviewed snapshot: `8b3326d99fd4b993cb33a24dad8af03175c642c5`.
Reviewed subtree: `ed6351a9f6ec6e18cc2dbf2ba673effa33f3c9fe`.
[Upstream comparison](https://github.com/cursor/plugins/compare/eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10...8b3326d99fd4b993cb33a24dad8af03175c642c5)

The version remains 0.15.30. All five changed sources and subtree identity were statically reviewed; no vendored helpers were executed and no source file additions, removals or mode changes were imported.

| Source | Review and disposition |
|---|---|
| `skills/statechart/SKILL.md` | Adapt baseline authors' passing config, shared-variable labels, condition-level file/line citations, observable rules, real-entry-point replay, copied-code provenance and known-baseline issue classification. Preserve explicit invocation and missing-tool limits. |
| `skills/statechart/scripts/lib.mjs` | Source-only: heuristic condition-citation scanning and partial TLC-output handling. Citations and parser output are not proof of semantic fidelity or complete verification. |
| `skills/statechart/scripts/statechart.mjs` | Source-only: explicit configs, separate temporal-property checks, unchecked-rule warnings and copy-based publish fallback. The fallback can produce mixed output under overlap; no runtime or concurrency guarantees are imported. |
| `skills/statechart/scripts/tlc-to-chart.mjs` | Source-only: rejects invented missing-variable values and distinguishes unchecked rules. Charts omit temporal-property failures, which the adapted guidance requires reporting separately. |
| `skills/statechart/scripts/test/statechart.test.mjs` | Source-only test changes cover config/property behavior, provenance, mapping guards, failure preservation and filesystem fallback. Native/Node/Java test machinery was not run. |

All 11 upstream support files remain excluded from the ZIP. The portable workflow does not invoke Node/TLC, install a renderer or execute upstream mappings. Omitted comparison rules mean not checked, not fixed. Partial or crashed checker output cannot justify exhaustive success. Model bounds, unavailable evidence and copied-code omissions remain explicit.

The initial 68-test candidate run had three real failures: pending source review, guarded statechart description and workflow contracts against the pending stub. These were candidate gaps, not released 0.1.10 regressions. `continue-on-error` allowed draft creation while the raw outcome and final gate failed. The scheduled workflow now writes that raw outcome into its summary, including a clear not-qualified result for failure, skipped or cancelled validation; it retains the final failure gate. A behavioral shell test covers each summary outcome and verifies the gate exits nonzero.

The package retains 57 skill entry points and 23 routes. Source hash approval followed review and adaptation. Attribution, licenses, host contracts, historical stable archives and release guards remain unchanged. Native installation, actual model behavior, TLC execution and PNG inspection were not qualified.
