# Perf issue

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Capture a representative baseline trace on the affected surface. Vet every reported number with benchmark-checklist.
2. Ground hypotheses with how. Try, in order: eliminate unused work, reuse results, do less, defer work, move it off the critical path, parallelize, then make it cheaper. Stop when the agreed target is met.
3. Design from the trace, use architect for boundary changes, and implement one evidence-backed attempt at a time. Review the diff and capture a post-change trace.
4. Compare actual artifacts and run regression checks. An inconclusive measurement is not a win. Revert ineffective or incorrect changes.
5. Follow opening-a-pr if authorized. Report baseline, after value, units, delta, and evidence paths. Use hillclimb for sustained optimization rather than a one-off fix.
