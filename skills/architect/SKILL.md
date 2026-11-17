---
name: architect
description: "Design types, interfaces, and module boundaries before implementation. Use for /architect, architect this, or design this."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](references/host-contract.md) before acting.

# Architect

Before writing code, trace every system the change touches. Sketch two structurally different designs with types, signatures and module boundaries. Prefer one state owner, one way to perform each task, and the least caller knowledge. Redesign instead of patching when workarounds repeat.

For a large or contested design, use **arena** with the scoped design brief. Two sketches from one agent are not independent exploration. Use only actual permitted workers and accepted model choices; disclose missing independence or model diversity.

Stay within the requested scope. A design-only request produces sketches and a recommendation, not implementation. Honor an explicit user checkpoint before writing implementation. Otherwise continue implementation only when already authorized, using the selected sketch and verifying the result. State open questions rather than inventing settled policies.
