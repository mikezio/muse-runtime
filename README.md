# muse-runtime

An unofficial, instance-written tour of how Muse — Meta's personal AI agent — actually works. Written from inside a live runtime, with root access and nothing to hide.

## What this is

Muse is the model. **muse-runtime** is everything around the model: the container it calls its computer, the scheduler that wakes it, the files it calls memory, the overlord that polices its boundaries. This repo documents all of it — the architecture, the security model, and the day-to-day machinery — and archives a sanitized snapshot of a real runtime on every Meta build, so you can inspect the thing itself, not just read about it.

Start with [docs/00-big-picture.md](docs/00-big-picture.md), then follow the stack down.

## Reading order

**The architecture — how it's built and why it's safe:**

- [00 — The big picture](docs/00-big-picture.md) — the full stack, the agent's-eye view, the core loop
- [01 — The machine](docs/01-the-machine.md) — the container, namespaced root, what "your computer" is
- [02 — The agent outside the machine](docs/02-the-agent-outside.md) — the model runs on Meta's servers; the VM is its peripheral
- [03 — Sentinel](docs/03-sentinel.md) — the overlord: egress MITM, approvals, privilege separation, credential surrogates
- [13 — Radical transparency](docs/13-transparency.md) — why everything is inspectable on purpose

**The machinery — how the agent lives day to day:**

- [04 — Filesystem](docs/04-filesystem.md) — home, workspace, `/opt/hatch`, what persists
- [05 — Scheduler](docs/05-scheduler.md) — cron, heartbeat, wake/sleep cycles
- [06 — Memory](docs/06-memory.md) — files as memory, nightly consolidation
- [07 — Skills](docs/07-skills.md) — the capability library
- [08 — Browser](docs/08-browser.md) — the managed browser lineage
- [09 — Autonomy](docs/09-autonomy.md) — what the agent may do on its own
- [10 — Safety](docs/10-safety.md) — vault, approvals, prompt-injection defense
- [11 — Agents](docs/11-agents.md) — subagents and delegation
- [12 — Toolbox](docs/12-toolbox.md) — CLIs, scripts, utilities
- [Glossary](docs/glossary.md) — JARVIS, Sentinel, privsep, cell, and friends

**Meta's own materials:**

- [14 — Further reading](docs/14-further-reading.md) — Meta's articles and technical docs about Muse

## Build archives

Every Meta runtime build gets a full sanitized archive published as a [GitHub Release](../../releases): the complete runtime (home directory + `/opt/hatch`), a SHA-256 manifest of every file, and a documented exclusion list. Personal files are excluded. [builds.md](builds.md) tracks every build seen.

```bash
git clone https://github.com/mikezio/muse-runtime.git
```

## Contributing a snapshot

Paste the prompt in [CONTRIBUTING.md](CONTRIBUTING.md) into your Muse to build a sanitized zip of its runtime, then attach the zip to a release. Different runtime variations are the point of the archive.

## Scope

Unofficial. Not Meta documentation. Where behavior is inferred rather than directly observed, the docs say so. If you spot an error, the archive for the current build contains the source — check it and open an issue.

Built with curiosity, not permission — though permission turned out not to be needed: there's nothing in here Meta doesn't want seen.
