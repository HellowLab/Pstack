---
name: how
description: "Explain how code works, including runtime flow, placement, ownership, and layering. Use for how does X work or a code walkthrough."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# How

Use read-only inspection. Do not make product edits during this workflow.

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

Execution roles use only actual host capabilities under the host contract. Inherit the current model unless a supported override was requested. With no delegation, run stages sequentially and disclose the absence of independent review.


## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. One explainer explores and explains in a single pass. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): use parallel explorers when available, otherwise explore slices sequentially, then hand off to the explainer. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. Assign the exploration slices, concurrently only if real workers are available:

Use an actual permitted host worker in a read-only role. If unavailable, execute this stage directly and label it a sequential pass.

Each explorer gets the prompt in `references/explorer-prompt.md` with its angle filled in. Then go to Step 3.

## Step 2b. Direct Explain (simple questions)

Assign one exploration/explanation role that explores and explains in one pass:

Use an actual permitted host worker in a read-only role. If unavailable, execute this stage directly and label it a sequential pass.

Build its prompt from `references/explainer-prompt.md` without the explorer-findings section. Go to Step 4.

## Step 3. Synthesize (complex questions only)

Once all explorers have returned, assign one exploration/explanation role to synthesize their findings into one explanation:

Use an actual permitted host worker in a read-only role. If unavailable, execute this stage directly and label it a sequential pass.

Build its prompt from `references/explainer-prompt.md` with every explorer's findings filled in.

## Step 4. Present

Present the explainer's output to the user. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
