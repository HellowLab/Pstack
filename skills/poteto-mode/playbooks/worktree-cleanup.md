# Worktree cleanup

Read [the host contract](../references/host-contract.md) before acting.

1. Inventory worktrees through the available Git or host API, along with tracked, untracked, and ignored work, branch state, size, and known active usage. Do not infer inactivity from age or a name.
2. Check pinned/active work through supported host tools or the user's supplied list. If usage cannot be determined, hold the candidate.
3. Present concrete removal candidates and retained work. Preserve recoverable snapshots where the host supports them. Deletion requires the user's applicable authorization; a cleanup skill is not permission.
4. Remove only confirmed, authorized, inactive worktrees through the supported host cleanup API or Git. Never force removal to bypass dirty-state checks and never broadly delete app data, caches, or simulator state.
5. Re-list and measure actual reclaimed space. Report removed paths, retained candidates and reasons, and any missing safety evidence. Simulator cleanup is separate host-specific work.
