---
id: muse-runtime-snapshot-refresh
title: Muse runtime repo weekly snapshot refresh
enabled: true
mode: task
schedule:
  kind: weekly
  timezone: '@user.current'
  time: 03:52:00
  dow: [Sun]
metadata:
  tags: [cron:flexible-time]
  originating_channel_context_json: '[REDACTED]'
  presentation_locale: en-US
---
Refresh the public muse-runtime repo's live snapshot.

1. Run ~/workspace/muse-runtime/tools/snapshot.sh to regenerate snapshot/home-tree.txt and snapshot/runtime-info.json.
2. In ~/workspace/muse-runtime, run git status --short. If nothing changed, end with "snapshot unchanged" and do nothing else.
3. Before committing, eyeball the diff (git diff --stat): confirm no personal data slipped in. The script prunes personal subtrees, but if a new unexpected top-level directory appeared, stop and report it instead of committing.
4. If the snapshot changed and is clean: git add snapshot/, commit with message "snapshot: weekly refresh YYYY-MM-DD", push to origin main.
5. Final message: what changed and whether the push succeeded. Stay quiet on success beyond one line.
