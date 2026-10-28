---
name: interrogate
description: "Try to break changes or designs with safe real-code runs, rerun findings and report evidence without applying fixes. Disclose unavailable execution or independent review. Use for /interrogate."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](references/host-contract.md) before acting.

# Interrogate

Adversaries try to break a change or design. Keep only findings established by an actual run against the relevant code and confirmed by rerunning it. Do not auto-apply fixes or post findings externally without the user's authorization. A single-agent critique is not an independent or multi-model review.

## Frame

Use the scope the user names. Otherwise include the branch diff from its merge base with the actual base branch through the working tree, including relevant staged, unstaged and untracked work. Preserve all original files. State the intent in your own words from the user's message, commits and PR description; clarify genuine ambiguity before assessing violations.

## Fan out

Use the framing, isolated output locations and fan-out practices in [arena](../arena/SKILL.md), with accepted `interrogate reviewers` preferences instead of arena runners. An unconfigured role has two inherited entries. Run only actual permitted reviewers. Inherit the current model unless a supported override was requested. Preserve confirmed panel lists and report unavailable seats; repeated inherited models do not establish model diversity. If explicitly requested independent or multi-model review cannot run, report that gate as blocked, not satisfied by a single-agent substitute.

Copy scoped uncommitted changes into each isolated reproduction workspace so reviewers test the actual candidate, not just HEAD. Give each reviewer the same scope and intent and this brief:

> Try to break this change. Prove each finding with a safe run against the real code, such as a failing test, reproduction script or command showing behavior that violates the intent. For a design or plan, use an authorized isolated prototype or probe the current tree. Keep reproduction files in your own workspace. Report a title, exact command, actual output and expected output for every finding. Leave out unexecuted claims, stylistic preferences and speculative future risks. No verified findings is a valid result.

Inspect reproduction commands before running them. Review permission does not authorize production writes, new credentials, dependency installation, external posting, or edits to the user's checkout. Use only available tools within scope. When execution is unavailable, unsafe or denied, record the exact missing check and reason; do not bypass it or invent output. Keep the real working tree unchanged and clean up only owned reproduction artifacts.

## Verify

Rerun each proposed finding's command in an authorized isolated environment matching the reviewed revision and working-tree changes. Keep it only when the observed output demonstrates a failure that breaks the stated intent. Record the rerun evidence. Merge findings that share a root cause and retain every distinct verified finding, not one reviewer's preferred list. Skip arena's cross-judge, base selection and grafting phases: review does not choose a candidate or apply fixes.

Drop unconfirmed findings with a reason. Blocked execution is an unverified coverage gap, not proof that no bug exists. Distinguish no verified findings from a complete clean bill of health; state what could not be exercised.

## Output

- Intent: the agreed purpose and exact reviewed revision, including any uncommitted scope.
- Findings: every verified issue, exact command, actual output, expected behavior, how it breaks intent and which real reviewers found it.
- Dropped: each reviewer's dropped count and reasons, including unavailable reruns.
- Coverage limits: missing tools, blocked execution, untested paths and any unmet independence or diversity requirement.
