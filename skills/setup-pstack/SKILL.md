---
name: setup-pstack
description: "Configure Pstack-GPT for the capabilities actually available in this host. Use for /setup-pstack, configure pstack models, or pstack budget."
---

Apply when the user's request matches the setup description.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Setup pstack

1. Inspect exposed tools and their documentation. List available repository access, execution, browsing, integrations, delegation, and persistence. Record unknowns as unknowns.
2. Explain which requested workflows can run, which need a sequential fallback, and which are blocked.
3. Use the current model by default. A requested model override must be supported by the host; this plugin cannot configure model families or reasoning budgets through an invented API.
4. If requested, write a short project-local preferences document to the authorized location. Do not write global rules, install plugins, change credentials, or alter security settings without that scope.
5. Summarize the configuration and its limits. No native always-on mode, background execution, or installation is implied by this setup.
