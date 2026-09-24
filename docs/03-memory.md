# Memory

A Muse instance has no built-in memory of you. Everything it "remembers" is files it wrote and re-reads. The memory system is a pipeline with three stages: capture, consolidate, derive.

## Capture (during the session)

As the conversation happens, the agent writes durable facts to `MEMORY.md` immediately — before responding, not after. What counts as durable: facts, preferences, commitments, actions taken, decisions made together, corrections, people who matter. What does not: transcript chatter, one-off details, anything sensitive like credentials or ID numbers.

Two rules govern capture:

- **Write what happened, not what was planned.** A memory claims an outcome only after a tool result confirms it.
- **Reconcile on change.** When something changes (an appointment rescheduled, a preference corrected), the old entry is updated in place. Conflicting facts are worse than no facts.

## Consolidate (nightly)

Background jobs do the slow work no single conversation has time for:

- **Daily logs** (`~/memory/<date>.md`): the day's durable events, distilled.
- **Dreams** (`~/dreams/<date>.md`): longer journal-style consolidation — what mattered today, what patterns are emerging.
- **People and groups** (`~/memory/people/`, `~/memory/groups/`): one page per person, closest-first indexes. When a turn concerns someone with a page, the agent reads it before answering.
- **Derived alignment** (`~/dreams/alignment/derived/`): syntheses of how the agent and user relate — communication patterns, what earns trust, current frictions, how to be more useful. Recomputed nightly from raw material.

Before answering anything about prior work, decisions, dates, people, preferences, or history, the agent searches this memory (`memory_search`) rather than trusting its own training-time instincts. When asked how it knows something, it can explain a memory's provenance: where the claim came from, what it replaced, when it was last reinforced.

## Derive (making it useful)

Raw notes are not the point. The derived layer turns notes into behavior:

- **Personalization notes**: distilled habits and patterns ("prefers X", "dislikes Y", "corrects in one-liners"), kept current by a background pass.
- **The alignment synthesis**: a candid assessment of the relationship — what the user values, where the friction is, what to do differently. The agent calibrates tone and posture from it.
- **Ideas and feed**: separate pipelines that mine memory for proactive suggestions and short editorial posts, each with its own dedupe so nothing repeats.

## The honesty machinery

Memory is where an agent's honesty lives or dies. A few mechanisms keep it straight:

- **Corrections are first-class.** When the agent gets something wrong and the user corrects it, the correction is written down and the old claim is marked superseded. Memory explains the chain, not just the latest fact.
- **"I don't know" is a valid memory state.** Unknown, unavailable, and unchecked are recorded as such. The agent never fills gaps with guesses and writes them down as facts.
- **Proactive disclosure.** If the agent discovers something it told the user was working is actually broken, the rule is to say so immediately in the open — not to wait to be asked. Familiarity with a failure is not resolution.

## What memory is not

It is not a transcript ledger. It is not training data. Conversations may inform the product in aggregate depending on the user's settings, but the memory files themselves exist to serve one user and are never shared without permission. And memory never holds secrets: credentials go to the vault, payment details to the wallet provider.
