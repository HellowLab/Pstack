# Shipping

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Confirm the user's landing scope, forge access, and ordered stack. Do not infer merge authority from a style skill, green CI, or babysit request.
2. Obtain a real independent verification verdict per PR on the actual changed surface. Record reviewer identity, base SHA, head SHA, stable patch identity, and evidence. CI and author self-review do not replace this gate. If independent verification is unavailable, stop at a documented ready-for-review state.
3. Walk bottom-up and stop at the first missing or failing verdict. A verified child above an unverified parent cannot land.
4. Before each landing, re-read current base, head, mergeability, reviews, and CI. Re-run verification after a changed patch; this adaptation conservatively re-verifies every changed patch instead of using upstream's build-noise exception.
5. Prepare only the current bottom PR against current trunk. Rebase or retarget only when authorized and safe for the branch. Re-check verdict validity and exact-head checks afterward.
6. Merge one PR at a time only within explicit authorization. Do not enable auto-merge unless separately requested and supported. Confirm the actual merged result and fetch trunk before preparing the next PR.
7. Recompute the remaining chain after each merge. Do not assume automatic retargeting or infer queue readiness from a single auto-merge flag.
8. Stop at the verified ceiling. Report landed revisions, actual verdicts, pending gates, and the next unverified PR. No automatic public release is part of shipping.
