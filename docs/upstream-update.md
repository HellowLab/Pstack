# Reviewed upstream adaptation

Reviewed all 59 changed, added or removed sources from upstream 0.15.36 to 0.15.42 (`bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7`). Vendored code was inspected as source, never executed.

| Source | Review disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `README.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `agents/comment-sicko.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `automations/benny/FOR_AGENTS.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `automations/benny/skills/reproduce-and-fix-issues/SKILL.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `automations/benny/skills/setup-benny/SKILL.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `automations/benny/skills/triage-issue-reports/SKILL.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `docs/guide/01-setup.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `docs/guide/02-poteto-mode.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `docs/guide/03-understand.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `docs/guide/04-design.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `docs/guide/10-recipes-and-pitfalls.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `docs/harness/claude-code.md` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `plugin.json` | Source-only metadata/documentation reviewed; preserve attribution and host-neutral package boundary. |
| `skills/architect/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/arena/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/blast-radius/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/how/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/how/references/explainer-prompt.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/how/references/explorer-prompt.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/no-comments/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/poteto-help/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/poteto-mode/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/poteto-mode/playbooks/bug-fix.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/poteto-mode/playbooks/feature.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/poteto-mode/playbooks/hillclimb.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/poteto-mode/playbooks/investigation.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/poteto-mode/playbooks/multi-phase-plan.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/poteto-mode/playbooks/perf-issue.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/poteto-mode/playbooks/refactoring.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/recall/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/reflect/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/reflect/references/synthesizer.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/setup-pstack/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/sharpen/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/statechart/scripts/backends/mermaid.ts` | Source-only implementation/test review; no executable or runtime imported. Error and chart readability lessons adapted as guarded instructions. |
| `skills/statechart/scripts/run.ts` | Source-only implementation/test review; no executable or runtime imported. Error and chart readability lessons adapted as guarded instructions. |
| `skills/statechart/scripts/test/chart.test.ts` | Source-only implementation/test review; no executable or runtime imported. Error and chart readability lessons adapted as guarded instructions. |
| `skills/statechart/scripts/test/cli.test.ts` | Source-only implementation/test review; no executable or runtime imported. Error and chart readability lessons adapted as guarded instructions. |
| `skills/statechart/scripts/test/corpus.test.ts` | Source-only implementation/test review; no executable or runtime imported. Error and chart readability lessons adapted as guarded instructions. |
| `skills/statechart/scripts/test/corpus/Login/chart.mmd` | Source-only implementation/test review; no executable or runtime imported. Error and chart readability lessons adapted as guarded instructions. |
| `skills/statechart/scripts/test/drawn.ts` | Source-only implementation/test review; no executable or runtime imported. Error and chart readability lessons adapted as guarded instructions. |
| `skills/statechart/scripts/test/labels.ts` | Source-only implementation/test review; no executable or runtime imported. Error and chart readability lessons adapted as guarded instructions. |
| `skills/statechart/scripts/test/render.test.ts` | Source-only implementation/test review; no executable or runtime imported. Error and chart readability lessons adapted as guarded instructions. |
| `skills/swarm/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/teach/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/why/SKILL.md` | Adapt portable semantics; preserve host permission, actual tools, inherited models and user-selected settings. |
| `skills/why/references/epistemics.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/investigator-prompt.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/source-playbook.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/sources/code-archaeology.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/sources/databricks.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/sources/datadog.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/sources/incident-postmortem.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/sources/linear.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/sources/notion.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/sources/sentry.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/sources/slack.md` | Retired upstream resource; remove stale routing and package declarations. |
| `skills/why/references/synthesizer-prompt.md` | Retired upstream resource; remove stale routing and package declarations. |

All 58 entry points remain. How uses one read-only worker; why uses cited history without stale templates. Arena cross-judging requires a different verified vendor. Native installation, model execution and rendering remain unqualified for v0.1.15; historical release archives are preserved.
