# Heartbeat checklist (illustrative template)

This is the *shape* of the background checklist a Muse instance works through every ~30 minutes. Real checklists are tailored to the user; this one shows the structure.

```
- Read the user's proactive preferences first. Standing prefs never
  override a live instruction.
- Check recent cron runs (last 48h) for failures. Diagnose and fix
  what you can; file a repair proposal with evidence for the rest.
- Look one hour ahead. Prep anything time-sensitive now.
- Session health: if a login the agent depends on is dead, or something
  needs the user (a code, an approval, a decision), surface it.
  Otherwise stay quiet.
- Keep helper daemons alive: check, restart, verify.
- Work the improvement queue: one real fix, verified, recorded.
- End with a report using exact outcome words per check:
  checked / no_findings / skipped (reason) / read_failed (blocker)
  / blocked (what is needed).
- A quiet tick with verified checks is a fine tick.
```

## The dedupe layer underneath

Every finding flows through a state helper so the user never gets nagged about the same thing every 30 minutes:

- **observe** - record what was seen. Never retries, never advances backoff.
- **attempt** - record a repair try under a stable operation id. Replays are idempotent.
- **report** - reserve one surfacing with a content fingerprint. Identical findings stay silent.
- **resolve** - close only on observed resolution.

Backoff between retries grows (1h, 4h, 12h, 24h cap). The helper owns atomic writes.
