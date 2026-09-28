# What you can inspect—and what remains hidden

The runtime exposes extensive shipped documentation, scripts, SDKs, schemas, configuration and binaries. That makes it unusually useful to study. It does not make the whole platform visible.

## Visibility map

| Surface | What inspection can reveal | Limit |
|---|---|---|
| Product/skill documentation | Intended workflows, prerequisites and tool contracts | Instructions are not execution evidence |
| Launch and cell scripts | How a particular build configures parts of the environment | Effective host state can differ or be inaccessible |
| SDK source | Public method/options/return shapes | Internal server implementation may be absent |
| Compiled daemon | Version, executable contents, embedded strings | The stripped binary is not a source release |
| Selected API responses | Current values and operation results | Some fields are omitted, redacted or not implemented |
| Native database schema/tool | Structured records within the tool's access scope | Does not grant a shell database connection |
| Browser/client code | UI logic and client feature configuration | Does not expose all backend gates or mobile policy |

September 26–27 inspection encountered protected process environment access, host-only browser service boundaries and missing per-request provider metadata. These limits matter when interpreting configuration and model experiments.

## Root does not erase the boundaries

Cell root is scoped by namespaces, mounts, process restrictions and mediated interfaces. Many files under `/opt/hatch` were readable while the mount was read-only. A file path or service name does not grant access to the corresponding host resource.

See [the machine](01-the-machine.md) for the distinction between cell privileges, permitted external actions and host authority.

## What an archive gives you

A release contains selected filesystem artifacts from an instance. It can support comparisons of shipped docs, skills, schemas and executables. It does not include a full reconstruction of hosted inference, account feature gates, host services or excluded personal state.

Use “artifact” or “installed source file” precisely. Some scripts and SDKs are source; a daemon binary is not its source code. The archive's exclusion rules also mean absence from an archive may reflect filtering.

## A productive investigation

Start with a concrete question, locate its interface or consumer, and record the smallest sufficient evidence. Follow [the archive workflow](archive-workflow.md) and [evidence template](evidence.md). When a result is unavailable, preserve that uncertainty instead of filling it with a plausible architectural story.
