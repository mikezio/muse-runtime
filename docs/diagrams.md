# Reading and maintaining the diagrams

The figures use conventional technical notation. Each answers one question; no single figure is a complete deployment trace or security audit.

## What each figure means

| Figure | Type and question | Evidence and limits |
|---|---|---|
| [Deployment](../assets/architecture.svg) | Containment: what runs in the cell, elsewhere on the personal VM, and remotely? | [Meta's launch architecture](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse), placement rechecked September 28, 2026. Arrows show selected interfaces; the service list does not prescribe execution order. |
| [Conversation turn](../assets/request-lifecycle.svg) | Sequence: how do inference and tool execution form a loop? | Logical synthesis of [runtime interfaces](runtime-api.md). Proxies and transport are omitted here; tools can be local or mediated. |
| [Agent ownership](../assets/agent-tree.svg) | Tree: which work belongs to the conversation, and which can have a separate activation? | Observed [agent roles and task contracts](15-agents.md). Ownership does not establish shared context, model or permissions. |
| [Browser lifecycle](../assets/browser-lineage.svg) | State flow: what follows submission, waiting, resuming or finishing? | Installed [browser task guidance](06-browser.md). Labels are conceptual, not a claim about exact API enum names. Authentication state is separate. |
| [Memory](../assets/memory-pipeline.svg) | Information map: which representations can inform later context? | [Memory guidance and observed surfaces](12-memory.md). This is not a verified storage schema or processing pipeline. |
| [Background work](../assets/scheduler-loop.svg) | Flow: how do triggers lead to a run, outcome and delivery? | [Scheduler/task guidance](11-scheduler.md). No fixed heartbeat, automatic retry or universal delivery rule is implied. |
| [Configuration](../assets/configuration-layers.svg) | Comparison: which independent surface controls which behavior? | [Configuration](configuration.md) and [feature-flag](feature-flags.md) observations from September 26–27. Row order is not precedence. |
| [Outbound authorization](../assets/trust-boundaries.svg) | Example flow: how can an outbound request be allowed, denied or sent for approval? | Named example based on the published egress design. Credential insertion is conditional. Browser, privileged-worker and device paths have their own details. |

## Notation

- **Nested boundaries** in the deployment figure mean physical/security placement, not task ownership.
- **Arrows** represent the relation named in the figure: request, result, ownership, activation or transition.
- **Dashed return arrows** in sequence/authorization figures indicate responses. The dashed child edge in the ownership tree is explicitly optional.
- **Dashed enclosures** group a cell, a conditional sequence or conceptual information, according to the figure's caption. They are not interchangeable security boundaries.
- **Service names** describe responsibilities. Sentinel's action authorization and `hatch-safety` inference checks are distinct.

Every SVG has a title, a descriptive alternative and source/scope metadata. The explanatory captions remain in this reference rather than being packed into nodes.

## Rebuild

The editable source is [tools/build-diagrams.py](../tools/build-diagrams.py). It uses Python's standard library and writes the eight SVGs in `assets/`:

```sh
python3 tools/build-diagrams.py
```

Each figure has explicit geometry suited to its diagram type. The files use system sans-serif fonts, a white background and monochrome strokes; they require no web fonts or external image assets.

Before publishing a change:

1. Check each placement and edge against its stated evidence. Do not add a line merely to fill space.
2. Regenerate, then render at native width and a typical GitHub reading width (800 pixels).
3. Inspect text, arrow endpoints, crossings and whitespace in the rendered image. XML validity alone cannot establish readability.
4. Keep the accessible description and this scope table in sync with the drawing.
5. Run `git diff --check` and inspect the changed artifacts.

The September 28 redraw corrected the inference proxy path, separated background-worker activation from conversation ownership, connected every scheduler trigger, restored the browser resume loop, and removed the implication that only Markdown files feed memory retrieval. These are semantic corrections as well as visual changes.
