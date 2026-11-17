# Reviewed upstream adaptation

Reviewed all 70 changed, added or removed sources from `bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7` (0.15.42) through `e1cc03121a0e71129a4fb730d7c5528a0a3e43c8` (0.15.43). Three independent source-review scopes covered every item, including deleted references and scripts. Vendored helpers were not executed. Reviewed hashes were refreshed after source review and adaptation.

[Upstream comparison](https://github.com/cursor/plugins/compare/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7...e1cc03121a0e71129a4fb730d7c5528a0a3e43c8)

| Source | Disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `README.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `agents/poteto-agent.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `docs/guide/01-setup.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `docs/guide/02-poteto-mode.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `docs/guide/04-design.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `docs/guide/05-build-and-clean.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `docs/guide/06-verify-and-ship.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `docs/guide/07-overnight.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `docs/guide/09-make-it-yours.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `docs/harness/claude-code.md` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `plugin.json` | Source-only documentation, manifest or native-agent configuration; no hardcoded vendor models, service tiers or runtime capabilities imported. |
| `skills/architect/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/architect/references/design-red-flags.md` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/architect/references/rationale-template.md` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/architect/references/runner-prompt.md` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/arena/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/automate-me/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/benchmark-checklist/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/figure-it-out/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/no-comments/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-help/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/autonomous-run.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/autopilot-full.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/autopilot-stack.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/babysit.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/bug-fix.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/eval.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/feature.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/hillclimb.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/multi-phase-plan.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/opening-a-pr.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/orchestrate.md` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/poteto-mode/playbooks/perf-issue.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/refactoring.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/runtime-forensics.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/session-pickup.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/shipping.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/trace-forensics.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/playbooks/worktree-cleanup.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/poteto-mode/scripts/check-plan.mjs` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/poteto-mode/scripts/check-plan.test.ts` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/poteto-mode/scripts/package.json` | Source-only helper metadata. No vendored execution or runtime import. |
| `skills/poteto-mode/worker.md` | Adapt self-contained worker briefing while preserving user, host and repository authority, required review and draft gates. |
| `skills/principle-attack-the-premise/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-boundary-discipline/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-build-the-lever/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-explain-the-number/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-fix-root-causes/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-foundational-thinking/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-make-operations-idempotent/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-minimize-reader-load/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-model-the-domain/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-prove-it-works/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-separate-before-serializing-shared-state/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-sequence-verifiable-units/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-test-behavior-not-implementation/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/principle-type-system-discipline/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/recall/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/reflect/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/reflect/references/divergent-reviewer.md` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/reflect/references/judgment-reviewer.md` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/reflect/references/synthesizer.md` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/reflect/references/tooling-reviewer.md` | Retired upstream source. Remove obsolete packaged resource or source-only classification; no helper execution. |
| `skills/setup-pstack/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/show-me-your-work/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/swarm/SKILL.md` | Reviewed supported behavior and updated affected adapters/callers; preserve explicit host capability, permission, verification and model-preference guards. |
| `skills/technical-writing/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |
| `skills/unslop/SKILL.md` | Reviewed portable simplification. Copy safe source; retain stronger existing type-system override. |

The package keeps 58 skills and 22 playbooks. Seven obsolete Architect/Reflect references the Orchestrate playbook and the obsolete plan-validation resource are removed; a guarded worker contract is added. Static instruction checks do not establish model behavior. Native installation, model execution and rendering remain unqualified for v0.1.16. Historical release assets remain unchanged.
