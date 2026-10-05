# Create verification skill

1. Inspect the project's actual launch command, user-facing surface, existing harness, observable output, and isolation needs. Check dependencies and supported tools before choosing a driver.
2. Create a skill in the project's documented skill location, or an ordinary draft directory if no install location is known. Include name and description metadata.
3. Write Launch, Doctor, Drive, Evidence, and Cleanup sections with real commands and selectors. Kill only processes started by the run. Keep evidence outside disposable state.
4. Add a feature map index and one page per initial feature. Each page identifies sub-features, user entry points, harness actions, observable outcomes, and gotchas.
5. Run the generated instructions through one feature end to end. Check launch readiness, user actions, side effects, teardown, and surviving evidence. Clean failed attempts too. If you cannot execute this, label the result an untested draft.
6. Point to [maintain-verification-skill](../maintain-verification-skill/SKILL.md) for future audits. Do not create a schedule unless requested.
