# Reviewed upstream adaptation

Reviewed upstream Pstack 0.15.26 at `0b8e952052d482ee6de06deebf14d590d77b1b34` for adaptation 0.1.7 on October 18.

[Source comparison](https://github.com/cursor/plugins/compare/101b274dd991f694e1f7024be2157e5f3adf07de...0b8e952052d482ee6de06deebf14d590d77b1b34)

All 21 changed source files were inspected, including an independent read-only review:

| Source | Disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Version bump; source-only Cursor manifest. |
| `plugin.json` | Version bump; source-only upstream manifest. Adapter version stays independent. |
| `README.md` | Formal verification discovery, fuller catch-up decisions, Claude setup and editorial changes. Source-only; no Cursor defaults or persistence imported. |
| `docs/guide/01-setup.md` | Cursor custom-mode link correction; source-only. |
| `docs/guide/02-poteto-mode.md` | Adds stack-autopilot description; source-only, unattended runtime remains unsupported. |
| `docs/guide/03-understand.md` | Editorial clarification; source-only. |
| `docs/guide/04-design.md` | Editorial clarification; source-only. |
| `docs/guide/05-build-and-clean.md` | Editorial clarification; source-only. |
| `docs/guide/06-verify-and-ship.md` | Clarifies evidence and regression language; source-only, supported evidence obligations retained. |
| `docs/guide/07-overnight.md` | Documents fresh minor-change verifier instead of repeated full swarm; source-only, no activation of unsupported autopilot. Exact-patch independent verification retained. |
| `docs/guide/08-principles.md` | Editorial clarification; source-only. |
| `docs/guide/09-make-it-yours.md` | Editorial clarification; source-only. |
| `docs/guide/10-recipes-and-pitfalls.md` | Clarifies design cost and shared-worktree hazards; source-only, isolation contract retained. |
| `docs/harness/claude-code.md` | Claude settings, model/path mappings and skipped-host-step behavior; source-only. No global settings writes or host-specific tools imported. |
| `skills/create-formal-verification-skill/SKILL.md` | New explicit portable adaptation: code-grounded properties, tool selection, counterexamples, bounded claims, reproducibility, drift triggers. Added host registration limits, isolated scratch changes and missing-verifier draft status. |
| `skills/ketchup/SKILL.md` | Adopt complete per-item decisions with evidence, recommendations and risk; remove blanket total word cap. Preserve read-only, current-chat privacy and missing-capability safeguards. |
| `skills/make-bot-ui/SKILL.md` | Name normalization only; retain unsupported webhook runtime explanation unchanged. |
| `skills/poteto-help/SKILL.md` | Add formal-verification route and expanded catch-up description; retain setup acceptance and host safeguards. |
| `skills/poteto-mode/SKILL.md` | Name normalization only; preserve adapted body, opt-out and workflow contract. |
| `skills/typescript-best-practices/SKILL.md` | Retain portable verifying-type-guard rule for branded values. |
| `skills/typescript-best-practices/references/patterns.md` | Copy reviewed matching validator example byte-for-byte. |

Reviewed hashes and subtree identity were updated only after this review and the affected adaptations. The six initial failures were pending-candidate gates and stale inventory, not regressions in released 0.1.6. Tests now cover all 55 entry points and the new semantic contracts.

The scheduled preview had replaced `dist/pstack-0.1.6.zip` at an unchanged manifest version. The exact released pair was restored from tag `v0.1.6`; ZIP SHA-256 is `77b4365e307d0e073b89f43033513be99b6bf4c051ea0e29ab420e32a061a5c1`. Pending snapshots now use tree-qualified archive names, including failed-generation invalidation. All historical pairs remain unchanged.

[Initial PR CI run](https://github.com/HellowLab/Pstack/actions/runs/39128033987) reported `action_required` with zero jobs. Its GitHub banner explicitly says it awaits maintainer approval in PR #12; this was not a test execution. Workflow permissions and approval policy are unchanged.

Native installation and model behavior were not checked for this candidate. The separate October 19 Ubuntu compatibility checkpoint remains outstanding and is not satisfied early by these checks.
