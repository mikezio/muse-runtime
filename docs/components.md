# Component reference

Use this page to translate names found in a file tree, tool schema or diagnostic output into responsibilities. “Runtime” can mean the whole system or the `hatch` service; distinguish those meanings when investigating.

**Evidence:** installed files and historical observations from September 26–27, 2026. Selected paths/schema names were rechecked on September 28 against build `1eefe22acda`. A path being present does not establish that every feature behind it is enabled. See [evidence](evidence.md).

## Control, execution and services

| Component/surface | Responsibility | Where to investigate |
|---|---|---|
| Web/mobile clients | Conversation UI, settings, approvals, task/artifact presentation | Rendered UI and authenticated client responses |
| Authenticated gateway/client transport | Routes the logged-in client's requests to services | Frontend method registry and actual responses; [API guide](runtime-api.md) |
| `hatch` daemon/harness | Runtime control, session/task orchestration, tool interfaces; inside the cell in the published design | `/opt/hatch/bin/hatch`, API results; compiled binary is not source |
| `spawnd` / lifecycle scripts | Provisioning and lifecycle of the execution environment | `/opt/hatch/runtime-cell/`; launch scripts show a build's wiring |
| `hatch-execd` / execution path | Runs commands in the execution cell | Execution tool results and shipped wrappers |
| Inference proxy/service | Carries requests to model serving | Route metadata where exposed; weights are not in the cell |
| Sentinel/policy and safety services | Enforce policy across supported actions/data paths | [Sentinel](03-sentinel.md), installed guidance, approval outcomes |
| Credential service / `hatch-authd` | Managed credential storage and use | [Credentials](07-credentials.md); inspect metadata rather than credential values |
| Browser broker and browser task system | Managed browsing, task ownership, session/auth handling | [Browser](06-browser.md), task records |
| Connector services | Account integrations and action permissions | Connector inventory, permission schemas and a scoped action result |
| Device service | Routes commands to paired, reachable devices | Device capability registry and per-command results |
| Application database | Durable structured agent/runtime state | Native `muse.db` plus its shipped schema |
| Scheduler/queues | Dispatch work and retain run outcomes | [Scheduler](11-scheduler.md); dispatch, execution and delivery are separate facts |

For the published cell-versus-protected-services placement, see [the machine](01-the-machine.md). This table groups responsibilities. Protected services are not made accessible merely by learning their names.

## Files and state

| Location or interface | What it helps explain |
|---|---|
| `/home/hatch/docs/` | Installed product guidance, including feature prerequisites and limitations |
| `/home/hatch/config/home.yaml` | User-visible runtime configuration; [reasoning configuration](configuration.md) |
| `/home/hatch/workspace/` | User projects, scripts, custom skills and outputs |
| `/opt/hatch/skills/` | Shipped skill instructions, references and SDKs |
| `/opt/hatch/runtime-cell/` | Cell boot/lifecycle/environment scripts |
| `/opt/hatch/bin/` | Runtime binaries and CLI entrypoints |
| `/etc/hatch/env.override` | Observed guest copy of operator configuration; not a supported user override |
| `muse.db` | Controlled query surface; not equivalent to a local PostgreSQL connection |
| `muse.session_status` | Selected runtime/session metadata; did not expose per-turn provider effort/tier |

The archive rewrites the two captured roots as `home/` and `opt/`. See [archive workflow](archive-workflow.md) before searching a release.

## Distinguish the capability types

- A **tool** has a callable interface and parameters.
- A **skill** teaches a workflow and may wrap tools or CLIs.
- A **connector** authorizes access to an external account/service.
- A **device command** requires an appropriate paired device and permissions.
- A **Space/artifact** is an application or deliverable with its own build/runtime lifecycle.
- A **feature gate** influences rollout or availability; its name is not a tool.
- A **model route** selects inference policy; it does not create a connector or permission.

Example: a skill can describe email, the connector can be absent, and the mailbox API can still reject the operation. These are different observations, not a contradiction.
