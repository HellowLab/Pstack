---
name: figure-it-out
description: "Design an auditable workflow for a large migration or a task without a suitable playbook. Use for /figure-it-out or figure it out."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Figure it out

1. State a falsifiable done condition, scope, uncertainty, and resource budget. Ground the system before designing the run.
2. Sequence small verifiable units, starting with the riskiest unknown. Build the measurement or verification harness first.
3. Record hypotheses, one experiment at a time, observed results, and keep-or-revert decisions with [show-me-your-work](../show-me-your-work/SKILL.md).
4. Run within the user's scope. Stop an unproductive loop to reconsider its premise. Preserve checkpoints when the session cannot continue.
5. Verify the final behavior and report evidence, tradeoffs, unresolved decisions, and what remains. A workflow is not authorization for external actions.
