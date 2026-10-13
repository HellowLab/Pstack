# Reviewed upstream 0.15.23 adaptation

Reviewed on 2026-10-13 against upstream 0.15.15 at `df581122cde17e6e27686b5a448bde23e4ad4318`.
New snapshot: `dbf49813a39c1a5389c5e28cb8e4c1c2379e2454`, subtree `fafe54a3bb94d4e5e6eee5070d97cb416e0f30ff`.
[Source comparison](https://github.com/cursor/plugins/compare/df581122cde17e6e27686b5a448bde23e4ad4318...dbf49813a39c1a5389c5e28cb8e4c1c2379e2454).

An independent source reviewer inspected all 65 changed or added files, including the source-only helpers and tests. No vendored helper was executed. Existing file modes did not change. Reviewed hashes were updated only after this inspection and the adaptations below.

## Adaptation decisions

- Add explicit-only `in-your-own-words` and `ketchup`, bringing the inventory to 53 skills. Ketchup stays within the current chat, checks actual status, and provides an honest text fallback when visual capabilities are absent. Help and recipes expose both workflows.
- Require usable startup from an empty data directory, migrations and seed data, failed journeys for missing prerequisites, and disclosure of stand-in versus real-target gaps.
- Pass actual host-accessible skill references to delegates. Keep playbook and task-list ownership in the receiving chat. Preserve explicit resource links rather than infer installation paths from titles.
- Inspect every review-thread page before a clear verdict. Incomplete status stays unknown. Require actual PR base information for worktree cleanup. Keep authorization and recoverability boundaries.
- Carry fenced-code semantics into the portable plan-validation contract. The Node implementation and its new tests remain source-only.
- Preserve complete standalone guidance for design exploration, structural lesson encoding, and the laziness principle through overrides. Upstream compression removed core guidance, including almost the entire design-exploration body. Existing richer explorer, source-investigation, reflection, and authorization overrides remain deliberate adaptations. Portable direct-copy principle and reference revisions receive reviewed upstream prose, including the diagnostic-signal suggestion in fix-root-causes.
- Retain adapter-owned metadata. The new upstream root manifest and Cursor agent definitions remain source-only. No vendor model defaults, native agent types, transcript scanning, forced ready-state behavior, automatic issue posting, or persistent orchestration claims enter the package.

The maintained branch guard now distinguishes unmerged human work from a closed branch with the same complete tree as main. Updates preserve the old tip as an ancestor and use a normal push. Real bare-remote fixtures cover squash reconciliation, hidden human commits, active drafts, concurrent pushes, normal updates, and PR recovery.

The 0.1.2 ZIP is a repository-validated candidate. Native installation and model-behavior qualification were not rerun. The submitted rc.5 and previous 0.1.1 archives remain byte-identical. GitHub checks do not establish plugin publication.

Changed files:

- `.cursor-plugin/plugin.json`
- `README.md`
- `agents/comment-sicko.md`
- `agents/poteto-agent.md`
- `plugin.json`
- `skills/architect/SKILL.md`
- `skills/arena/SKILL.md`
- `skills/benchmark-checklist/SKILL.md`
- `skills/create-verification-skill/SKILL.md`
- `skills/figure-it-out/SKILL.md`
- `skills/how/SKILL.md`
- `skills/how/references/explorer-prompt.md`
- `skills/in-your-own-words/SKILL.md`
- `skills/interrogate/SKILL.md`
- `skills/interrogate/references/reviewer-prompt.md`
- `skills/interrogate/references/rubric.md`
- `skills/ketchup/SKILL.md`
- `skills/no-comments/SKILL.md`
- `skills/poteto-help/SKILL.md`
- `skills/poteto-help/references/recipes.md`
- `skills/poteto-mode/SKILL.md`
- `skills/poteto-mode/playbooks/babysit.md`
- `skills/poteto-mode/playbooks/opening-a-pr.md`
- `skills/poteto-mode/playbooks/trace-forensics.md`
- `skills/poteto-mode/playbooks/worktree-cleanup.md`
- `skills/poteto-mode/scripts/check-plan.mjs`
- `skills/poteto-mode/scripts/check-plan.test.ts`
- `skills/poteto-mode/scripts/package.json`
- `skills/poteto-mode/scripts/watch-pr/fakes.test-helper.ts`
- `skills/poteto-mode/scripts/watch-pr/github.test.ts`
- `skills/poteto-mode/scripts/watch-pr/github.ts`
- `skills/poteto-mode/scripts/watch-pr/policy.test.ts`
- `skills/poteto-mode/scripts/watch-pr/policy.ts`
- `skills/poteto-mode/scripts/watch-pr/types.ts`
- `skills/poteto-mode/scripts/worktree-audit.sh`
- `skills/principle-build-the-lever/SKILL.md`
- `skills/principle-encode-lessons-in-structure/SKILL.md`
- `skills/principle-exhaust-the-design-space/SKILL.md`
- `skills/principle-explain-the-number/SKILL.md`
- `skills/principle-fix-root-causes/SKILL.md`
- `skills/principle-guard-the-context-window/SKILL.md`
- `skills/principle-laziness-protocol/SKILL.md`
- `skills/principle-minimize-reader-load/SKILL.md`
- `skills/principle-model-the-domain/SKILL.md`
- `skills/principle-never-block-on-the-human/SKILL.md`
- `skills/principle-redesign-from-first-principles/SKILL.md`
- `skills/principle-subtract-before-you-add/SKILL.md`
- `skills/principle-test-behavior-not-implementation/SKILL.md`
- `skills/principle-type-system-discipline/SKILL.md`
- `skills/reflect/SKILL.md`
- `skills/reflect/references/divergent-reviewer.md`
- `skills/reflect/references/judgment-reviewer.md`
- `skills/reflect/references/synthesizer.md`
- `skills/reflect/references/tooling-reviewer.md`
- `skills/technical-writing/SKILL.md`
- `skills/unslop/SKILL.md`
- `skills/why/SKILL.md`
- `skills/why/references/epistemics.md`
- `skills/why/references/investigator-prompt.md`
- `skills/why/references/sources/code-archaeology.md`
- `skills/why/references/sources/datadog.md`
- `skills/why/references/sources/incident-postmortem.md`
- `skills/why/references/sources/sentry.md`
- `skills/why/references/sources/slack.md`
- `skills/why/references/synthesizer-prompt.md`
