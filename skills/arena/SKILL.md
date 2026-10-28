---
name: arena
description: "Compare competing solutions, choose a base, and incorporate useful parts. Use for /arena, arena this, or design bakeoffs."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](references/host-contract.md) before acting.

# Arena

Fan out N parallel attempts at the same task. Read every candidate end to end. Pick the strongest as the base. Graft the best ideas from the others into it. Verify the synthesized result.

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## Phase A: Frame

The N candidates will receive the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric. State what success looks like for *this* task, then turn it into 3-6 concrete gradeable criteria. The rubric is the picker's tool in Phase D. Candidates only see the task.
3. Pick actual permitted host workers. Inherit the current model unless a supported model override was requested. Record the real runner/model capabilities. Without delegation, produce clearly labeled sequential candidates; if independent or multi-model judgment is required, that gate stays blocked.
   Use accepted `arena runners` preferences from the current session or an authorized project document. An unconfigured role has two inherited entries. Run one permitted worker per entry. Preserve the accepted `arena cross-judge pool`; its order expresses preference. An unconfigured pool has two inherited entries, which are not eligible cross-family judges. If a runner is unavailable, use only an observed, permitted replacement consistent with the accepted preferences, or report the dropped seat. Do not silently change saved choices or expand access. Preserve a minimum of two runners unless the accepted list explicitly requested one; if permitted replacements cannot run, disclose the reduced coverage. Repeated inherited models do not establish model diversity.
4. Assign output paths. Each candidate writes to its own location (a git worktree where possible, otherwise `/tmp/arena-<slug>/candidate-<n>/`), per the **separate-before-serializing-shared-state** principle skill.

## Phase B: Fan out

Assign all N candidates, concurrently only when the host supports permitted independent workers, each with the task, the path to the shared grounding, its own output path, and instructions to produce both the artifact and a short rationale.

Each rationale names the alternatives the candidate considered and what it rejected.

If a candidate fails to produce output, proceed with N-1 and note the dropout in the synthesis record.

## Phase C: Cross-judge

After all Phase B candidates complete, try the accepted pool in order and select at most one actual read-only judge from a model family different from the parent's. `inherit-parent` and `auto` never qualify as cross-judges. Use only observed supported models and authorized overrides; do not invent family defaults or change access. If the parent's family is unknown, disclose that the family check could not run and do not claim cross-family review. If no eligible permitted judge runs, skip the judge and say so; the parent may pick the base alone. An explicit independent or diverse-review requirement remains unfulfilled rather than being silently downgraded.

The judge sees the rubric and completed candidates by path label, scores each criterion and recommends a base. Run it alongside the parent's reading only when supported, never while candidates are still writing.

## Phase D: Pick a base

Read every candidate end to end before picking.

Score each candidate against the rubric criterion by criterion, not on holistic feel. Compare against the cross-judge when one ran. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base on which candidate a future maintainer can extend most easily without breaking invariants. Prefer the cleaner boundary or smaller API when two feel tied, per the Laziness Protocol.

Record the pick and the reason in a short synthesis note alongside the base artifact, including the cross-judge's verdict or the reason it was skipped.

## Phase E: Graft

Walk each losing candidate once more and identify what is worth porting into the base. The signal is usually one or two things per candidate, not most of it.

Fold each graft in by hand, per the **redesign-from-first-principles** principle skill. Don't paste mechanically. The result has to remain coherent under one mental model.

Record what was grafted, from which candidate, and what was rejected and why.

When N candidates converge on the same shape, that is a strong agreement signal. Note the convergence in the record and ship the consensus shape. No graft is needed. When N candidates wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

The synthesized artifact has to hold up under the same scrutiny as any other output, per the **prove-it-works** principle skill.

If verification surfaces a problem the arena did not catch, either Phase A was wrong (re-frame and re-run) or one candidate caught it and you missed the graft (go back to Phase E). Don't paper over.

## Outputs

One synthesized artifact. One short synthesis note alongside, naming the base, the grafts (with source candidate), the rejections, the dropouts if any, and the verification result.
