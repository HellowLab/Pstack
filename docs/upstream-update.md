# Reviewed upstream adaptation

Reviewed upstream Pstack 0.15.28 at `d457567332aa6989e753ea289f30ea2bfbc80bc0` for adaptation 0.1.8 on October 19.

[Source comparison](https://github.com/cursor/plugins/compare/0b8e952052d482ee6de06deebf14d590d77b1b34...d457567332aa6989e753ea289f30ea2bfbc80bc0)

All 16 changed source files were inspected, including independent read-only review. Subtree identity and modes were reviewed separately.

| Source | Disposition |
|---|---|
| `.cursor-plugin/plugin.json` | Source-only upstream version bump. |
| `plugin.json` | Source-only upstream version bump; independent adapter version preserved. |
| `README.md` | Source-only discovery of formal verification maintenance. |
| `docs/guide/01-setup.md` | Source-only Claude installation and formal-verification offer. Do not import global settings or persistence claims. |
| `docs/guide/02-poteto-mode.md` | Source-only opening-PR, restatement and sharpen guidance. Explicit user constraints remain binding. |
| `docs/guide/06-verify-and-ship.md` | Source-only formal workflow, sync tracking, evidence and watcher descriptions. No unavailable runtime imported. |
| `docs/guide/07-overnight.md` | Source-only catch-up recipe; existing guarded adaptation covers the behavior. |
| `docs/guide/09-make-it-yours.md` | Source-only formal workflow discovery. |
| `docs/guide/10-recipes-and-pitfalls.md` | Source-only sharpen, formal-verification and catch-up recipes. |
| `docs/guide/README.md` | Source-only guide index. |
| `skills/create-formal-verification-skill/SKILL.md` | Adopt tool selection, covered-code records, sync commits and maintenance handoff. Generated-input fallback is explicitly testing, not formal proof. Retain registration, tool, authorization and scratch-isolation safeguards. |
| `skills/maintain-formal-verification-skill/SKILL.md` | New explicit-only adaptation preserving six stages and in-sync/updated/bug/blocked outcomes. Cover dirty code, moved functions and new writers; isolate negative controls and rerun restored baseline. Unknown history stays unknown; blocked replay cannot advance sync. |
| `skills/poteto-help/SKILL.md` | Add maintenance discovery and route, plus optional setup offers. Inspect existing verifier harnesses rather than treating absence of a skill as absence of verification. Keep host installation and permission limits. |
| `skills/poteto-help/references/recipes.md` | Add creation/maintenance recipe behind existing host guard. Existing catch-up section covers the new catch-up recipe. |
| `skills/setup-pstack/SKILL.md` | Add eighth optional offer, once only, invoking generation only after acceptance. Preserve role preferences and project-local persistence limits. |
| `skills/sharpen/SKILL.md` | Adopt removal of the redundant rewritten-prompt prohibition. Still requires performing authorized work, preserving explicit constraints and an actual outside check. |

Reviewed hashes were refreshed only after review and adaptation. Historical archives, original artwork, MIT license and Lauren Tan's attribution remain unchanged. Native installation and actual model behavior are not inferred from static workflow-contract tests.

The October 19 Ubuntu checkpoint adds explicit 24.04 and 26.04 validation jobs. Both must pass before release; artifact names include the OS to avoid collisions. The main-only release job retains serialized publication, exact-head checks, immutable tags, exact changelog notes and stale-version protection. See validation.md for observed run evidence.
