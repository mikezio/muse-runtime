# Documentation guide

Start with [How Muse fits together](00-big-picture.md). This reference is for readers trying to understand an agent system, inspect a Muse instance, or compare runtime releases.

## Suggested reading paths

- **New to agent systems:** architecture → worked examples → components → memory and agents.
- **Building or customizing:** capabilities → skills/Spaces → configuration → API surfaces.
- **Investigating behavior:** troubleshooting → evidence → model routes/feature flags.
- **Following updates:** archive workflow → manifest comparison → the changed component's reference.

## Learn the system

| Question | Read |
|---|---|
| What runs where, and what is the “VM”? | [Architecture](00-big-picture.md), [cell and host](01-the-machine.md) |
| How does a message become actions? | [Inference and execution](02-the-agent-outside.md), [worked examples](walkthroughs.md) |
| What are all these component names? | [Component reference](components.md), [glossary](glossary.md) |
| How do parent, child and browser agents relate? | [Agents](15-agents.md), [browser](06-browser.md) |
| Where do memory and state live? | [Memory](12-memory.md), [filesystem](10-filesystem.md) |

## Inspect and experiment

| Question | Read |
|---|---|
| Which settings are actually changeable? | [Configuration layers](configuration.md) |
| What do Spark, Avocado, Auto and Muse Special mean? | [Model routes and reasoning](model-routes.md) |
| Why did this operation fail? | [Troubleshooting](troubleshooting.md) |
| Which daemon methods were observed? | [API surface](runtime-api.md) |
| Is a feature installed, enabled or working? | [Feature flags](feature-flags.md), [capability atlas](capabilities.md) |
| How do I compare downloaded builds? | [Archive workflow](archive-workflow.md) |
| How strong is a claim in these docs? | [Evidence and open questions](evidence.md) |

## Topic chapters

- Security: [Sentinel](03-sentinel.md), [prompt injection](05-prompt-injection.md), [credentials](07-credentials.md), [payments](08-paying-for-things.md), [data/privacy](09-data-and-privacy.md).
- Agent behavior: [published model background](04-the-model.md), [scheduler](11-scheduler.md), [skills](13-skills.md), [autonomy](14-autonomy.md), [toolbox](16-toolbox.md).
- Research: [inspection boundaries](17-transparency.md), [sources](sources.md), [build index](../builds.md).

The original security/model chapters summarize published material. Operational reference pages record dated instance observations. Neither is a guarantee about every account or future build.
