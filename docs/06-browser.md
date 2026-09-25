# The browser

A real Chromium the agent drives — and the most heavily armored tool in the runtime, because the web is where untrusted content lives.

## What it is

Muse has a real, up-to-date Chromium-based browser running behind a virtualization layer. It isn't a text scraper or a simplified reader: the agent navigates actual pages, fills real forms, clicks through checkouts, and handles JavaScript-heavy sites. The user can watch what it's doing in the browser and **take over at any time** — and while the user is in control, or while credentials are being filled, the agent is paused and can't act at all.

Driving the browser is something Muse Spark is specifically good at (see [04-the-model](04-the-model.md)): a dedicated **browser subagent** handles each task — reading pages, traversing sites, filling forms — with web-specific instructions about which parts of page content may be adversarial.

## The accessibility tree, not the DOM

The key architectural decision: the browser subagent never sees the raw DOM. It sees an **accessibility tree snapshot** of the page — the same semantic structure a screen reader uses: buttons, headings, form fields, text. This has three consequences:

1. **It can't run JavaScript** in the page context. No script verbs, no exec in the browser process, Chrome DevTools disabled. The most powerful web-attack primitive simply isn't in its hands.
2. **It can't read credentials** entered from the credential store — or manually back them out of the DOM. What the credential filler types is invisible to the agent by construction.
3. **It gets less attack surface.** A huge class of DOM-based trickery (hidden elements, event-handler smuggling, CSS exfiltration) operates below the abstraction the agent sees.

The browser itself is managed by a **separate broker** outside the runtime cell that owns the Chrome DevTools Protocol connection. The subagent gets a narrow, controlled interface to that broker — the same privilege-separation pattern as the connector skills (see [03-sentinel](03-sentinel.md)).

## The classifier layer

On top of the structural limits sits a family of classifiers providing another independent layer of protection, tuned to what the browser is for. They watch for:

- Egress of personal data not related to the task at hand, via the browser.
- Attempted prompt injection in the page DOM.
- Attempted prompt injection via images and media on the page.
- Attempted prompt injection via files downloaded through the browser.
- Attempted submission of high-risk forms.

Depending on the threat detected, they either block the action outright or prompt the user to review what's about to happen. Meta also matches navigation against its existing malicious-website detection systems — the same ones that protect its family of apps — and stops the browser from reaching known harmful sites.

## Signing in: credentials without exposure

One of the most common browser tasks is signing in to websites, and it's handled with the same never-show-the-model philosophy as API tokens (see [07-credentials](07-credentials.md)):

- A custom UI on the client captures the username and password and routes them **directly to `authd`**, stored in the secure credential store outside the runtime cell.
- What the user enters goes straight to secure storage and is never visible to the agent.
- At the point of need, the credential is **injected into the browser window** — typed into the form by the trusted filler, not by the agent.

The agent can drive a login flow end to end without ever being able to see, copy, or leak the password. Even a fully prompt-injected browser subagent couldn't exfiltrate credentials it was never given.

## Purchases: the highest-friction flow

Buying things is one of the most popular browser uses, and mistakes cost real money, so it's treated with special care:

- If the site already has payment credentials on file, the browser **detects the checkout page** and prompts a human-in-the-loop approval with the exact purchase details, every time.
- For new sites, Muse has a wallet for storing payment credentials. At launch the partner is **Stripe Link** (Shop Pay coming), and every payment issues a **single-use card number** passed to the merchant instead of the real card. The credential is tied to that merchant, that dollar amount, and a limited time window — stolen, it's nearly useless.
- Every one of these events gets a human-in-the-loop approval.

Full treatment in [08-paying-for-things](08-paying-for-things.md).

## The session problem

One honest operational wrinkle, observed from inside: the browser holds its logins in a persistent profile tied to a long-lived browser-task lineage. A fresh task starts with a blank cookie jar — sessions don't transfer. This is why X/Twitter work, for example, runs through one persistent lineage rather than fresh tasks. It's a usability consequence of the isolation: the thing that keeps sessions safe (they live in the broker's profile, not somewhere the agent can copy) also makes them non-portable.

## The one-line version

The agent gets a real browser with a screen reader's view of the web, no JavaScript, no credential visibility — and a user who can grab the wheel at any moment.
