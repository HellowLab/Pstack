# Feature

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Run how over the affected subsystem, then architect for design alternatives.
2. Write the throughput checkpoint: blocking first steps, independent workstreams, shared mutable state, and smallest safe decomposition. Keep inapplicable items with a reason. Separate shared writable state before adding synchronization.
3. Name the data shape before code. Assign the implementation a precise scope and success criteria. Prefer a distinct implementation owner when real delegation is available; otherwise implement directly and disclose the missing independent review. Use arena when multiple valid shapes need comparison.
4. Verify the real user surface. Inconclusive or wrong-surface checks are not passes. Review shared-primitive changes at every consumer.
5. Build, verify, and commit small ordered units when commits are in scope. Use interrogate for contested designs. Follow opening-a-pr only when PR delivery is authorized.

Report behavior built, choices and alternatives, throughput checkpoint, evidence, and open decisions.
