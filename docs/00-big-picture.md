# How Muse fits together

Muse combines model inference, an agent runtime, an isolated Linux environment, durable state, and services that connect it to the outside world. Calling all of these “the agent” makes it hard to understand what a setting or permission actually changes.

This guide separates them. It combines the repository's architecture research with dated runtime observations. The main diagram distinguishes the published deployment boundaries from the logical request flow. See [evidence and limitations](evidence.md).

## Start with five pieces

![Muse architecture: clients, runtime, inference, isolated tools, and mediated services](../assets/architecture.svg)

| Piece | What it does | Distinction |
|---|---|---|
| **Client** | Web/mobile chat, settings, approvals, rendered artifacts | Presents the system; does not run model inference locally |
| **Agent runtime** | Assembles context, calls inference, dispatches tools, tracks sessions/tasks, delivers results | More than a prompt or a model |
| **Inference service** | Takes context and produces assistant output or tool calls | Remote from the user's Linux cell |
| **Execution cell** | Runs shell commands and user software; exposes files and bundled tooling | Cell root is not host administrator access |
| **Mediated services and state** | Browser broker, credentials, connectors, device commands, databases, scheduling and storage | Not all accessible as ordinary files from a shell |

Meta's launch architecture places the Hatch harness inside the runtime cell and the security-sensitive services outside that cell, within the personal VM. Model inference is remote. See [cell and host](01-the-machine.md) for the deployment distinction.

An **agent** is a role plus context and execution state managed by the runtime. A root agent, browser task, and background worker can have different instructions, tools, and model policies. The model performs inference for those roles; the runtime supplies the filesystem interfaces, memory retrieval, permissions and task lifecycle.

## Follow one request

![A request from chat through inference and tools to a final reply](../assets/request-lifecycle.svg)

For example: “Read this document and make a chart.”

1. A client submits the request into a conversation/session.
2. The runtime assembles available conversation, instructions, relevant memory and tool definitions. The exact selection is not fully exposed.
3. An inference request produces text, a tool call, or both.
4. The runtime routes the call. Reading a local file, browsing a website, and calling a connector use different execution paths and permissions.
5. A result comes back: file contents, structured data, a task receipt, or an error. A receipt for asynchronous work is not the finished result.
6. Further inference can use that result. This loop can repeat or delegate work.
7. The runtime delivers the reply or artifact and retains the appropriate session/task state.

The inference service is remote from the cell. The broader agent system spans these pieces; saying “the entire agent runs outside the VM” is too imprecise.

## What can you change?

| Layer | Examples | Reference |
|---|---|---|
| User files | Persona notes, workspace code, custom skills | [Filesystem](10-filesystem.md), [skills](13-skills.md) |
| Runtime preferences | Root/subagent reasoning effort | [Configuration](configuration.md) |
| Model selection | Auto, named routes, aliases | [Model routes](model-routes.md) |
| Connected capabilities | Account links, per-action permissions, paired devices | [Capability atlas](capabilities.md) |
| Client presentation | Some local display/debug preferences | [Feature flags](feature-flags.md) |
| Platform policy | Server gates, launch environment, host service access | Observable in part; not ordinary user settings |

Editing a file does not prove a running process loaded it. Selecting a model route does not prove the upstream checkpoint identity. A tool definition does not prove the account can execute it.

## Where does state live?

- **Files:** workspace projects, standing Markdown notes, configuration and generated outputs.
- **Application state:** sessions, agents, requests, browser tasks, usage, memory indexes and provenance exposed through selected runtime tools.
- **Managed service state:** browser profiles, connector authorization, credentials and device associations.
- **Server-side configuration:** evaluated feature gates and model routing policy.

Archives capture selected filesystem contents. They cannot reconstruct all of this state or reproduce the hosted service by themselves.

## Choose your next step

- **Understand isolation:** [The machine](01-the-machine.md) and [remote inference](02-the-agent-outside.md).
- **Identify a component:** [Component reference](components.md).
- **Understand configuration:** [Configuration layers](configuration.md).
- **Find capabilities:** [Capability atlas](capabilities.md).
- **Inspect an API result:** [Daemon and API surfaces](runtime-api.md).
- **Investigate a new build:** [Archive workflow](archive-workflow.md).

The [documentation index](README.md) links the complete topic chapters.
