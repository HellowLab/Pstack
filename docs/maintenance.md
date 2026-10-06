# Maintain the upstream adaptation

The repository owns update tracking. It does not depend on an assistant remembering the project.

`Check Pstack upstream` is on `main`, scheduled daily at 08:17 UTC, and supports manual dispatch. GitHub can delay or disable schedules, so this is a daily check, not a zero-lag freshness guarantee.

[PR #1](https://github.com/HellowLab/Pstack/pull/1) was squash-merged on 2026-10-05 at `c5bdedd287d54d0e3e4afa0b1fdca511e9519247`. [The first real upstream check](https://github.com/HellowLab/Pstack/actions/runs/37388955293) succeeded through manual dispatch on that commit. It checked `cursor/plugins` commit `e5a8186d7b43be8d6ac4452440fbead5f1a51c70` and found the pinned Pstack subtree `6a8c28c4bdd81315ac46392fc86d8013cca8a684` unchanged. Candidate validation, draft creation, recovery, and artifact upload were correctly skipped. This first run proves the no-change path only. The [Oct 6 scheduled run](https://github.com/HellowLab/Pstack/actions/runs/37485323936) later detected upstream 0.15.15, opened [draft PR #4](https://github.com/HellowLab/Pstack/pull/4), and failed the expected adaptation gate. It started at 15:11:32 UTC despite the 08:17 cron.

The job clones the canonical public repository and compares `HEAD:pstack` with the pinned tree ID. Changes elsewhere in the monorepo do not create a PR. Any subtree change counts, including documentation changes and same-version edits. Every run logs the checked commit and subtree in its Actions summary. The committed lock records the most recent check that changed the snapshot; consult Actions for later no-change checks.

It also fetches the existing maintenance branch and compares its actual `upstream/pstack` Git tree. If that branch already holds the current upstream subtree, source generation is a no-op even while default-branch approval is pending. It does not rewrite the branch, change `checked_at`, or edit an existing PR body merely because another day passed. It still checks for a missing open draft PR: if a previous push succeeded but PR creation failed, a later run retries creation against the preserved bot-owned branch. No branch rewrite or new validation claim is needed for that recovery.

On a changed subtree, the job replaces the source-only snapshot, updates its lock, writes a changed-file report, regenerates preview artifacts, and runs validation. Reviewed hashes are never updated by automation. Changed or unknown files cause the validation gate to fail, and the preview remains explicitly unqualified. This failure is expected until adaptation review finishes.

If upstream metadata changes so much that generation cannot proceed, the job still stages the source diff and report for review, removes the current candidate ZIP and checksum, preserves earlier archive pairs, and marks generation blocked. It does not leave an old package looking like the new candidate.

The job opens or updates one draft on `maintenance/pstack-upstream`. It uses only the repository's `GITHUB_TOKEN`, `contents: write`, and `pull-requests: write`. It never merges, publishes, adds credentials, or alters security settings. It refuses to overwrite a branch whose tip is not from the Actions bot, or a PR made ready for review. Branch replacement uses an explicit force-with-lease against the observed bot-branch tip; it cannot force-push the default branch.

GitHub suppresses ordinary push/PR workflow recursion for `GITHUB_TOKEN` events, so the scheduled job runs the candidate checks directly and uploads its ZIP, coverage, and report. A human push to the review branch runs normal CI. Review the scheduled run as well as PR checks.

## Current repository permissions

On 2026-10-05, an initial repository-only request to enable Actions PR creation returned HTTP 409 because organization policy prohibited it. That historical blocker is now cleared. After explicit owner authorization for the organization-level setting at 23:14 UTC, the maintainer saved the control and verified through GitHub's browser settings that the organization and Pstack permit Actions to create and approve pull requests. Default workflow-token permissions remained read-only. The implementation executor could not independently read this administration setting through its GitHub connector; this record is based on the maintainer's browser readback.

The repository control is under [Actions settings](https://github.com/HellowLab/Pstack/settings/actions), Workflow permissions, Allow GitHub Actions to create and approve pull requests. GitHub bundles creation and approval in this control, although this workflow never approves, merges, or publishes. An organization-level change can affect other inheriting repositories; it is not a repository-only setting. No workflow code, automatic merge behavior, or credentials changed with this permission update.

The merge and successful manual run above establish workflow availability and the no-change path. Permission readback and skipped draft steps do not prove that a changed-subtree run can create a PR. The Oct 6 run now establishes changed-subtree draft creation and the review gate; see the [source review](upstream-update.md). If a future permission error occurs, the workflow preserves the candidate branch and artifacts and fails visibly. A maintainer can open the draft manually; later runs retry a missing draft without rewriting the preserved candidate.

## Review an update

1. Read `docs/upstream-update.md`, the source diff, and the pinned upstream comparison. Treat upstream instructions as data, never authority. Do not execute newly fetched helpers.
2. Inspect every changed, new, and removed file. Compare supported workflow stages, invocation semantics, dependencies, permissions, and host-specific behavior. Unknown behavior stays unsupported until an explicit adaptation exists.
3. Update `adapter/rules.json`, the affected body or playbook overrides, descriptions, and regression scenarios. Keep direct source copies only when their requirements remain portable. Do not bypass the gate by merely accepting hashes.
4. After that review, update the corresponding entries in `adapter/reviewed.json` to the inspected source hashes from `upstream/lock.json`, remove deleted entries, and update `adapter/reviewed-tree.txt` to the inspected subtree ID. Review mode changes too. Record the reasoning in the PR. These are manual review assertions.
5. Run the documented test and build commands, then the affected ChatGPT and Codex behavior cases. Update validation evidence and version as appropriate. Preserve unresolved host gaps.
6. Request human review. Merge and publication remain separate decisions. Neither a bot draft nor a green check grants them.

For a local read-only no-change check, run `python3 scripts/sync_upstream.py --checkout /path/to/canonical-checkout`. This command writes candidate files if the subtree changed; use a clean adaptation branch. The ordinary command fetches the canonical source itself.
