A filesystem snapshot of the Muse runtime at build 8b82da8f82 (built 2026-10-22T05:06:41Z). Personal files are excluded. The SHA-256 manifest and exclusion list are attached. See builds.md for the full build index.

---

## What changed vs build `5990826e25`

Build `8b82da8f82` (2026-10-22T05:06:41Z).
106 files changed (0 added, 0 removed, 106 modified) out of 18,534 archived.

### Binaries (`opt/bin/`, 100 changed)
- `aftership` (12.5 MB, +728 bytes)
- `asana` (12.7 MB, +728 bytes)
- `authdc` (38.1 MB → 38.2 MB)
- `avatar-media-generation` (38.1 MB → 38.2 MB)
- `box-cli` (14.8 MB → 14.9 MB)
- `browser-broker` (37.8 MB → 37.9 MB)
- `browser-service` (38.1 MB → 38.2 MB)
- `calendly` (14.4 MB, +728 bytes)
- `canva` (12.8 MB, +1,880 bytes)
- `device-data` (38.1 MB → 38.2 MB)
- `dropbox` (12.9 MB, +728 bytes)
- `duffel` (14.5 MB, +3,032 bytes)
- `edits` (38.1 MB → 38.2 MB)
- `etsy-cli` (12.5 MB, +728 bytes)
- `evernote` (17.2 MB, +5,280 bytes)
- `facebook-cli` (22.8 MB → 22.9 MB)
- `feature-request` (38.1 MB → 38.2 MB)
- `figma` (12.7 MB, +728 bytes)
- `flightaware` (14.9 MB, +728 bytes)
- `function-health` (14.4 MB, +728 bytes)
- `genui-display-render` (18.8 MB, +1,056 bytes)
- `geocode` (38.1 MB → 38.2 MB)
- `ghl` (14.9 MB, +728 bytes)
- `github` (12.8 MB, +4,824 bytes)
- `granola-cli` (12.5 MB, +728 bytes)
- `hatch` (486.9 MB → 487.1 MB)
- `hatch-browser-lease-helper` (10.0 MB, +136 bytes)
- `hatch-doctor` (11.9 MB, +416 bytes)
- `hatch-execd` (9.5 MB, -928 bytes)
- `hatch-healthd` (8.9 MB, +376 bytes)
- `hatch-multicall` (38.1 MB → 38.2 MB)
- `hatch-rescue` (12.7 MB, -8,160 bytes)
- `hatch-slide-style` (11.7 MB, +728 bytes)
- `hatch-ws-client` (16.3 MB, +2,624 bytes)
- `hatch-zeitgeist` (14.8 MB, +728 bytes)
- `hatch_gws_auth` (11.9 MB, +728 bytes)
- `hatch_gws_cli` (22.7 MB, +1,568 bytes)
- `hatch_messenger_cli` (19.4 MB, +1,184 bytes)
- `health-cli` (23.4 MB, +1,120 bytes)
- `healthex` (14.3 MB, +4,824 bytes)
- …and 60 more

### Other (6 changed)
- `home/config/filesystem_watch_hashes.json`
  - +1/-1 lines
- `home/config/recent-skills.json`
  - +2/-1 lines
- `opt/connectors/duffel/CONNECTOR.md`
  - +2/-2 lines; sections: Validate and book
- `opt/runtime-cell/launch-daemon.sh`
  - +16/-0 lines; sections: Image support is independent of the product gate. Older images, The service's existing private mount namespace confines this config overlay, intact: --settings=override would discard a command-line --bind-ro addition., just like the scoped-content overlays below; the installed file never changes.
- `opt/runtime-cell/pre-start.sh`
  - +6/-2 lines; sections: Read-only publication mount points INSIDE the home (assets, .pki/nssdb, and, The private upload mask is attached below the bridge before cell startup and, fail-open for assets availability, but are recorded separately from the overall, is included in the later RV home tree. The real staging directory's unmapped
- `opt/workflow-skills/muse_db/references/schema.md`
  - +1/-1 lines; sections: PostgreSQL schema for `muse.db`

_Ephemeral runtime state rotated (4 db change-signal files, not meaningful)._

Full per-file hashes: see the attached manifest. Compare any two manifests locally with `python3 tools/compare-manifests.py before.manifest.txt after.manifest.txt`.
