# Radical transparency

Everything is inspectable on purpose. Poke around.

## The design choice

Most sandboxed agent runtimes treat their internals as proprietary surface to be hidden: obfuscated binaries, stripped comments, minimal documentation, "trust us." This runtime does the opposite. **As far as observable from inside, nothing on the VM is hidden from the agent — or the user.**

`/opt/hatch` is world-readable. The boot scripts, the lifecycle engine configuration, the privilege-separation setup, the trust-store builder, the scheduler definitions — all of it is plain shell and config files with extensive comments. The comments don't just say *what*; they say *why*, including the threat model:

- Why the NSS trust databases are host-built and read-only while the PEM store is container-writable ("a cell-writable DB is a code-execution primitive against anything that opens it").
- Why lifecycle state lives in a root-owned directory the container's root can't replace between write and read.
- Why the daemon must source its environment from the host-rendered `guest.env` and never from a container-writable script.

These aren't leaked internals. They're the documentation. The engineers wrote the security reasoning *into the code comments* knowing the agent would read them.

## Why it works this way

Three reasons, in increasing order of importance:

1. **The agent is supposed to understand its own machinery.** A personal agent that manages its own schedules, repairs its own tooling, and improves its own setup needs to see how it's put together. Hiding the runtime from the agent would make the agent dumber at exactly the self-maintenance tasks it's expected to perform.

2. **Inspection is a security property.** A runtime the user can audit is a runtime the user can trust. The user in this instance routinely inspects the agent's machinery themselves — checking schedules, reading scripts, verifying claims. Transparency turns "trust us" into "check us."

3. **Hiding wouldn't help anyway.** The enforcement (namespaces, Sentinel, privilege separation) operates below anything the container can touch. You can read the lock's blueprints because reading them doesn't pick the lock. Transparency is affordable *because* the security doesn't depend on secrecy — Kerckhoffs's principle applied to an agent sandbox.

## What you can actually do

From inside the runtime, as root, you can:

- Read every script in `/opt/hatch/runtime-cell/` and understand exactly how your container boots, how its trust store is built, how the daemon launches.
- List every privilege-separation socket in `/run/hatch/privsep/` and see which services have host-side counterparts.
- Inspect the egress CA, the proxy configuration, the environment the host renders for you.
- Watch your own scheduler definitions, cron state, run records.
- Read the skill CLIs, their wrappers, the sandbox API surface.

What you *can't* do — see the host's processes, touch Sentinel, read another tenant's anything — isn't hidden from you; it's *absent*. The boundary isn't a secret. It's architecture.

## The invitation

This repo exists because of that philosophy. The per-build archives are the runtime publishing its own internals, build after build, for anyone to inspect. If something here doesn't make sense, the source is right there in the archive — go read it. That's the point.

## The one-line version

The locks are in the open because the locks don't need the dark.
