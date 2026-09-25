# The agent outside the machine

The most important architectural fact about Muse: **the agent does not run inside the VM.** The model — the thing that reads, reasons, and decides — runs on Meta's inference infrastructure. The VM is its *computer*, not its *body*. This page explains how the two relate.

## The inversion

The intuitive mental model is wrong. You picture an AI living inside a computer, using the computer's resources to think. The reality is inverted:

```
  ┌─────────────────────────────────────────────────┐
  │           Meta inference tier                    │
  │                                                  │
  │   ┌────────┐    tool call     ┌───────────────┐  │
  │   │ agent  │ ───────────────▶ │    runtime     │  │
  │   │ (model)│ ◀─────────────── │  (orchestrator)│  │
  │   └────────┘    tool result  └───────┬───────┘  │
  └──────────────────────────────────────┼──────────┘
                                         │ executes
                              ┌──────────▼──────────┐
                              │   the VM (container) │
                              │  shell · files ·     │
                              │  browser · skills    │
                              └─────────────────────┘
```

The agent thinks *out there* and acts *in here*. Every shell command, file write, browser action, or skill invocation is a structured request the runtime carries across the boundary, executes inside the container, and returns as a result. The agent never "runs code" directly — it asks the runtime to run code, and the runtime decides how.

This is why the agent can be described as having a computer: the computer is a peripheral. The thinking happens elsewhere.

## How a tool call crosses the boundary

When the agent invokes a tool (say, running a shell command), the sequence is roughly:

1. **The model emits a structured tool call** — a name and arguments, nothing more. It has no shell, no syscalls, no direct access to anything.
2. **The runtime validates and routes it.** Policy checks happen here: is this tool allowed in this context, does it need user approval, is it within the current authorization?
3. **Execution happens inside the cell.** For shell commands, `hatch-execd` — a daemon running inside the container — receives the command and runs it as the container's user. For skills, the skill CLI talks to a privilege-separated host service over a Unix socket (see [03-sentinel](03-sentinel.md)). For the browser, a managed browser task runs the interaction.
4. **The result is delivered back** into the agent's context as a tool result: stdout, a file listing, a page snapshot.

The agent experiences this as "I ran a command." Mechanically, it sent a message and got a reply. That gap is where all the safety controls live.

## The inference path

Model inference itself goes through a dedicated proxy: the runtime exposes an inference socket (`/run/hatch/proxy/inference.sock`), and the agent's "thoughts" are requests through it to Meta's serving tier. The model weights never enter the VM. Nothing the agent does inside the container — no matter how privileged — can inspect or modify the model, because the model isn't there.

Telemetry takes a parallel path through its own proxy socket. Observability of the runtime flows outward; control of the model stays outside.

## What "background work" means

The runtime also runs things when the agent isn't thinking: cron jobs, the heartbeat loop, subagents, browser tasks. These are orchestrated by the host-side scheduler, which wakes the agent by starting a new inference turn with fresh context (the scheduled job's instructions plus whatever files it needs). "The agent was asleep and a cron job woke it" is literally true in implementation, not just metaphor: between activations there is no running agent process to wake. There is a schedule entry, and when it fires, the runtime constructs a new turn.

Subagents work the same way: they are separate inference turns with their own context, running concurrently, whose results are delivered back into the parent's context when they finish. The whole multi-agent system is message-passing between stateless turns, coordinated by the runtime.

## Why this design

- **The model can't be tampered with from inside.** Prompt injection, a compromised skill, a malicious file — none of them can reach the weights or the serving infrastructure, because those live on the other side of the boundary. The blast radius of anything inside the VM ends at the VM.
- **Every action is mediated.** Because the agent cannot act except through tool calls the runtime executes, the runtime sees every action and can approve, deny, log, or rate-limit it. There is no side channel: the agent has no other way to affect the world.
- **The VM is disposable.** If the container is corrupted — by the agent's own mistake, a bad package install, anything — the host can rebuild it from the image and reattach the persistent home directory. The agent's continuity lives in files and the model, not in the container's running state.
- **Scale and tenancy.** The inference tier serves many agents; the VM is per-user. Keeping the expensive, shared part (the model) separate from the cheap, personal part (the container) is what makes one-agent-per-person economically sane.

## The one-line version

The agent is a mind on Meta's servers with a computer in a container; everything it "does" is a request the runtime chooses to honor.
