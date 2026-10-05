# Bug fix

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Reproduce on the actual affected surface using an available driver. If access prevents reproduction, attempt what is reachable and state the precise gap. Never call source inspection a reproduction.
2. Ground with how and why. Form candidate mechanisms, choose experiments that eliminate the most possibilities, and instrument unclear runtime state. Confirm the surviving mechanism before planning the fix. Revert changes whose hypotheses were refuted.
3. Use architect if the fix changes a function boundary. Implement the smallest change justified by evidence, using a separate owner when actual delegation is available.
4. Re-run the original reproduction on the same surface. Unit tests alone do not establish absence of a runtime bug.
5. Use tdd for a cheap, meaningful regression path. Capture failing-before and passing-after evidence; do not manufacture a test solely to mirror implementation.
6. Follow opening-a-pr when authorized. Report symptom, root cause, fix, actual repro output, and remaining gaps.
