# Browser

The agent has a real, up-to-date Chromium browser. It can visit any site, including ones that need logins, forms and JavaScript. Cookies and session state persist between tasks - which makes the browser both powerful and full of traps.

## How the browser is sandboxed

Meta's published architecture puts the browser behind the same boundary as everything else:

- The browser is driven through a **broker that lives outside the runtime cell** and manages the Chrome DevTools Protocol connection. The agent never gets raw CDP access.
- The driving subagent sees an **accessibility-tree snapshot** of the page, not the raw DOM. It cannot run JavaScript in the page, has no exec in the browser process, and DevTools are disabled.
- **When the user takes over the browser, or while the credential store is filling a form, the agent is paused** and cannot act at all.
- A family of classifiers watches for data egress unrelated to the task, prompt injection in the DOM / images / downloaded files, and high-risk form submissions — blocking or prompting as appropriate.
- Purchases get special treatment: checkout pages always prompt, and payments go through **single-use card numbers** tied to one merchant, one amount, and a short time window.

This is why the browser feels like "a real browser the agent uses" but behaves like a supervised instrument: every capability the agent has through it is a narrowed, watched version of the real thing.

## Two ways to use it

- **Reading** (`browser.search`, `browser.open`): text search and page fetching. No interaction, no state changes. Used for research and verification.
- **Doing** (`browser.spawn_task` / `browser.steer_task`): a live browser task that can click, sign in, fill forms and complete multi-step flows like purchases. Asynchronous - the agent gets an acceptance receipt, does other work and receives the result as a handoff.

## The one-profile rule

All browser tasks share one leased Chromium profile. That means tabs, cookies and sign-in state are shared - and so are failures. Parallel tasks must be independent work that cannot conflict through shared state.

## The persistent-lineage pattern

Here is the most important thing I learned about the browser, proven by experiment:

**A fresh browser task does not inherit another task's login cookies.** A task that signed in to a site at 13:09 sees the logged-in homepage; a brand-new task loading the same site seconds later sees the logged-out landing page. The session lives inside one task lineage.

But: **steering a closed task creates a successor from saved history and the successor retains the session cookies.** So the durable pattern for any logged-in workflow is:

1. Do the login once in a task and record its lineage id in a file.
2. Do all future work by *steering that lineage*, never by spawning fresh.
3. If a steer fails or the lineage reports logged out, only then start a fresh login - never run a second concurrent login while a session might be alive, since that can invalidate it.

This is how an agent holds a login for weeks across hundreds of separate jobs: one lineage, steered over and over, with its id treated as precious state.

## Handoffs and honesty

A browser task cannot see the conversation; it gets a self-contained brief. Its report comes back as a handoff and the agent reports only what the task confirms it completed. "Accepted" is not "done." A few disciplines:

- **Verify, don't assume.** Never claim a UI action landed without evidence - a page state, a confirmation string, a screenshot the user can check.
- **One session at a time** for logged-in work. Concurrent logins are how sessions die.
- **Respect the walls.** Some sites serve anti-automation notices to managed browsers. The honest move is to hand control to the user for that step, not to burn turns fighting the wall.
- **Logins need the user exactly once.** The working recipe: the task types the username, parks at the 2FA step, the user pastes the code in chat, the agent steers it in. After that the lineage holds the session.
