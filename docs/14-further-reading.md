# Further reading

Meta's own articles and technical docs about Muse, plus the best independent teardowns. Every URL below was verified to exist; items marked accordingly where only excerpts could be read.

## From Meta

### [How We Built Safety Into Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) — Meta AI Research
The single most important source for this repo. Meta's official architecture and security writeup names every mechanism documented here: the `systemd-nspawn` runtime cell with root mapped to an unprivileged host user, filtered syscalls, reduced capabilities, the host-side services (`hatch-safety`, `privsep` workers, `hatch-authd`, Sentinel, Postgres), `SO_PEERCRED` Unix-socket IPC, Sentinel as sole authority for connector actions and network egress, eBPF "tainted egress," surrogate credential insertion at the network boundary, and the human-in-the-loop approval path that bypasses the model. Also covers the accessibility-tree browser architecture, OTP filtering in the email connector, single-use payment card numbers, the bug bounty (up to $300,000; up to $130,000 for single-user prompt injection), and the Confidential VM roadmap (`muse-security@meta.com`).

### [Introducing Muse: The World's First Personal AI Agent Built for Everyone](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) — Meta Newsroom, September 2026
The canonical product announcement. Key claims: Muse runs on a dedicated per-user "Muse Secure VM"; a separate Sentinel agent runs on the same machine but is kept apart at the system level; nothing Muse does reaches the internet unless Sentinel approves it; Muse never sees passwords or payment methods; sensitive actions need user approval; VM data is not shared with ad systems; a user-keyed Confidential VM is promised later in 2026.

### [Introducing Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) — Meta, 2026
Documents the model behind Muse: 1M-token context, multi-agent orchestration, computer use, zero-shot generalization to new tools and skills, context compaction. Notes safety evaluation under Meta's Advanced AI Scaling Framework (Chemical & Biological, Cybersecurity, Loss of Control). Quirk: the URL slug now serves the 1.1 announcement — check the page title before citing it for 1.0-era claims.

## Independent teardowns

### [Modern AI Agent Architecture: Muse vs Grok Bot (2026)](https://www.ngram.com/blog/anatomy-of-a-modern-ai-agent) — ngram.com
The best independent technical teardown found. Separates confirmed public documentation from interpretation, frames the architecture in six planes (cognition, orchestration, execution, state, identity, control), and contrasts Muse's "model-controlled cell is compromised by default" design with per-user microVM alternatives. The strongest secondary citation for the trust-boundary diagrams in this repo.

### [Meta's new model is Muse Spark, and meta.ai chat has some interesting tools](https://simonwillison.net/2026/Apr/8/muse-spark/) — Simon Willison, April 2026
Independent hands-on look at Muse Spark's launch: benchmarks, Instant/Thinking modes, and the tools extracted from the harness. Willison is the authority Meta itself cites on prompt injection (the research blog quotes his "lethal trifecta" framing), making this the strongest independent voice on the model lineage.

### [Meta debuts its 'secure by design' personal AI agent Muse](https://siliconangle.com/2026/09/08/meta-debuts-its-secure-by-design-personal-ai-agent-muse/) — SiliconANGLE, September 2026
Carries the key quote from Meta VP of Superintelligence Labs Tarek Sheasha: "The harness runs in its own isolated cell, it doesn't see real credentials, and every interaction with the outside world runs through a Sentinel which the agent can't override." (Verified via excerpt.)

## Worth knowing about (second-hand)

- **WIRED, "Muse, Meta's New Personal AI Agent, Needs You to Trust It"** (September 2026) — the original is bot-walled, but it's substantially quoted in secondary coverage: Meta VP Engineering David Singleton on approval dialogs going directly to the user unfiltered by the model, and Meta being barred by *policy* (not technically) from looking inside today's Secure VMs. The fullest readable quotation is at [huntaegis.com](https://huntaegis.com/article/a9a5e63f2c59fbf96f29d2bdfc8f8bf3). Treat WIRED-attributed claims as second-hand until the original is readable.
- **[groundtruth.day on Muse's agent boundaries](https://groundtruth.day/news/meta-muse-agent-security-prompt-injection-boundaries.html)** (~September 2026) — independent analyst explainer of the credential/browser/egress boundaries, with the right caveat: vendor-authored descriptions, no third party has yet established robustness against sophisticated attacks. (Verified via excerpt.)
- **[The Biggest News From Connect 2026](https://about.fb.com/news/2026/09/the-biggest-news-from-connect-2026/)** — Meta Newsroom, September 24, 2026: Muse coming to Meta AI glasses, voice mode, new connectors (Walmart, Best Buy, PayPal, Instacart, Notion, GitHub, Box), and Muse getting its own email address. Useful for what's next, not for architecture.

## The honest caveats

Meta's materials describe the system *at launch* and say so explicitly. Where this repo's live-instance observations differ from Meta's published description (e.g. the capability set noted in [01-the-machine](01-the-machine.md)), the repo notes the difference rather than picking a side. And the Confidential VM — the version that would cryptographically prevent even Meta from accessing the VM — is a stated plan, not a shipped product. This repo documents what's actually running.
