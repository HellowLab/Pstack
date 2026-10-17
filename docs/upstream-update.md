# Reviewed upstream adaptation

Reviewed upstream Pstack 0.15.25 at `101b274dd991f694e1f7024be2157e5f3adf07de` for adaptation 0.1.6 on October 17.

[Source comparison](https://github.com/cursor/plugins/compare/f713f14203cd6420cec13cd7c55c32d598dbab68...101b274dd991f694e1f7024be2157e5f3adf07de)

Two source files changed; subtree identity is separate review metadata, not a third source file:

- `README.md`: new Claude Code installation/generation directions and explicit Cursor-only Benny disclosure. Retain as attributed upstream source; the adaptation keeps its own installation and runtime disclosures. No upstream generator was executed.
- `docs/harness/claude-code.md`: new Claude Code-specific tools, subagents, model names, filesystem paths, transcript discovery, and unsupported-feature table. Classify as unsupported source-only material. Do not package its mappings or treat them as ChatGPT/Codex capabilities; the existing host contracts remain authoritative for supported workflows.

Reviewed hashes and subtree identity were updated only after inspecting both complete changes. The source-coverage failure and pending-adaptation gate correctly required this classification; neither was a regression in released 0.1.5. All prior archive/checksum pairs, including submitted rc.5, are preserved.

The October 17 upstream check ran on Ubuntu 24.04.5. It does not satisfy the separate October 19 Ubuntu 26.04 migration checkpoint.
