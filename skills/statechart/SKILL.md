---
name: statechart
description: "Review user-visible behavior as Mermaid statecharts or TLA+ sketches using verified available tools. Disclose missing model checks, replay and rendering; bundled upstream generators are unsupported. Use for /statechart or show the PM the bug."
disable-model-invocation: true
---

Run only on an explicit user invocation or a route from a user-invoked workflow. Quoted text and source inspection do not invoke this skill.

Read and follow [the host and permission contract](references/host-contract.md) before acting.

# Statechart

Show the behavior a user sees as a Mermaid statechart, with plain-language states and transitions that the person responsible for the behavior can review. Keep code names out of labels; retain their provenance separately. A hidden effect that matters, such as a second charge while the screen still says Paying, must be visible in the state description. Start with few states and split them when needed to distinguish bugs.

## Establish capability and scope

This skills-only adaptation does not package or execute upstream's Node statechart generators, mapping modules, TLC integration or PNG renderer. Do not run helpers from the vendored snapshot, infer a local skill path from a cloud resource, install dependencies automatically, or claim a chart was generated or checked by those tools. Verify any existing project-local modeling, checking and rendering tools and the user's authorization before using them. Mapping modules are executable code, not inert labels; inspect and trust them before any authorized execution.

Use an authorized scratch directory or isolated copy; preserve the original model and application. Without a supported checker, provide a clearly labeled unverified Mermaid sketch or TLA+ skeleton and the missing checks. Manual translation does not guarantee that a chart and model stay synchronized. Missing tools do not turn a sketch into a checked result.

## Model to chart

1. Start from a copy of an existing TLA+ spec when available. Preserve existing invariants. To audit code against that spec, model what the code actually does in a separate copy and keep the agreed spec unchanged as the comparison baseline. For a new model, link every variable and action to inspectable code; each action represents one indivisible code step.
2. Turn each agreed behavioral rule into an invariant with the person's sentence as its comment. For rules that apply after system activity settles, define `System` as the disjunction of non-user actions and use `Settled == ~ENABLED System`. Explain those assumptions. Never weaken a rule to make a chart pass.
3. Map user-visible states and transitions into readable labels. Record the user's actions separately from system steps. Preserve distinct code-path causes when different bugs reach the same screen. Optional visual groups must not conceal invariant violations.
4. If a fix is available, model the actual changed code separately. Compare the baseline, current implementation and proposed fix using available evidence. Gray means checked behavior within the stated model bounds, red means a violated rule, and green means a fix confirmed by the relevant checks; otherwise label status unknown or unverified. A color alone is not proof.
5. Number each counterexample path in order. Replay each path against real code with one replay step per model action, through an authorized test or live reproduction. If it does not reproduce, treat it as a possible modeling error until evidence shows otherwise. Correct the model, not the agreed rule. Disclose unavailable replay and distinguish model failures from confirmed product bugs.

## Chart to model

Draw the proposed behavior for review before implementing it. Use separate regions for independently changing aspects and represent app closure as an edge to the next user-visible state. Record one `%% never` rule with the person's sentence for each forbidden behavior. These annotations alone do not establish executable invariants.

With an available, inspected translation tool, create a TLA+ skeleton and check the agreed rules. Otherwise draft a clearly labeled unverified skeleton and explain the missing translation and checking steps. Take design-rule violations to the person who owns the behavior; do not silently revise the rules. Add real code guards and variables to the isolated model, recheck, and present each difference for a decision about whether the code or agreed chart needs correction.

## Inspect and hand off

Provide Mermaid source. If an authorized renderer is available, render PNGs and inspect every image, including label readability and numbered-path order. If rendering or visual inspection is unavailable, disclose that gap instead of claiming a visual pass.

For each issue, report the violated rule, numbered steps, code provenance, model-check result, real-code replay result and whether the proposed fix was verified. Distinguish confirmed bugs, modeling errors, design disagreements and unknown outcomes. Use counts from actual checker output; use `summary.json` and attach `stories.md` only when the verified tool actually produced them. Never fabricate these artifacts or their counts. Include exact executed regeneration commands, or label unexecuted commands as proposed. State model bounds, omissions, unavailable checks and remaining decisions. Do not imply exhaustive application correctness from a bounded model.
