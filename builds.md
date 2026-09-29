# Build archive

Sanitized filesystem snapshots from one Muse instance, published as [GitHub Releases](https://github.com/mikezio/muse-runtime/releases). These are filtered live-instance captures, not pristine platform images or bootable VMs.

**Start with the [archive workflow](docs/archive-workflow.md)** to compare small manifests, reassemble split downloads and distinguish archive checksums from per-file hashes. The [evidence guide](docs/evidence.md) explains what each kind of artifact can establish.

## Observed builds

| Build | Built (UTC) | Detected (as recorded) | Archive |
|---|---|---|---|
| `10ba995fed7` | 2026-09-24T04:05:12Z | 2026-09-24 | n/a (predates per-build archiving) |
| `b78e5ff2c40` | 2026-09-24T07:33:52Z | 2026-09-24 | n/a (predates per-build archiving) |
| `a59dd3004f9` | 2026-09-24T08:20:45Z | 2026-09-24 | n/a (predates per-build archiving) |
| `1adcf02f1dd` | 2026-09-24T12:35:03Z | 2026-09-24 | n/a (predates per-build archiving) |
| `0e24421e029` | 2026-09-24T14:18:55Z | 2026-09-24 | n/a (predates per-build archiving) |
| `d0ab766c92c` | 2026-09-24T16:41:27Z | 2026-09-24 | n/a (predates per-build archiving) |
| `9b494088272` | 2026-09-24T18:43:04Z | 2026-09-24 | n/a (predates per-build archiving) |
| `a271cb6c87c` | 2026-09-24T20:55:31Z | 2026-09-24 | n/a (predates per-build archiving) |
| `12a16619aa1` | 2026-09-24T23:36:48Z | 2026-09-24 | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-12a16619aa1) |
| `f43d26fc581` | 2026-09-25T01:57:05Z | 2026-09-25 | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-f43d26fc581) |
| `938bf351786` | 2026-09-25T04:53:39Z | 2026-09-25 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-938bf351786) |
| `fd7a22489a5` | 2026-09-25T12:18:43Z | 2026-09-25 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-fd7a22489a5) |
| `f4d11031a1f` | 2026-09-25T14:09:35Z | 2026-09-25 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-f4d11031a1f) |
| `bfea4bc4abe` | 2026-09-25T15:35:26Z | 2026-09-25 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-bfea4bc4abe) |
| `3da4b728da3` | 2026-09-25T17:18:23Z | 2026-09-25 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-3da4b728da3) |
| `a01af45e4b9` | 2026-09-25T18:57:22Z | 2026-09-25 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-a01af45e4b9) |
| `679b103d9f6` | 2026-09-25T20:47:25Z | 2026-09-25 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-679b103d9f6) |
| `934f5cdf557` | 2026-09-25T23:22:36Z | 2026-09-25 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-934f5cdf557) |
| `e23a18c35c8` | 2026-09-26T02:20:17Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-e23a18c35c8) |
| `b6a533c6775` | 2026-09-26T04:07:17Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-b6a533c6775) |
| `3afcf8b9998` | 2026-09-26T07:37:50Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-3afcf8b9998) |
| `4c594beb933` | 2026-09-26T09:18:38Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-4c594beb933) |
| `3449240a34c` | 2026-09-27T03:01:01Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-3449240a34c) |
| `51db0eafcef` | 2026-09-26T11:25:52Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-51db0eafcef) |
| `cc5957e62fe` | 2026-09-26T13:02:36Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-cc5957e62fe) |
| `cbf4585c898` | 2026-09-26T15:11:39Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-cbf4585c898) |
| `d96cc26a11d` | 2026-09-26T16:51:40Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-d96cc26a11d) |
| `0decec9a6b1` | 2026-09-26T17:31:17Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-0decec9a6b1) |
| `572213748ab` | 2026-09-26T19:38:48Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-572213748ab) |
| `61c470cfc94` | 2026-09-26T21:27:09Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-61c470cfc94) |
| `8d0554d8f9e` | 2026-09-26T22:42:31Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-8d0554d8f9e) |
| `8dfd7f19e85` | 2026-09-27T01:00:10Z | 2026-09-26 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-8dfd7f19e85) |
| `8d5fea02416` | 2026-09-27T02:35:10Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-8d5fea02416) |
| `9bbc62e15ff` | 2026-09-27T05:41:39Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-9bbc62e15ff) |
| `49d7dfcc81f` | 2026-09-27T07:37:04Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-49d7dfcc81f) |
| `f24b087f6e6` | 2026-09-27T11:10:27Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-f24b087f6e6) |
| `f12c5827e17` | 2026-09-27T13:19:02Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-f12c5827e17) |
| `985a51dd9c3` | 2026-09-27T15:26:48Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-985a51dd9c3) |
| `41dba52bf1c` | 2026-09-27T17:37:39Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-41dba52bf1c) |
| `d146dbe8fdf` | 2026-09-27T19:52:46Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-d146dbe8fdf) |
| `a1057248754` | 2026-09-27T22:21:00Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-a1057248754) |
| `1eefe22acda` | 2026-09-28T00:41:38Z | 2026-09-27 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-1eefe22acda) |

