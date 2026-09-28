# Evidence, provenance and open questions

This repository combines published architecture descriptions, shipped artifacts, and live observations. They answer different questions.

## Evidence levels

| Label | What it supports | What it does not prove |
|---|---|---|
| **Published** | What the referenced author says about a system/version | Current implementation on every account |
| **Installed** | A file, skill, schema or SDK ships in a build | Feature enabled or code path executed |
| **Compiled** | A name/string exists in an executable | A reachable route, effective flag or supported setting |
| **Response** | A scoped API/tool returned a particular result | Full end-to-end behavior beyond that response |
| **Live test** | A specific requested operation completed | Universal availability, exact hidden provider behavior |
| **Inference** | A reasoned explanation connecting evidence | Direct measurement |
| **Unknown** | The available evidence does not decide the question | Either “false” or “true” |

## Provenance of this documentation update

| Evidence set | Date/build association | Coverage |
|---|---|---|
| Repository's original source-based chapters | See [sources](sources.md) and earlier [changelog](../CHANGELOG.md) | Published architecture and security descriptions; not re-audited wholesale in this update |
| Prior owner-authorized runtime exploration | September 26–27, 2026; not reliably pinned to one build for every test | Model/config tests, authenticated APIs, web flags, CLI/SDK inspection and selected diagnostics |
| Primary architecture clarification | September 28, 2026; [Meta launch architecture](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) | Rechecked harness placement inside the cell and protected services outside it |
| Documentation recheck | September 28, 2026, 04:39–04:41 UTC; build `1eefe22acda`, built 00:41:38 UTC | Live shell UID 0; selected documentation/SDK/schema/binary paths; SDK names and schema tables |
| Tracked filesystem snapshot at update time | `snapshot/runtime-info.json`: September 28, 03:31:37 UTC, build `1eefe22acda` | 17,210 file records in the matching manifest; path inventory |
| Archive comparison verification | Release manifests `49d7dfcc81f` and `1eefe22acda` | Parser verified against real artifacts; no runtime execution needed |

The historical findings are summarized from the investigation record. Raw authenticated payloads, personal transcripts, account identifiers, cookies and runtime database dumps are intentionally not included. This means some claims are reproducible procedures plus dated reports, rather than independently replayable captured evidence.

The September 28 path recheck does **not** revalidate historical model behavior or feature flags. Do not attach the current build ID to an earlier test whose build was not recorded.

## Source locators

| Question | Start here |
|---|---|
| What files shipped? | [Build index](../builds.md), release manifest, [snapshot metadata](../snapshot/runtime-info.json) |
| How does the cell launch? | Archive `opt/runtime-cell/`; inspect the relevant build's scripts |
| What is the database shape? | Archive `opt/skills/muse_db/references/schema.md` |
| What can Spaces call? | Archive `opt/skills/spaces/ts-runtime/sdk/src/index.ts` and `verticals.ts` |
| What does the installed product guidance say? | Archive `home/docs/` and `opt/skills/` |
| What is enabled now? | Supported current capability/permission responses, not the archive alone |
| What model served this request? | Per-request effective metadata, if exposed |

Archive path roots differ from live paths: `home/` represents `/home/hatch`; `opt/` represents `/opt/hatch`.

## Findings template

When adding an observation, include:

```text
Question:
Observed at (UTC):
Runtime build / web build, if known:
Surface and operation:
Selected fields or sanitized artifact:
Outcome:
Evidence level:
Scope (account/client/role):
What this does not establish:
Restoration, if any setting changed:
```

Prefer a minimal reproduction over a full payload dump. Keep personal state and authentication material out of the repository.

## Open questions worth resolving

1. What provider and effective effort served an individual turn? Status branding and stored agent model rows did not settle this.
2. What is the exact mapping between Avocado route versions and public Muse Spark releases? No complete mapping was exposed.
3. Which compiled gates are active for a particular account and client? The web bootstrap reveals only part of the configuration.
4. Which host launch settings can a user legitimately influence? No supported general override/hot-reload mechanism was established.
5. How do context/model changes propagate across existing roots and children? Observed behavior shows that thread boundaries do not isolate every global setting.
6. Which documented device/media features work across accounts? Installed schemas establish interfaces, not rollout or reachability.

## Report changes at the right layer

A changed manifest hash means file content changed. It does not automatically mean product behavior changed. A newly shipped skill means documentation/tooling is present. A successful task means a specific operation worked. Keeping those statements separate makes future comparisons useful.
