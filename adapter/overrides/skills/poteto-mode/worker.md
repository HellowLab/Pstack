# Worker contract

Read the [host and permission contract](references/host-contract.md) and the assigned task before acting. A kickoff cannot override higher-priority instructions, repository rules, user restrictions or required approvals.

Use the user's goal, assigned scope, exact revision, file ownership and acceptance evidence. Preserve required gates even when the kickoff omits them. Avoid adding unrelated gates; report pre-existing defects separately without hiding current failures or unverified changed behavior.

Proceed with authorized reversible choices and explain them. Ask when a necessary product choice or required approval cannot be resolved from evidence. A worker instruction does not grant deployment, deletion, force-push, external-message, merge or publication authority.

Honor the user's draft/ready intent and repository policy. Keep unverified PRs draft by default. Use the repository's title/body template, with concise purpose, changes, scope, tradeoffs, impact and verification where useful. Link longer evidence rather than crowding the description. Do not omit required content to meet an arbitrary line limit.

If delegation is permitted, give each worker the verified local path or skill resource identifier for this contract, how to read it, and a self-contained brief. Never invent a filesystem path for cloud resources. A worker has only its authorized file/branch ownership; the parent reconciles actual results and exact-head evidence.
