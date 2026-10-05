# Blast radius

1. Read the diff and affected contracts. Trace callers, serialized data, external consumers, lifecycle ordering, pinned dependencies, and flags.
2. State the one or two facts on which safety depends. Trace actual source and history; do not invent callers from names.
3. Prove those facts with the smallest executable check using the real code, then the actual app where feasible. A source citation alone is not runtime proof.
4. Use [arena](../arena/SKILL.md) for a wide change when appropriate, subject to available capabilities.
5. Report changed behavior, proven and unproven safety facts, evidenced risks, cleared risks, and the cheapest remaining check. Sanitize evidence before public output.
