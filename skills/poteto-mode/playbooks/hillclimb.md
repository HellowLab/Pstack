# Hillclimb

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Ground a realistic workload with how. Reproduce the complaint before choosing a metric. Set direction, target, attempt floor, and resource budget from the user's request or clarify unresolved goals.
2. Build a sensitive harness and vet it with benchmark-checklist. Prove contrasting workloads separate, include error and work counts, establish repeated baseline samples and green regression checks, then freeze the harness.
3. Keep an isolated decision log with hypothesis, change, before, after, delta, tests, kept/reverted, and rationale. Read it before each attempt.
4. Run one hypothesis per attempt. Order performance ideas as in perf-issue. Use isolated workers only when available and permitted. Measure before and after with the frozen harness and rerun the regression gate.
5. Keep only changes that beat noise and preserve correctness; revert others fully. Record every result and make one commit per accepted unit when authorized.
6. At a plateau, revisit the mechanism and try a different category. Never relax the target to claim success. Stop at the agreed predicate, budget, or a demonstrated dead end, reporting the reason.
7. Follow opening-a-pr if authorized. Report metric, target, baseline to final, attempts, accepted changes, decision trail, and best remaining hypothesis.
