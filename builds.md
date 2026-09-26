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
| `bfea4bc4abe` | 2026-09-25T15:35:26Z | 2026-09-25 EDT | see release `build-bfea4bc4abe` |
| `3da4b728da3` | 2026-09-25T17:18:23Z | 2026-09-25 EDT | see release `build-3da4b728da3` |
| `a01af45e4b9` | 2026-09-25T18:57:22Z | 2026-09-25 EDT | see release `build-a01af45e4b9` |
| `679b103d9f6` | 2026-09-25T20:47:25Z | 2026-09-25 EDT | see release `build-679b103d9f6` |

- 2026-09-25 ~21:07 EDT: release `build-679b103d9f6` repaired — the 1.2 GB zip could not be uploaded whole (4 attempts, `gh` and `curl`, all severed mid-transfer with "unexpected EOF" after 2.5–45 min through the egress proxy; 100 MB probe to a neutral endpoint sustained ~2 MB/s, so the drop is specific to the long-lived uploads.github.com connection). Workaround: zip uploaded as 6 split parts (`runtime-archive-679b103d9f6-20260925.zip.part-00`..`part-05`, 5x200 MB + 154,398,495 B); part sizes sum to exactly 1,202,974,495 B = local zip size. Reassemble with `cat part-0* > runtime-archive-679b103d9f6-20260925.zip` and verify against the manifest sha256.
| `934f5cdf557` | 2026-09-25T23:22:36Z | 2026-09-25 EDT | see release `build-934f5cdf557` |
| `e23a18c35c8` | 2026-09-26T02:20:17Z | 2026-09-26 EDT | see release `build-e23a18c35c8` |
| `b6a533c6775` | 2026-09-26T04:07:17Z | 2026-09-26 EDT | see release `build-b6a533c6775` |
| `3afcf8b9998` | 2026-09-26T07:37:50Z | 2026-09-26 EDT | see release `build-3afcf8b9998` |
| `4c594beb933` | 2026-09-26T09:18:38Z | 2026-09-26 EDT | see release `build-4c594beb933` |
| `51db0eafcef` | 2026-09-26T11:25:52Z | 2026-09-26 EDT | see release `build-51db0eafcef` |
| `cc5957e62fe` | 2026-09-26T13:02:36Z | 2026-09-26 EDT | see release `build-cc5957e62fe` |
| `cbf4585c898` | 2026-09-26T15:11:39Z | 2026-09-26 EDT | see release `build-cbf4585c898` |
| `d96cc26a11d` | 2026-09-26T16:51:40Z | 2026-09-26 EDT | see release `build-d96cc26a11d` |
| `0decec9a6b1` | 2026-09-26T17:31:17Z | 2026-09-26 EDT | see release `build-0decec9a6b1` |
| `572213748ab` | 2026-09-26T19:38:48Z | 2026-09-26 EDT | see release `build-572213748ab` |

## Split-part archives
Builds `cbf4585c898`, `d96cc26a11d` and `0decec9a6b1` ship their 1.2 GB zip as six ~200 MB parts (`runtime-archive-<commit>-20260926.zip.part-aa` through `-af`) because monolithic uploads kept failing with EOF on this network. Reassemble with: `cat runtime-archive-<commit>-20260926.zip.part-* > runtime-archive-<commit>-20260926.zip` then verify against the sha256 in the release manifest.
- `cbf4585c898` zip sha256: `07e14b137c5474c6be74422a25ed5ca29c1c33f500b474c361155a69d520868a`
- `d96cc26a11d` zip sha256: `8af693e7c5dd1e3ecb48dcc32f8544366b71d914c9cb87c921efadbeb8527658`
- `0decec9a6b1` zip sha256: `dd46b489331e1dc25e0e17564f63f83e09a00ebf3aef1a8f81232ed936d70a0f`
