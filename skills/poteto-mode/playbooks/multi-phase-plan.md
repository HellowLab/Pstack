# Multi-phase or multi-PR plan

Apply the [host and permission contract](../references/host-contract.md). The plan is the deliverable. Do not implement.

1. For an obvious one- or two-file change, explain why a separate plan is unnecessary and stop.
2. Settle experimentally answerable questions through the authorized Prototype playbook. Ask the operator about product or preference decisions no run can settle; do not exceed a read-only request or mandatory approval boundary.
3. Write the plan at an authorized path or as a host-supported artifact. Open with the goal, PR ids in landing order, dependency graph and file ownership. Distinguish independent PRs branching from trunk from genuine stacked dependencies. Give each PR checkboxes for dependencies, edited files, one change, observable result and verification. State whether authorization calls for merge or operator handoff; after handoff, no further pushes without operator authorization.
4. Tests alone are not sufficient verification. Cover unit, live and performance evidence appropriate to each PR. Each live scenario names the actual control surface and pass predicate. Each applicable perf check names metric, probe, trunk baseline measured first and failing threshold. Explain non-applicable checks and unavailable capabilities; do not fabricate execution or ratios across unlike scenarios. Changed interactions wait for operator review before merge. Existing required gates remain binding.
5. Return the plan path, PR dependencies, review-gated set and what remains unproven, then stop. Execution starts on the operator's explicit go.

Review the plan against its task and preserve independent-review requirements. No fixed lane count, mandatory appendix skeleton or bundled executable checker is required.

Report this checklist review as structural review, never as a script run.
