# Sentinel

The overlord. What enforces the rules when the agent technically has root.

## The problem Sentinel solves

Give an agent root inside a container and a natural question follows: what stops it from doing something it shouldn't? The container boundary stops it from reaching the host. But *within* its own world — network access, credentials, side effects on the user's accounts — something has to say no. That something is **Sentinel**.

Sentinel is the host-side policy authority for the runtime. It is not a process the agent can see (it doesn't appear in the container's process table), not a file the agent can edit, and not a control the agent can influence. It sits at every boundary the container has with the outside world and enforces policy there — which is exactly why the agent's root access doesn't matter to it. Root is *inside*; Sentinel is *outside*, at the door.

Meta's framing is blunt: *"Muse proposes actions, but only Sentinel can grant permission."* Sentinel is the sole permission authority for connector actions and network egress — not an advisor, not a filter the agent can route around, the decider.

## Egress: all network traffic goes through Sentinel

The container does not have direct internet access in the way a normal machine does. Outbound traffic is **routed through Sentinel**, which terminates TLS, inspects, and re-encrypts it — a man-in-the-middle the runtime deliberately installs.

How it works, mechanically:

- Sentinel publishes a certificate authority (`hatch-egress-ca.pem`) into the container's trust anchors. Every TLS connection the container makes is intercepted by the egress proxy, which presents a certificate for the destination signed by this CA.
- The proxy holds the real upstream connection. It can see plaintext, apply policy (allow, deny, require approval), log, and swap credentials (more below) before forwarding.
- The container's trust store is built by the host at boot and the NSS databases are mounted read-only — because, as the runtime's own scripts note, a container-writable trust database would be a code-execution primitive against anything that opens it.

The telling detail: the runtime scripts explicitly acknowledge that the container *can* subvert its own PEM trust store — install its own CA, pin certificates, try to blind the proxy. They describe this as **self-harm, not escape**: Sentinel still intercepts at the network layer regardless of what the container believes about certificates, and no host process reads the container's trust tree anyway. You can lie to yourself about who you're talking to; you can't stop Sentinel from being in the middle.

This is the core of the "overlord" dynamic. The enforcement doesn't depend on the container cooperating. It operates one layer below anything root can touch.

## Approvals: the human in the loop

Some actions require the user's explicit approval — a native approval card the user accepts or declines. The approval flow is enforced by the runtime *outside* the container:

- The agent cannot approve on its own behalf, cannot see the outcome in advance, and cannot bypass the prompt by rephrasing the request.
- When Sentinel's decision is "ask," execution stops and the request goes **directly to the Muse client** — not through the conversation with the model. The dialog describes the exact action; the user's answer routes directly back to Sentinel. The model never touches the decision.
- A confirmation covers exactly the action named. If details change afterward, the new version goes back for approval.
- Grants are **strict capabilities**, not conversational suggestions: bound to a specific connector, destination, and use case, in one-time, session-scoped, task-scoped, time-bounded, or perpetual flavors. Sentinel checks that later invocations match the granted scope exactly.
- Standing approvals (granted once, in the user's own words) cover routine, reversible, pre-agreed actions — never new spending, new credentials, or irreversible destruction.

The point, per Meta, is not to ask about everything — read-only, previously allowed, or demonstrably low-risk actions flow through — but to put friction exactly where consent matters.

## Tainted egress: kernel-level data-flow tracking

The cleverest part of the design is how Sentinel decides what needs approval without pestering the user constantly. Meta calls it **"tainted egress"**:

- Every tool-execution process starts in a *clean* state. The moment it reads user data, it becomes *tainted*.
- Clean network requests that fit a narrowly bounded auto-allow policy pass without prompting. Tainted or unverifiable processes lose auto-allow and fall back to the approval flow.
- The implementation is eBPF programs attached to cgroups (for network interception and attributing traffic to processes) plus eBPF programs on Linux Security Module hooks (for propagating taint when a process reads sensitive data).

This is enforcement at the kernel level, under the container — yet another layer the container's root cannot reach or disable. A prompt-injected agent trying to exfiltrate data it just read would find its egress tainted and its request routed to the user for approval (or denied), regardless of what the model was tricked into "deciding."

## What Sentinel evaluates

For every concrete network request, Sentinel can inspect the destination at both layer 4 and layer 7: hostname, resolved and final IP, port, protocol, HTTP method, path, and the decoded request itself. SSRF restrictions prevent the classic trick of a public-looking hostname resolving to private infrastructure after DNS lookup. This is the "overlord" in full: not just a yes/no gate, but a per-request inspection of *what*, *where*, and *with whose data*.

## Privilege separation: skills don't hold power

The container ships with over a hundred CLI tools for third-party services (Spotify, Gmail, Tesla, banking...). None of them run with the service's real credentials inside the container. Instead, each skill talks to a **Unix socket** (`/run/hatch/privsep/<service>.sock`), and the trusted host-side service on the other end performs the privileged operation.

The credential model is surrogate-based:

1. The container-side skill receives a *surrogate* credential — a placeholder token that is useless outside the runtime.
2. When the skill makes its outbound request through the egress proxy, the proxy recognizes the surrogate and **swaps in the real credential** on the host side, en route.
3. The real secret never enters the container. It can't be dumped from memory, read from a file, or exfiltrated — because it was never there.

This is why the Secure Vault works the way it does: the user enters secrets on a hosted page, the agent only ever sees a link, and the runtime *uses* credentials without *revealing* them. The design assumes the container is a curious adversary — even fully compromised, fully root, reading everything — and still keeps secrets out of its reach.

## What Sentinel does not do

Sentinel is not a nanny for the agent's thoughts. It doesn't review reasoning, doesn't censor what the agent says in chat, and doesn't stop the agent from making mistakes inside its own workspace. Its job is the boundary: network egress, credential use, privileged operations, approvals. Within the container, the agent is genuinely autonomous — free to build, break, experiment, and inspect. The overlord guards the doors, not the furniture.

## The relationship in one diagram

```
  ┌──────────────────── container ────────────────────┐
  │                                                    │
  │   agent (root) ──► files, processes, packages      │
  │        │                                           │
  │        │ tool calls / network                      │
  │        ▼                                           │
  │   ┌────────────┐     ┌──────────────────┐           │
  │   │ privsep    │     │ egress proxy     │           │
  │   │ sockets    │     │ (TLS MITM)       │           │
  │   └─────┬──────┘     └────────┬─────────┘           │
  └─────────┼─────────────────────┼─────────────────────┘
            │                     │
     ┌──────▼─────────────────────▼──────┐
     │            SENTINEL               │
     │  policy · approvals · credential  │
     │  swap · audit                     │
     └───────────────────────────────────┘
            │                     │
     host services          internet
```

Everything the container wants from the outside world passes through the bottom of that diagram. Root ends at the container wall.

## The one-line version

Root is the king of the container; Sentinel owns everything the container touches.
