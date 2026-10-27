# Install and update Pstack

Use the prompts in the [README](../README.md#install-pstack) with an agent that can reach your chosen target. These instructions authorize only the installation or update you request. They do not authorize public submission, repository edits, access expansion, or changes to another installation.

## Choose and verify the release

1. Resolve the [Latest GitHub release](https://github.com/HellowLab/Pstack/releases/latest). Use its versioned `pstack-<version>.zip` asset and matching `.zip.sha256`, not GitHub's source-code ZIP, an unqualified preview, or a moving branch.
2. Check the release version, tag target, changelog, and passing validation evidence. Download both assets over HTTPS from that release. Compare the ZIP's SHA-256 with the checksum file and the release asset digest when available. A checksum verifies matching bytes; it does not replace trusting the source.
3. Inspect the archive before extracting it. Reject unsafe paths, confirm both manifests name Pstack and the release version, and retain the license and attribution. Record the release URL, tag commit, checksum, and chosen target for future updates.

Do not downgrade an existing installation. If its source, identity, or local customizations are unclear, resolve that before replacing files.

## Install on one computer

Check the installed client's help and plugin support first. OpenAI documents local marketplace catalogs and native installation through the desktop plugin directory. Its current [CLI reference](https://learn.chatgpt.com/docs/cli/reference#codex-plugin) also documents `codex plugin list --json`, `codex plugin marketplace list --json`, `codex plugin add`, and `codex plugin remove`. Use only commands your installed version supports.

Inspect existing entries before creating one. For a first installation, use an isolated checkout of the verified release tag and run `python3 scripts/stage_local.py /absolute/new/staging-directory`. Choose a durable user-owned directory outside application projects. The script refuses an existing destination and stages the exact checked archive in a marketplace named `pstack-preview`; it does not install anything. Confirm that the staged files match the downloaded release ZIP.

Register that directory with `codex plugin marketplace add /absolute/new/staging-directory`. On a compatible CLI, install with `codex plugin add pstack@pstack-preview`. Otherwise, if the desktop app supports the registered local source, select it in the Plugins Directory and install Pstack there. Stop if neither route is available. Do not change credentials or enable unsupported features to force installation. OpenAI's [local packaging guide](https://developers.openai.com/plugins/build/plugins) describes marketplace setup.

Start a new session. Check the installed version, enabled state, skill discovery, and a harmless read-only invocation. Record what ran and what remains untested. Local catalogs and caches do not provide account synchronization.

### Why there is no direct Git shortcut yet

This repository does not expose a release-only Git marketplace. Its root contains vendored upstream helpers and review material that the qualified ZIP excludes. Do not register the repository root as a plugin source or install a moving maintenance branch.

A future Git route needs a dedicated package directory, immutable release pinning, and guarded catalog updates. It also needs a native upgrade test that verifies the installed cache and version. Until then, use the verified ZIP staging route. Refreshing a Git marketplace alone is not evidence that its installed plugin was updated.

## Install in a private personal account

Use [Plugin Creator](https://learn.chatgpt.com/docs/build-plugins) only when available and permitted. Inspect the current account context and any existing Pstack plugin before writing. Resolve an existing plugin by its actual identity, not its name alone.

PRIVATE visibility is not personal scope. The current creation tool defaults to the active WORKSPACE when one exists; it creates personal USER scope only without an active workspace. Confirm the current tool contract before each operation. If personal scope cannot be established, stop and explain the required account-context change. Do not silently create a workspace plugin or substitute a local installation.

If a matching personal plugin exists, update that identity through supported tools and preserve its audience, metadata, prompts, and user configuration. Create one private personal copy only when none exists and creation is authorized. Use the verified release package rather than reconstructing its skills from summaries. Read back the saved scope, visibility, version, and packaged files.

Saving a plugin is separate from installing or enabling it. Complete any supported installation step, start a new session, and verify access there. Repeat checks in the clients you intend to use. [OpenAI's plugin guide](https://learn.chatgpt.com/docs/plugins) describes supported clients; it currently excludes the IDE extension. Account saving does not prove availability in every Codex client.

## Update only the chosen installations

Compare the recorded installed version with the latest qualified release. If there is a newer version, verify its assets and inspect the package delta before updating. Preserve existing identity, settings, and customizations. Use a new staging directory and the client's supported update procedure for local installs; do not assume refreshing a catalog updates installed files. `codex plugin marketplace upgrade` refreshes Git marketplace sources, not arbitrary local ZIP installs. If the client lacks a safe update path, report that limitation before removing or replacing anything.

For private plugins, use the existing identity and recheck personal scope before saving. Re-read the target's current version immediately before writing to avoid overwriting a newer concurrent update. Verify the installed version and new-session behavior afterward. Separate a successful save from an untested installation or behavior check.

A weekly assistant task must record the selected targets and have supported access when it runs. Confirm the schedule exists and what actions it can execute. Report an offline computer, missing tool, or required approval without changing another target. Never create duplicate installs, downgrade, edit this repository, or submit a public plugin. Notify the user when an update completes or action is needed; keep unchanged checks quiet.

## Remove an installation

For the local example above, a compatible CLI supports `codex plugin remove pstack@pstack-preview`. Inspect the actual identity first if yours differs. Remove `pstack-preview` with `codex plugin marketplace remove pstack-preview` only if you no longer need that source and it contains no other wanted plugins. Do not delete unrelated staging files or configuration.

For a private account installation, use the host's supported uninstall or disable control for that exact plugin. Removing access and deleting an owned plugin are different actions; do not delete the plugin or its files without an explicit request. Verify the result in a new session.

## Qualification limits

Pstack 0.1.13 has repository-test, reproducible-package, and isolated Linux CLI installation/discovery evidence. The native test used Codex CLI `0.159.0-alpha.3`, separate empty home/configuration directories, and no copied credentials. It verified all 183 installed files, 58 discovered skills, relative references, and native uninstall cleanup. Model smoke tests were blocked by missing authentication in that isolated environment. Account installation, macOS/Windows installation, and actual model behavior were not tested in this check. The agent must report the actual capabilities and verification results of your environment. See [version-specific validation](validation.md).
