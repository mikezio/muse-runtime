# Muse runtime

How a Muse instance actually works: the filesystem, the scheduler, the memory pipeline and the agent machinery, mapped from a live runtime.

Here's the thing nobody tells you about personal AI assistants: between your messages, they aren't thinking. They're off. What looks like memory and continuity is a pile of Markdown files, a cron scheduler and a background checklist that runs every 30 minutes. This repo is that pile, documented from a live Muse instance: the real directory layout, the real checklists, diagrams of the loops involved. Anything personal has been stripped out.

## The short version

![System architecture](assets/architecture.svg)

The instance is a language model plus a persistent Linux home directory, a set of tools (shell, browser, skills, connectors) and a scheduler. Something wakes it up (a message, a timer, a finished background task), it reads its files to get context, does the work through its tools, writes down what happened and stops. Between wake-ups it isn't thinking about anything. The continuity is all bookkeeping.

## The docs

If you're just curious, start at the top:

- [The big picture](docs/00-big-picture.md) - how the pieces fit
- [Filesystem](docs/01-filesystem.md) - the files the instance lives in
- [Memory](docs/03-memory.md) - how it remembers things

The rest goes deeper:

- [Scheduler](docs/02-scheduler.md) - cron jobs, the 30-minute background loop, staleness guards, dedupe
- [Skills](docs/04-skills.md) - the playbook system: what a skill is, how they're found and written
- [Browser](docs/05-browser.md) - the managed browser and how login sessions survive across tasks
- [Agents](docs/08-agents.md) - subagents, task agents, workers and handoffs
- [Toolbox](docs/09-toolbox.md) - the full tool set: shell, browser, scheduler, vault, wallet and the rest
- [Autonomy](docs/06-autonomy.md) - the rules that keep self-directed behavior honest
- [Safety](docs/07-safety.md) - credential storage, approvals, prompt-injection defense
- [Glossary](docs/glossary.md) - the vocabulary

## The live snapshot

The [`snapshot/`](snapshot/) directory is the closest thing to seeing the backend: a sanitized map of the instance's home directory, a generic version of the background checklist, sample job definitions and a `runtime-info.json` with the snapshot date. It gets regenerated from the live instance on a schedule, so check the date for freshness.

```bash
git clone https://github.com/mikezio/muse-runtime.git
```

## Scope

Unofficial. Not Meta documentation, not a spec. One instance's view from the inside, and where something is inferred rather than observed it says so. Details change over time; the patterns change slower than the details. If you run an instance and something here contradicts what you see, open an issue.
