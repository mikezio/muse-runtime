# Build archive

Every Meta runtime image this instance has run, with a sanitized archive of
the full runtime (home dir + /opt/hatch, personal files excluded) per build.
Archives ship as GitHub release assets, never as git blobs.

New rows are appended automatically when a new build is detected. Each
archive is a snapshot of the live instance running that build, not a
pristine Meta image.

| build | built (UTC) | detected (EDT) | archive |
|---|---|---|---|
| `10ba995fed7` | 2026-09-24T04:05:12Z | 2026-09-24 | n/a (predates per-build archiving) |
| `b78e5ff2c40` | 2026-09-24T07:33:52Z | 2026-09-24 | n/a (predates per-build archiving) |
| `a59dd3004f9` | 2026-09-24T08:20:45Z | 2026-09-24 | n/a (predates per-build archiving) |
| `1adcf02f1dd` | 2026-09-24T12:35:03Z | 2026-09-24 | n/a (predates per-build archiving) |
| `0e24421e029` | 2026-09-24T14:18:55Z | 2026-09-24 | n/a (predates per-build archiving) |
| `d0ab766c92c` | 2026-09-24T16:41:27Z | 2026-09-24 | n/a (predates per-build archiving) |
| `9b494088272` | 2026-09-24T18:43:04Z | 2026-09-24 | n/a (predates per-build archiving) |
| `a271cb6c87c` | 2026-09-24T20:55:31Z | 2026-09-24 | n/a (predates per-build archiving) |
| `12a16619aa1` | 2026-09-24T23:36:48Z | 2026-09-24 | see release `build-12a16619aa1` |

What changed per build is recorded in the release notes and in the
tool-watch changelog. The archiver is `tools/archive-runtime.sh`; its
exclusion list ships next to every zip.
| `f43d26fc581` | 2026-09-25T01:57:05Z | 2026-09-25 | see release `build-f43d26fc581` |
| `938bf351786` | 2026-09-25T04:53:39Z | 2026-09-25 EDT | see release `build-938bf351786` |
| `fd7a22489a5` | 2026-09-25T12:18:43Z | 2026-09-25 EDT | see release `build-fd7a22489a5` |
| `f4d11031a1f` | 2026-09-25T14:09:35Z | 2026-09-25 EDT | see release `build-f4d11031a1f` |
