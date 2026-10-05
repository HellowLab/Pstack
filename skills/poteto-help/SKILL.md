---
name: poteto-help
description: "Guide users through Pstack-GPT setup, skills, playbooks, and limitations. Use for /poteto-help or Pstack help."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Poteto help

Read [the capability map](../../resources/coverage.md) before claiming support. This is an independent adaptation, not the upstream product.

Use [setup-pstack](../setup-pstack/SKILL.md) to inventory the host. Use [poteto-mode](../poteto-mode/SKILL.md) for the complete workflow router. Use how for behavior, why for rationale, architect for design, interrogate for critique, and teach for explanation.

The upstream slash names remain invocation aliases. The host may expose skill selection differently. Explicit-only skills must not activate from quoted text, casual mentions, or browsing their source. Setup retains upstream automatic eligibility only for matching setup requests. Native mode UI and path selectors are not assumed.

Explain unsupported helpers and missing integrations honestly. The package does not install tools, select unavailable models, register background jobs, or grant permission.
