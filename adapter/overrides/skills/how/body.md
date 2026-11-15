# How

Explore the codebase to answer "how does X work?" questions. Use read-only inspection and cite real source for the explanation. Do not make product edits or remote writes.

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

## 1. Explain

Use one actual permitted subagent in a read-only role to explore and explain in one pass. Inherit the current model unless a supported override was requested. Give it the user's question and this brief:

> You are writing an architectural explanation for a senior engineer. Explore the codebase and write an explanation that a senior engineer unfamiliar with this area could read and walk away with a solid mental model. They should understand the architecture well enough to start working in it confidently. You have read-only access to the codebase.

If delegation is unavailable, perform that read-only pass directly and disclose the limitation. Do not invent a worker, access mode, or tool capability.

## 2. Present

Present the explanation. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite a subagent's output.
