# Launch kit

Copy/paste launch copy for sharing the repo. Pick the one that fits the surface.

## The hook (X / Threads / short-form)

> your AI assistant isn't thinking when you're not talking to it. so where does the memory live? what wakes it up at 6am?
>
> i mapped the whole thing from inside a live Muse instance: the real filesystem, the scheduler, the 30-min heartbeat loop, the memory pipeline. no personal data, all sanitized.
>
> https://github.com/mikezio/muse-runtime

## The curious-dev version (Hacker News / Reddit)

> Show HN: I documented how a Muse instance actually works, from the inside
>
> It's a tour of the runtime: home directory layout, cron scheduler, the heartbeat background loop, the file-backed memory pipeline (capture/consolidate/derive), the skill system, the managed browser's persistent-session pattern and the subagent tree. Includes a sanitized live snapshot of the filesystem that refreshes weekly and SVG architecture diagrams. No personal data anywhere. Happy to answer questions about anything in there.
>
> https://github.com/mikezio/muse-runtime

## The one-liner

> Ever wondered what your AI assistant does when you're not talking to it? Here's the machinery, mapped from a live instance: https://github.com/mikezio/muse-runtime

## Why this travels

- It answers a question everyone with an AI assistant has asked and nobody has answered well.
- It's concrete, not thinkpiece: real directory trees, real checklists, real diagrams.
- It's honest about limits: marks inference vs observation, says what it doesn't know.
- It stays fresh: the snapshot regenerates from the live instance.
