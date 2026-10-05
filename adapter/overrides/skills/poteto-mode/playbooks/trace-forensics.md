# Trace forensics

Read [the host contract](../../../resources/host-contract.md) before acting.

The captured artifact is the evidence. Diagnose it without re-running the workload or changing product code.

1. Identify the format and use an available parser. Process large captures in bounded slices or actual permitted delegates. Keep the reduced findings in the main context.
2. Transform the capture into a queryable structure, such as a table of samples, frames, or heap nodes. Preserve the original artifact.
3. Find the hot path, retainer chain to a garbage-collection root, or blocked thread and its wait reason. Trace the mechanism instead of reporting only the largest number.
4. Map the finding to file, symbol, and line using the capture's source information. Resolve missing symbols where possible; otherwise report the limitation.
5. Compare a paired capture when available. Without corroboration, call the finding the strongest supported hypothesis rather than a confirmed cause.
6. Return the artifact format, reduced finding, source mapping, evidence paths, and confidence. Record throughput checkpoint: n/a, read-only forensics. Route to bug-fix or perf-issue only when that work is requested.
