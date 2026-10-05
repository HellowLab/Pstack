---
name: maintain-verification-skill
description: "Audit a project verification skill and feature map against source and live behavior. Use for /maintain-verification-skill or audit the verify skill."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Maintain verification skill

1. Locate the requested verification skill in the project's documented location. If absent, report it and route to [create-verification-skill](../create-verification-skill/SKILL.md).
2. Reconcile its index and feature pages. Read the implementation of every mapped feature and identify missing user entry points.
3. Drive every feature through the real user surface with one coordinator owning the session. Health-check before use and after unexpected results. Preserve evidence through cleanup and clean only resources this run created.
4. Classify drift in docs, gaps in the harness, and product regressions separately. Edit only the verification skill and its harness; report product bugs without rewriting expectations to hide them.
5. Re-run every harness fix. Report clean only with complete source and live coverage, changed with verified corrections, or blocked with gaps. Open at most one PR only when authorized.
