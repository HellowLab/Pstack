# Pause safely

Read [the host contract](../../../resources/host-contract.md) before acting.

1. On an explicit pause or an impending session boundary, finish or back out of the current atomic step, stop new work, and stop owned delegates through available controls.
2. Do not perform an irreversible action to create a checkpoint. Save work in its authorized location; commit only if authorized and the branch contains only intended changes.
3. Write a resume note with goal, branch and revision, verified progress, failed checks, active processes, next actions, key files, and the decision-log path. Keep private notes out of public commits.
4. Report what is durable and the first resume action. If asked to keep working, continue within session and host limits; do not claim that an unavailable background mechanism exists.
