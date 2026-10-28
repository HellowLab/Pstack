# Reviewed upstream adaptation

Reviewed all 29 changed or removed sources from `519d36aa98955bf680db01bcde5fdfba686dc901` (0.15.34) through `c742dd61706fbacc1b95f1a20b7b988cf096ce6c` (0.15.36). Source data was inspected without running vendored helpers. Reviewed hashes and subtree identity were refreshed only after adaptation.

[Upstream comparison](https://github.com/cursor/plugins/compare/519d36aa98955bf680db01bcde5fdfba686dc901...c742dd61706fbacc1b95f1a20b7b988cf096ce6c)

| Source | Review disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Version metadata reviewed; adapter retains its own portable manifest. |
| `README.md` | Source-only documentation reviewed for changed review, dependency-stack and orchestration semantics; adapted guidance carries supported behavior. |
| `docs/guide/04-design.md` | Source-only documentation reviewed for changed review, dependency-stack and orchestration semantics; adapted guidance carries supported behavior. |
| `docs/guide/07-overnight.md` | Source-only documentation reviewed for changed review, dependency-stack and orchestration semantics; adapted guidance carries supported behavior. |
| `docs/guide/10-recipes-and-pitfalls.md` | Source-only documentation reviewed for changed review, dependency-stack and orchestration semantics; adapted guidance carries supported behavior. |
| `plugin.json` | Version metadata reviewed; adapter retains its own portable manifest. |
| `skills/arena/SKILL.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/interrogate/SKILL.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/interrogate/references/code-quality-review.md` | Removed upstream; remove obsolete review resources or excluded orchestration classification. No executable imported. |
| `skills/interrogate/references/lead-judgment.md` | Removed upstream; remove obsolete review resources or excluded orchestration classification. No executable imported. |
| `skills/interrogate/references/reviewer-prompt.md` | Removed upstream; remove obsolete review resources or excluded orchestration classification. No executable imported. |
| `skills/interrogate/references/rubric.md` | Removed upstream; remove obsolete review resources or excluded orchestration classification. No executable imported. |
| `skills/ketchup-video/SKILL.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-help/SKILL.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-help/references/recipes.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-mode/SKILL.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-mode/playbooks/autonomous-run.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-mode/playbooks/autopilot-full.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-mode/playbooks/autopilot-stack.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-mode/playbooks/babysit.md` | Retain stricter existing topology guard while unattended runtimes remain unsupported. |
| `skills/poteto-mode/playbooks/multi-phase-plan.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-mode/playbooks/opening-a-pr.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-mode/playbooks/orchestrate.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |
| `skills/poteto-mode/scripts/orch/orch.test.ts` | Removed upstream; remove obsolete review resources or excluded orchestration classification. No executable imported. |
| `skills/poteto-mode/scripts/orch/orch.ts` | Removed upstream; remove obsolete review resources or excluded orchestration classification. No executable imported. |
| `skills/poteto-mode/scripts/orch/store.ts` | Removed upstream; remove obsolete review resources or excluded orchestration classification. No executable imported. |
| `skills/poteto-mode/scripts/package.json` | Source-only test command change; no upstream helper executed or packaged. |
| `skills/principle-explain-the-number/SKILL.md` | Copy reviewed portable pre-measurement decision threshold and noise-floor guidance. |
| `skills/setup-pstack/SKILL.md` | Adapt supported semantics; retain permissions, actual host capabilities, current-head evidence and honest unavailable-capability reporting. |

The package keeps 58 skill entry points. Four obsolete interrogate references are removed. Native installation, model execution and video rendering remain unqualified for v0.1.14. Historical archives are preserved byte for byte.
