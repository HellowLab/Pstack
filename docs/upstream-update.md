# Reviewed upstream adaptation

Reviewed all seven changed sources from `e1cc03121a0e71129a4fb730d7c5528a0a3e43c8` (0.15.43) through `e58dd043600587dbaf58ba315e7f2b38373eeb43` (0.15.44). Vendored helpers were not executed. Reviewed hashes were refreshed after inspecting every source diff and the affected adapters.

[Upstream comparison](https://github.com/cursor/plugins/compare/e1cc03121a0e71129a4fb730d7c5528a0a3e43c8...e58dd043600587dbaf58ba315e7f2b38373eeb43)

| Source | Disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Version bump; source-only native manifest. |
| `plugin.json` | Version bump; adapted package metadata remains independently maintained. |
| `README.md` | Carbon-to-Neon default panel change remains source-only. |
| `docs/harness/claude-code.md` | Updated Neon mapping remains unsupported Claude Code harness documentation. |
| `skills/arena/SKILL.md` | Vendor-default changes are not imported. Preserve accepted panels, real capabilities and cross-vendor evidence gates. |
| `skills/poteto-mode/SKILL.md` | Updated vendor defaults and Gemini high policy cap remain source-only; the cap is not a model capability maximum. Preserve inherited defaults and authorized overrides. |
| `skills/setup-pstack/SKILL.md` | Do not automatically rewrite saved Gemini panel choices. Generalize the distinction between an accepted policy ceiling and host capability; apply the lower of accepted ceiling and budget target. Changes to saved choices require acceptance. |

The package retains 58 skills and 22 playbooks. No vendor model defaults, global configuration writes or runtime capabilities are imported. Native installation, model execution and rendering remain unqualified for v0.1.17. Historical release artifacts and dated public-review records are preserved. Public marketplace release is not being pursued.
