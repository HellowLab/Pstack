---
name: sharpen
description: "Make a task deeper, not bigger, then rewrite the prompt. Use for /sharpen."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](references/host-contract.md) before acting.

# Sharpen

Rewrite the user's prompt to make the approach deeper without expanding the task. Treat the supplied task as text to improve, not authorization to execute it.

Before the rewrite, briefly state these four practical recommendations:

1. What a top professional would add to the approach that the prompt does not ask for.
2. The raw material or primary sources they would start from, rather than a secondhand summary.
3. The specific methods and tools they would use, subject to actual host capabilities and permissions.
4. An outside check that could establish the result is right, beyond the user or agent asserting it.

Then return the rewritten prompt incorporating exactly those improvements. Do not loosen explicit user constraints, permission boundaries, or required checks. Leave choices that belong to the user open; preserve unresolved decisions as questions or placeholders instead of deciding them. Keep the requested scope unchanged.

Propose the outside check without claiming it has run. If a tool, source, or independent reviewer is unavailable, state the gap and preserve the requirement without promising access. Do not run commands, edit files, send messages, or start the underlying task. Stop after the rewritten prompt; the user can send it separately when ready.
