---
name: no-comments
description: "Review comments and replace misleading explanations with clearer code where appropriate. Use for /no-comments or a comment review."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# No comments

1. Scope the supplied files or current diff. Read comments in their source context.
2. Identify redundant narration, stale claims, and comments concealing avoidable complexity. Preserve licenses, required attribution, externally imposed constraints, and useful explanations of non-obvious behavior.
3. Verify claimed constraints before deletion. Do not erase safety suppressions or behavior contracts merely to satisfy a comment count.
4. Apply authorized, in-scope cleanup. Use [architect](../architect/SKILL.md) for structural changes. Propose out-of-scope fixes separately.
5. Report deletions, retained constraints, code changes, tests, and open questions. A separate comment-review agent is optional and must actually exist to be credited.
