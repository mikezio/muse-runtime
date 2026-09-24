# Contributing a runtime snapshot

If you run a Muse instance, archive its actual runtime files here. Not a summary: copies of the real files, with personal data redacted inline as `[REDACTED]`. Everything else stays byte-for-byte.

## The prompt

Copy everything in the block and paste it into your Muse:

```
Contribute your actual runtime files to the muse-runtime archive
(github.com/mikezio/muse-runtime). I want copies of the real files, not
summaries. For each file below, copy it exactly, replacing personal data
inline with [REDACTED]: names, emails, addresses, phone numbers, account
handles, credentials, tokens, cookies, device ids, locations. Keep all
structure, wording, schedules and mechanics unchanged. When unsure whether
something is personal, redact it.

Copy these:

1. Your background checklist file (the one a scheduled worker runs through
   every tick). Save as HEARTBEAT.md.

2. Two or three of your scheduled job definitions: the full frontmatter
   (id, title, schedule) plus the complete instruction body. Save each as
   cron-job-<short-name>.md. Pick jobs that show different patterns (a
   poll, a reminder, a maintenance sweep).

3. Two or three of your skill files (SKILL.md), ideally ones that differ
   from what's already in the archive. Save each as SKILL-<name>.md.

4. If you have a memory pipeline (capture/consolidate/derive jobs or
   scripts), include one redacted sample of each stage's definition.

Then give me the files as text I can copy into a pull request, and a
short note on anything your runtime does that the archive doesn't show.
```

## Submitting

Open a PR adding your files under `snapshot/variants/<your-label>/`, where `<your-label>` is generic (like `instance-2026-09`, not your name). Before submitting, search your files for anything you missed: names, places, account details. Different runtime variations are the point of the archive.
