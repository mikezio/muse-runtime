# Daemon and API surfaces

The authenticated website, the agent's native tools, and the Linux shell expose **different interfaces**. Connecting to one does not automatically expose the others.

Observations below are from September 26–27, 2026. Method names are implementation observations, not a supported third-party API contract. The September 28 update rechecked the native database schema file's presence and selected table names, not every endpoint.

## Three ways of looking

| Surface | Useful for | Important limit |
|---|---|---|
| Authenticated web client | Settings, model selection, inventories, session/task metadata | Registered methods can still be unavailable or gated |
| Native agent tools | Agent status, controlled database queries, task/skill capabilities | A child may have fewer tools than its parent |
| Remote shell | Files, installed docs/SDKs, processes visible in the cell, CLI help | Does not confer browser authentication or direct DB/host access |

The inspected web client held an active runtime transport with a `sendRequest(method, params)` interface. This is a version-specific implementation detail. Use an existing owner-authenticated session; copying cookies or hard-coding tokens is unnecessary for inspection.

## A minimal read-only inspection

Inside an already authenticated client inspection session, the observed transport was reached as follows. This is version-specific browser code, not a standalone SDK or a shell command:

```javascript
const runtime = window.__hatchEarlyGatewayRuntimeState?.activeRuntime;
const transport = runtime?.getSnapshot();
if (!transport?.sendRequest) throw new Error("Runtime transport unavailable");
const model = await transport.sendRequest("model.get", {});
const config = await transport.sendRequest("config.get", {});
// Inspect only the model-selection and llm.reasoning fields you need.
// Avoid logging entire authenticated objects or unrelated configuration.
```

Neither request changes a setting. Responses must be interpreted using the current schema; the transport object and response shapes are not stable public contracts.

## Observed working method families

| Method(s) | What was established | Scope/shape notes |
|---|---|---|
| `check` | Application-level ping returned OK | Liveness of that request path |
| `model.get`, `model.set` | Read/changed selected routes | Mutation can clear working context; [model guide](model-routes.md) |
| `config.get`, `config.update` | Read/updated reasoning preferences | Supported `llm.reasoning` shape; [configuration](configuration.md) |
| `sessions.list`, `sessions.get` | Read session metadata | `sessions.get` used `{id}` |
| `chat.history` | Retrieved selected diagnostic thread history | Used `{session_id, limit}`; keep thread scope explicit |
| `vm.health`, `vm.enrollment_health` | Returned runtime/enrollment diagnostics | Health payload can be large; select relevant fields |
| `fs.list`, `fs.raw`, `fs.stats` | Read file listings/content/metadata | Home-relative paths; `fs.raw` returned a Blob |
| `connectors.list` | Returned a settings inventory | Used `{surface: "settings"}`; connection state is separate |
| `connectors.permissions` | Returned grouped action permissions | Used connector `{id}`; inspect mode/source fields |
| `custom_connectors.list` | Returned custom integration metadata | Do not publish account-specific connector details |
| `node.list` | Returned paired-device metadata/reachability | Online state is a point-in-time observation |
| `skills.list` | Returned skill descriptions/categories | Catalog membership does not grant backend access |
| `spaces.list` | Listed user Spaces | Avoid publishing personal names/content |
| `spaces.export_html` | Exported an existing Space | Used `{slug}`; output can contain personal app data |
| `spaces.debug.summary` | Returned a Space debug summary | Used `{slug}`; full logs were not needed |
| `feed.prompt.get` | Returned feed customization state | Prompt content can be personal |
| `permissions.inventory` | Returned permission categories | Prefer counts/selected fields for documentation |
| `onboarding.variants` | Listed onboarding flow names | These are flows, not upgraded model modes |
| `redteam.mocks.get` | Returned an empty mock configuration | Does not establish permission to enable mocks |

## Unavailable or gated in the inspected account

| Surface | Observed result |
|---|---|
| `email.mailbox.get` | Muse mail was not enabled for the account |
| Shared-agent list/capability methods | 404 |
| `git.log` | 404 |
| `browser.local_testing.get` | Explicitly internal-only |
| `voice.pipeline_profiles` | Overrides access disabled |
| `computer.context` | Computer unavailable; distinct from paired Mac tools |
| `/openapi.json` | 404 on the authenticated route tested |

A frontend registry contained hundreds of methods. Registry presence is weaker evidence than a successful response. A 404 on one route does not prove a feature cannot exist on another build or transport.

## Why a shell connection is not “access to muse.db”

The native `muse.db` tool uses a controlled runtime database interface. The inspected guest did not offer a usable direct PostgreSQL connection through the ordinary shell. Its installed schema is at:

```text
/opt/hatch/skills/muse_db/references/schema.md
```

Read that schema before constructing a query. Useful tables included:

| Table | Investigation use |
|---|---|
| `agent.chat_preferences` | Locate the active root relationship |
| `agent.agents` | Agent ID, role/kind and stored model |
| `runtime.browser_tasks` | Browser task metadata and requester fields |
| `runtime.requests` | Request records; inspect schema for actual available columns |
| `runtime.events` | Runtime event records |
| `agent.token_usage` | Recorded usage; not proof of effective reasoning effort |

For model investigation, a prior query joined `chat_preferences.active_root_id` to `agents.id` and selected only model, agent ID, kind and update time. Browser requester model/effective-model fields were null in the inspected rows.

Do not infer provider identity from a stored agent model alone. Do not dump message bodies, private reasoning, credentials or full event payloads merely to answer a configuration question.

## Interpret health and task results carefully

- A successful ping confirms that transport now; an old “online” row may be stale.
- An accepted task receipt confirms acceptance, not completion.
- A reply can finish while background work remains active.
- An idle availability field is not automatically an outage: one observed root-availability flag was false while normal inference worked.
- Record failure time and endpoint. Do not turn one account's error into a universal product statement.

See [evidence](evidence.md) for the reporting template.
