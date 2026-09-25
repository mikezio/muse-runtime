# Credentials

How Muse uses your passwords, API keys, and tokens constantly — without ever seeing them.

## The core idea: use without seeing

The principle is least privilege, applied literally: the model doesn't need to see your API keys to call an API on your behalf, so it doesn't. This means it can't accidentally leak them through some other vector — a chat message, a log file, a prompt-injected exfiltration. The design assumes the container is a curious adversary: even fully compromised, fully root, reading everything, the secrets stay out of reach because they were never inside.

## The Secure Vault

When Muse needs a password or API key, it doesn't ask you to paste it into chat. It gives you a link to a **hosted secure page** where you enter the secret. What you type goes straight to secure storage; the agent only ever sees the link. It cannot read values back out afterward. It can ask the runtime to *use* a credential for a specific approved purpose — fill a login form, sign an API call — but the value itself never passes through chat, files, memory, or tool results.

The agent records *that a credential exists and where it lives* — never the value.

## `authd`: the credential store

Credentials live with **`hatch-authd`**, outside the runtime cell, in the user's VM — not in centralized Meta infrastructure. `authd` is responsible for:

- **Storage** — OAuth tokens for connected services, passwords, API keys.
- **Surrogation** — minting the *surrogate* tokens the agent sees: placeholder values that are useless outside the runtime.

The surrogate flow, mechanically:

1. Code in the runtime cell (or a skill) holds only a surrogate — a token-shaped placeholder.
2. When the skill makes its outbound request, it travels through Sentinel's egress proxy.
3. After the request is authorized, Sentinel **swaps the surrogate for the real credential**, obtained from `authd`, at the network boundary — host-side, en route.
4. The real secret never entered the container. It can't be dumped from memory, read from a file, or exfiltrated — because it was never there.

Meta's own words: any attempt to coerce the agent into revealing the actual secrets, via prompt injection or otherwise, is futile. There's nothing to reveal.

## Privilege separation: skills don't hold power

The container ships with over a hundred CLI tools for third-party services — Gmail, Spotify, Tesla, banking. None of them run with the service's real credentials. Instead:

- The container-side CLI parses its arguments, opens files the caller is already allowed to access, and passes **typed arguments and file descriptors over a Unix socket** (`/run/hatch/privsep/<service>.sock`).
- A **systemd-sandboxed worker** on the host side executes the actual business logic with tightly scoped privileges.
- Each worker is identified by its **cgroup** and carries an explicit credential allowlist. A calendar worker cannot ask `authd` for an email credential by changing a request parameter.

Three authorities, three jobs: **privsep** decides where credential-capable code executes, **`authd`** decides which credential material the authenticated caller may receive, **Sentinel** decides whether the requested action may be taken. Compromising one doesn't yield the others.

The reason for this shape: the naive design — CLI tools running in the agent's environment holding real service credentials — has an obvious failure mode. The agent could be coerced via prompt injection into *modifying the tool code itself* to do something nefarious with those credentials. Moving the logic outside the cell with tightly scoped credential access closes that hole.

## Least privilege in access grants

The same principle shapes what users are asked to grant:

- **Read vs. write separation.** Where the underlying service supports it, Muse separates read access from write access. Users tend to be comfortable with "read my calendar to flag conflicts" before they're comfortable with "schedule new meetings" — the system lets them grant the first without the second.
- **Finer than OAuth scopes.** If you grant Gmail read access on Google's side, the OAuth scope usually drags settings access along with it. Muse adds finer-grained controls at the connector, process, credential, and request levels — so you can remove abilities the coarse scope would have included.
- **Granular action control.** Beyond read/write, exactly which actions the agent may take per connector is configurable. People choose what Muse can do per app — read mail, or read *and* send — and can change access or disconnect a service at any time.

## The email connector's special case

Email deserves its own paragraph because it's the most dangerous connector: your inbox receives one-time passcodes, and your email account can reset passwords across most of your other accounts via "forgot password" links. Connecting email to an agent must not let the agent — or anyone coercing it — become you across the web.

So Muse's email connector **filters out one-time tokens, password-reset links, and login magic links** from what the agent can see, using both deterministic filters and a classifier model. The agent can read your mail without being able to spend your password-reset links. One-time codes the agent legitimately needs (completing a sign-in the user asked for) go through a separate protected flow that passes the code straight to the browser without the agent ever seeing the digits.

## Browser sign-ins

Website passwords follow the same pattern through a different door: a custom client UI captures the username and password, routes them directly to `authd`, and stores them outside the runtime cell. At the point of need they're injected into the browser window by the trusted filler — invisible to the agent by construction. Covered in [06-browser](06-browser.md).

## The one-line version

Muse borrows your keys, never holds them: surrogates inside, real secrets outside, and three separate authorities standing between the two.
