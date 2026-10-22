A filesystem snapshot of the Muse runtime at build 5990826e25 (built 2026-10-22T03:44:10Z). Personal files are excluded. The SHA-256 manifest and exclusion list are attached. See builds.md for the full build index.

---

## What changed vs build `994ca06e2d`

Build `5990826e25` (2026-10-22T03:44:10Z).
111 files changed (0 added, 0 removed, 111 modified) out of 18,534 archived.

### Binaries (`opt/bin/`, 101 changed)
- `aftership` (12.5 MB, +4,000 bytes)
- `asana` (12.7 MB, +3,632 bytes)
- `authdc` (38.0 MB → 38.1 MB)
- `avatar-media-generation` (38.0 MB → 38.1 MB)
- `box-cli` (14.8 MB, -712 bytes)
- `browser-broker` (37.9 MB → 37.8 MB)
- `browser-service` (38.0 MB → 38.1 MB)
- `calendly` (14.4 MB, +4,224 bytes)
- `canva` (12.8 MB, +9,336 bytes)
- `device-data` (38.0 MB → 38.1 MB)
- `dropbox` (12.9 MB, +9,240 bytes)
- `duffel` (14.5 MB, +8,344 bytes)
- `edits` (38.0 MB → 38.1 MB)
- `etsy-cli` (12.5 MB, +4,184 bytes)
- `evernote` (17.2 MB, +26,568 bytes)
- `facebook-cli` (22.8 MB, +33,576 bytes)
- `feature-request` (38.0 MB → 38.1 MB)
- `figma` (12.7 MB, +9,352 bytes)
- `flightaware` (14.9 MB, +8,032 bytes)
- `function-health` (14.3 MB → 14.4 MB)
- `genui-display-render` (18.8 MB, -1,648 bytes)
- `geocode` (38.0 MB → 38.1 MB)
- `ghl` (14.9 MB, +3,352 bytes)
- `github` (12.8 MB, +4,808 bytes)
- `granola-cli` (12.5 MB, +3,416 bytes)
- `hatch` (484.7 MB → 486.9 MB)
- `hatch-browser-lease-helper` (10.0 MB, +1,912 bytes)
- `hatch-doctor` (11.9 MB, +29,248 bytes)
- `hatch-execd` (9.5 MB, -39,008 bytes)
- `hatch-healthd` (8.9 MB, +2,872 bytes)
- `hatch-multicall` (38.0 MB → 38.1 MB)
- `hatch-rescue` (12.7 MB, -1,256 bytes)
- `hatch-rescue-systemctl` (2.3 MB, -96 bytes)
- `hatch-rescuectl` (8.3 MB, +1,144 bytes)
- `hatch-slide-style` (11.7 MB, +8,760 bytes)
- `hatch-vault` (10.2 MB, +544 bytes)
- `hatch-ws-client` (16.3 MB, +30,112 bytes)
- `hatch-zeitgeist` (14.8 MB, +4,192 bytes)
- `hatch_gws_auth` (11.9 MB, +3,488 bytes)
- `hatch_gws_cli` (22.6 MB → 22.7 MB)
- …and 61 more

### Product docs (`home/docs/`, 2 changed)
- `calls-texts-notifications.md` (8.6 KB → 9.0 KB)
  - +14/-9 lines; sections: Phone calls
- `client-surfaces.md` (28.2 KB → 28.3 KB)
  - +3/-2 lines; sections: Where users access Muse

### Other (8 changed)
- `home/assets/ideas/new-user/catalog.json`
- `home/config/filesystem_watch_hashes.json`
  - +1/-1 lines
- `opt/assets/ideas/new-user/catalog.json`
- `opt/runtime-cell/bin-scopes.conf`
- `opt/runtime-cell/connector-scopes.conf`
- `opt/workflow-skills/muse-feedback/SKILL.md`
  - +6/-4 lines; sections: Filing
- `opt/workflow-skills/muse_db/references/schema.md`
  - +1/-1 lines; sections: PostgreSQL schema for `muse.db`
- `opt/workflow-skills/muse_db/references/tables/runtime.browser_tasks.md`
  - +4/-0 lines; sections: Columns

_Ephemeral runtime state rotated (4 db change-signal files, not meaningful)._

Full per-file hashes: see the attached manifest. Compare any two manifests locally with `python3 tools/compare-manifests.py before.manifest.txt after.manifest.txt`.
