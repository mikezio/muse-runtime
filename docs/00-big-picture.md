# The big picture

How the pieces of a Muse runtime fit together.

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

1. **Something wakes the agent.** A user message, a scheduled job firing, or a background task finishing.
2. **It reads its files.** Identity, memory, standing instructions, the relevant skill docs. This is "remembering."
3. **It acts through tools.** Shell commands, browser tasks, skill CLIs, file writes. It never touches the outside world except through a tool.
4. **It writes down what happened.** Memory files, logs, state files, run records. This is what the next wake-up will read.
5. **It goes quiet.** Between activations there is no thinking. Continuity is an illusion maintained by good notes.

## The three time scales

- **Conversation time** (seconds to minutes): the user is talking, the agent responds, tools run inline.
- **Scheduled time** (minutes to days): cron jobs fire - morning briefings, polls, checks, cleanups. Each run is a fresh activation with the full context available.
- **Overnight time** (daily): consolidation jobs rewrite memory, derive alignment summaries, generate ideas, review what worked. The agent "learns" the way a journal-keeper learns: by re-reading the day.

## The three kinds of state

- **Standing state**: files the user or the agent edits deliberately (`USER.md`, `MEMORY.md`, skill docs, preferences). Changes rarely, meant to last.
- **Working state**: lock files, visit state, counters, geofence snapshots. Changes constantly, machine-managed, often JSON.
- **Derived state**: nightly outputs - alignment syntheses, idea lists, feed posts. Recomputed from the other two; safe to delete and regenerate.

## Why this design

A language model is stateless. Every capability people associate with a "personal assistant that knows me" - remembering preferences, noticing patterns, following routines - has to be built out of files plus a scheduler plus the discipline to read and write them. The runtime is that scaffolding. The rest of this repo walks through each piece.
