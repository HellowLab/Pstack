# Architect

Before writing code, trace every system the change touches. Sketch two structurally different designs with types, signatures and module boundaries. Prefer one state owner, one way to perform each task, and the least caller knowledge. Redesign instead of patching when workarounds repeat.

For a large or contested design, use **arena** with the scoped design brief. Two sketches from one agent are not independent exploration. Use only actual permitted workers and accepted model choices; disclose missing independence or model diversity.

Stay within the requested scope. A design-only request produces sketches and a recommendation, not implementation. Honor an explicit user checkpoint before writing implementation. Otherwise continue implementation only when already authorized, using the selected sketch and verifying the result. State open questions rather than inventing settled policies.
