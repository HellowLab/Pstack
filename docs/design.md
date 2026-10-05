# Adaptation design

Pstack keeps the upstream snapshot as evidence and produces a separate skills-only package. A small Python build joins explicitly classified source files, reviewed body overrides, invocation guards, and a shared host contract. It never executes upstream scripts or performs broad string replacements.

## Sources of truth

- `upstream/pstack/` is the complete canonical subtree, including unsupported helpers and documentation. Do not load it as a plugin.
- `upstream/lock.json` records the commit, subtree tree ID, upstream version, latest checked monorepo commit, date, and file hashes.
- `adapter/reviewed.json` records the source bytes considered during adaptation review. `adapter/reviewed-tree.txt` pins the reviewed Git tree, including file modes. A changed, added, or removed file or a changed tree blocks the review gate, even if the upstream version is unchanged.
- `adapter/rules.json` classifies every file and each registered skill. `adapter/overrides/` holds readable replacement bodies and playbooks. `adapter/descriptions.json` changes descriptions that would otherwise promise unavailable host behavior.
- Root `plugin.json` and `resources/host-contract.md` are maintained directly. The build copies that one canonical contract byte for byte into each generated skill's `references/host-contract.md`. Entrypoints, nested references, and playbooks link to their own skill's copy because cloud skill readers may not expose plugin-root resources. The copies are generated, never independently authored. `skills/`, coverage reports, `.codex-plugin/plugin.json`, and `dist/` are generated. The Codex compatibility manifest derives all shared metadata from the root manifest, maps OpenAI interface fields to the older layout, and omits only `supportURL`, which that layout does not support. It adds no tools or permissions.

The build uses only the Python standard library. Test-only dependencies validate YAML and the pinned official JSON schema. ZIP entries have a fixed order, timestamp, permissions, and uncompressed representation so rebuilding does not depend on compression-library versions.

## Fidelity and deliberate differences

All 51 upstream registered names and all 23 playbook routes are represented. That is inventory coverage, not a claim that every upstream capability works. The [file-level coverage map](../resources/coverage.md) records the distinction. Portable skill bodies retain their exact source content behind the common guard. Host-bound workflows use explicit overrides, which a reviewer can compare with the vendored original.

The adaptation preserves grounding before changes, competing designs, source-backed rationale, real-surface verification, review before landing, evidence at exact revisions, and the distinct meanings of investigation, babysit, shipping, and the two autopilots. Core workflows preserve the upstream stage order, full role prompts, rubrics, rationale templates, epistemic guidance, and decision-log protocol. Setup preserves all seven stages, four budget choices, and 17 role entries, including panel cardinality and explicit confirmation. Its defaults inherit the parent; only observed host model/effort combinations can be selected. Persistence uses an authorized project instruction mechanism when available and never implies automatic loading. Comment-review uncertainty handling, cleanup, and unavailable persistent runtimes remain explicitly narrower implementations. Comparative host evaluation remains required before public release.

The following differences are intentional and visible:

| Upstream behavior | Adaptation |
|---|---|
| Cursor Task calls, named agent types, fixed vendor/model defaults | Discover actual host capabilities. Use supported delegation only; otherwise disclose a sequential pass. No fictional independent panel. |
| Explicit-only skills and mode UI | Preserve `disable-model-invocation: true` and add a body guard. Keep setup's automatic eligibility. Native mode UI, icon/reminder metadata, and TypeScript path selectors are not assumed; descriptions preserve the trigger intent. |
| External actions allowed by upstream autonomy prose | User scope and host permissions govern actions. Reading a skill never grants authority. |
| Hard-coded transcript paths and connector assumptions | Use documented host access, requested scope, and explicit unavailable-source gaps. |
| Bundled Bun orchestration, watcher, bootstrap, audit, and logging helpers | Retain as source only. Ordinary in-session review/check workflows use available tools. Persistent runtime capabilities remain unsupported. |
| Always open ready PRs and aggressively reset worktrees | Honor requested draft state and preserve unrelated work. Unverified work stays draft by default. |
| Shipping can reuse certain verdicts after build-noise analysis | Conservatively rerun verification after any changed patch. This costs more but avoids asserting an unported build-comparison procedure. |
| Comment Sicko agent and delete-on-ambiguity posture | The full reviewer role is a prompt resource, with no native agent registration. The comment review workflow preserves licensing and evidenced constraints and fixes root causes within scope. It does not delete uncertain safety constraints to satisfy a comment count. |

The full unattended `orchestrate`, `autopilot-full`, and `autopilot-stack` runtimes and `make-bot-ui` are not implemented. Their entry points explain the missing runtime and preserve the intended gates. They do not silently simulate success. Benny automation is source-only. Shipping stops without real independent verification when its gate cannot be met.

These are release decisions, not hidden implementation details. A future faithful runtime port would need explicit host adapters and live validation. Adding those adapters would expand this project's current skills-only scope. Public release should wait until maintainers accept the declared gaps and comparative evaluation demonstrates that supported workflows retain their intent.

## What qualifies a release

Passing repository tests means the package is reproducible, internally consistent, and reviewed against its pinned source. It does not prove that ChatGPT or Codex registered the skills correctly or that a model followed them. Native installation, invocation, behavior, permission, and fidelity checks in [validation](validation.md) remain separate gates. The generated coverage always says `host_validation: not-qualified` in this initial candidate. No automated path changes that status, submits a listing, or publishes a release.
