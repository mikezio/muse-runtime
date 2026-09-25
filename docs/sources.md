# Sources

Everything in this repo is built from two kinds of material: **Meta's own publications** about Muse, and **direct observation from inside a live runtime** (whose snapshots are archived as releases). This page lists the former; the observation side is the archive itself.

Meta's materials describe the system at launch and say so explicitly. Where live-instance observations in this repo differ from Meta's published description, the docs note the difference rather than picking a side.

## From Meta

- [How We Built Safety Into Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) — Meta AI Research. The primary source: the systemd-nspawn runtime cell, the host-side services, Sentinel, tainted egress, surrogate credentials, the approval path, the browser architecture, and the bug bounty. Names Muse Spark 1.3.
- [Introducing Muse: The World's First Personal AI Agent Built for Everyone](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) — Meta Newsroom, September 2026. The product announcement: the Secure VM, Sentinel as a separate agent, the privacy commitments, Link payments, and the Confidential VM plan.
- [Introducing Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) — Meta Superintelligence Labs. The model line: 1M-token context, multi-agent orchestration, computer use, zero-shot generalization to new tools and skills, safety evaluation under the Advanced AI Scaling Framework.

## Independent

- [Modern AI Agent Architecture: Muse vs Grok Bot](https://www.ngram.com/blog/anatomy-of-a-modern-ai-agent) — ngram.com. The best independent teardown; useful framing of the trust boundaries.
- [Meta's new model is Muse Spark, and meta.ai chat has some interesting tools](https://simonwillison.net/2026/Apr/8/muse-spark/) — Simon Willison. Hands-on look at the Spark launch; Willison's "lethal trifecta" framing is the one Meta itself quotes on prompt injection.
- [Meta debuts its 'secure by design' personal AI agent Muse](https://siliconangle.com/2026/09/08/meta-debuts-its-secure-by-design-personal-ai-agent-muse/) — SiliconANGLE. Carries Meta VP Tarek Sheasha's summary quote on the harness, credentials, and Sentinel.
