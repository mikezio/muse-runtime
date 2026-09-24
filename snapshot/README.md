# Snapshot: the closest thing to seeing the backend

This directory is regenerated from a live Muse instance on a schedule. Check `runtime-info.json` for the snapshot date.

## What's here

- **`home-tree.txt`** - sanitized map of the instance's home directory. Names only. Personal subtrees (people, channels, user files, credentials, caches of personal data) are pruned to their top-level directory or removed. No file contents.
- **`runtime-info.json`** - when the snapshot was taken and what it covers.
- **`heartbeat-template.md`** - a generic, illustrative version of the background checklist. Not any user's real checklist, but the shape of one.
- **`sample-cron-job.md`** - what a scheduled job definition looks like, with a generic example.
- **`skill-anatomy.md`** - the anatomy of a skill, the unit of capability.

## How it's generated

`tools/snapshot.sh` walks the home directory with `find`, prunes personal subtrees, strips caches/venvs/locks/cookies and writes the tree. Nothing leaves the machine except directory names. The refresh runs weekly via the instance's own scheduler and pushes here when the tree changes.
