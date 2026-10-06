# Capability coverage

Upstream 0.15.15 at `df581122cde17e6e27686b5a448bde23e4ad4318`.
Subtree `9d9cb20f79203a97c925de402c66183d0fa26c42`. Latest checked commit `df581122cde17e6e27686b5a448bde23e4ad4318` on 2026-10-06.
Adaptation status: pending. Host qualification remains incomplete.

All registered skill names remain discoverable. Explicit-only invocation metadata and a body guard are retained; setup keeps its upstream automatic eligibility. Native mode and path-selector metadata are replaced by description and body instructions.

Unchanged means exact copied bytes. Adapted means host-neutral instructions or guarded source content. Unsupported material remains in the repository snapshot only, except clearly marked explanatory entry points.

| Upstream file | Status | Adaptation or limitation | Review |
|---|---|---|---|
| `.cursor-plugin/plugin.json` | unsupported | Source-only supporting material; not loaded or executed by the package. | pending |
| `.gitignore` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `LICENSE` | unchanged | Complete MIT license preserved at repository and package root. | reviewed |
| `README.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | pending |
| `agents/comment-sicko.md` | adapted | Complete comment-review role preserved as a prompt resource; no native agent registration. Uncertain constraints remain until resolved rather than being deleted on ambiguity. | reviewed |
| `agents/poteto-agent.md` | unsupported | Native agent registration unsupported; poteto-mode and no-comments adapt the workflow without a fictitious agent type. | reviewed |
| `assets/logo.png` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `automations/benny/FOR_AGENTS.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/README.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/skills/reproduce-and-fix-issues/SKILL.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/skills/reproduce-and-fix-issues/references/feature-map.example.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/skills/reproduce-and-fix-issues/references/verify-existing-fix.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/skills/setup-benny/SKILL.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/skills/triage-issue-reports/SKILL.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/skills/triage-issue-reports/references/routing.example.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/templates/configuration.example.yaml` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/templates/reproduce-automation-prompt.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `automations/benny/templates/triage-automation-prompt.md` | unsupported | Benny external issue automation is outside the skills-only runtime; no automatic external actions. | reviewed |
| `docs/guide/01-setup.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | pending |
| `docs/guide/02-poteto-mode.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/03-understand.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/04-design.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | pending |
| `docs/guide/05-build-and-clean.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/06-verify-and-ship.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/07-overnight.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/08-principles.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/09-make-it-yours.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/10-recipes-and-pitfalls.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/README.md` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/images/design.jpg` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/images/overnight.jpg` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/images/recipes.jpg` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/images/router.jpg` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/images/understanding.jpg` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `docs/guide/images/verification.jpg` | unsupported | Source-only supporting material; not loaded or executed by the package. | reviewed |
| `skills/architect/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | pending |
| `skills/architect/references/design-red-flags.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/architect/references/rationale-template.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/architect/references/runner-prompt.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | pending |
| `skills/arena/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | pending |
| `skills/automate-me/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/benchmark-checklist/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/blast-radius/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | pending |
| `skills/bro/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/correct/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/create-verification-skill/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/create-verification-skill/references/feature-map-example/README.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/create-verification-skill/references/feature-map-example/create-note.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/create-verification-skill/references/feature-map-example/search.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/figure-it-out/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/how/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | pending |
| `skills/how/references/explainer-prompt.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/how/references/explorer-prompt.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/interrogate/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | pending |
| `skills/interrogate/references/code-quality-review.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/interrogate/references/lead-judgment.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/interrogate/references/reviewer-prompt.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/interrogate/references/rubric.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/maintain-verification-skill/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/make-bot-ui/SKILL.md` | unsupported | Explanatory entry point only; Grok Bot webhook runtime is not supplied. | reviewed |
| `skills/no-comments/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/poteto-help/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | pending |
| `skills/poteto-help/references/prompting.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/poteto-help/references/recipes.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/poteto-mode/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | pending |
| `skills/poteto-mode/playbooks/authoring-a-skill.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/autonomous-run.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/autopilot-full.md` | unsupported | Explanatory entry point; persistent worker lifecycle and orchestration runtime are not supplied. | reviewed |
| `skills/poteto-mode/playbooks/autopilot-stack.md` | unsupported | Explanatory entry point; persistent worker lifecycle and orchestration runtime are not supplied. | reviewed |
| `skills/poteto-mode/playbooks/babysit.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/bug-fix.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/eval.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/feature.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/hillclimb.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/investigation.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/multi-phase-plan.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/opening-a-pr.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/orchestrate.md` | unsupported | Explanatory entry point; persistent worker lifecycle and orchestration runtime are not supplied. | reviewed |
| `skills/poteto-mode/playbooks/pause-safely.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/perf-issue.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/prototype.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/refactoring.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/runtime-forensics.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/session-pickup.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/shipping.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/trace-forensics.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/visual-parity.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/playbooks/worktree-cleanup.md` | adapted | Workflow stages retained with explicit capability, scope, and evidence gates. | reviewed |
| `skills/poteto-mode/references/bugbot-triage.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/poteto-mode/scripts/bootstrap.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/bun.lock` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/check-plan.mjs` | adapted | Preserve structural checks as an explicit review contract; no Node helper, vendor-model assertion, scheduler, or project-trunk plugin path is assumed. | reviewed |
| `skills/poteto-mode/scripts/orch/orch.test.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | pending |
| `skills/poteto-mode/scripts/orch/orch.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/orch/store.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/package.json` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/cli.test.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/cli.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/fakes.test-helper.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/github.test.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/github.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/policy.test.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/policy.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/render.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/tsconfig.json` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/types.compile.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/types.ts` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/watch-pr/watch-pr` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/poteto-mode/scripts/worktree-audit.sh` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/principle-attack-the-premise/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-boundary-discipline/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-build-the-lever/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-encode-lessons-in-structure/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-exhaust-the-design-space/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-experience-first/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-explain-the-number/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-fix-root-causes/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-foundational-thinking/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-guard-the-context-window/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/principle-laziness-protocol/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-make-operations-idempotent/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-minimize-reader-load/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-model-the-domain/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-never-block-on-the-human/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/principle-outcome-oriented-execution/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-prove-it-works/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-redesign-from-first-principles/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-separate-before-serializing-shared-state/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-sequence-verifiable-units/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-subtract-before-you-add/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-test-behavior-not-implementation/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/principle-type-system-discipline/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/recall/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/reflect/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | pending |
| `skills/reflect/references/divergent-reviewer.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/reflect/references/judgment-reviewer.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/reflect/references/synthesizer.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/reflect/references/tooling-reviewer.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/setup-pstack/SKILL.md` | adapted | Preserve all seven setup stages, four budget choices, and 17 role entries; use observed host model controls and authorized project persistence rather than vendor defaults or a global rule. | pending |
| `skills/show-me-your-work/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/show-me-your-work/references/decision-log-template.tsv` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/show-me-your-work/scripts/log.sh` | unsupported | Host-specific helper retained only as source. No helper is executed or distributed in the ZIP. | reviewed |
| `skills/swarm/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | reviewed |
| `skills/tdd/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/teach/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/technical-writing/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/typescript-best-practices/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/typescript-best-practices/references/patterns.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/unslop/SKILL.md` | adapted | Upstream body retained; invocation and host/permission guards added. | reviewed |
| `skills/why/SKILL.md` | adapted | Explicit host workflow adaptation; source identity and invocation intent retained. | pending |
| `skills/why/references/epistemics.md` | unchanged | Portable reference contract retained byte-for-byte and invoked by its workflow. | reviewed |
| `skills/why/references/investigator-prompt.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/source-playbook.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/sources/code-archaeology.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/sources/databricks.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/sources/datadog.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/sources/incident-postmortem.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/sources/linear.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/sources/notion.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/sources/sentry.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/sources/slack.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
| `skills/why/references/synthesizer-prompt.md` | adapted | Full reference retained with capability/permission preface and narrow host-path or runner corrections. | reviewed |
