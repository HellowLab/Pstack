---
name: make-bot-ui
description: "Explain the unsupported Grok Bot webhook UI workflow. Use for make-bot-ui or a request to build the upstream bot UI."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Make bot ui

This upstream workflow depends on a Grok Bot webhook runtime, sender-key setup, and network exposure. This skills-only package supplies none of those capabilities.

Do not invent a ChatGPT webhook endpoint, ask for secrets in chat, or install a tunnel. State that the upstream workflow is unsupported here. If requested, draft a provider-neutral UI specification or adapt to an existing, documented integration after verifying its actual interface and authorization. Label that as separate integration work, not Pstack bot execution.
