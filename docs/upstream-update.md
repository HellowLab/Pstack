# Reviewed upstream adaptation

Reviewed all 14 changed sources from `e58dd043600587dbaf58ba315e7f2b38373eeb43` (0.15.44) through `aaeb0ea3a0584995aa8f55ce44c6c5259414b896` (0.15.46). The snapshot matches the canonical Pstack subtree. Vendored helpers were not executed.

[Upstream comparison](https://github.com/cursor/plugins/compare/e58dd043600587dbaf58ba315e7f2b38373eeb43...aaeb0ea3a0584995aa8f55ce44c6c5259414b896)

| Source | Disposition |
|---|---|
| `.cursor-plugin/plugin.json`, `plugin.json` | Upstream version bumps; downstream metadata remains independently maintained. |
| `docs/harness/claude-code.md` | Vendor-specific model mapping stays source-only. |
| `skills/arena/SKILL.md`, `skills/poteto-mode/SKILL.md` | Do not import changed vendor defaults or raise any accepted policy ceiling. |
| `skills/setup-pstack/SKILL.md` | Do not rewrite accepted model or effort values on rerun; preserve budget and consent gates. |
| `skills/statechart/SKILL.md` | Do not import Node or TLC invocation. Preserve raw checker output when inspecting a normalized copy. |
| `skills/statechart/scripts/frontends/dot.ts`, `run.ts` | Line-ending and UTF-8 handling, child execution flags and pipeline changes stay source-only. |
| `skills/statechart/scripts/janitor.ts`, `kill.ts`, `statechart.ts` | Detached cleanup, process-control, temporary-file and platform behavior stay source-only. |
| `skills/statechart/scripts/test/cli.test.ts`, `test/messages.test.ts` | New line-ending coverage is upstream-only and was not executed. |

The package retains 58 skills and 22 playbooks. No vendor defaults, launchers, checker integration or process-control code are added. Native installation, model execution, rendering and Windows runtime behavior are unverified. Historical release artifacts and public-review records are preserved.
