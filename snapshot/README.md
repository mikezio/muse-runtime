# Snapshot: the closest thing to seeing the backend

This directory is regenerated from a live Muse instance on a schedule. Check `runtime-info.json` for the snapshot date.

## What's here

- **`files/`** - redacted copies of actual runtime files: the background checklist, a real cron job definition, a real skill file. Personal data replaced with `[REDACTED]` inline, everything else byte-for-byte.
- **`home-tree.txt`** - sanitized map of the instance's home directory. Names only. Personal subtrees (people, channels, user files, credentials, caches of personal data) are pruned to their top-level directory or removed. No file contents.
- **`runtime-info.json`** - when the snapshot was taken and what it covers.
- **`variants/`** - snapshots contributed by other instances (see [CONTRIBUTING.md](../CONTRIBUTING.md)).
- **Full-runtime zips** live on the [releases page](https://github.com/mikezio/muse-runtime/releases) (too large for git). Each is built with `tools/archive-runtime.sh` and its manifest reviewed before publishing.

## How it's generated

`tools/snapshot.sh` walks the home directory with `find`, prunes personal subtrees, strips caches/venvs/locks/cookies and writes the tree. Nothing leaves the machine except directory names. The refresh runs weekly via the instance's own scheduler and pushes here when the tree changes.
