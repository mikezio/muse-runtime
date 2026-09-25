# Changelog

## 2026-09-25 - The book rebuild

Mike's call: the repo was a mess — information scattered, and the further-reading page just pointed at Meta's articles instead of using them. Rebuilt as a coherent book in two parts.

Part I — How Meta built it — now absorbs Meta's publications into real chapters instead of linking out:

- 04 — The model: Muse Spark (Spark 1.1 announcement + the safety writeup's Spark 1.3 mention), what it was trained for, why it still isn't trusted alone
- 05 — Prompt injection: the lethal trifecta and the five defensive layers, plus the bug bounty (up to $300,000; up to $130,000 for single-user prompt injection)
- 06 — The browser: Meta's browser architecture (accessibility tree, no JS, CDP broker, credential injection, classifier family, malicious-site blocklist) plus observed session behavior
- 07 — Credentials: the Vault, `authd`, surrogate flow, privsep's three authorities, least-privilege grants, the email connector's OTP filtering
- 08 — Paying for things: Stripe Link single-use cards, checkout detection, human approval on every payment
- 09 — Data and privacy: VM as system of record, trajectory sanitizing + training opt-out, no ad sharing, the Confidential VM roadmap

The old further-reading link farm is gone, replaced by a short [sources](docs/sources.md) page. Part II (the observed machinery: filesystem, scheduler, memory, skills, autonomy, agents, toolbox, transparency) renumbered 10–17 with all cross-references fixed. README rewritten around the new structure; the "nothing Meta doesn't want seen" overclaim removed from the README and qualified in the transparency chapter.

## 2026-09-24 - The architecture deep-dive

The rewrite Mike asked for: the repo now explains the system the way it actually works, verified against a live runtime and Meta's own published architecture.

New docs:

- 01 — The machine: the systemd-nspawn container, namespaced root (uid 0 mapped to an unprivileged host UID), the three filesystem layers, the host-side services
- 02 — The agent outside the machine: the model runs on Meta's inference tier; the VM is its peripheral; every tool call is a mediated request
- 03 — Sentinel: the overlord. Egress TLS interception, tainted-egress eBPF tracking, approvals as strict capabilities, privilege separation, surrogate credential insertion
- 13 — Radical transparency: why everything is inspectable on purpose
- 14 — Further reading: Meta's safety architecture post, the Newsroom announcement, Muse Spark, and the best independent teardowns — all URLs verified

Expanded: the big picture (full-stack diagram, the inversion), safety (Sentinel as the enforcement layer), browser (Meta's broker/a11y-tree/single-use-card architecture), glossary (cell, JARVIS, Sentinel, privsep, namespaced root, credential surrogates, and more). Fixed doc cross-references after renumbering.

Sourcing standard: architecture claims verified by inspecting the live runtime (boot scripts, trust-store builder, privsep sockets, capability sets); Meta's [safety architecture post](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) used to confirm and extend. Where live observation differs from Meta's published description (capability set), the difference is noted, not hidden.

## 2026-09-24 - Launch

Initial release. The full tour:

- The big picture: how the pieces fit, one diagram
- Filesystem: the self files and directory layout
- Scheduler: cron jobs, the heartbeat loop, dedupe state machine, staleness guards
- Memory: capture, consolidate, derive - plus the honesty machinery
- Skills: anatomy, discovery, the built-in catalog, skill-creator and forget
- Browser: the persistent-lineage pattern, spawn vs steer
- Agents: subagents, task agents, workers, coordinators, handoffs
- Toolbox: every tool namespace and what it's for
- Autonomy: the rules that keep self-directed behavior honest
- Safety: vault, approvals, injection defense, discretion
- Snapshot: sanitized live home-directory map, regenerated weekly
- Five SVG architecture diagrams
