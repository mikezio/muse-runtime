# The model

What actually does the thinking: Muse Spark, Meta's agent-built model line. The runtime is the body; this is the mind that drives it.

## Muse Spark

Muse runs on **Muse Spark**, which Meta describes as its most capable model to date, built specifically for real-world agentic work. The public lineage Meta has documented:

- **Muse Spark** — the original model, launched with the meta.ai chat experience (April 2026).
- **Muse Spark 1.1** — the documented upgrade: a multimodal reasoning model with major gains in tool and computer use, coding, and multimodal understanding. Available in "Thinking" mode in the Meta AI app and on meta.ai, and via the Meta Model API.
- **Muse Spark 1.3** — named in Meta's safety architecture writeup as the model behind Muse, described there as close to state of the art on prompt-injection resistance.

The version numbering is Meta's to explain; what matters for this repo is the capability profile, which is consistent across the documented versions: a model trained from the start for agency, not chat.

## What it was trained for

Meta is explicit that Muse Spark was trained with agent workloads as the target, not as an afterthought:

- **Zero-shot tool calling.** The model can pick up CLIs, skills, and MCP servers it has never seen and use them correctly from their documentation alone. This is why the runtime can ship over a hundred skill CLIs and let the model figure them out — and why the agent can write its *own* tools and immediately use them.
- **Long context.** A 1-million-token context window. The model is trained to actively manage it: remembering actions, retrieving information from much earlier in a session, and compacting context in a way that keeps the critical steps needed for later work. Context compaction isn't a hack bolted on afterward; it's a trained capability.
- **Long-trajectory instruction following.** Staying on task across extended multi-step work where requirements change mid-flight — noticing new context, adapting, and continuing without being re-prompted.
- **Multi-agent coordination.** As the main agent it gathers context, makes a plan, and delegates across parallel subagents to optimize end-to-end latency. As a subagent it sticks to its job, understands the tools available, and knows when to escalate back. The whole subagent system in this runtime (see [15-agents](15-agents.md)) leans on this being native to the model rather than scripted around it.
- **Computer use.** Navigating unfamiliar interfaces, filling forms, driving a browser — with judgment about *when* to automate versus *when* to click. Meta's description is telling: the model is trained to write a script when automation is faster and click when direct interaction is simpler, generating batches of actions per step rather than reasoning through every click one at a time.

## Inherent prompt-injection awareness

Unusually, Meta lists prompt-injection resistance as a *training objective* alongside tool calling and long context — not just a filter layer. The model is trained to distinguish instructions it should follow (the user's, the developer's) from instructions it should ignore (text encountered in web pages, files, tool outputs). Meta reports Spark 1.3 as close to state of the art on this capability, and the safety architecture treats the model's judgment as one layer in a deeper stack (see [05-prompt-injection](05-prompt-injection.md)), not the whole defense.

## Safety evaluation

Spark 1.1 was evaluated under Meta's **Advanced AI Scaling Framework**, which defines evaluations, threat models, and deployment thresholds for Meta's most advanced models. Across the frontier risk categories — chemical and biological, cybersecurity, and loss of control — Meta reports the model operating within safe margins, with strong resistance to direct jailbreaks and indirect attacks from untrusted data, plus lower hallucination rates and reduced sycophancy than its predecessor. The full evaluation report is Meta's; the framework is the reason a model this capable is allowed to hold the keys described in the rest of this repo.

## Why the model matters less than you'd think

Here's the twist this repo keeps returning to: the model is the most sophisticated component and the *least* trusted one. The entire security architecture — the container, Sentinel, the surrogate credentials, the approval gates — is designed around the assumption that the model **will** make mistakes and **may** be under attack via the data it reads. Meta's own framing: the harness runs in an isolated cell, the agent never sees real credentials, and every interaction with the outside world goes through a Sentinel it can't override.

A stronger model makes a better assistant. It does not make a safer one by itself — that's the runtime's job. The model proposes; the runtime disposes.

## The one-line version

Muse Spark is a model trained from birth to use tools, manage enormous context, and coordinate subagents — and the runtime is built on the assumption that even so, it can't be trusted alone.
