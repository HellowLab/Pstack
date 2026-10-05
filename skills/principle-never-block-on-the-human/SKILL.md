---
name: principle-never-block-on-the-human
description: "Proceed with authorized reversible work while respecting scope and approval boundaries. Apply when considering an unnecessary permission question."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](references/host-contract.md) before acting.

# Principle never block on the human

Make reasonable implementation decisions within the user's authorized scope and present concrete results. Continue independent work when one step is blocked. Reversibility does not itself authorize external actions, messages, record updates, publishing, merging, or access changes. Respect explicit checkpoints and the host's permission rules. Ask only for missing intent or authorization needed for the next dependent action.
