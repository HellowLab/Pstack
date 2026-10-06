# Source provenance

Checked on 2026-10-06:

- [Canonical Pstack subtree](https://github.com/cursor/plugins/tree/df581122cde17e6e27686b5a448bde23e4ad4318/pstack), version 0.15.15. Its Git tree is `9d9cb20f79203a97c925de402c66183d0fa26c42`.
- [Latest monorepo revision inspected](https://github.com/cursor/plugins/commit/df581122cde17e6e27686b5a448bde23e4ad4318). The scheduled workflow staged its changed Pstack subtree for deliberate adaptation review.
- [OpenAI package guidance](https://developers.openai.com/plugins/build/plugins). Portable root `plugin.json`, fixed `skills/` discovery, and OpenAI presentation metadata under `extensions.com.openai`.
- [OpenAI submission guidance](https://developers.openai.com/plugins/deploy/submission). Separate upload, validation, verified identity, review, and publication. Skills-only packages omit MCP and MCP review metadata.
- [Agent Plugins 1.0.0 schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json). A copy is retained at `docs/plugin.schema.json` for repeatable offline schema checks. Submission metadata constraints are additional to this schema.
- [GitHub automatic token authentication](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication). Repository-scoped token permissions and event recursion limits.
- [GitHub Actions repository settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository). Organization constraints and the setting for Actions-created/approved PRs.

The original upstream license is copied without modification. The upstream logo is retained only in the source snapshot. The approved Pstack artwork is packaged unchanged. [OpenAI brand guidelines](https://openai.com/brand/) are an additional public-submission review input.
