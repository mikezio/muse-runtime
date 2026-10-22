A filesystem snapshot of the Muse runtime at build f181c0d811 (built 2026-10-22T18:57:22Z). Personal files are excluded. The SHA-256 manifest and exclusion list are attached. See builds.md for the full build index.

---

## What changed vs build `940f1a8368`

Build `f181c0d811` (2026-10-22T18:57:22Z).
119 files changed (4 added, 1 removed, 114 modified) out of 18,540 archived.

### Binaries (`opt/bin/`, 99 changed)
- `aftership` (12.5 MB, -320 bytes)
- `asana` (12.7 MB, -256 bytes)
- `authdc` (38.3 MB, +256 bytes)
- `avatar-media-generation` (38.3 MB, +256 bytes)
- `box-cli` (14.9 MB, -224 bytes)
- `browser-broker` (37.9 MB → 37.8 MB)
- `browser-service` (38.3 MB, +256 bytes)
- `calendly` (14.5 MB, -320 bytes)
- `canva` (12.9 MB, -256 bytes)
- `device-data` (38.3 MB, +256 bytes)
- `dropbox` (12.9 MB, -320 bytes)
- `duffel` (14.6 MB, -320 bytes)
- `edits` (38.3 MB, +256 bytes)
- `etsy-cli` (12.6 MB, -256 bytes)
- `evernote` (17.2 MB, -256 bytes)
- `facebook-cli` (22.9 MB, +8,976 bytes)
- `feature-request` (38.3 MB, +256 bytes)
- `figma` (12.7 MB, -320 bytes)
- `flightaware` (15.0 MB, -256 bytes)
- `function-health` (14.4 MB, -256 bytes)
- `genui-display-render` (18.8 MB, +256 bytes)
- `geocode` (38.3 MB, +256 bytes)
- `ghl` (14.9 MB, -320 bytes)
- `github` (12.8 MB, -320 bytes)
- `granola-cli` (12.5 MB, -320 bytes)
- `hatch` (488.6 MB, -16,032 bytes)
- `hatch-browser-lease-helper` (10.0 MB, -128 bytes)
- `hatch-doctor` (12.0 MB, +256 bytes)
- `hatch-execd` (9.6 MB → 9.5 MB)
- `hatch-healthd` (8.9 MB, +32 bytes)
- `hatch-multicall` (38.3 MB, +256 bytes)
- `hatch-rescue` (12.8 MB, +408 bytes)
- `hatch-rescue-systemctl` (2.3 MB, +96 bytes)
- `hatch-rescuectl` (8.3 MB, +32 bytes)
- `hatch-slide-style` (11.7 MB, -4,416 bytes)
- `hatch-vault` (10.2 MB, +152 bytes)
- `hatch-ws-client` (16.3 MB, -1,712 bytes)
- `hatch-zeitgeist` (14.8 MB, -256 bytes)
- `hatch_gws_auth` (11.9 MB, -320 bytes)
- `hatch_gws_cli` (22.7 MB, -320 bytes)
- …and 59 more

### Other (15 changed)
- `home/config/filesystem_watch_hashes.json`
  - +1/-1 lines
- `opt/connectors/facebook_cli/CONNECTOR.md`
  - +21/-21 lines; sections: Feature guides, Find people, Open Facebook links, Present results
- `opt/connectors/facebook_cli/references/feed.md`
  - +20/-12 lines; sections: Facebook feeds, Present a feed, References
- `opt/connectors/facebook_cli/references/friends.md`
  - +19/-46 lines; sections: Explain a match, Facebook friends, Search by name or profile details
- `opt/connectors/facebook_cli/references/groups.md`
  - +73/-25 lines; sections: Facebook groups, Read Group posts, Read a group's details, Search groups
- `opt/connectors/facebook_cli/references/pages.md`
  - +18/-109 lines; sections: Continue a list, Facebook Pages, Find a Page, Handle consent and access
- `opt/connectors/facebook_cli/references/saved.md`
  - +32/-23 lines; sections: Facebook saved items, Find saved content, Read the saved content, Save or remove an item
- `opt/connectors/facebook_cli/references/shopping-links.md`
  - +1/-1 lines; sections: Shop a Facebook Reel
- `opt/connectors/facebook_cli/references/timeline.md`
  - +2/-2 lines; sections: Facebook timelines, Present the posts
- `opt/connectors/onepassword/CONNECTOR.md`
  - +14/-0 lines; sections: When 1Password can be used
- `opt/connectors/spotify/manifest.yaml`
  - +1/-0 lines
- `opt/connectors/spotify/references/wearable-playback.md`
  - +2/-0 lines; sections: Play on the requested device
- `opt/workflow-skills/style-tryon/SKILL.md`
- `opt/workflow-skills/style-tryon/references/flow.md`
- `opt/workflow-skills/style-tryon/skill.yaml`

### Added (4)
- `opt/connectors/facebook_cli/references/pages-insights.md`
- `opt/connectors/facebook_cli/references/pages-publishing.md`
- `opt/connectors/facebook_cli/references/reading-posts.md`
- `opt/connectors/facebook_cli/references/writing-posts.md`

### Removed (1)
- `opt/connectors/facebook_cli/references/posts.md`

_Ephemeral runtime state rotated (6 db change-signal files, not meaningful)._

Full per-file hashes: see the attached manifest. Compare any two manifests locally with `python3 tools/compare-manifests.py before.manifest.txt after.manifest.txt`.
