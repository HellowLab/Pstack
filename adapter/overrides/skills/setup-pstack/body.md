# Setup pstack

Configure the user's model choices and reasoning budget for each Pstack role using capabilities the host actually exposes. This workflow does not install models or create an always-applied host rule.

## Steps

### 1. Detect available models

Inspect the actual delegation tool schema and any documented model-capability API available in this session. Record supported model identifiers, reasoning controls, and combinations. Never invent an identifier, infer model entitlement from a name, or treat a model list as permission to delegate.

`inherit-parent` and `auto` are preference aliases: both mean omit the model override and inherit the parent. They are not API model identifiers. If model selection or reasoning control is unavailable, explain that limitation and keep the affected choice inherited. Do not request credentials or change host settings to work around it.

### 2. Load current state

Read the Pstack role preferences already supplied in this conversation or in an explicitly identified, authorized project document. Do not search unrelated global configuration. Start with inherited roles when no configuration exists. Keep existing user-selected models and panel lists when still available; mark unavailable choices for resolution. Identify retired roles and show them before removing them from the proposed configuration.

### 3. Budget, map, and confirm

Ask for a budget, naming the current choice when known. Use the host's structured question tool when available, otherwise ask in plain text. Preserve these upstream choices as requested effort targets:

- `unlimited — keep max`
- `large — xhigh reasoning`
- `medium — high reasoning`
- `small — medium reasoning`

These labels are preferences, not price estimates or guaranteed host capabilities. `unlimited` retains each role's existing effort; the other choices target `xhigh`, `high`, or `medium`. Apply the target to every explicit model choice, including panel entries, only through documented supported controls. When the host exposes effort-bearing model variants, choose an observed same-family variant at or below the target on the ladder `max` > `xhigh` > `high` > `medium` > `low`. Do not derive a new identifier by editing its text. If no valid combination is known, mark the role as needing a choice. Inherited aliases keep the parent's settings.

Show every role and its model/effort or inherited setting. Ask whether to accept the proposed table or change particular roles, offering only observed choices and the two inherited aliases. Reuse choices the user has already confirmed. A model choice becomes an override request only when the user accepts it; this skill alone does not authorize an override.

Preserve all of these roles in the table:

```text
feature, refactoring: inherit-parent
bug-fix: inherit-parent
perf-issue: inherit-parent
hillclimb: inherit-parent
judgment and prose: inherit-parent
hardest tasks: inherit-parent
how explorer: inherit-parent
how explainer: inherit-parent
why investigators: inherit-parent
why synthesizer: inherit-parent
reflect tooling: inherit-parent
reflect judgment, divergent, synthesizer: inherit-parent
arena runners: inherit-parent, inherit-parent, inherit-parent
arena cross-judge pool: inherit-parent, inherit-parent, inherit-parent
swarm workers: inherit-parent
architect runners: inherit-parent, inherit-parent, inherit-parent
interrogate reviewers: inherit-parent, inherit-parent, inherit-parent
```

For arena runners, architect runners, and interrogate reviewers, one actual worker runs per list entry when delegation is permitted. Alias entries still count toward panel size. Multiple inherited workers do not establish model diversity. Arena chooses one cross-judge from its pool, preferring an observed model family different from the parent's when available. Swarm uses its worker default unless a race or comparison assigns another supported model per arm. Unavailable independent or diverse review remains a stated gap.

### 4. Validate

Validate each explicit identifier and effort combination against observed host capabilities. Validate every panel entry separately. Do not silently replace an unavailable choice: resolve it with the user or leave that role blocked. Preserve inherited aliases as preferences, omitting model and effort overrides when calling a tool.

### 5. Write the rule

Use the accepted table in the current session. If the user requests persistence, write it to the authorized project-local preferences document using the project's existing instruction mechanism where documented. Include the budget, all roles, and any unresolved limitations. Replace only the Pstack configuration section so reruns are idempotent and unrelated instructions survive. Do not write global rules, install plugins, or change credentials or access controls without that scope.

If no supported persistence mechanism is available, return the complete table for reuse and say it is session-only. A Markdown file is not automatically loaded by every host. Do not promise that a saved preference applies to new sessions unless the host's actual loading mechanism has been verified.

### 6. Confirm

Report the accepted budget and role choices, any blocked roles, and the exact saved location when a write succeeded. Distinguish current-session use, saved preferences, and verified future loading. Re-running setup updates the configuration rather than adding duplicate sections.

### 7. Offer a verification skill (optional)

Inspect the project's existing verification skills or test harness. If none can drive the real app, offer once to create a project-local verification skill. On acceptance, route to [create-verification-skill](../create-verification-skill/SKILL.md). On refusal, continue without repeating the offer.
