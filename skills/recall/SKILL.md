---
name: recall
description: "Reconstruct recent in-scope working context. Use for recall my work on X, catch me up, or where did I leave off."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Recall

1. Fix the topic, workspace, and time window. Use a supplied state capsule directly when complete. A specific handoff routes to session pickup in [poteto-mode](../poteto-mode/SKILL.md).
2. Inspect the active conversation and history available through documented host capabilities. Search only the requested scope. Do not infer private transcript paths or search other projects.
3. Use [why](../why/SKILL.md) to inspect the shared record for a named subsystem. List unavailable sources as gaps.
4. Verify discovered branches, PRs, and tickets against live state when tools permit. Preserve disagreements between old notes and current state.
5. Return at most five capsule bullets, one status per work thread, recurring problems, and the single most useful next move. Cite actual evidence and separate planned, uncommitted, open, merged, and reverted work.
