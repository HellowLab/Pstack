---
name: principle-guard-the-context-window
description: "Manage large context and outputs without losing evidence. Apply when context is filling up."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](references/host-contract.md) before acting.

# Principle guard the context window

Read targeted source ranges, search before loading whole files, and keep compact evidence-linked summaries. Use actual permitted subagents for large independent slices when available; otherwise process bounded slices sequentially. Keep frequently used instructions near their consumers. Preserve decision state and artifact paths before handoff. Do not claim delegated inspection when none occurred.
