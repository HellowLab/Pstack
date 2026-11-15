---
name: why
description: "Investigate why code or a design exists using available evidence. Use for why does X work this way, design rationale, regressions, or postmortems."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](references/host-contract.md) before acting.

# Why

Answer from the record, not the code: read the commits and PR discussions that introduced the target and each later change, and other sources if the trail is thin. Cite what the authors wrote, mark your own inferences as inferences, and say what the record does not answer.

Remain read-only, use only authorized sources actually available in the host, and report missing evidence rather than guessing.
