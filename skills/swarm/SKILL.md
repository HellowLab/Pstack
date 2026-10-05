---
name: swarm
description: "Coordinate coverage, races, or exploration across available workers. Use for /swarm, swarm this, or parallel coverage."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](../../resources/host-contract.md) before acting.

# Swarm

1. Frame the done condition and choose partitioned coverage, identical-brief race, or a mix. Declare first-pass, rank-all, or best-of selection before a race.
2. Assign scopes, exact revisions, verification methods, and isolated writable outputs. Use only real, permitted host workers. Without them, perform serial coverage and call it sequential, not a swarm.
3. Each result records PASS, ISSUES, or BLOCKED with evidence, revision, and method. Missing evidence is a gap, never a pass. Retry a missing report at most once when practical.
4. Read all results, verify material claims, and aggregate coverage and disagreements. For races, apply the declared selection rule.
5. Report a compact table, evidenced issues, dropouts, and unresolved slices. Do not promise cloud workers or model diversity unavailable in this session.
