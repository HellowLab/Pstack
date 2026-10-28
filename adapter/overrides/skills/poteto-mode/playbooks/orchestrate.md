# Orchestrate

Read [the host contract](../references/host-contract.md) before acting.

Full unattended orchestration is unsupported without a tested host adapter. Upstream removed its custom orch CLI and now relies on host-owned task tracking, durable state and event subscriptions. No orchestration runtime is bundled here.

The coordinator owns assignments and topology, not implementation. Give each PR one isolated branch writer and a self-contained brief with the user’s goal, scope, exact revision and acceptance evidence. Independent verifiers return actual current-head evidence. Reconcile late results against the current head and bound retries; a stale result never authorizes landing. Merge only within explicit authority after all required gates pass.

For available in-session workers, use figure-it-out or swarm within their host contracts. For a multi-day program, provide the plan and name missing lifecycle, durable-state and scheduler capabilities. Do not pretend a Markdown checklist supplies those capabilities or invent background subscriptions.
