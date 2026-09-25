# Changelog

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
