A filesystem snapshot of the Muse runtime at build 8f5a4fa6cb (built 2026-10-21T23:15:42Z). Personal files are excluded. The SHA-256 manifest and exclusion list are attached. See builds.md for the full build index.

---

## What changed vs build `955c893682`

Build `8f5a4fa6cb` (2026-10-21T23:15:42Z).
118 files changed (0 added, 0 removed, 118 modified) out of 18,534 archived.

### Binaries (`opt/bin/`, 100 changed)
- `aftership` (12.4 MB, +9,768 bytes)
- `asana` (12.6 MB, +5,736 bytes)
- `authdc` (37.9 MB, +13,056 bytes)
- `avatar-media-generation` (37.9 MB, +13,056 bytes)
- `box-cli` (14.8 MB, +5,488 bytes)
- `browser-broker` (37.8 MB, +71,840 bytes)
- `browser-service` (37.9 MB, +13,056 bytes)
- `calendly` (14.4 MB, +5,216 bytes)
- `canva` (12.7 MB, +5,536 bytes)
- `device-data` (37.9 MB, +13,056 bytes)
- `dropbox` (12.8 MB, +16,208 bytes)
- `duffel` (14.4 MB, +23,288 bytes)
- `edits` (37.9 MB, +13,056 bytes)
- `etsy-cli` (12.5 MB, +10,096 bytes)
- `evernote` (17.1 MB, +20,608 bytes)
- `facebook-cli` (22.7 MB, +19,872 bytes)
- `feature-request` (37.9 MB, +13,056 bytes)
- `figma` (12.6 MB, +9,456 bytes)
- `flightaware` (14.9 MB, +5,920 bytes)
- `function-health` (14.3 MB, +4,064 bytes)
- `genui-display-render` (18.7 MB, +7,472 bytes)
- `geocode` (37.9 MB, +13,056 bytes)
- `ghl` (14.8 MB, +8,416 bytes)
- `github` (12.7 MB, +9,624 bytes)
- `granola-cli` (12.4 MB, +9,520 bytes)
- `hatch` (480.5 MB → 483.3 MB)
- `hatch-browser-lease-helper` (10.0 MB, -5,448 bytes)
- `hatch-doctor` (11.8 MB, +2,528 bytes)
- `hatch-execd` (9.5 MB, +6,176 bytes)
- `hatch-healthd` (8.9 MB, -1,816 bytes)
- `hatch-multicall` (37.9 MB, +13,056 bytes)
- `hatch-rescue` (12.7 MB, -1,688 bytes)
- `hatch-rescue-systemctl` (2.3 MB, -2,024 bytes)
- `hatch-rescuectl` (8.3 MB, -1,808 bytes)
- `hatch-slide-style` (11.6 MB, +80,832 bytes)
- `hatch-vault` (10.2 MB, -6,320 bytes)
- `hatch-ws-client` (16.3 MB, +37,000 bytes)
- `hatch-zeitgeist` (14.7 MB, +8,184 bytes)
- `hatch_gws_auth` (11.8 MB, +12,048 bytes)
- `hatch_gws_cli` (22.5 MB, +30,632 bytes)
- …and 60 more

### Product docs (`home/docs/`, 2 changed)
- `whatsapp.md` (3.6 KB, -71 bytes)
  - +4/-5 lines
- `payments-and-purchases.md` (8.0 KB → 10.1 KB)
  - +45/-11 lines; sections: Assign the purchase, Cart and payment decisions, Changes and uncertain outcomes

### Other (16 changed)
- `home/assets/avatar/reference/call-portrait-specs.json`
  - +2/-0 lines
- `home/config/filesystem_watch_hashes.json`
  - +1/-1 lines
- `opt/connectors/duffel/CONNECTOR.md`
  - +1/-1 lines; sections: Validate and book
- `opt/connectors/healthex/CONNECTOR.md`
  - +18/-7 lines; sections: Connect, Handle incomplete responses, HealthEx
- `opt/connectors/shop-pay/CONNECTOR.md`
  - +1/-1 lines; sections: Pay
- `opt/connectors/stripe-link/CONNECTOR.md`
  - +4/-2 lines; sections: Check spending limits, Check that Link fits the checkout, Pay
- `opt/skills/booking/references/browser-booking.md`
  - +2/-2 lines; sections: Run one checkout
- `opt/skills/booking/references/checkout.md`
  - +2/-2 lines; sections: Collect details safely
- `opt/skills/spaces/ts-runtime/dist/playwright-audit.js`
- `opt/skills/spaces/ts-runtime/dist/probe-ui.js`
- `opt/skills/spaces/ts-runtime/worker/src/playwright-audit.ts`
- `opt/skills/spaces/ts-runtime/worker/src/probe-ui-cli.ts`
- `opt/workflow-skills/custom-connector-setup/SKILL.md`
  - +3/-1 lines; sections: Connect the credential, Verify before saving
- `opt/workflow-skills/custom-connector-setup/templates/connector/CONNECTOR.md`
  - +3/-2 lines
- `opt/workflow-skills/generate_podcast/references/publishing.md`
- `opt/workflow-skills/generate_podcast/scripts/podcast-helper`

_Ephemeral runtime state rotated (16 db change-signal files, not meaningful)._

Full per-file hashes: see the attached manifest. Compare any two manifests locally with `python3 tools/compare-manifests.py before.manifest.txt after.manifest.txt`.
