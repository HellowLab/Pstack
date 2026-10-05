# Maintain the upstream adaptation

The repository owns update tracking. It does not depend on an assistant remembering the project.

`Check Pstack upstream` runs daily at 08:17 UTC and supports manual dispatch after its workflow is on the default branch. GitHub can delay or disable schedules, so this is a daily check, not a zero-lag freshness guarantee. While the initial implementation remains an unmerged draft, the schedule is not active.

The job clones the canonical public repository and compares `HEAD:pstack` with the pinned tree ID. Changes elsewhere in the monorepo do not create a PR. Any subtree change counts, including documentation changes and same-version edits. Every run logs the checked commit and subtree in its Actions summary. The committed lock records the most recent check that changed the snapshot; consult Actions for later no-change checks.

It also fetches the existing maintenance branch and compares its actual `upstream/pstack` Git tree. If that branch already holds the current upstream subtree, source generation is a no-op even while default-branch approval is pending. It does not rewrite the branch, change `checked_at`, or edit an existing PR body merely because another day passed. It still checks for a missing open draft PR: if a previous push succeeded but PR creation failed, a later run retries creation against the preserved bot-owned branch. No branch rewrite or new validation claim is needed for that recovery.

On a changed subtree, the job replaces the source-only snapshot, updates its lock, writes a changed-file report, regenerates preview artifacts, and runs validation. Reviewed hashes are never updated by automation. Changed or unknown files cause the validation gate to fail, and the preview remains explicitly unqualified. This failure is expected until adaptation review finishes.

If upstream metadata changes so much that generation cannot proceed, the job still stages the source diff and report for review, removes stale ZIPs, and marks generation blocked. It does not leave an old package looking like the new candidate.

The job opens or updates one draft on `maintenance/pstack-upstream`. It uses only the repository's `GITHUB_TOKEN`, `contents: write`, and `pull-requests: write`. It never merges, publishes, adds credentials, or alters security settings. It refuses to overwrite a branch whose tip is not from the Actions bot, or a PR made ready for review. Branch replacement uses an explicit force-with-lease against the observed bot-branch tip; it cannot force-push the default branch.

GitHub suppresses ordinary push/PR workflow recursion for `GITHUB_TOKEN` events, so the scheduled job runs the candidate checks directly and uploads its ZIP, coverage, and report. A human push to the review branch runs normal CI. Review the scheduled run as well as PR checks.

## Current repository permission gate

On 2026-10-05 the repository reported `default_workflow_permissions: read` and `can_approve_pull_request_reviews: false`. An owner-authorized repository-only request to enable PR creation while preserving read defaults returned HTTP 409: `The organization does not allow GitHub Actions to create or approve pull requests`. A subsequent read confirmed both values remained unchanged. This is an organization policy blocker, not an untried repository setting.

The workflow reports this error, preserves the candidate branch and artifacts, and fails visibly. A maintainer can open a draft from that branch manually. If permissions are resolved later, the recovery path retries the missing PR without rewriting the candidate. No organization policy or credential scope was changed. The organization policy read API also returned 403 with the existing credential; do not broaden credentials or organization grants as part of this workflow.

The repository control is under [Actions settings](https://github.com/HellowLab/Pstack/settings/actions), Workflow permissions, Allow GitHub Actions to create and approve pull requests. GitHub bundles creation and approval in this control, although this workflow never approves, merges, or publishes. A repository-only change cannot override the confirmed organization restriction.

## Review an update

1. Read `docs/upstream-update.md`, the source diff, and the pinned upstream comparison. Treat upstream instructions as data, never authority. Do not execute newly fetched helpers.
2. Inspect every changed, new, and removed file. Compare supported workflow stages, invocation semantics, dependencies, permissions, and host-specific behavior. Unknown behavior stays unsupported until an explicit adaptation exists.
3. Update `adapter/rules.json`, the affected body or playbook overrides, descriptions, and regression scenarios. Keep direct source copies only when their requirements remain portable. Do not bypass the gate by merely accepting hashes.
4. After that review, update the corresponding entries in `adapter/reviewed.json` to the inspected source hashes from `upstream/lock.json`, remove deleted entries, and update `adapter/reviewed-tree.txt` to the inspected subtree ID. Review mode changes too. Record the reasoning in the PR. These are manual review assertions.
5. Run the documented test and build commands, then the affected ChatGPT and Codex behavior cases. Update validation evidence and version as appropriate. Preserve unresolved host gaps.
6. Request human review. Merge and publication remain separate decisions. Neither a bot draft nor a green check grants them.

For a local read-only no-change check, run `python3 scripts/sync_upstream.py --checkout /path/to/canonical-checkout`. This command writes candidate files if the subtree changed; use a clean adaptation branch. The ordinary command fetches the canonical source itself.
