---
name: automate-me
description: "Capture or update the user's working preferences in a personal mode skill. Use for automate me or create/update my mode skill."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Automate me

1. Locate an existing mode skill only in the user-selected project or supplied skill location. Preserve it unless replacement was requested.
2. Use the active conversation and explicitly accessible, in-scope history. Do not search private transcript directories. Ask for examples when evidence is missing.
3. Separate recurring preferences from one-off instructions. Ask a small number of questions about unresolved preferences.
4. Draft one mode skill with a specific description, explicit-only invocation, and concise rules. Use [unslop](../unslop/SKILL.md). Do not encode broader authority than the user granted.
5. Present the draft and iterate. Save to the authorized location. Committing, opening a PR, or installing globally requires the corresponding scope; drafting alone does not authorize those actions.
