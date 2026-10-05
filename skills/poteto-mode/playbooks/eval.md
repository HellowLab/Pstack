# Eval

Read [the host contract](../../../resources/host-contract.md) before acting.

1. State the variant and expected behavior. Define three to six observable rubric criteria outside candidate context.
2. Use isolated, neutrally named task directories and a natural user prompt. Do not leak labels such as eval, test, judge, experiment, rubric, score, candidate, or arena into candidate-visible context. Do not request hidden reasoning or lists of applied principles.
3. Run actual available independent candidates with equivalent task inputs. A multi-model comparison requires real supported models; if absent, report it blocked rather than role-playing diversity.
4. Give an actual independent judge sanitized outputs and the rubric without model labels. One judge scores both variants on the same scale. If unavailable, label any manual assessment non-blinded and non-independent.
5. Inspect observable tool traces through documented host access, not private app storage. Grade opened resources and resulting behavior, not self-report. If traces are absent, report that coverage gap.
6. Read all outputs, reconcile findings, and report variant, rubric, actual candidates, judge, failures, synthesis, and promotion recommendation. Do not promote solely on static checks.
