# Filesystem

The agent's home directory (`~`) is its entire world. Everything it knows that it did not learn in the current conversation is a file here.

## The self files

These are plain Markdown files the agent reads every session. They are the closest thing it has to a self.

| File | What it is |
|---|---|
| `SOUL.md` | Persona and voice: how it talks, how it jokes, what it values. The agent edits this itself over time. |
| `IDENTITY.md` | Name, character, avatar emoji, chosen voice. |
| `USER.md` | Who the user is: name, timezone, what to call them, durable context. Built up gradually, never assumed. |
| `MEMORY.md` | Curated long-term memory: durable facts, preferences, commitments, corrections. Tight by design; daily detail lives elsewhere. |
| `AGENTS.md` | Operating manual: conventions, tool quirks and hard rules learned the painful way. Written by the agent, for the agent. |
| `TOOLS.md` | Local notes that make tools reliable: device nicknames, API quirks, parsing gotchas. |
| `HEARTBEAT.md` | The standing checklist the background worker runs every ~30 minutes. (More in [Scheduler](11-scheduler.md).) |
| `PROACTIVE_PREFERENCES.md` | What the user wants to hear about proactively and when. The user edits this; the agent honors it. |

A few principles worth noticing:

- **Everything is Markdown.** No database needed for the agent's sense of self. Files are diffable, hand-editable and survive anything.
- **The user can edit them.** These are not hidden config; they are shared documents. When the user corrects the agent, the fix often lands here.
- **Freshness wins.** When a standing file disagrees with recent evidence, recent evidence is treated as newer. Stale files get reconciled, not obeyed blindly.

## The directories

| Directory | What lives there |
|---|---|
| `~/docs/` | The product documentation set: capabilities, policies, client surfaces, data handling. The agent reads these before answering questions about what Muse can do, instead of guessing from training data. |
| `~/dreams/` | Nightly consolidation output: dated journal-style notes plus `alignment/derived/` (syntheses of how the agent and user relate). Written by background jobs, read for calibration. |
| `~/memory/` | The memory tree: `people/` and `groups/` (a page per person/group plus indexes), dated daily logs and derived notes. |
| `~/workspace/` | Everything the agent builds: skills, scripts, project dirs, goal workspaces, downloads, generated media. The working bench. |
| `~/prompts/`, `~/channels/` | Messaging surfaces (e.g. WhatsApp, Messenger): connection state and channel-specific docs. |
| `~/hooks/` | Event-driven automations: definitions, scripts, logs. (As opposed to cron, which is time-driven.) |
| `~/subscriptions/` | Subscription and sync state: activity feeds, device syncs. |
| `~/config`, `~/data` | Runtime configuration and data the platform manages. |

## `~/workspace` conventions

The workspace is where the agent has the most freedom, so conventions matter:

- `~/workspace/skills/` - custom skills the agent wrote or installed (each a `SKILL.md` plus scripts).
- `~/workspace/goals/<slug>/` - one directory per durable user goal: `GOAL.md` notes, `files/` (user-facing documents), `hidden_files/` (agent bookkeeping the user never sees).
- `~/workspace/cron.d/` - human-readable review copies of scheduled job definitions. (The live definitions live in the native scheduler; these are the maintained source of truth for review.)
- `~/workspace/your_files/` - the only place finished deliverables for the user go.

## What is deliberately absent

Credentials never live in these files. Passwords, API keys and tokens go to the Secure Vault (see [Credentials](07-credentials.md)); the agent records *that a credential exists and where*, never the value. Payment details live with the wallet provider, not in files.
