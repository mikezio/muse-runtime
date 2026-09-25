# Data and privacy

What happens to your data inside Muse: where it lives, what leaves, what it's used for, and where the boundaries are.

## Your VM is the system of record

Everything you put into Muse — files, memory, credentials, the agent's notes about you — lives in your dedicated VM. Meta's statement is direct: your VM is the system of record for everything you put in Muse. Credentials and auth tokens for third-party services are stored in a separate isolated container in your VM, not in other Meta services. Your VM data is backed up continuously so you can restore it if something goes wrong.

You can inspect, edit, and download these files freely — including Muse's memory about you. This repo exists because that promise is real: it's written from inside a VM whose entire contents are inspectable.

## What leaves the VM

Muse sends **limited data out of the VM when necessary for inference and telemetry**:

- **Inference.** The model runs on Meta's serving tier, not in your VM (see [02-the-agent-outside](02-the-agent-outside.md)). Your conversation, tool calls, and context cross that boundary because that's where the thinking happens. This is the fundamental data flow of the product — there is no local model.
- **Telemetry.** Operational data about the runtime flows out through its own constrained proxy path.

That's the list. Everything else stays.

## Training on your trajectories

The back-and-forth of conversations, tool calls, and subagent handoffs — what Meta calls **trajectories** — is useful data for training new checkpoints of the model. Before any of it is used in training, it's **sanitized to remove key personally identifiable information**. Meta's stated default: every user gets a better personal agent as everyone collectively uses the product.

If you don't want your data used in model training at all, there's **a simple opt-out switch in Muse settings**. The default is on; the choice is yours. This is worth knowing precisely because it's a default-on arrangement — the kind of thing that should be stated plainly rather than discovered.

## What's not shared

- **Ad systems.** Muse doesn't share your conversations or your VM data with Meta's ad systems. One honest caveat Meta states itself: when Muse browses the internet *as you*, it looks like your activity — so if it buys a shirt from a designer's site, that designer might use the visit to show you an Instagram ad. The agent's actions have the same ad footprint yours would.
- **Other users.** Your VM is isolated per user; no one else's agent can reach it.

## Forgetting

You can tell Muse to forget specific things it has learned, and it will. Because memory is files (see [12-memory](12-memory.md)), forgetting is a concrete operation — entries removed from the memory files — not a polite fiction. What's deleted from the files is gone from what future sessions read.

## The roadmap: Confidential VM

Today's architecture isolates your data from other users and restricts Meta personnel access through **operational policy** — Meta is barred by policy, not by cryptography, from looking inside. Meta is explicit that this does not prevent access when necessary to support, secure, or operate the service.

The planned end state is **Muse Confidential VM**: the whole VM — data, conversations, everything — encrypted with a key only you hold, so not even Meta can access it. Meta says the system is already running with a small group of trusted testers, that design and source are being shared with external auditors, and that a continuous audit will be visible to and inspectable by anyone once launched. Experts will be able to *verify* that Meta cannot access the data, rather than taking it on trust.

Until that ships, the honest description is: strong isolation between users, policy-based protection from Meta itself, cryptographic protection planned. This repo documents what's actually running.

Security and privacy experts can reach Meta's team at **muse-security@meta.com** — including about early access to the Confidential VM program.

## The one-line version

Your data lives in your VM, leaves only for thinking and telemetry, trains models only after sanitizing (unless you opt out) — and the endgame is a VM even Meta can't open.
