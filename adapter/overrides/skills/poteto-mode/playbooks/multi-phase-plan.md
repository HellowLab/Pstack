# Multi phase plan

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Ground the goal and produce a program checklist with checkable phase gates. Order by dependencies and the riskiest uncertainty. Each unit names owner role, exact inputs, output, verification, and stop condition.
2. Record one base-branch chain for dependent changes and separate branches for independent work. A single coordinator owns topology. Actual concurrent workers require isolated writable outputs and available lifecycle controls.
3. Include a boot recipe for each lane: scope, source revision, prerequisites, setup, launch, verification, cleanup, and handoff artifacts. Avoid private data and secrets.
4. Record prototype evidence, rejected alternatives, risks, and real reference links. Mark planned, active, verified, blocked, and completed work explicitly.
5. Keep implementation, independent verdict, and landing gates separate. A parent report cannot satisfy an unavailable verifier or grant merge authority.
6. Close by reconciling every unit with actual artifacts, checks, and remaining work. For persistent multi-day execution, route to orchestrate and report its unsupported runtime requirements.
