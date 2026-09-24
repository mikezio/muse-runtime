# What a cron job definition looks like

A scheduled job is a timetable plus a self-contained instruction body. The worker that wakes up has no conversation context, so the body carries everything it needs. Generic example:

```yaml
id: weekday-evening-checkin
schedule: "0 18 * * 1-5"        # 6 PM, weekdays (cron expression)
timezone: America/New_York
body: |
  1. Read ~/memory/attendance.json for today's arrival/departure.
  2. If no arrival detected by 8:30 AM, ask the user for their
     actual start time instead of assuming.
  3. Otherwise fill the day's timesheet hours (8:00-17:00, 1h lunch)
     per standing rules and log the entry.
  4. Report what was entered, or what is blocked and why.
  Never invent hours. A missing record is a question, not a zero.
```

Real instances carry dozens of these: morning briefings, polls, deadline nags, cleanup sweeps, session-health checks. The definitions live in the native scheduler; human-readable review copies live in the workspace.

## The rules around jobs

- **Staleness guard first.** The body compares its scheduled time against the actual time. If the gap is too big (missed fire, VM was down), it no-ops instead of acting late.
- **Pending until proven.** A job is not "live" until one full successful run has been observed end to end.
- **Final message = delivery.** A worker's run report is the handoff. No "someone else will deliver this."