The archiver is [tools/archive-runtime.sh](tools/archive-runtime.sh). Exclusions accompany each release. Keep new build rows inside this table; put transfer notes below it.

## Historical upload note

- 2026-09-25 ~21:07 EDT: release `build-679b103d9f6` repaired — the 1.2 GB zip could not be uploaded whole (4 attempts, `gh` and `curl`, all severed mid-transfer with "unexpected EOF" after 2.5–45 min through the egress proxy; 100 MB probe to a neutral endpoint sustained ~2 MB/s, so the drop is specific to the long-lived uploads.github.com connection). Workaround: zip uploaded as 6 split parts (`runtime-archive-679b103d9f6-20260925.zip.part-00`..`part-05`, 5x200 MB + 154,398,495 B); part sizes sum to exactly 1,202,974,495 B = local zip size. Reassemble with `cat part-0* > runtime-archive-679b103d9f6-20260925.zip` and verify against a published whole-ZIP checksum when available; the per-file manifest is a different check.

## Split-part archives
Builds `cbf4585c898`, `d96cc26a11d`, `0decec9a6b1`, `61c470cfc94`, `8d0554d8f9e`, `49d7dfcc81f`, `f24b087f6e6`, `374ca3b66a7` and `f12c5827e17` ship their 1.2 GB zip as six ~200 MB parts (`runtime-archive-<commit>-20260926.zip.part-00` through `-05`; earlier builds used `-aa` through `-af`) because monolithic uploads kept failing with EOF on this network. Reassemble with: `cat runtime-archive-<commit>-20260926.zip.part-* > runtime-archive-<commit>-20260926.zip` then verify against the published whole-ZIP checksum for that build (not the per-file manifest).
- `8d0554d8f9e` zip sha256: `81037c2817c76772ea112c8905a00607bb63b8289a0c108add28a4dc018849d2`
- `61c470cfc94` zip sha256: `819a5e85072d570951b3a973258312124561e7c663fa891c88e0d72c5e48d0b5`
- `cbf4585c898` zip sha256: `07e14b137c5474c6be74422a25ed5ca29c1c33f500b474c361155a69d520868a`
- `d96cc26a11d` zip sha256: `8af693e7c5dd1e3ecb48dcc32f8544366b71d914c9cb87c921efadbeb8527658`
- `0decec9a6b1` zip sha256: `dd46b489331e1dc25e0e17564f63f83e09a00ebf3aef1a8f81232ed936d70a0f`
- `8d5fea02416` zip sha256: `7ac510fd31be9fe5f4788618a7b9f45ef20fcdb65eabbeb66ca3957d7eee620f` (monolithic 1.2 GB upload succeeded; no split parts)
- `3449240a34c` zip sha256: `03311a209710ceaedb1a57b9691aa37c3b16426d231520be0fdbbea126d7ae5e` (monolithic 1.2 GB upload succeeded; no split parts)
- `49d7dfcc81f` zip sha256: `e52234733db9625726f1b2365312c9d51183f4ec3513f71944030cfb0b7e698f` (monolithic 1.2 GB upload failed with EOF; six ~200 MB parts instead)
- `f24b087f6e6` zip sha256: `ba54838583e35761f01577bcd5d32185912867337e305ca8c295b6c27230b806` (monolithic 1.2 GB upload failed with EOF; six ~200 MB parts instead; part sizes sum to exactly the local zip size)
- `374ca3b66a7` zip sha256: `f78fb85ad09696fea7f1bbc2aa0a7e16c6ce5bedb3ce3325ca1ecc0ff365c1e6` (six ~200 MB parts, part-00..part-05)
- `f12c5827e17` zip sha256: `befdd9b19b8c8244033c8bd6a30d9a6f7bc43e7390bf5b9ae49a29a92ade8c8c` (monolithic 1.2 GB upload stalled >18 min with zero bytes landed on GitHub; killed and uploaded six ~200 MB parts part-00..part-05 instead)
- `985a51dd9c3` zip sha256: `79adb0e13a81d69d54714b7ad69bb20df55408ed8135d1dbe503fbd973f8ad01` (monolithic 1.2 GB upload failed with EOF; six ~200 MB parts, part sizes sum to exactly the local zip size)
- `a1057248754` zip sha256: `5114183243cf8925655b48f0be3e44930d311937f7ae6818e8fd1fd47e06f6f9` (six ~200 MB parts part-00..part-05; part sizes sum to exactly the local zip size)
- `1eefe22acda` zip sha256: `462b6398aede5a390e7e8034a105d904372d626b2cf86e3bb05eb5ab63408e0a` (monolithic 1.2 GB upload stalled with zero bytes landed on GitHub; six ~200 MB parts part-00..part-05 instead; part sizes sum to exactly the local zip size)
- `34136f0a759` zip sha256: `fe5a34cfcc831bfa12272a4f84cc7fc4b6985660c989b7731065c94714088fc9` (monolithic 1.2 GB upload EOFs; 200 MB parts silently truncated at ~197.9 MB by egress proxy; twelve ~100 MB parts p100m-00..p100m-11 instead, all verified byte-identical on re-download; part sizes sum to exactly the local zip size; release first created under truncated tag build-34136f0a75, fixed to build-34136f0a759)
- `89ec2feef66` zip sha256: `a1b2d4ac01832b8e000cdf5d1c557de4bb9b9b2c42733c928f4754a04154abdb` (twelve ~100 MB parts p100m-00..p100m-11, same as the 34136f0a759 pattern; first four pieces verified byte-identical on re-download; part sizes sum to exactly the local zip size of 1187345940 bytes)
| `82da44d37c3` | 2026-09-28T02:23:22Z | 2026-09-28 EDT | see release `build-82da44d37c3` |
| `16bddaccfa2` | 2026-09-28T04:24:52Z | 2026-09-28 EDT | see release `build-16bddaccfa2` |
| `34136f0a759` | 2026-09-28T06:19:31Z | 2026-09-28 EDT | see release `build-34136f0a759` |
| `89ec2feef66` | 2026-09-28T06:23:02Z | 2026-09-28 EDT | see release `build-89ec2feef66` |
- `5c8050fc67` zip sha256: `4e5c7bae5aedbdb417e26a5dd67fbbc85c28a5cbb7d11d188ab9954472a76fec` (twelve ~100 MB parts p100m-aa..p100m-al, same pattern as 34136f0a759/89ec2feef66; manifest clean; part sizes sum to exactly the local zip size of 1186961227 bytes)
| `5c8050fc67` | 2026-09-28T09:59:17Z | 2026-09-28 EDT | see release `build-5c8050fc67` |
| `04e50fc89d` | 2026-09-28T14:33:13Z | 2026-09-28 EDT | see release `build-04e50fc89d` |
| `3a8c7f3991` | 2026-09-28T18:34:00Z | 2026-09-28 EDT | see release `build-3a8c7f3991` |
| `9344a6fdedf` | 2026-09-28T20:44:22Z | 2026-09-28 EDT | see release `build-9344a6fded` (tag uses 9 chars: earlier 18:29-EDT-run created the release with a truncated tag before the 10-char rule was enforced; no duplicate tag created) |
- `9344a6fdedf` zip sha256: `b954bb4109acb2523a3758c8ce6cdd5d74786ccced973afbc4385e3f6e74388e` (17239 files, 1189821105 bytes; manifest clean; release already existed with manifest+exclusions from the truncated-tag run. monolithic zip upload failed twice with unexpected EOF, switched to twelve ~100 MB parts p100m-aa..p100m-al, same pattern as 34136f0a759/5c8050fc67; part sizes sum to exactly the local zip size)
| `b5fc85534c` | 2026-09-28T22:43:21Z | 2026-09-28 EDT | see release `build-b5fc85534c` |
- `baf0a304aa` zip sha256: `bee7699f5b72bca15c0c064b6fca8239c0e20ee53dac8f5e289229f7a8cb184e` (17363 files, 1308508537 bytes; manifest clean, no personal-data hits; monolithic zip upload stalled >18 min with zero bytes landed, killed and uploaded thirteen ~100 MB parts p100m-aa..p100m-am instead; part sizes sum to exactly the local zip size)
| `baf0a304aa` | 2026-09-29T05:26:23Z | 2026-09-29 EDT | see release `build-baf0a304aa` |
| `610ce13ff2` | 2026-09-29T07:00:12Z | 2026-09-29 EDT | see release `build-610ce13ff2` |
| `af173b0f79` | 2026-09-29T09:03:47Z | 2026-09-29 EDT | see release `build-af173b0f79` |
| `db4b4add0f` | 2026-09-29T11:14:18Z | 2026-09-29 EDT | see release `build-db4b4add0f` |
- `db4b4add0f` zip sha256: `b5c62ca88fe755eb848faec43bbbab814da8f506a0d13da5266a5267f8c4c252` (17368 files, 1308898698 bytes; manifest clean, no personal-data hits; monolithic zip upload stalls, thirteen ~100 MB parts p100m-aa..p100m-am, part sizes sum to exactly the local zip size; two parts verified byte-identical on re-download)
- `af173b0f79` zip sha256: `7220496f91530274ca9fd89a3912217c5c2427580302ee0029d328a12d928e87` (17366 files, 1309528671 bytes; manifest clean; monolithic zip upload stalled ~13 min with zero bytes landed, killed and uploaded thirteen ~100 MB parts p100m-00..p100m-12 instead; part sizes sum to exactly the local zip size)
