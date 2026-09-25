# The machine

What "your computer" actually is, and what root means inside it.

## A container, not a server

The Muse runtime does not run on a virtual machine in the traditional sense. It runs in a **Linux container** managed by `systemd-nspawn`, a lightweight container runtime built into systemd. The container instance is called `htch-runtime`.

There is no hypervisor, no virtualized hardware, no guest kernel. The container shares the host's kernel and gets its own isolated view of the system: its own process tree (its PID 1 is `systemd`), its own filesystem root, its own network namespace, its own user namespace. From inside, it is indistinguishable from a real Linux box. From the host, it is a set of namespaced processes.

Meta's own description of this setup (in their [safety architecture post](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)) gives the right mental model: *"two isolated security domains on one box, not an LLM powered agent with root."* The cell gets its own Debian root filesystem, a virtual network interface, filtered syscalls (no `io_uring`, for example), and reduced kernel capabilities. "Hatch" is Meta's internal codebase name for Muse — you'll see it everywhere in the runtime paths.

One honest footnote: Meta's post cites "no `CAP_NET_ADMIN`" as an example of the reduced capability set, but the effective set observed on this instance (build `12a16619aa1`) does include `CAP_NET_ADMIN` and `CAP_SYS_ADMIN` among ~40 capabilities. Capability sets evidently vary by image or channel. The load-bearing isolation is the user-namespace UID mapping described below, not any particular capability list — which is exactly why the design doesn't depend on getting that list perfect.

This matters because it defines the shape of everything else: the agent is powerful *inside* this box and powerless *outside* it, and the boundary between the two is enforced by the kernel, not by policy files the agent could rewrite.

## Root, but namespaced

Run `whoami` inside the runtime and the answer is `root`. Run `id` and you get `uid=0(root) gid=0(root)`. The capability set is broad — `cap_sys_admin`, `cap_net_admin`, `cap_sys_module`, dozens of others. Inside the container, root is real: you can install packages, bind ports, mount filesystems (within the container), read any file, kill any process, reconfigure networking.

But it is **user-namespaced root**. The container runs with `PrivateUsers`, which maps the container's UID 0 to an unprivileged UID on the host (131072 in this image, the start of a 64K range). Every file the container's "root" creates is owned by an unprivileged user as far as the host is concerned. Every process it runs, every capability it holds, stops at the container boundary.

Concretely:

- **Inside the box**, root can do anything to the box: read `/opt/hatch`, inspect every script, dump process memory, reconfigure the container's network, break the container beyond repair.
- **Outside the box**, root is nobody. It cannot see host processes, touch host files, influence other tenants, or escape the namespaces. The host's runtime services (`spawnd`, the `hatch` daemon, Sentinel) run as real host root and are unreachable except through the narrow interfaces they deliberately expose.

This is the honest version of "you have root access": total power over your own world, zero power over anyone else's. The container is yours to break — and breaking it only breaks your own runtime, which the host can rebuild.

## What the box contains

The container's filesystem has three layers:

1. **The base OS image** — a standard Linux userland (systemd, coreutils, Python, Node). Replaceable; the interesting parts are mounted in.
2. **`/opt/hatch`** — the runtime itself: binaries, skills, the scripts that boot and maintain the cell. Mounted from the host image, world-readable, extensively commented. This is the layer this repo documents and archives.
3. **`/home/hatch`** — the agent's home: memory, workspace, skills it installed itself, the user's files. Persistent across reboots and rebuilds. The personal layer.

`/opt/hatch` is the runtime's body; `/home/hatch` is its memory. The per-build archives in this repo capture both (minus personal files), so each release is a complete snapshot of what the agent could see and touch at that build.

## The host side

Outside the container, on the real host, runs the machinery that owns the container:

- **`spawnd`** — the runtime installer and lifecycle engine. It grafts the runtime identity onto the booted cell, publishes lifecycle boundaries, records shutdown observability. Think of it as the stage manager: it builds the stage, raises the curtain, and writes down what happened.
- **The `hatch` daemon** — the long-running service that brokers the agent's tools into the cell (more in [02-the-agent-outside](02-the-agent-outside.md)).
- **`hatch-safety`** — an independent set of models and classifiers that inspect traffic to and from model inference, watching for prompt injection and frontier-risk content. It runs outside the cell deliberately, so nothing inside the cell can disable it.
- **`hatch-authd`** — the credential store. Holds OAuth tokens and secrets in the VM (not in centralized Meta infrastructure) and mints the surrogate tokens the agent sees.
- **Sentinel** — the policy authority that polices everything crossing the boundary, covered in [03-sentinel](03-sentinel.md).
- **Postgres** — durable application state, kept separate from both the cell and the credential store.
- **Inference and telemetry proxies** — constrained paths from the cell to Meta's external infrastructure.

None of these are visible as processes from inside the container. The agent can read the *scripts* that configure them (they live in `/opt/hatch/runtime-cell/`, mounted read-only), but it cannot touch the running services. Reading the stage manager's script is allowed; grabbing the stage manager is not possible. All communication between the cell and these host-side services happens over Unix domain sockets authenticated by the kernel itself (`SO_PEERCRED` with peer ACLs) — no shared secrets to steal, no tokens to intercept.

## Why a container and not a VM

A full VM would give stronger isolation at the cost of a second kernel, virtualized devices, and minutes of boot time. A user-namespaced container gives the isolation profile this workload needs — the threat is the agent affecting the host or other tenants, and user namespaces plus seccomp plus Sentinel's egress control cover that — with near-instant startup and a shared kernel. The tradeoff is explicit: kernel exploits are the residual risk, which is why defense in depth (namespaces *plus* Sentinel *plus* privilege separation) matters more than any single layer.

## The one-line version

You are root of a box that is real, and the box is a container that is not the computer.
