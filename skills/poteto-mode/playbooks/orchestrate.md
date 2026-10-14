# Orchestrate

Read [the host contract](../references/host-contract.md) before acting.

This upstream standing-program workflow depends on a persistent orchestration store, worker lifecycle controls, scheduling, and cloud-agent behavior. Those helpers are not part of this skills-only package. Full unattended orchestration is unsupported until an explicit host adapter is implemented and tested.

Preserve the program design: one coordinator owns topology and landing; isolated workers own assigned implementation; independent verifiers own evidence. Track exact revisions, dependencies, phase gates, liveness, and stop orders. Worker reports never authorize merges or access changes.

For an in-session task, use figure-it-out and swarm only within available capabilities, and label it an in-session adaptation. For a multi-day program, deliver the plan, capability requirements, and blocking gaps. Do not pretend a Markdown checklist replaces the durable upstream orchestration service.
