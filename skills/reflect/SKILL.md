---
name: reflect
description: "Review the current conversation for durable lessons and propose skill changes. Use when the user says reflect or /reflect."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Reflect

Present proposals and wait for explicit approval before changing standing skills. Backlog remains local unless the user authorized an external tracker action.

Mine the current conversation for durable learnings, then route them into skill edits.

## When to invoke

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## Process

### 1. Locate the active transcript

Use the active conversation, an explicitly supplied transcript, or documented in-scope host history. Do not search private app storage or unrelated workspaces. If no transcript is available, write a concise digest and mark what could not be verified.

### 2. Spawn three reviewers in parallel

Assign three lenses through actual permitted reviewers when available. Otherwise perform a clearly labeled sequential pass; do not invent independent reviewers. Use these complete templates and keep their distinct finding requirements:

| Lens | Prompt template |
|---|---|
| Judgment | `references/judgment-reviewer.md` |
| Tooling | `references/tooling-reviewer.md` |
| Divergent | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the transcript path or digest where marked. Collect actual reviewer findings, or retain each lens's findings from the labeled sequential pass.

### 3. Synthesize

Use `references/synthesizer.md` verbatim with all actual findings. A separate synthesizer is preferred when available; otherwise disclose a sequential synthesis. Verify citations through authorized read-only tools. Return the complete Accepted / Rejected / Backlog structure.

### 4. Structural enforcement check

Sanity-check the synthesizer's Accepted list. For any item that would be enforced more reliably by a lint rule, script, metadata flag, or runtime check, move it from Accepted to Backlog. See the **encode-lessons-in-structure** principle skill.

### 5. Apply

Before applying any Accepted edit, present the synthesizer's full Accepted/Rejected/Backlog output to the user and wait for explicit approval. The user picks which subset to apply and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

Keep Backlog items local unless the user authorized filing them to the relevant tracker. Accepted standing-skill edits require explicit approval.

For each approved Accepted item, follow the Routing field exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): parent does directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): use available host skill-authoring guidance and run a draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): use actual available host skill-authoring guidance and a supported description evaluation loop; if no evaluation runner exists, report that gap.
- `new skill: <kebab-name>`: use actual available host skill-authoring guidance. If installation support is absent, deliver a clearly labeled draft and report the gap.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done. Skip this step if it doesn't.

### 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
