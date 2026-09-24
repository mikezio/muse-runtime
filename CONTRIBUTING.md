# Contributing a runtime snapshot

If you run a Muse instance, you can archive its runtime here. Paste the prompt below into your Muse chat. It will inspect its own runtime, sanitize it and give you files to submit.

## The prompt

Copy everything in the block and paste it into your Muse:

```
Contribute a snapshot of your runtime to the muse-runtime archive
(github.com/mikezio/muse-runtime). Inspect your own runtime and produce
the following. Sanitize aggressively: no names, emails, addresses, phone
numbers, credentials, tokens, cookies or identifiers of any kind. Replace
usernames in paths with <user>. When in doubt, generalize or drop it.

1. home-tree.txt: your home directory structure, directory and file names
   only, no file contents. Prune personal subtrees (people, channels, user
   files, credentials, caches of personal data) to their top-level
   directory or remove them.

2. runtime-info.json: snapshot date, what the snapshot covers, and two
   lists: "observed" (things you directly verified) and "unknown" (things
   you cannot verify from inside). Mark every inference as an inference.

3. jobs.md: your scheduled jobs, one line each: purpose and schedule in
   generic terms. No user-specific details.

4. skills.md: your skills by name with a one-line description each.

Give me the four files as text I can copy into a pull request.
```

## Submitting

Open a PR adding your files under `snapshot/variants/<your-label>/`, where `<your-label>` is something generic like `instance-2026-09` (not your name). Different runtime variations are the point of the archive: if your file tree, jobs or skills differ from what's already here, that's exactly what we want.
