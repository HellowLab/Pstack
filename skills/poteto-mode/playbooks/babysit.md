# Babysit

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Declare mode before polling: check means one status pass; threads-only means requested comment work; drive means work toward merge-ready; background requires a real available background mechanism. Small documentation changes use check unless requested otherwise. Opening a PR alone does not invoke babysit.
2. Resolve an available authorized forge tool. Freeze the stack order, choose its lowest unmerged PR as the frontier, and ensure there is only one active coordinator.
3. Inspect conflicts, then review threads, then CI. Report conflicts requiring topology changes; babysit does not retarget bases, rewrite branches, or reorder the stack. Batch evidenced fixes in the owning branch.
4. Verify bot claims against source. Fix real issues with regression evidence, dismiss false positives with concrete disproof, and retain uncertainty. Post replies only when the user authorized communication.
5. Classify CI failures from logs before retrying. Check for a stale base. Allow at most one justified infrastructure rerun; identical repeated failure needs diagnosis. Never churn code to quiet a bot.
6. Use available bounded checks or waits. Report missing watcher support. A green check at an older head is not evidence for the current patch.
7. Stop drive at merge-ready or an approval boundary. Babysit does not authorize merge or auto-merge. Route an explicitly authorized landing request to shipping.

Report mode, frontier, exact revision, checks, fixed and dismissed findings, pending work, and human gates.
