A filesystem snapshot of the Muse runtime at build 92c304f261 (built 2026-10-23T02:07:45Z). Personal files are excluded. The SHA-256 manifest and exclusion list are attached. See builds.md for the full build index.

---

## What changed vs build `9a4eb56798`

Build `92c304f261` (2026-10-23T02:07:45Z).
112 files changed (1 added, 0 removed, 111 modified) out of 18,541 archived.

### Binaries (`opt/bin/`, 101 changed)
- `aftership` (12.5 MB, +32,512 bytes)
- `asana` (12.7 MB, +27,424 bytes)
- `authdc` (38.3 MB → 38.4 MB)
- `avatar-media-generation` (38.3 MB → 38.4 MB)
- `box-cli` (14.9 MB, +21,360 bytes)
- `browser-broker` (37.8 MB → 37.9 MB)
- `browser-service` (38.3 MB → 38.4 MB)
- `calendly` (14.5 MB, +30,832 bytes)
- `canva` (12.9 MB, +23,584 bytes)
- `device-data` (38.3 MB → 38.4 MB)
- `dropbox` (12.9 MB, +28,384 bytes)
- `duffel` (14.6 MB, +44,280 bytes)
- `edits` (38.3 MB → 38.4 MB)
- `etsy-cli` (12.6 MB, +32,248 bytes)
- `evernote` (17.2 MB → 17.3 MB)
- `facebook-cli` (22.9 MB, +33,496 bytes)
- `feature-request` (38.3 MB → 38.4 MB)
- `figma` (12.7 MB → 12.8 MB)
- `flightaware` (15.0 MB, +19,936 bytes)
- `function-health` (14.4 MB, +19,304 bytes)
- `genui-display-render` (18.8 MB → 18.9 MB)
- `geocode` (38.3 MB → 38.4 MB)
- `ghl` (14.9 MB, +32,584 bytes)
- `github` (12.8 MB → 12.9 MB)
- `granola-cli` (12.5 MB → 12.6 MB)
- `hatch` (488.6 MB → 488.8 MB)
- `hatch-browser-lease-helper` (10.0 MB, +216 bytes)
- `hatch-doctor` (12.0 MB → 12.1 MB)
- `hatch-execd` (9.5 MB → 9.6 MB)
- `hatch-healthd` (8.9 MB, +2,216 bytes)
- `hatch-multicall` (38.3 MB → 38.4 MB)
- `hatch-rescue` (12.8 MB, +1,120 bytes)
- `hatch-rescue-systemctl` (2.3 MB, -5,432 bytes)
- `hatch-rescuectl` (8.3 MB, -4,344 bytes)
- `hatch-slide-style` (11.7 MB → 11.8 MB)
- `hatch-vault` (10.2 MB, -2,760 bytes)
- `hatch-ws-client` (16.3 MB → 16.5 MB)
- `hatch-zeitgeist` (14.8 MB, +19,248 bytes)
- `hatch_gws_auth` (11.9 MB → 12.0 MB)
- `hatch_gws_cli` (22.7 MB, +38,408 bytes)
- …and 61 more

### Product docs (`home/docs/`, 3 changed)
- `client-surfaces.md` (28.3 KB → 28.4 KB)
  - +7/-5 lines; sections: Settings
- `connectors.md` (10.2 KB → 10.4 KB)
  - +16/-12 lines; sections: Connection state: verify this turn
- `voice.md` (580 B → 574 B)
  - +6/-6 lines; sections: Voice

### Other (7 changed)
- `home/config/filesystem_watch_hashes.json`
  - +1/-1 lines
- `opt/connectors/instagram/CONNECTOR.md`
  - +6/-2 lines; sections: Manage saved posts, interests and the profile
- `opt/connectors/meta_catalog_search/manifest.yaml`
  - +18/-1 lines
- `opt/connectors/spotify/references/wearable-playback.md`
  - +1/-1 lines; sections: Resolve the item
- `opt/skills/spaces/ts-runtime/dist/probe-ctx.js`
- `opt/skills/spaces/ts-runtime/dist/probe-ui.js`
- `opt/skills/spaces/ts-runtime/worker/src/probe-ui-cli.ts`

### Added (1)
- `opt/skills/spaces/ts-runtime/dist/space-ts-deps/node_modules/@hatch/space-sdk/.bun-tag`

_Ephemeral runtime state rotated (10 db change-signal files, not meaningful)._

Full per-file hashes: see the attached manifest. Compare any two manifests locally with `python3 tools/compare-manifests.py before.manifest.txt after.manifest.txt`.
