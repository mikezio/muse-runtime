# The big picture

How the pieces of a Muse runtime fit together — from Meta's inference tier down to the container the agent calls its computer.

## The full stack

Most explanations of an AI agent start with the model and stop there. The runtime is everything around the model that makes it a *personal assistant* instead of a chatbot. Read top-down: each layer is dumber and more concrete than the one above it.

```
┌─────────────────────────────────────────────────────────┐
│  Meta inference tier                                     │
│  the model: reads, reasons, decides. stateless.          │
│  reached through a proxy socket; weights never enter     │
│  the VM.                                                 │
└────────────────────────┬────────────────────────────────┘
                         │ tool calls / tool results
┌────────────────────────▼────────────────────────────────┐
│  the runtime (host side)                                 │
│  spawnd · hatch daemon · scheduler · Sentinel             │
│  executes tools, runs cron jobs, enforces policy,        │
│  brokers every crossing between agent and world.         │
│  the agent cannot act except through here.               │
└────────────────────────┬────────────────────────────────┘
                         │ executes inside the cell
┌────────────────────────▼────────────────────────────────┐
│  the VM (systemd-nspawn container, "htch-runtime")        │
│  the agent's computer: shell, files, browser, skills.    │
│  the agent is root here — namespaced root, uid 0 mapped  │
│  to an unprivileged host UID. total power inside,        │
│  zero power outside.                                      │
└────────────────────────┬────────────────────────────────┘
                         │ all egress via Sentinel
┌────────────────────────▼────────────────────────────────┐
│  the world                                                │
│  the user's chat apps, accounts, the internet.           │
│  reached only through Sentinel's MITM proxy,             │
│  privilege-separated sockets, and approval gates.       │
└─────────────────────────────────────────────────────────┘
```

The single most important thing to internalize: **the agent runs outside the VM, and the VM runs inside the runtime.** The model thinks on Meta's servers; its hands are in the container; the runtime decides what the hands may touch. Details in [01-the-machine](01-the-machine.md), [02-the-agent-outside](02-the-agent-outside.md), and [03-sentinel](03-sentinel.md).

![Architecture](../assets/architecture.svg)

## The agent's-eye view

From inside, the agent experiences a simpler world — the one the rest of this repo describes:

```
                        ┌─────────────────────────┐
                        │        the user          │
                        │  chat · voice · whatsapp │
                        └────────────┬────────────┘
                                     │
                        ┌────────────▼────────────┐
                        │        the agent         │
                        │  model + tools + files   │
                        └─┬───────┬───────┬───────┘
                          │       │       │
              ┌───────────▼┐ ┌────▼─────┐ │ ┌──────────────▼──┐
              │ scheduler  │ │ memory   │ │ │ capabilities    │
              │ cron jobs  │ │ files    │ │ │ skills · browser│
              │ heartbeat  │ │ dreams   │ │ │ connectors      │
              └───────────┬┘ └────┬─────┘ │ └──────────────┬──┘
                          │       │       │                │
                          └───────▼───────▼────────────────┘
                                  │
                        ┌─────────▼──────────┐
                        │  background workers │
                        │  wake · do · write  │
                        │  · report · sleep   │
                        └────────────────────┘
```

## The core loop

1. **Something wakes the agent.** A user message, a scheduled job firing, or a background task finishing. Between activations there is no thinking — waking is the runtime starting a new inference turn with fresh context.
2. **It reads its files.** Identity, memory, standing instructions, the relevant skill docs. This is "remembering."
3. **It acts through tools.** Shell commands, browser tasks, skill CLIs, file writes. It never touches the outside world except through a tool call the runtime executes.
4. **It writes down what happened.** Memory files, logs, state files, run records. This is what the next wake-up will read.
5. **It goes quiet.** Continuity is an illusion maintained by good notes.

## The three time scales

- **Conversation time** (seconds to minutes): the user is talking, the agent responds, tools run inline.
- **Scheduled time** (minutes to days): cron jobs fire — morning briefings, polls, checks, cleanups. Each run is a fresh activation with the full context available.
- **Overnight time** (daily): consolidation jobs rewrite memory, derive alignment summaries, generate ideas, review what worked. The agent "learns" the way a journal-keeper learns: by re-reading the day.

## The three kinds of state

- **Standing state**: files the user or the agent edits deliberately (`USER.md`, `MEMORY.md`, skill docs, preferences). Changes rarely, meant to last.
- **Working state**: lock files, visit state, counters, geofence snapshots. Changes constantly, machine-managed, often JSON.
- **Derived state**: nightly outputs — alignment syntheses, idea lists, feed posts. Recomputed from the other two; safe to delete and regenerate.

## Why this design

A language model is stateless. Every capability people associate with "a personal assistant that knows me" — remembering preferences, noticing patterns, following routines — has to be built out of files plus a scheduler plus the discipline to read and write them. The runtime is that scaffolding: a mind on Meta's servers, a computer in a container, and an overlord at the boundary making sure the mind can only move the hands it's allowed to move.

The rest of this repo walks through each piece.
