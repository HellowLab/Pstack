# Prepare public distribution

This repository contains a release candidate, not a published or approved marketplace plugin. No publisher agreement, dashboard upload, review submission, or marketplace publication was performed.

The root portable manifest follows [OpenAI packaging guidance](https://developers.openai.com/plugins/build/plugins). The distribution process follows [OpenAI submission guidance](https://developers.openai.com/plugins/deploy/submission), checked on 2026-10-05. Recheck those pages before submission because requirements can change.

## Before upload

1. Resolve pending source adaptation, fidelity decisions, and both-host installation/behavior checks in [validation](validation.md). Review the ZIP contents and its checksum from a clean checkout of the exact approved commit.
2. Have the owner select the OpenAI organization and project that will own the plugin and complete individual or business publisher verification. GitHub organization membership does not establish an OpenAI verified publisher. An OpenAI organization owner can submit; another member needs the appropriate Apps Management Write role.
3. Confirm the actual verified publisher name, listing text, category, support route, and supplied artwork. The package uses HellowLab's independent identity and preserves Lauren Tan's attribution. It does not reuse the upstream logo. The display name and banner are `Pstack`; the listing subtitle is exactly `Ship faster. Build better.`. The original artwork retains its approved `The unofficial Plugin` text; the listing change does not modify the raster. The machine identifier `pstack` passes package-schema validation, but marketplace identifier availability is unverified without publisher access.
4. Resolve any dashboard metadata requirements against current guidance. A skills-only package does not require the four MCP review URLs or MCP review test-case block. Do not invent legal URLs, reviewer credentials, or demo evidence. The approved original artwork is included and referenced by both required icon fields. Verify its presentation in the target host and publisher dashboard before submission.
5. Decide whether the documented unsupported runtime capabilities are acceptable for the initial public offering. Do not market those capabilities as implemented. A real runtime port needs separately reviewed scope.

## Artwork gate

The approved original is [assets/pstack.jpeg](../assets/pstack.jpeg): 1254 × 1254 pixels, RGB JPEG, 723089 bytes, SHA-256 `fa5786e6f6a39ea36fd5bc09ac542b647094268c192de421b8eb4e771c87585d`. Its bytes and pixels were checked before packaging. The banner reads `Pstack` and the subtitle reads `The unofficial Plugin`. The repository and ZIP retain the exact original; there is no crop, conversion, redraw, or substitute.

Both `logo` and `composerIcon` reference `./assets/pstack.jpeg`. The original meets the documented [image format, size, and dimension requirements](https://developers.openai.com/plugins/deploy/submission#icons-and-screenshots). Host rendering and marketplace branding approval remain distinct checks. The chalkboard's "Always up to date" text is artwork copy, not a zero-lag claim: [maintenance](maintenance.md) describes the daily check, review gate, and current permission limitation. Listing approval and identifier availability remain publisher-dashboard checks; do not infer them from a valid local manifest.

## Submission sequence

After the owner authorizes submission, upload the complete ZIP from `dist/` in the OpenAI Plugins dashboard under the verified developer identity. Resolve package and skill scan findings, upload corrected versions, and complete applicable review information. Skills-only packages omit MCP configuration and the MCP review block. Current guidance does not support adding an MCP server later to an existing skills-only plugin, so reconsider that product boundary before the first public publication.

The owner must separately authorize and complete required policy attestations and submission. Track review feedback and make corrections. After approval, publication is still an explicit owner decision. No GitHub workflow in this repository performs any of these actions.

For metadata or skill updates, build and upload a complete new ZIP version, repeat applicable checks and review, then publish only after approval. Keep the pinned upstream commit, adaptation review, host evidence, and package checksum with every release.
