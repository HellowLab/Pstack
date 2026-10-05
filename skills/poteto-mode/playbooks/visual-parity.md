# Visual parity

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Establish an immutable screenshot baseline across relevant states before migration. No baseline means no parity claim.
2. Keep the harness, baseline, and acceptance criterion fixed. Do not restructure components just to hide differences. If the baseline is wrong, raise the issue before replacing it.
3. Migrate shared primitives first, then one component at a time. Use isolated outputs for actual permitted parallel work.
4. Capture and diff each component on the matching surface. For an exact-parity task, nonzero differences fail; investigate every delta. Missing image tooling is a verification gap.
5. Follow opening-a-pr for authorized batches. Report each component, diff result, harness location, evidence, and remaining work.
