# Refactoring

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Learn and pin the behavior contract with how plus characterization tests, snapshots, or an equivalence harness before moving structure. Type checks and lint alone are not the behavioral pin.
2. Name the missing structure and target module layout, types, and call graph. Use architect for a change crossing function boundaries. Large migrations route to figure-it-out.
3. Delete dead code and redundant layers first. Move in small behavior-preserving steps. Migrate every caller and delete replaced internal APIs in the same wave. Check references in strings and prose too.
4. Use an actual permitted delegate for mechanical edits when available; otherwise work sequentially. Separate new features and discovered bugs from the agreed structural scope.
5. Prove equivalence using real output or the matching user surface. Keep each step green. Retain the change only if it reduces reader effort.
6. Prepare ordered subtraction, reshape, and cleanup commits when in scope; follow opening-a-pr if authorized.

Report changed structure, pinned contract, equivalence evidence, reduced complexity, and reverted work.
