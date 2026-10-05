# Opening a pr

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Confirm PR delivery is in the user's scope. Use an isolated branch or worktree where supported. Preserve unrelated edits and never reset a dirty checkout to simplify the task.
2. Make small ordered commits. Run project checks, review the actual diff, remove unnecessary complexity, and review comments with no-comments. Apply technical-writing and unslop to titles and descriptions. No external cleanup plugin is assumed.
3. Use a short Conventional Commits title. Write Why, What changed, Scope, Tradeoffs, Blast radius, and Verification sections when they have content. Link detailed evidence rather than pasting logs. Name real verification gaps.
4. Resolve an available supported forge API or CLI. Follow host instructions for artifact attachment. Verify remote branch and PR head revisions after pushing.
5. Preserve the user's requested draft or ready state. Without a preference, keep an unverified change draft. A ready state is not a merge authorization.
6. For dependent work, set each child base to its actual parent; only the root targets trunk. Verify topology explicitly.
7. Return the PR URL, state, checks, and remaining gates. Do not begin babysitting merely because a PR was opened.
