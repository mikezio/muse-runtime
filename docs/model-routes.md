# Model routes, names and reasoning

**Observed September 26–27, 2026; not re-tested by switching models during the September 28 documentation update.** Exact serving policy can change independently of an archived filesystem.

## Four different meanings of “the model”

| Evidence | What it answers | Limitation |
|---|---|---|
| Display branding, e.g. Muse Spark | What the product/runtime calls the model | May be stable across route changes |
| Selected route from `model.get` | Which selection the runtime has accepted | An alias may resolve to another identifier |
| Agent database `model` field | What model value is recorded for that agent | Can persist after global selection changes |
| Effective provider request metadata | What handled a particular inference call | Not exposed in the inspected status surfaces |

Native root status reported `meta/muse-spark`, display name “Muse Spark”, provider “Meta”. This alone did not resolve the other layers.

A root created during a Muse Special test retained `azure/muse-special` in its agent row after Auto was restored. A subsequently observed child recorded `ipnext/avocado-5.16-v4`. A stored row is therefore not sufficient proof of the model used for each reply.

## What is “Avocado”?

Avocado is a family of internal model-route labels found in configuration catalogs, selected routes, and agent records. The inspected Auto path was associated with `ipnext/avocado-5.16-v4`. Nothing in the observations provides a complete mapping from every Avocado suffix to a public model release, architecture, benchmark or capability tier.

Names such as `browser`, `compaction`, `memory-flush` and `voice` also occur in catalogs. They suggest specialized roles; names alone do not establish active deployment or performance.

## Selection tests and live results

“Accepted” means the selector accepted the value. “Reply worked” means a harmless diagnostic turn completed in that test. Failures below do not establish permanent unavailability.

| Input route | Selector | Canonical route / reply result |
|---|---|---|
| `auto/auto` | Accepted | Auto; root/child diagnostics worked |
| `ipnext/avocado-5.16-v4` | Accepted | Diagnostic reply worked |
| `ipnext/avocado-5.16-browser` | Accepted | Canonicalized to v4 |
| `ipnext/avocado-5.16-v0` through `v3` | Accepted | Diagnostic replies failed; cause not exposed |
| `ipnext_responses/avocado-5.16-v0` | Accepted | “Responses Experimental”; diagnostic reply failed |
| `azure/muse-special` | Accepted | Diagnostic replies and tool use worked |
| `azure/gpt-5.6-sol` | Accepted | Canonicalized to `azure/muse-special` |
| `kimi_chat_completions/kimi-k3` | Accepted | Diagnostic reply failed; cause not exposed |

The Sol alias is evidence of alias resolution. It does **not** independently verify an underlying GPT checkpoint or serving provider.

Several guessed Anthropic, Codex/OpenAI, Fireworks and older Avocado routes were rejected. This is not a complete provider support matrix; server-side catalogs and account availability can differ.

## Catalog-only findings

Compiled identifiers included `cerebras/msl-muse-spark-1.2`, `azure/avocado-compaction-v1`, `azure/avocado-memory-flush-v1`, `ipnext/avocado-9b-voice-staging`, and additional Anthropic/historical Avocado names.

They belong in a **discovery inventory**, not an “available models” menu. A string in a binary can be dormant, retired, restricted or used by a different role.

## Reasoning levels

| Result | Values |
|---|---|
| Accepted by the runtime configuration interface | `minimal`, `low`, `medium`, `high`, `xhigh`, `max` |
| Rejected in the tests | `none`, `ultra` |
| Completed Muse Special diagnostics with the setting configured | `high`, `max` |
| Provider-effective effort and serving tier | Not exposed; unresolved |

Root and subagent effort are independently configured in `llm.reasoning`. See the [configuration guide](configuration.md). Token usage, response length and latency are not reliable substitutes for request metadata.

## Context capacity versus use

An inspected native status reported:

| Field/meaning | Observed value |
|---|---|
| Runtime context window | 350,000 tokens |
| Model/agent compaction trigger | 150,000 tokens |
| Current context usage estimate | A changing usage number, not the capacity |
| `auto_compact_limit_tokens` | -1; semantics not established |

These are instance observations. The public model specification discussed in [the model chapter](04-the-model.md) describes a different layer and should not be substituted for runtime settings.

## How to investigate without fooling yourself

Read the selected route, record the agent role and time, and distinguish a completed reply from an accepted setting. If using `muse.db`, read its schema first and select only the needed fields. Agent rows and browser task requester fields are useful clues, not universal per-request ground truth.

**Model changes cleared working context in existing chats.** Use [the configuration verification sequence](configuration.md) before running intentional tests.
