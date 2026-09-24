# Scheduler

The agent is not thinking between conversations. The scheduler is what makes it seem alive: it wakes the agent on a timetable, the agent does a bounded piece of work, writes down the result, and sleeps again.

## Cron jobs

Scheduled work is managed through native cron tooling (create, list, update, remove, run-now, history). A job definition has:

- **A schedule**: daily/weekly times, intervals, or one-shot runonce jobs.
- **A body**: the instructions the worker follows when the job fires. Bodies are written to be self-contained — the worker that wakes up has the full context it needs.
- **Ownership**: jobs can belong to a user goal (a goal-owned check-in or reminder) or stand alone.

Typical jobs on a lived-in instance: morning briefings, commute/arrival polls, evening timesheet check-ins, weekly deadline nags, nightly cleanup sweeps, periodic session-health checks.

### Lessons from the field

- **Dispatch is not execution.** A scheduler firing and handing off work does not prove the work happened. Each side — scheduling and execution — needs its own proof.
- **Staleness guards.** A job that fires late (after a VM restart, a scheduler catch-up) must compare its *scheduled* time against the *actual* time and no-op if the gap is suspicious. Without this, a missed 6:30 AM alarm can fire at 3 AM and wake a household. This exact failure happened; the guard was added the same day.
- **Schedules are pending until proven.** A job definition existing proves nothing. The rule: never call an automation "live" until one full successful run has been observed end to end.
- **A worker's final message is the delivery.** Background workers cannot tap the user on the shoulder. Their run's final report *is* the handoff. A run that ends with "the main agent must deliver this" instead of the message itself has failed at its one job.

## The heartbeat

One special job runs about every 30 minutes and works through a standing checklist (`HEARTBEAT.md`). A quiet tick with verified checks is a fine tick. The checklist covers:

1. **Read the user's proactive preferences first.** Standing preferences scope what may interrupt the user; the user's latest explicit instruction beats any stored text.
2. **Check recent cron runs for failures.** Failing jobs get diagnosed and fixed if possible, otherwise a concrete repair proposal with evidence.
3. **Look ahead one hour.** Anything time-sensitive gets prepped or started now.
4. **Session health.** If a login session the agent depends on is dead, or something needs the user's input (a code, an approval), surface it — otherwise stay quiet.
5. **Keep the lights on.** Verify helper daemons are running (device links, CLI shims); restart what died.
6. **Work the improvement queue.** At least once a day when a tick has capacity, take the highest-value queued improvement, do it, verify the actual result, record the outcome.
7. **End with a report.** Exact outcome words per check: `checked`, `no_findings`, `skipped` (with reason), `read_failed` (with blocker), `blocked` (with what is needed).

### Dedupe and issue state

A tick must not nag the user about the same thing every 30 minutes. Every finding flows through a small state helper with verbs like `observe`, `attempt`, `report`, `resolve`:

- **Observe** records what was seen. It never retries, never advances backoff.
- **Attempt** records a repair try under a stable operation id, making replays idempotent.
- **Report** reserves a single surfacing with a content fingerprint, so identical findings do not re-notify.
- **Resolve** closes the issue only on observed resolution.

Backoff between retries grows (1h, 4h, 12h, 24h cap). The helper owns atomic writes and never hand-edits its JSON.

## Hooks vs cron

- **Cron** fires on the clock: reminders, polls, cleanups.
- **Hooks** fire on events: a message arriving, data landing from a connected source. A hook is a small script that watches and acts the moment the event arrives.

Use cron for "every weekday at 6 PM", hooks for "the instant this happens."

## Workers and subagents

Long or multi-step work gets delegated to subagents that run in the background while the main conversation stays responsive. Rules that keep this sane:

- Truly independent tasks fan out in parallel; a coordinator fans out further when needed.
- A subagent inherits the parent's context, so briefs stay short: task, outcome, constraints.
- Results arrive as handoffs; the parent never polls in a loop.
- Irreversible actions are never retried blindly. If the outcome is unknown, the agent investigates before repeating.
