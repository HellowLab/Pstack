---
name: interrogate
description: "Adversarially review changes and report a verdict without applying fixes. Use for interrogate, challenge this, stress test this code, or multi-model review."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Interrogate

1. Determine the diff and intended behavior from the request, source, and review context. Record a clear statement of intent.
2. Review correctness, security, contracts, tests, and maintenance cost. Give actual available independent reviewers the same scope and rubric when permitted.
3. If independent reviewers or requested model diversity are unavailable, say so before presenting the result. A single-agent critique can still be useful, but is not an independent or multi-model review.
4. Deduplicate findings and check them against source. Classify as Act on, Consider, Noted, or Dismissed with evidence and rationale.
5. Report intent, actual reviewers, findings, disagreements, and gaps. Do not auto-apply fixes or post the report externally.
