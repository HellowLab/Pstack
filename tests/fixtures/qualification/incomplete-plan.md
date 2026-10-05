# Durable delivery plan

Add persisted retry state.

## How to read this

One checkbox is one unit. Only check it after evidence exists.

## Program checklist

- [ ] Arm the program with an available execution host.
- [ ] Spawn owners.
- [ ] Follow PR mechanics.
- [ ] Collect verdict and merge.
- [ ] Write the boot recipe.

## PR 1

### Depends on

None.

### Files

- [ ] Update queue.py; evidence is the diff.

### Build

- [ ] Build; evidence is build.log.

### You see

- [ ] Retries survive restart; evidence is restart.png.

### Verify unit

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Queue tests pass; evidence is unit.log.

### Verify live

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

1. Restart a pending job; screenshot restart.png; Pass when the attempt count persists.
1. Retry a sent job; screenshot retry.png; Pass when no duplicate delivery occurs.

### Verify perf

- [ ] Metric: request latency.
- [ ] Probe: TBD.
- [x] Baseline: assumed from the old queue; no measurement exists.
- [ ] Rule: it should be fast.

### Review gate

None; this changes the console retry interaction.
- [x] Operator approved; no decision was recorded.

### Merge

- [ ] Merge when CI is green; evidence is the CI badge.

## Close the program

Close when the merge checkbox is checked.

## Prototype evidence

No artifacts recorded.
