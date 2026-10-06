# Reviewed upstream 0.15.15 adaptation

[The Oct 6 scheduled run](https://github.com/HellowLab/Pstack/actions/runs/37485323936) detected Pstack 0.15.15 and opened [draft PR #4](https://github.com/HellowLab/Pstack/pull/4). The cron is 08:17 UTC; the run started at 15:11:32 UTC. Sync, draft creation, and preview upload succeeded. Candidate validation reported seven failures and the final review gate deliberately failed.

Six failures withheld changed skills and resources pending review. The seventh came from a test that assumed upstream version 0.15.13. This update preserves the review gate and makes that test independent of the pinned version.

The reviewed comparison is [2cbf585 to df58112](https://github.com/cursor/plugins/compare/2cbf58508f40de470d7490b55c51d71241928fa2...df581122cde17e6e27686b5a448bde23e4ad4318). The candidate subtree is `9d9cb20f79203a97c925de402c66183d0fa26c42`. Every changed file remains mode 100644.

## Source review

Each changed file was inspected as source data. Vendored helpers were not executed.

| Source | Review disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Version becomes 0.15.15. Cursor registration remains unsupported. |
| `README.md` | Fresh vendor panels shrink to two; migration guidance becomes generic. Confirmed preferences remain unchanged. |
| `docs/guide/01-setup.md` | Unlimited requests maximum supported reasoning; large means xhigh. Adapted with observed host controls and inherited defaults. |
| `docs/guide/04-design.md` | Reviewer wording changes. Actual independent review remains required when requested. |
| `skills/architect/SKILL.md` | Fresh panel defaults become two. Keep at least two distinct designs and host inheritance. |
| `skills/architect/references/runner-prompt.md` | Parallel-runner wording changes. Existing honest independence disclosure remains appropriate. |
| `skills/arena/SKILL.md` | Vendor defaults and fallback families change. Only observed, accepted host model choices are usable. |
| `skills/blast-radius/SKILL.md` | Multiple-model wording changes. Existing host capability limits remain appropriate. |
| `skills/how/SKILL.md` | Vendor explainer default changes effort. Existing inherited model policy remains appropriate. |
| `skills/interrogate/SKILL.md` | Fresh reviewer panel becomes two. Preserve actual independence and confirmed panel lists. |
| `skills/poteto-help/SKILL.md` | Add a relevant setup offer once per chat while answering the original question. Use authorized preference sources. |
| `skills/poteto-mode/SKILL.md` | Vendor judgment default changes effort. Existing host inheritance and accepted preferences remain appropriate. |
| `skills/poteto-mode/scripts/orch/orch.test.ts` | Fixture verifier changes. The orchestration runtime remains unsupported and excluded. |
| `skills/reflect/SKILL.md` | Vendor assignments change. Keep three distinct lenses and host inheritance. |
| `skills/setup-pstack/SKILL.md` | Adapt max-target semantics and fresh two-seat panels. Never migrate confirmed preferences silently. |
| `skills/why/SKILL.md` | Vendor synthesizer default changes effort. Existing inherited model policy remains appropriate. |

Reviewed hashes and the subtree assertion are deliberate review records. Automation still cannot approve future source changes.

## Candidate and limits

The adapted package is prepared as stable version 0.1.1. It is an unreleased candidate, not a marketplace update. The submitted 0.1.0-rc.5 ZIP and checksum remain byte-identical. Builds retain and validate earlier archive pairs; failed upstream generation removes only the current candidate pair.

Vendor-specific model defaults, Cursor global rules and native agent registration, orchestration helpers, unattended persistence, and webhook hosting remain unsupported. No credentials, security settings, publisher details, or saved user preferences changed.

Repository tests cover real local Git update behavior and archive preservation. Skill contract assertions are static checks, not proof of model compliance. Prior installation and behavior evidence retains its original version and scope. Fresh native installation and full host behavior qualification of 0.1.1 remain separate work.

Merge, release, marketplace upload, and publication require separate authorization.
