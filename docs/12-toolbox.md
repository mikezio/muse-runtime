# Toolbox: the tools behind the curtain

Skills give the agent *knowledge*. Tools give it *hands*. A tool is a function the model can call: run a shell command, read a file, steer a browser task, spawn a subagent. The model never touches the outside world except through a tool call - that is the entire security boundary in one sentence.

## The core set

**Shell & files** - execute commands, read/write/edit files, list directories. The computer the agent lives on is a real Linux VM with a persistent filesystem, so this is where scripts run, logs land and builds happen.

**Browser** - text search, page fetching and the live-browser task system (`spawn_task` for new work, `steer_task` for continuations). Reading and doing are separate tools with separate rules. See [Browser](08-browser.md).

**Subagents** - delegate bounded work to child agents: spawn, list, send follow-up input, close. The tree is managed, not fire-and-forget. See [Agents](11-agents.md).

**Scheduler** - create, update, list, inspect and remove cron jobs; run one immediately; read run history. Hooks get the same treatment for event-driven automations.

**Chat** - manage conversations: list chats, create side chats, send messages between them. Side chats are separate persistent threads with their own context.

**Artifacts** - build durable deliverables: documents, pages, decks, spreadsheets, web apps. Creating an artifact is a background build with its own lifecycle, not a file write.

**Media** - generate images, video and audio (TTS, podcasts). Separate from the file tools because generation is its own pipeline with its own limits.

**Widgets** - interactive in-chat UI: option buttons, HTML visualizations, maps. The model describes data; the widget renders it.

## Trust & money tools

**Credentials (Secure Vault)** - request a login capture or API-key setup, list saved logins (metadata only). The agent gets a link to a secure page; the secret itself never passes through chat or files. See [Safety](10-safety.md).

**Wallet** - list payment providers, connect one, view saved methods and addresses. Card details are never visible to the agent. Spending requires the user's approval through a native card, following a strict purchase flow.

**Permissions** - inspect pending approval requests: what action, what access, when it was asked. Read-only; the agent can explain a pending permission but never grant it.

## Memory & tracking tools

**Memory** - semantic search over memory files, snippet reads and provenance explanations ("where did this fact come from, what did it replace"). The agent must consult this before answering from history.

**Tracking / goals** - durable user goals and concrete commitments (reservations, deliveries, trips): create, update, log progress, close when done. Goals get workspaces; the agent reads a goal's notes before acting on it.

**Feed & ideas** - the personal-newspaper pipeline and the idea backlog: prompts, published units, generation status. Separate from memory, with their own dedupe.

## Device & comms tools

**Device** - run commands on paired devices (phone, computer), pull data like messages and calendars. Each device has a guidance file the agent reads first.

**Phone** - place calls to verified businesses for legitimate customer-side tasks, with confirmation. Blocked for unverifiable destinations.

**Map** - geocode addresses, reverse-geocode coordinates. Location is used only when the answer depends on where the user is.

**Social** - search public social platforms for topic discussion; turn the user's footage into shareable clips.

## How tools stay safe

- **Schemas, not strings.** Every tool declares its parameters; the model fills them in. There is no "run arbitrary code" tool - the shell is the closest thing and it runs as an unprivileged user in the agent's own VM.
- **Approvals are native.** Sensitive calls trigger a user-facing approval card the agent cannot dismiss, forge, or predict.
- **Deferred loading.** Tool namespaces load on demand; the model sees a function's full schema only when it needs it. This keeps the context lean and the authority explicit.
- **Every call is logged.** Tool calls and their outputs are recorded, which is what makes the honesty rules enforceable: "I did X" can be checked against what actually ran.

## The one-line version

The model thinks; the tools act; the files remember; the scheduler wakes. Everything else is commentary.
