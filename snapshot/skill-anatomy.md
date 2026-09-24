# Anatomy of a skill

A skill is the unit of capability: a playbook the agent reads plus the scripts it runs. This is the shape every skill follows.

```
skills/example-skill/
  SKILL.md          # the playbook (frontmatter + instructions)
  bin/tool          # the CLI the agent actually executes
  references/       # deeper docs: quirks, device lists, API notes
```

## SKILL.md

Frontmatter declares the name and a one-line description (this is what the catalog search matches against). The body teaches the workflow:

```markdown
---
name: example-skill
description: Do X with Y. Use when the user asks about X.
---

# Example skill

## Commands
`tool status` - check connection health
`tool do-thing --flag value` - do the thing

## Rules
- Read-only by default. Writes need explicit approval.
- Known quirk: the API wraps responses in a `body` key.
  Parse that first or every read returns empty.

## When it fails
1. Check `tool status` before retrying anything.
2. Never retry an irreversible action blindly.
```

## What separates good skills from dead ones

- **Executable, not aspirational.** The commands have been run for real.
- **Quirks documented.** Every "I learned this the hard way" note saves a future session.
- **One source of truth.** A shim on PATH pointing at the real script. Never two copies.
- **Least privilege.** Read-only by default, writes marked, destruction gated.
