A filesystem snapshot of the Muse runtime at build 0bf1debf76 (built 2026-10-23T07:21:49Z). Personal files are excluded. The SHA-256 manifest and exclusion list are attached. See builds.md for the full build index.

---

## What changed vs build `c6187b72fc`

Build `0bf1debf76` (2026-10-23T07:21:49Z).
9 files changed (0 added, 0 removed, 9 modified) out of 18,541 archived.

### Binaries (`opt/bin/`, 8 changed)
- `hatch` (490.2 MB → 490.4 MB)
- `hatch-execd` (9.6 MB, -4,096 bytes)
- `browser-broker` (rebuilt, same size)
- `hatch-healthd` (rebuilt, same size)
- `hatch-rescue` (rebuilt, same size)
- `hatch-rescuectl` (rebuilt, same size)
- `hatch-vault` (rebuilt, same size)
- `spawnd` (rebuilt, same size)

### Other (1 changed)
- `opt/workflow-skills/muse_db/references/schema.md`
  - +1/-1 lines; sections: PostgreSQL schema for `muse.db`

_Ephemeral runtime state rotated (2 db change-signal files, not meaningful)._

Full per-file hashes: see the attached manifest. Compare any two manifests locally with `python3 tools/compare-manifests.py before.manifest.txt after.manifest.txt`.
