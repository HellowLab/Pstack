# Prepare public distribution

This repository contains a release candidate, not a published or approved marketplace plugin. No publisher agreement, dashboard upload, review submission, or marketplace publication was performed.

The root portable manifest follows [OpenAI packaging guidance](https://developers.openai.com/plugins/build/plugins). The distribution process follows [OpenAI submission guidance](https://developers.openai.com/plugins/deploy/submission), checked on 2026-10-05. Recheck those pages before submission because requirements can change.

## Before upload

1. Resolve pending source adaptation, fidelity decisions, and both-host installation/behavior checks in [validation](validation.md). Review the ZIP contents and its checksum from a clean checkout of the exact approved commit.
2. Have the owner select the OpenAI organization and project that will own the plugin and complete individual or business publisher verification. GitHub organization membership does not establish an OpenAI verified publisher. An OpenAI organization owner can submit; another member needs the appropriate Apps Management Write role.
3. Confirm the actual verified publisher name, listing text, category, support route, and supplied artwork. The package uses HellowLab's independent identity and preserves Lauren Tan's attribution. It does not reuse the upstream logo. The current display name is Pstack-GPT and the stable machine identifier is `pstack-gpt`.
4. Resolve any dashboard metadata requirements against current guidance. A skills-only package does not require the four MCP review URLs or MCP review test-case block. Do not invent legal URLs, reviewer credentials, or demo evidence. The supplied artwork could not be transferred into this build environment after one supported retry. No substitute icon is included. Add the inspected, approved original before Codex distribution or public submission, since those require icons.
5. Decide whether the documented unsupported runtime capabilities are acceptable for the initial public offering. Do not market those capabilities as implemented. A real runtime port needs separately reviewed scope.

## Branding gate

The supplied artwork and product name require review against the [OpenAI brand guidelines](https://openai.com/brand/), particularly incorporated OpenAI marks and GPT naming. This is an unresolved public-submission issue, not a confirmed rejection. Do not silently rename the project, redesign the supplied image, crop it, or substitute a different logo. Resolve any necessary marketplace-specific variant with the owner first.

## Submission sequence

After the owner authorizes submission, upload the complete ZIP from `dist/` in the OpenAI Plugins dashboard under the verified developer identity. Resolve package and skill scan findings, upload corrected versions, and complete applicable review information. Skills-only packages omit MCP configuration and the MCP review block. Current guidance does not support adding an MCP server later to an existing skills-only plugin, so reconsider that product boundary before the first public publication.

The owner must separately authorize and complete required policy attestations and submission. Track review feedback and make corrections. After approval, publication is still an explicit owner decision. No GitHub workflow in this repository performs any of these actions.

For metadata or skill updates, build and upload a complete new ZIP version, repeat applicable checks and review, then publish only after approval. Keep the pinned upstream commit, adaptation review, host evidence, and package checksum with every release.
