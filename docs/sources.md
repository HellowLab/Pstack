# Source provenance

Checked on 2026-10-05:

- [Canonical Pstack subtree](https://github.com/cursor/plugins/tree/2cbf58508f40de470d7490b55c51d71241928fa2/pstack), version 0.15.13. Its Git tree is `6a8c28c4bdd81315ac46392fc86d8013cca8a684`.
- [Latest monorepo revision inspected](https://github.com/cursor/plugins/commit/e5a8186d7b43be8d6ac4452440fbead5f1a51c70). Its Pstack subtree matched the pinned tree, so unrelated monorepo changes were not treated as Pstack changes.
- [OpenAI package guidance](https://developers.openai.com/plugins/build/plugins). Portable root `plugin.json`, fixed `skills/` discovery, and OpenAI presentation metadata under `extensions.com.openai`.
- [OpenAI submission guidance](https://developers.openai.com/plugins/deploy/submission). Separate upload, validation, verified identity, review, and publication. Skills-only packages omit MCP and MCP review metadata.
- [Agent Plugins 1.0.0 schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json). A copy is retained at `docs/plugin.schema.json` for repeatable offline schema checks. Submission metadata constraints are additional to this schema.
- [GitHub automatic token authentication](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication). Repository-scoped token permissions and event recursion limits.
- [GitHub Actions repository settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository). Organization constraints and the setting for Actions-created/approved PRs.

The original upstream license is copied without modification. The upstream logo is retained only in the source snapshot. The replacement user-supplied branding has not been included because transfer into the build environment failed. No substitute logo is packaged. [OpenAI brand guidelines](https://openai.com/brand/) are an additional public-submission review input.
