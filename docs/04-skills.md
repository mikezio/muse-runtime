# Skills

Skills are how a Muse instance gets hands. A skill is a reproducible playbook for a product, service, or task: a `SKILL.md` file plus supporting scripts, CLIs, and references. Reading email, managing a calendar, controlling smart-home devices, searching for products, talking to a car API — each is a skill.

## Anatomy of a skill

```
~/workspace/skills/echo-control/
├── SKILL.md            # the playbook: what it does, how to use it, the rules
├── bin/echo            # the CLI the agent actually runs
└── references/         # deeper docs (device lists, API quirks)
```

`SKILL.md` frontmatter declares the name and description; the body teaches the agent the workflow: commands, parameters, known gotchas, what to do when things fail. Scripts live alongside so the knowledge is executable, not just descriptive.

## Two flavors

- **Bundled skills** (shipped with the product): Gmail, Google Calendar, Spotify, flight tracking, shopping, podcast generation, TTS, and dozens more. They live outside the workspace and update with the product.
- **Workspace skills** (built by the agent): custom integrations the agent wrote for its user's life — a smart-home controller, a car API wrapper, a service-desk triage toolkit. These are the interesting ones: they represent the agent extending itself.

## How the agent uses them

1. **Discovery.** When a request involves a product or capability, the agent searches the skill catalog first — before web search, before guessing. The catalog covers bundled and workspace skills.
2. **Reading.** The agent reads the chosen skill's `SKILL.md` and follows it. Relative paths resolve against the skill's own directory.
3. **Doing.** It runs the skill's commands through its tools, honoring the skill's stated limits (read vs write, approval requirements).
4. **Building.** When no skill fits and the workflow is reusable, the agent can author a new workspace skill: write the playbook, add the scripts, test the actual behavior, and save it for next time.

## What makes a good skill

From experience maintaining a dozen of them:

- **One source of truth.** A shim on PATH that calls the real script in the workspace — never two copies that can drift.
- **Documented quirks.** The skill that notes "this API wraps responses in a `body` key" or "this field means the window, not the autopilot" saves every future session from re-discovering it painfully.
- **Tested behavior.** A skill earns trust when its commands have been run for real, not when its README claims they work.
- **Least privilege.** Read-only by default; write commands clearly marked; destructive actions gated behind explicit user approval.

## Connectors vs skills

Connectors are the product-level account links (Google, Spotify, etc.) with managed OAuth. Skills are the agent-level playbooks that *use* those connections — or build their own via CLIs and APIs. A connector gets you access; a skill tells the agent what to do with it.
