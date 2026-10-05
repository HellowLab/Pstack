# Authoring a skill

Read [the host contract](../../../resources/host-contract.md) before acting.

1. Use documented host skill-authoring guidance or an available authoring skill. Do not assume a particular built-in dependency.
2. Keep instructions that change decisions. Reference structural sources and other skills by resolvable paths. Preserve explicit invocation intent.
3. Validate name and description metadata, links, packaged resources, and host/permission boundaries.
4. Run representative positive, negative, and unavailable-capability cases when behavior changes. A prose edit still needs review; static validation is not a host test.
5. Follow opening-a-pr only when authorized. Report the skill, design choices, executed checks, and remaining host validation.
