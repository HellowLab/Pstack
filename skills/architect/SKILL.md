---
name: architect
description: "Design types, interfaces, and module boundaries before implementation. Use for /architect, architect this, or design this."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Architect

1. Ground the affected system with [how](../how/SKILL.md). Use [why](../why/SKILL.md) when ownership or layering changes.
2. Sketch at least two structurally different designs using [arena](../arena/SKILL.md). Write caller usage first, then types, signatures, ownership, data flow, and invariants. Compare interface depth, failure cases, and maintenance cost.
3. Choose a design and record rejected alternatives. Pause at the sketch if the user requested a checkpoint; otherwise proceed within the authorized implementation scope.
4. Implement against the sketch and verify behavior. Repeated deviations are evidence that the sketch needs redesign, not more patches.
5. Deliver the interface sketch, rationale, implemented result, and verification evidence. Sequential alternatives are not independent reviews.
