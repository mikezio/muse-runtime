# The machine: cell, host, and persistent home

“VM” is the product-facing name for the personal computing environment. The inspected runtime uses a `systemd-nspawn` Linux **container/cell** as an execution boundary. The cell is an isolation layer inside the product's broader personal VM; “container” and “VM” refer to different boundaries.

## What root means here

The inspected shell reported UID 0, including a recheck on September 28, 2026, build `1eefe22acda`. Runtime configuration described user namespaces and a mapping to an unprivileged host UID. Root inside that namespace is not host root.

The cell can run software, create files, and support development within its available resources, mounts, network policy and capabilities. Installing a package does not expand the account's connector permissions or expose host-only services.

Avoid both extremes: “it can do nothing outside the cell” and “root can read or change everything.” It can contact permitted external services; it cannot treat host files, protected processes or sockets as its own.

| Operation | Interpretation |
|---|---|
| Install software or run Python/Node | Uses the cell's execution environment, subject to resource and filesystem limits |
| Edit a workspace project | Changes user files, not the hosted inference model |
| Read `/opt/hatch` | Inspects shipped files; the observed runtime mount was read-only |
| Read a daemon binary | Does not provide its Rust source or effective configuration |
| Call a connector or device | Uses an authorized interface and that action's permissions |
| Access protected host state | Requires a separately authorized interface; cell root is insufficient |

In the September 26–27 observations, the daemon executable was a stripped Rust ELF, selected process environment access was denied, and a browser broker helper was host-only. These are visibility boundaries even though many scripts and skill files are readable.

## Three filesystem areas

| Area | Purpose | Persistence implications |
|---|---|---|
| Base OS/root filesystem | Linux userland and local package/service changes | May be replaced during a recycle |
| `/opt/hatch` | Shipped binaries, skill references, SDKs, launch/cell scripts | Updated by the platform; observed as read-only |
| `/home/hatch` | Home configuration, workspace, user-maintained files | Persistent home in the observed lifecycle |

One observed recycle removed an added systemd unit under `/etc/systemd/system` while home files remained. A helper configured only in the replaceable OS should not be assumed to survive recycling. Persistence of a file and persistence of a service are different questions.

## The boundary around the cell

Meta's [published launch architecture](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) places the Hatch daemon/harness **inside** the runtime cell. Sentinel, safety services, credential handling, privileged connector workers, application Postgres and proxies sit **outside** that cell. The browser broker is also outside it. This corrects the older version of this chapter, which placed the daemon on the host side.

![Execution cell and protected service boundaries](../assets/trust-boundaries.svg)

Use the current build's launch scripts when investigating implementation details. A filename or binary string alone does not prove where a service currently runs.

The names `spawnd`, `hatch`, `hatch-execd`, `hatch-authd` and `hatch-safety` occur in the architecture and shipped tooling. See the [component reference](components.md) for responsibilities and evidence sources.

The security model described in the original [Meta source list](sources.md) includes namespace isolation, syscall/capability restrictions, credentials mediated outside the agent's ordinary execution context, and policy checks. An observed capability set varied from one published example. This repository is not an isolation audit and cannot prove the absence of escape paths.

## What these boundaries do—and do not—establish

Cell root alone does not establish a host compromise. Conversely, isolation does not make every agent action harmless. A program can damage accessible files; an authorized connector can expose or modify data; actions on a website can have consequences. Sentinel and other controls are additional defenses, not proof that harmful outcomes are impossible.

The useful security questions are concrete: which resource is reachable, through which interface, with which permission, and what checks apply? See [Sentinel](03-sentinel.md), [credentials](07-credentials.md), and [inspection limits](17-transparency.md).

## Read an archive with the right expectations

The archiver maps `/home/hatch` to `home/` and `/opt/hatch` to `opt/`. An archive is a filtered instance snapshot, not a bootable VM image or complete platform backup. Host services, inference weights, effective server gates, and excluded personal state are not reconstructed by extracting it.

Next: [Inference and tools](02-the-agent-outside.md), [archive workflow](archive-workflow.md).
