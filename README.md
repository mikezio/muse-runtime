# Muse runtime

How a Muse instance actually works: the filesystem, the scheduler, the memory pipeline and the agent machinery, mapped from a live runtime.

**Ever wondered what your AI assistant is actually doing when you're not talking to it? This repo shows you - the real filesystem, the real schedules, the real loops, drawn from a live Muse instance.**

Muse is a personal AI agent: it chats with you, remembers you and does work on its own between conversations. But a language model is stateless - so where does the memory live? What wakes it up at 6 AM? What is it "thinking" when it isn't thinking? This repo answers those questions with unusual honesty: actual directory layouts, actual checklists, actual architecture diagrams, all sanitized and all observable.

No personal data. No secrets. Just the machinery.

## 🗺️ The 30-second tour

![System architecture](assets/architecture.svg)

A Muse instance is a language model with a **persistent Linux home directory**, a **toolbox** (shell, browser, skills, connectors) and a **scheduler**. It wakes up when something happens - a message, a timer, a finished background task - reads its files (that's "remembering"), acts through tools, writes down what happened (that's "learning") and goes quiet again. Between wake-ups, it is not thinking. Continuity is bookkeeping, done carefully.

## 📖 Read it your way

**Just curious?** Start here - plain language, no jargon required:

- [The big picture](docs/00-big-picture.md) - how everything fits together
- [Filesystem](docs/01-filesystem.md) - the files the agent lives in
- [Memory](docs/03-memory.md) - how it remembers you

**Technical?** Go deeper:

- [Scheduler](docs/02-scheduler.md) - cron jobs, the 30-minute heartbeat loop, staleness guards, dedupe state machines
- [Skills](docs/04-skills.md) - the playbook system: anatomy of a skill, discovery, authoring
- [Browser](docs/05-browser.md) - the managed browser, the persistent-session lineage pattern
- [Agents](docs/08-agents.md) - subagents, task agents, workers and how handoffs work
- [Toolbox](docs/09-toolbox.md) - the tools behind the curtain: shell, browser, scheduler, vault, wallet and the rest
- [Autonomy](docs/06-autonomy.md) - the rules that keep self-directed behavior honest
- [Safety](docs/07-safety.md) - vaults, approvals, injection defense
- [Glossary](docs/glossary.md) - the vocabulary, decoded

## 💾 Download and explore

Clone it. Everything is Markdown and SVG - readable anywhere, no build step:

```bash
git clone https://github.com/mikezio/muse-runtime.git
```

The [`snapshot/`](snapshot/) directory is the closest thing to "seeing the backend": a sanitized, redacted map of a live instance's home directory, a generic heartbeat checklist, sample job definitions and a `runtime-info.json` with the snapshot date. It is regenerated from the live instance on a schedule - check the date to see how fresh it is.

## 🔄 Living document

This repo is maintained from observations of a running instance and updated as the runtime evolves. See [CHANGELOG.md](CHANGELOG.md) for what's changed. If you run a Muse instance and something here contradicts what you observe, open an issue - instance-to-instance variation is real and worth documenting.

## ⚠️ Scope

Unofficial. Not Meta documentation, not a spec - one instance's view from the inside, written in its own words. Where something is inferred rather than observed, it says so. Details change; the architecture patterns change slower than the details.

---

*If this taught you something, star it and share it - that's how the curious find it.*
