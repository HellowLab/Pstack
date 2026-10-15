# Reviewed upstream adaptation, October 15

Pstack 0.15.24 to 0.15.25, commit `e5136d82418d2db3165ea1050d17577cd618cc05`. All 11 changed source files and the subtree identity were inspected. The twelfth review gap is the tree assertion, not another file. No vendored helper was executed.

- Source manifests only change the upstream version; package listing metadata remains adapter-owned.
- README and principle-guide summaries align with the revised principles, not new host capabilities.
- Correct now judges tests against observable behavior and internal refactors rather than a blanket undefined-return heuristic; preserve its portable source body.
- Ketchup explains changes with captured visuals and relationship diagrams, not disconnected status boxes. Its text budget excludes visuals; status and action items remain plain bullets. Keep current-chat/read-only scope, actual evidence, unknown-responsibility honesty and unavailable-renderer fallback.
- Poteto-mode's principle index matches the revised leaf skills.
- Attack the Premise tests a falsifiable observation directly before another fix, distinguishing contrary and confirming evidence rather than assuming per-actor skew is always the cause.
- Fix Root Causes distinguishes legitimate state needing handling from invalid state whose producer must be fixed. Keep reproduction, instrumentation, and actual-state evidence.
- Make Operations Idempotent derives actions from observed state and requires reliable stale-artifact evidence across interruption points, replacing the overly specific PID-only-lock prescription.
- Test Behavior evaluates both broken-behavior and internals-only edits. External side effects, absence paired with a positive case, and invariant checks can be meaningful contracts; internal helper calls are not equivalent evidence.

All changed skills preserve explicit invocation and local host contracts. New workflow cases are static content-contract checks, not model-behavior qualification. Persistent runtimes and helpers remain excluded. All previously released ZIPs/checksums and submitted rc.5 are preserved exactly; only the new 0.1.4 archive is generated.

Changed files:

- `.cursor-plugin/plugin.json`
- `README.md`
- `docs/guide/08-principles.md`
- `plugin.json`
- `skills/correct/SKILL.md`
- `skills/ketchup/SKILL.md`
- `skills/poteto-mode/SKILL.md`
- `skills/principle-attack-the-premise/SKILL.md`
- `skills/principle-fix-root-causes/SKILL.md`
- `skills/principle-make-operations-idempotent/SKILL.md`
- `skills/principle-test-behavior-not-implementation/SKILL.md`
