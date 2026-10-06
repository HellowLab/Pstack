# Prepare public distribution

The rc.4 private beta remains privately installed. The rc.5 candidate adds approved publisher and privacy metadata for a draft upload. No public review submission or marketplace publication has occurred.

The root portable manifest follows [OpenAI packaging guidance](https://developers.openai.com/plugins/build/plugins). The distribution process follows [OpenAI submission guidance](https://developers.openai.com/plugins/deploy/submission), checked on 2026-10-06. Recheck those pages before submission because requirements can change.

## Current preparation status

The verified individual publisher name is `SEAN P KUDRNA`. HellowLab remains the maintainer, and Lauren Tan retains the upstream MIT attribution. The rc.5 candidate uses that verified name for `author.name` and `extensions.com.openai.interface.developerName`. Verification does not authorize publisher attestations or submission.

The upload candidate is [pstack-0.1.0-rc.5.zip](../dist/pstack-0.1.0-rc.5.zip), 1,414,277 bytes, SHA-256 `26415a9643c42ecd8c83a79788446b858d90ad88c68ff315296b725325de9cdc`. Its 168 members include 51 skills, both manifests, original artwork, license, and attribution. Only the two manifests and coverage report's package version differ from rc.4. All skills, references, contracts, artwork, and approved listing copy are byte-identical. The private installed rc.4 was not updated. See [validation](validation.md#submission-candidate-rc5) for the candidate checks.

### Platform requirements and optional fields

Current [submission guidance](https://developers.openai.com/plugins/deploy/submission) permits JPEG. Release notes and country targeting are optional. Skills-only metadata validation does not require all four listing URLs, MCP review cases, a demo recording, or MCP credentials. Required skill scans must pass. The selected verified developer identity controls the directory publisher name.

The [plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines#privacy-policy) require a published privacy policy. The owner approved [the policy](privacy.md), privacy contact `me@seankudrna.com`, and [GitHub Issues support](https://github.com/HellowLab/Pstack/issues). Policy-only [PR #2](https://github.com/HellowLab/Pstack/pull/2) published the policy to `main`; its returned public text was verified byte for byte before adding `privacyPolicyURL` to rc.5.

The approved offering is free and available in all OpenAI-supported countries. The documented manifest setting is `extensions.com.openai.publication.countries: []`, which removes plugin-specific country restrictions. Do not enumerate countries or use an invented wildcard. The current documentation defines no plugin-price field; free availability is an operating and listing decision, not `review.commerce`. Leave the skills-only review object absent. These settings do not remove host eligibility, supported-country, or subscription requirements.

The package inspection found no MCP configuration, executable helper, hook, telemetry implementation, or publisher-controlled collection endpoint. This does not establish that no data is processed or that everything stays local. Workflows can use authorized host prompts, code, history, and integrations, and can save project preferences or decision logs. The policy must distinguish those host operations from any actual publisher support or collection practices.

### Remaining work

| Gate | Evidence and smallest next step |
|---|---|
| Individual publisher | Verification and exact display name `SEAN P KUDRNA` are confirmed. Use the selected identity for the authorized draft upload while retaining HellowLab maintainer attribution. |
| Privacy policy | Published and verified. rc.5 references the public policy and includes the approved contact. |
| Final candidate | rc.5 passes all 30 tests, reproducible build, isolated native installation, 168-file comparison, 51-skill discovery, 60 resource reads, and removal. The host returned the new publisher and policy URL. |
| Host qualification | Retain the coverage limits in [validation](validation.md#public-release-evidence-assessment). A limited beta requires explicit acceptance of those gaps; draft upload does not qualify untested behavior. |
| Listing and scans | Confirm identifier availability, publisher rendering, and the existing directory icon fallback. Run the required dashboard checks only after an authorized upload; no platform scan result exists yet. |
| Release decision | The owner authorized a draft upload after validation. Capability-limit acceptance, owner attestations, review submission, and marketplace publication remain separate decisions. |

Optional release-note draft: "Initial public candidate of HellowLab's independent adaptation of Pstack 0.15.13. Includes 51 skill entrypoints, 23 playbook routes, skill-local host contracts, architecture screening, and approved original artwork. Workflows use available, authorized host tools. Grok Bot UI and persistent orchestration runtimes remain unsupported. Upstream changes require review, and full host qualification remains incomplete." This text is prepared only; it is not a publication record.

## Before upload

1. Review the ZIP contents and checksum from a clean checkout of the exact approved commit, and verify the completed candidate checks in [validation](validation.md). Retain unresolved behavior and host coverage as explicit gaps. Draft upload allows dashboard validation; it does not pass the separate pre-submission and public-release gates.
2. Use the owner's selected OpenAI organization and project and Sean's verified individual identity. Confirm the exact display name and submission access. An OpenAI organization owner can submit; another member needs the appropriate Apps Management Write role.
3. Confirm the actual verified publisher name, listing text, category, support route, and supplied artwork. The package uses HellowLab's independent identity and preserves Lauren Tan's attribution. It does not reuse the upstream logo. The display name and banner are `Pstack`; the listing subtitle is exactly `Ship faster. Build better.`. The original artwork retains its approved `The unofficial Plugin` text; the listing change does not modify the raster. The machine identifier `pstack` passes package-schema validation, but marketplace identifier availability is unverified without publisher access.
4. Resolve any dashboard metadata requirements against current guidance. A skills-only package does not require the four MCP review URLs or MCP review test-case block. Do not invent legal URLs, reviewer credentials, or demo evidence. The approved original artwork is included and referenced by both required icon fields. Verify its presentation in the target host and publisher dashboard before submission.
5. Decide whether the documented unsupported runtime capabilities are acceptable for the initial public offering. Do not market those capabilities as implemented. A real runtime port needs separately reviewed scope.

## Artwork gate

The approved original is [assets/pstack.jpeg](../assets/pstack.jpeg): 1254 × 1254 pixels, RGB JPEG, 723089 bytes, SHA-256 `fa5786e6f6a39ea36fd5bc09ac542b647094268c192de421b8eb4e771c87585d`. Its bytes and pixels were checked before packaging. The banner reads `Pstack` and the subtitle reads `The unofficial Plugin`. The repository and ZIP retain the exact original; there is no crop, conversion, redraw, or substitute.

Both `logo` and `composerIcon` reference `./assets/pstack.jpeg`. The original meets the documented [image format, size, and dimension requirements](https://developers.openai.com/plugins/deploy/submission#icons-and-screenshots). Host rendering and marketplace branding approval remain distinct checks. The chalkboard's "Always up to date" text is artwork copy, not a zero-lag claim: [maintenance](maintenance.md) describes the daily check, review gate, and verified no-change run. Listing approval and identifier availability remain publisher-dashboard checks; do not infer them from a valid local manifest.

## Submission sequence

The owner authorized uploading the complete rc.5 ZIP from `dist/` as a draft in the OpenAI Plugins dashboard under the verified developer identity. Upload is separate from review submission. Resolve package and skill scan findings, upload corrected versions, and complete applicable review information. Skills-only packages omit MCP configuration and the MCP review block. Current guidance does not support adding an MCP server later to an existing skills-only plugin, so reconsider that product boundary before the first public publication.

The owner must separately authorize and complete required policy attestations and submission. Track review feedback and make corrections. After approval, publication is still an explicit owner decision. No GitHub workflow in this repository performs any of these actions.

For metadata or skill updates, build and upload a complete new ZIP version, repeat applicable checks and review, then publish only after approval. Keep the pinned upstream commit, adaptation review, host evidence, and package checksum with every release.
