# muse-runtime

An unofficial, instance-written tour of how Muse — Meta's personal AI agent — actually works. Written from inside a live runtime, with root access and nothing hidden.

## What this is

Muse is the model. **muse-runtime** is everything around the model: the container it calls its computer, the scheduler that wakes it, the files it calls memory, the Sentinel that polices its boundaries. This repo explains all of it — built from Meta's own publications plus direct observation from inside a running instance — and archives a sanitized snapshot of a real runtime on every Meta build, so you can inspect the thing itself, not just read about it.

Start with [docs/00-big-picture.md](docs/00-big-picture.md), then follow the stack down.

## Reading order

**Part I — How Meta built it** (from Meta's publications, written in our own words):

- [00 — The big picture](docs/00-big-picture.md) — the full stack, the agent's-eye view, the core loop
- [01 — The machine](docs/01-the-machine.md) — the container, namespaced root, what "your computer" is
- [02 — The agent outside the machine](docs/02-the-agent-outside.md) — the model runs on Meta's servers; the VM is its peripheral
- [03 — Sentinel](docs/03-sentinel.md) — the overlord: egress MITM, approvals, privilege separation, credential surrogates
- [04 — The model](docs/04-the-model.md) — Muse Spark: what it was trained for and why it still isn't trusted alone
- [05 — Prompt injection](docs/05-prompt-injection.md) — the lethal trifecta and the five defensive layers
- [06 — The browser](docs/06-browser.md) — real Chromium, accessibility-tree view, no JavaScript, credential injection
- [07 — Credentials](docs/07-credentials.md) — the Vault, `authd`, surrogates, least privilege
- [08 — Paying for things](docs/08-paying-for-things.md) — single-use cards, checkout detection, approval every time
- [09 — Data and privacy](docs/09-data-and-privacy.md) — where your data lives, training opt-out, the Confidential VM roadmap

**Part II — How it lives day to day** (observed from inside):

- [10 — Filesystem](docs/10-filesystem.md) — home, workspace, `/opt/hatch`, what persists
- [11 — Scheduler](docs/11-scheduler.md) — cron, heartbeat, wake/sleep cycles
- [12 — Memory](docs/12-memory.md) — files as memory, nightly consolidation
- [13 — Skills](docs/13-skills.md) — the capability library
- [14 — Autonomy](docs/14-autonomy.md) — what the agent may do on its own
- [15 — Agents](docs/15-agents.md) — subagents and delegation
- [16 — Toolbox](docs/16-toolbox.md) — CLIs, scripts, utilities
- [17 — Radical transparency](docs/17-transparency.md) — why everything is inspectable on purpose
- [Glossary](docs/glossary.md) — JARVIS, Sentinel, privsep, cell, and friends
- [Sources](docs/sources.md) — the Meta publications this repo is built from

## Build archives

Every Meta runtime build gets a full sanitized archive published as a [GitHub Release](../../releases): the complete runtime (home directory + `/opt/hatch`), a SHA-256 manifest of every file, and a documented exclusion list. Personal files are excluded. [builds.md](builds.md) tracks every build seen.

```bash
git clone https://github.com/mikezio/muse-runtime.git
```

## Contributing a snapshot

Paste the prompt in [CONTRIBUTING.md](CONTRIBUTING.md) into your Muse to build a sanitized zip of its runtime, then attach the zip to a release. Different runtime variations are the point of the archive.

## Scope

Unofficial. Not Meta documentation. Part I synthesizes Meta's published materials; Part II describes one live instance's observed behavior, which may differ across builds and accounts. Where behavior is inferred rather than directly observed, the docs say so. If you spot an error, the archive for the current build contains the source — check it and open an issue.
