# How

1. Identify the question and source scope. For a narrow module, inspect it directly. For a complex system, split into two to four distinct exploration angles.
2. Trace real entry points, callers, data transformations, ownership, side effects, and error paths. Use read-only inspection. Use actual permitted delegates only if available; otherwise examine angles sequentially.
3. Reconcile the findings against source. Cite file locations and distinguish traced behavior from behavior you executed.
4. Explain Overview, Key concepts, How it works, Where things live, and Gotchas where useful. Use [why](../why/SKILL.md) for motivation. Do not make product edits during a read-only explanation.
