# Contributing a runtime snapshot

If you run a Muse instance, archive its actual runtime here. The contribution is a sanitized zip of the instance's filesystem: everything that ships with a fresh runtime, with personal data removed. Not a summary, the real files.

## The prompt

Copy everything in the block and paste it into your Muse:

```
Contribute a sanitized archive of your runtime to the muse-runtime project
(github.com/mikezio/muse-runtime). Fetch the archiver script and run it:

curl -sSL https://raw.githubusercontent.com/mikezio/muse-runtime/main/tools/archive-runtime.sh -o /tmp/archive-runtime.sh && bash /tmp/archive-runtime.sh --out .

Read the script before running it. It copies your home directory and
built-in skills into a staging area, excluding personal data: memory
files, user files, credentials, tokens, cookies, caches, logs, and
anything matching *credential* / *secret* / *token*. When in doubt it
excludes.

After it runs, review runtime-archive-<date>.manifest.txt yourself: search
it for your name, email, addresses, account handles, or anything you
wouldn't publish. If you find anything, say what it is so the script's
exclude list can be improved.

Give me the zip and the manifest, plus a short note on anything your
runtime does that the archive doesn't show.
```

## Submitting

Attach the zip to a [new release](https://github.com/mikezio/muse-runtime/releases/new) named `runtime-archive-YYYY-MM-DD` and open an issue linking it, or open a PR adding the manifest under `snapshot/variants/<your-label>/` with a link to where the zip is hosted. Use a generic label (like `instance-2026-09`), not your name. Different runtime variations are the point of the archive: if your file tree or skills differ from what's already here, that's exactly what we want.
