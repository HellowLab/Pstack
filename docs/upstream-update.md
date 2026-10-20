# Reviewed upstream adaptation: 0.15.29

Previous snapshot: `d457567332aa6989e753ea289f30ea2bfbc80bc0`.
Reviewed snapshot: `88d47514b82e7c44f00f2b2a72ff6dd12158038c`.
Reviewed subtree: `34a0b817e5ea92375bb10f20b15cf750d4e8095a`.
[Upstream comparison](https://github.com/cursor/plugins/compare/d457567332aa6989e753ea289f30ea2bfbc80bc0...88d47514b82e7c44f00f2b2a72ff6dd12158038c)

All eight changed source files and the subtree identity were inspected:

| Source | Review and disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Version-only bump; remains source-only Cursor metadata. |
| `plugin.json` | Version-only bump; adapter-owned portable manifests remain authoritative. |
| `README.md` | Sharpen now rewrites a prompt and does not perform the task; reflected in the adapted skill and help. Source README remains background material. |
| `docs/guide/02-poteto-mode.md` | Prompt rewrite precedes a separately submitted task; retain as source-only guidance, without importing Cursor runtime assumptions. |
| `docs/guide/10-recipes-and-pitfalls.md` | Recipe changes from execution to rewrite-only; adapted recipes now agree. |
| `skills/poteto-help/SKILL.md` | Update the sharpen routing row; preserve existing setup consent, once-per-chat offer and host safeguards. |
| `skills/poteto-help/references/recipes.md` | Accept the prompt-to-rewrite example and state that the user sends the result separately. |
| `skills/sharpen/SKILL.md` | Preserve explicit invocation. Give four concise recommendations covering expert approach, raw material, specific methods/tools and an outside check, then return the rewritten prompt. Remove earlier task-execution instructions. Preserve explicit constraints, scope, user choices and missing-capability disclosure. |

No source files were added or removed and no new executable mode changes were introduced. Upstream attribution and unsupported host/runtime classifications remain intact. Reviewed hashes were updated only after this source and adapter review.

The 0.1.9 package contains 56 skill entry points and 23 routes. Static contract tests check rewrite-only semantics, unresolved choices, unavailable verification and agreement between help and the skill. They do not establish actual model behavior. Native installation and model execution were not run. Historical release archives are preserved unchanged.
