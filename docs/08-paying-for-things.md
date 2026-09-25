# Paying for things

How Muse buys stuff on your behalf — the highest-friction flow in the runtime, because mistakes here cost real money.

## Two paths to checkout

**Sites where you already have payment credentials on file.** The browser detects that you're on a checkout page and triggers a human-in-the-loop approval with the exact details of the purchase — every time, no exceptions. The agent can't silently complete a purchase with a stored card; the moment of money always surfaces to you.

**Sites where you haven't shopped before.** Muse has a wallet for storing payment credentials compliantly. At launch the partner is **Stripe Link**, with Shop Pay on the way. When it's time to pay, the wallet issues a **single-use card number** — and that's what gets passed to the merchant's website, not your real card.

## The single-use card

This is the elegant part. The credential handed to the merchant is:

- **Tied to that particular merchant** — it doesn't work anywhere else.
- **Tied to a particular dollar amount** — it can't be charged for more.
- **Valid for a limited period of time** — it expires.

Even if the number were stolen — via prompt injection, a compromised merchant, any of the attack paths this repo documents — it would be nearly useless to the attacker. The blast radius of a leaked payment credential is engineered down to one merchant, one amount, one short window. Compare that to a leaked real card number, which is a blank check until you notice.

## Approval every time

Every payment event gets a **human-in-the-loop approval** — the same mechanism described in [03-sentinel](03-sentinel.md): the request goes directly to the Muse client, the dialog describes the exact action, the model never touches the decision, and the user's answer routes directly back to Sentinel. A confirmation covers exactly the action named; if the total, the items, or the merchant change afterward, the new version goes back for approval.

This is also why the purchase flow distinguishes wallet payments from merchant-saved cards: a saved card at the merchant is identified by its masked details and selected explicitly, while a wallet payment goes through the wallet's own approval card. Either way, spending requires the user's explicit approval through a native card — the agent can prepare a checkout down to the last detail, but it can't pay.

## Purchase protections

Muse is the first AI agent covered by **Link's purchase protections**: free coverage for damaged or lost items, price drops, no-fee returns, and a return guarantee on eligible purchases. 1Password support is on the way, so Muse can use logins a person already has. The direction is consistent: make the agent useful for commerce while making each individual transaction as low-risk as possible.

## Why this design

Payments concentrate every hard problem in agent safety into one flow: untrusted page content (the merchant's site), real credentials (your money), irreversible side effects (a charge), and an attacker incentive (stealing the card). The design answers each one:

- Untrusted content → the browser's classifier layer and accessibility-tree limits ([06-browser](06-browser.md)).
- Real credentials → single-use numbers, never the real card ([07-credentials](07-credentials.md)).
- Irreversible side effects → human approval with exact details, every time.
- Attacker incentive → merchant/amount/time-bound credentials that are worthless stolen.

No single layer is the defense. The combination is.

## The one-line version

The agent can fill your cart, but only you can pay — and the card it hands the merchant self-destructs.
