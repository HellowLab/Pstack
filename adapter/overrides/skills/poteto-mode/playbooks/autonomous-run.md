# Autonomous run

Read [the host contract](../references/host-contract.md) before acting.

1. State a checkable exit predicate and resource limits before iteration.
2. Use an available event or wait mechanism during this session. Persistent recurrence requires a supported scheduler and user authorization. No host-neutral background loop is bundled.
3. Make one evidence-backed change, verify, keep or revert, and log the result with show-me-your-work. Verify each unit before starting the next.
4. Address related discoveries only within scope; prepare follow-up proposals otherwise. Continue independent authorized work at a blocker.
5. Stop when the predicate is met, the agreed budget is exhausted, the user stops work, or a concrete blocker prevents progress. Never weaken the predicate to call the task complete.
6. Report predicate, attempts, retained and discarded work, current state, and durable handoff.
