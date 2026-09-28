# Capability atlas

A practical map of what the runtime contains and how the pieces can be combined.

**Evidence key:** **Live** = a bounded operation succeeded; **Interface** = schema/SDK/help inspected; **Docs** = installed instructions; **Compiled** = name found in a binary. These are dated observations, not a guarantee of access on another account. See [evidence](evidence.md).

## Tools, skills and connectors

A tool is callable; a skill explains a workflow; a connector supplies authorized service access. Installing a skill does not create an account connection. Device commands also depend on reachability and operating-system permissions.

| Area | Useful capability | Evidence and limits |
|---|---|---|
| Shell and files | Install libraries, transform data, build projects, create custom CLIs | **Live:** real cell execution; base OS changes may not survive recycling |
| Custom skills | Package repeatable workflows with instructions, scripts and references | **Docs/Interface:** `~/workspace/skills/<name>/`; [skills](13-skills.md) |
| Connected accounts | Read/update service data through supported operations | **Live inventory:** each connector/action has its own state and permission |
| Custom connectors | Add supported custom integrations | **Live inventory:** observed OAuth/API-key metadata; account details omitted |
| Native database | Ask structured questions about agent/runtime records | **Live/Interface:** `muse.db`; [API and schema guide](runtime-api.md) |
| Search/browsing | Search/fetch sources or delegate interactive website work | **Live/Docs:** different interfaces; authenticated browser tasks have ownership and session state |

## Apps, Spaces and artifacts

The installed Spaces TypeScript SDK exposes a useful combination of application state, managed tools and inference. The SDK paths were rechecked on September 28, build `1eefe22acda`:

```text
/opt/hatch/skills/spaces/ts-runtime/sdk/src/index.ts
/opt/hatch/skills/spaces/ts-runtime/sdk/src/verticals.ts
```

| Interface | What it enables | Limitation |
|---|---|---|
| `ctx.inference.complete(prompt, options)` | Structured inference constrained by a schema, with supported image input | No model/effort selector was exposed in the inspected public options |
| `ctx.agent.spawnTask(message, options)` | Delegate application work with a task handle and callback workflow | Task acceptance is not completion; inspect ownership and status |
| `ctx.emit(data)` | Send application events/data through the SDK | Follow the current runtime contract |
| `ctx.invalidateQueries(...)` | Refresh app queries after state changes | Does not itself perform the underlying write |
| `ctx.tool.web_search` | Managed search | Verify current return schema |
| `ctx.tool.weather`, `sports_data`, `finance_ticker` | Structured domain data | Use typed values rather than parsing display prose |
| `ctx.tool.generate_media` | Managed media within the app workflow | Availability/options depend on the runtime |

**Example design:** a research app searches for sources, asks for schema-constrained extraction, saves the result, and refreshes its UI. This illustrates the interfaces; it is not a separately deployed sample in this repository.

The inspected public inference wrapper returned the schema result without exposing all internal provider metadata. It should not be used as evidence of a hidden model override.

## Media and documents

| Capability | What was found | Evidence / limitation |
|---|---|---|
| Image generation/editing | Reference images, iterative edits, PNG/JPEG/WebP output | **Interface/Docs:** up to four outputs per response in the inspected interface |
| Video generation | Text/still inputs, audio and continuation | **Docs:** no video-to-video in the inspected guidance |
| Avatars | Create/edit and animation workflows | **Interface/Docs:** not an entitlement guarantee |
| Voice/TTS | Multiple speakers, speed/language settings, saved voices and voice creation guidance | **Docs/Interface:** web voice/design flags were false in the inspected account |
| Podcasts | Multi-host audio and publishing workflows | **Docs:** no publishing performed in this investigation |
| Photo library | Search descriptions, OCR, date/location metadata; request shortlist/gallery | **Docs:** device and permissions required; observed search guidance described BM25 |
| MagicMoment | Coordinated narrative-video workflow | **Installed:** rollout/execution not established |
| Slide themes | 260 themes in 26 families returned by the style CLI | **Live:** `hatch-slide-style list-themes` |
| PowerPoint export | Slide-image export, with editable HTML source workflow | **Docs:** exported slide images are not editable native text/shapes |
| PDF and Word | Fillable forms, tracked-change/comment workflows | **Docs:** task-specific tools and verification still needed |
| In-chat/generated UI | Mobile and wearable-oriented rendering options | **Interface:** `genui-display-render` help; no generation performed |

## Devices and the physical world

| Surface | Examples in the capability registry/docs | Prerequisites and evidence |
|---|---|---|
| Paired Mac | Desktop, files, Notes, Mail, messages, calendar/reminders, camera commands | **Interface:** relevant commands inspected; avoid treating the full inventory as executed |
| Paired iPhone | Device data, HomeKit writes/scenes, location-related workflows, Bluetooth/accessory operations | **Interface:** requires reachable device and OS permissions |
| HomeKit choreography | Ordered writes/scenes with delays | **Interface:** distinct from concurrent scene synthesis |
| HomeKit/geofence bridge | Location-triggered home actions | **Docs:** Always location and HomeKit prerequisites |
| Home Link | Experimental ESP32-C5 Wi-Fi/BLE bridge, signed OTA, local device integration guidance | **Docs:** no paired Home Link or successful bridge action observed |

Home Link guidance lives at `/home/hatch/docs/devices/home_link.md`; that path was rechecked on the September 28 build. A document describing printers, lighting or HTTP tunneling is not evidence that the instance has discovered those devices.

## Less obvious installed tools

| Tool | Use | What was verified |
|---|---|---|
| `hatch-zeitgeist` | Public social search across supported Meta surfaces, with query/filter options | A bounded public Threads search worked; output limits can differ between summary and raw results |
| `nutrition-cli` | Structured food/nutrient, barcode and meal-photo workflows | Help/schema only; no personal health records inspected |
| `local-search` | Place search with geographic constraints | Interface; despite its name it is not local filesystem search |
| `browser-service` | Fetch/open/find and source-link workflows | Interface; distinct from interactive browser task ownership |
| `device-data` | Stored device-origin contacts/calendar interfaces | Help only; no personal records dumped |
| `remote-storage` | Upload/delete files and podcast publishing operations | Help only; no upload/publication performed |
| Expedia tooling | Lodging search/quotes and booking/cancellation workflow | Help only; no transaction performed |
| `edits` | Development media tooling | Capability token required; execution not established |

## Personalization and background intelligence

- **Identity/persona:** editable standing documents such as `SOUL.md` and `IDENTITY.md`.
- **Memory:** files plus structured records, retrieval and provenance; [memory chapter](12-memory.md).
- **Feed/ideas:** customization and derived-output pipelines; personal prompt content was not published.
- **Goals/tasks:** durable work state and delegation, with ownership and result delivery.
- **Forgetting:** a workflow that identifies copies and affected automations before confirmed changes.
- **Early-access requests:** installed guidance distinguishes delivery, pending review and admission. Submitting a request is not feature enablement.

A useful contribution to this atlas records **what was tried, on which build/date, what result came back, and what remains unknown**. A list of impressive names is not enough.
