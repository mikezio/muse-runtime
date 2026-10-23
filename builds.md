# Build archive

Filesystem snapshots of the Muse runtime, published as [GitHub Releases](https://github.com/mikezio/muse-runtime/releases). They capture the runtime as it actually runs, not a clean install image, and they are not bootable VMs.

**Start with the [archive workflow](docs/archive-workflow.md)** to compare small manifests, reassemble split downloads and distinguish archive checksums from per-file hashes. The [evidence guide](docs/evidence.md) explains what each kind of artifact can establish.

## Observed builds

| Build | Built (UTC) | Detected (as recorded) | Archive |
|---|---|---|---|
| `801e25284d` | 2026-10-19T20:46:28Z | 2026-10-19 20:50 EDT | see release `build-801e25284d` |
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

- 2026-09-25 ~21:07 EDT: release `build-679b103d9f6` repaired; the 1.2 GB zip could not be uploaded whole (4 attempts, `gh` and `curl`, all severed mid-transfer with "unexpected EOF" after 2.5–45 min through the egress proxy; 100 MB probe to a neutral endpoint sustained ~2 MB/s, so the drop is specific to the long-lived uploads.github.com connection). Workaround: zip uploaded as 6 split parts (`runtime-archive-679b103d9f6-20260925.zip.part-00`..`part-05`, 5x200 MB + 154,398,495 B); part sizes sum to exactly 1,202,974,495 B = local zip size. Reassemble with `cat part-0* > runtime-archive-679b103d9f6-20260925.zip` and verify against a published whole-ZIP checksum when available; the per-file manifest is a different check.

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
| `ed356ed358` | 2026-09-29T13:32:36Z | 2026-09-29 EDT | see release `build-ed356ed358` |
| `27d509bb08` | 2026-09-29T14:18:42Z | 2026-09-29 EDT | see release `build-27d509bb08` |
| `b52c8ada52` | 2026-09-29T18:32:39Z | 2026-09-29 EDT | see release `build-b52c8ada52` |
| `ebef376b69` | 2026-09-30T06:16:46Z | 2026-09-30 EDT | see release `build-ebef376b69` |
- `ebef376b69` zip sha256: `7719272d36a0886be0e848d20889d0c3b5994a9c22bfaa21c5c1af6393ca85ad` (17405 files, 1310404205 bytes; manifest clean, no personal-data hits; monolithic zip upload historically stalls at this size, thirteen ~100 MB parts p100m-aa..p100m-am instead; part sizes sum to exactly the local zip size)
- `115d4d07d5` zip sha256: `892823dcf48629c7de050cc3bfb883b546d6cf39a2c424f2bc03e0d2bca33a00` (17397 files, 1312318966 bytes; manifest clean, no personal-data hits; monolithic zip upload stalls at this size, thirteen ~100 MB parts p100m-00..p100m-12 instead; part sizes sum to exactly the local zip size)
| `75d3f9af2a` | 2026-09-30T14:30:28Z | 2026-09-30 EDT | see release `build-75d3f9af2a` |
- `75d3f9af2a` zip sha256: `a46bdd0511e854cfbf39c1429aa34cd8f28e61cbf577c53802fb0147d969c39c` (17414 files, 1310151949 bytes; manifest clean, no personal-data hits; monolithic zip upload historically stalls at this size, thirteen ~100 MB parts p100m-aa..p100m-am instead; part sizes sum to exactly the local zip size)
| `8b308cd0bb` | 2026-09-30T17:03:36Z | 2026-09-30 EDT | see release `build-8b308cd0bb` |
- `8b308cd0bb` zip sha256: `baf83b85c59be86d5a0aa95dd1afec99a95cb326fe96f91d5960bc66b2b1440c` (17441 files, 1527941443 bytes; manifest clean, no personal-data hits; monolithic zip upload stalls at this size, fifteen ~100 MB parts p100m-00..p100m-14 instead; part sizes sum to exactly the local zip size)
| `712e72d913` | 2026-09-30T23:29:09Z | 2026-09-30 EDT | see release `build-712e72d913` |
- `712e72d913` zip sha256: `735dd0e10e88158fb05da4516421461d97b737d1ba465cd6658e326468630a63` (17449 files, 1529846909 bytes; manifest clean, no personal-data hits; monolithic zip upload stalls at this size, fifteen ~100 MB parts p100m-aa..p100m-ao instead; part sizes sum to exactly the local zip size)
| `78b0b45cde` | 2026-10-01T02:13:46Z | 2026-10-01 EDT | see release `build-78b0b45cde` |
- `78b0b45cde` zip sha256: `b948ad4021bf21e385a746b75357f037177bff0b1591a7c7ed664d73d2d20cd9` (17451 files, 1529959718 bytes; manifest clean, no personal-data hits; monolithic zip upload stalls at this size, fifteen ~100 MB parts p100m-aa..p100m-ao instead; part sizes sum to exactly the local zip size)
| `88e6d3da09` | 2026-10-01T05:08:15Z | 2026-10-01 EDT | see release `build-88e6d3da09` |
- `bd6af2f652` zip sha256: `5165181fd4d5d428cb88ec0f8f18f0a8416c1ac0a1a5bd2c530c433a2f1f76ea` (17454 files, 1532671054 bytes; manifest clean, no personal-data hits; monolithic zip upload stalls at this size, fifteen ~100 MB parts p100m-00..p100m-14 instead; part sizes sum to exactly the local zip size)
| `bd6af2f652` | 2026-10-01T07:43:40Z | 2026-10-01 EDT | see release `build-bd6af2f652` |
- `88e6d3da09` zip sha256: `081ebf35df3d3b0e837cd0ba755a3d259b10187d846a4c4c6741fd2d73934ebb` (17454 files, 1533003466 bytes; manifest clean, no personal-data hits; monolithic zip upload stalls at this size, fifteen ~100 MB parts p100m-aa..p100m-ao instead; part sizes sum to exactly the local zip size)
| `b65ea7e787` | 2026-10-01T09:51:24Z | 2026-10-01 EDT | see release `build-b65ea7e787` |
- `b65ea7e787` zip sha256: `b7b9ff54db6e3c859ccec56be89503acf3a0eeaa0999c0c0f84adec6eab62e5a` (17454 files, 1541408045 bytes; manifest clean, no personal-data hits)
| `7224aaae38` | 2026-10-01T12:24:24Z | 2026-10-01 EDT | see release `build-7224aaae38` |
- `7224aaae38` zip sha256: `a4e0309cdcc6da13fdcc3e52e56484e948c6971aae5bf5724a08e2fce3f21640` (17454 files, 1541422286 bytes; manifest clean, no personal-data hits; monolithic zip upload succeeded this time)
| `e2c23bddfb` | 2026-10-01T18:18:37Z | 2026-10-01 EDT | see release `build-e2c23bddfb` |
- `e2c23bddfb` zip sha256: `114088bf9bc70de0eb95589a8c2a565618167448c2757ed48100dc406c3cf58c` (17454 files, 1542236374 bytes; manifest clean, no personal-data hits; monolithic zip upload stalled at this size, fifteen ~100 MB parts p100m-00..p100m-14 instead; part sizes sum to exactly the local zip size)
| `aca82f2542` | 2026-10-01T20:21:34Z | 2026-10-01 EDT | see release `build-aca82f2542` |
| `2256c97385` | 2026-10-01T22:05:36Z | 2026-10-01 EDT | see release `build-2256c97385` |
- `2256c97385` zip sha256: `410b22e4091a27fd6a279d36b124721f44bd4387855f7d2848cd7f669b84a51d` (17454 files, 1543924148 bytes; manifest clean, no personal-data hits; monolithic zip upload stalled at this size, fifteen ~100 MB parts p100m-aa..p100m-ao instead; part sizes sum to exactly the local zip size)
| `78321c6c08` | 2026-10-02T00:47:29Z | 2026-10-02 EDT | see release `build-78321c6c08` |
- `78321c6c08` zip sha256: `e2dff12dc1df0b7e614aff0eea7f04d3e97adc5cc98555321536e1fe77ddfb8f` (17454 files, 1544298070 bytes; manifest clean, no personal-data hits; monolithic zip upload EOF'd, fifteen ~100 MB parts p100m-00..p100m-14 instead; concatenated parts sha256 match the zip exactly)
| `fa593de972` | 2026-10-02T03:42:31Z | 2026-10-02 EDT | see release `build-fa593de972` |
- `fa593de972` zip sha256: `e7bb763966486b6bd55f98df2656c2de8947a7379e1c206dfa78b441f230a4ae` (17456 files, 1552586188 bytes; manifest clean, no personal-data hits; monolithic zip upload stalled at this size, fifteen ~100 MB parts part-aa..part-ao instead; concatenated parts sha256 match the zip exactly)
| `fe0797cca7` | 2026-10-02T04:31:04Z | 2026-10-02 EDT | see release `build-fe0797cca7` |
- `fe0797cca7` zip sha256: `cf67d910fd021e53c1790227fd6de25287c3fca61a6b14ce42619f08e17d9399` (17456 files, 1.5G; manifest clean, no personal-data hits; monolithic zip upload stalled at this size on prior builds, fifteen ~100 MB parts p100m-00..p100m-14 instead; concatenated parts sha256 match the zip exactly)
| `6d1e7e8fbf` | 2026-10-02T05:45:04Z | 2026-10-02 EDT | see release `build-6d1e7e8fbf` |
| `e71589bd1b` | 2026-10-02T09:19:02Z | 2026-10-02 EDT | see release `build-e71589bd1b` |
- `e71589bd1b` zip sha256: `79295811e76747b65358f0f8bc2a624839b6b604392aca37f30840e2716c87d0` (17456 files, 1.5G; manifest clean, no personal-data hits; monolithic zip upload stalled at this size on prior builds, fifteen ~100 MB parts part-aa..part-ao instead; concatenated parts sha256 match the zip exactly)
| `5f8088bd9e` | 2026-10-02T11:15:20Z | 2026-10-02 EDT | see release `build-5f8088bd9e` |
- `5f8088bd9e` zip sha256: `8b88eb182d6b5920c4ff11e899db4e83c4f3bd6a3416e9658d5efb64bdaa8f0d` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts part-aa..part-ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `4957713dcf` | 2026-10-02T12:59:40Z | 2026-10-02 EDT | see release `build-4957713dcf` |
- `4957713dcf` zip sha256: `4585528263041b546c0a8f4ca11c88aeeb06fedb1b1c8259a2fa9b8569ed738d` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `49c5a26cbc` | 2026-10-02T16:51:48Z | 2026-10-02 EDT | see release `build-49c5a26cbc` |
- `49c5a26cbc` zip sha256: `1bfe1d8dda6c2661d62fea9e6f580b5b94e2ee84a722e09714ff8a3af663aada` (17454 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `83f77f7f30` | 2026-10-02T19:06:52Z | 2026-10-02 EDT | see release `build-83f77f7f30` |
- `83f77f7f30` zip sha256: `2e0df8554aa1138b6b5c39002f741f64ac55cf561f92d2b55b38c4f8abcaa427` (17455 files, 1.5G; manifest clean, no personal-data hits; monolithic zip upload stalled at this size on prior builds, fifteen ~100 MB parts p100m-00..p100m-14 instead; concatenated parts sha256 match the zip exactly)
| `aff7c5a212` | 2026-10-02T22:19:24Z | 2026-10-02 EDT | see release `build-aff7c5a212` |
- `aff7c5a212` zip sha256: `125ba0a1d7fdc226e44e2299b226c2dc61ec025d3d0b7b3715b923273ad2e620` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; concatenated parts sha256 match the zip exactly)
- `f1807780ef` zip sha256: `343e5e6994b3a2c3b52c276ab74692ee195b36fd633f52836c961523c2ea83f0` (17455 files, 1.5G; manifest clean, no personal-data hits; monolithic zip upload stalled at this size on prior builds, fifteen ~100 MB parts p100m-00..p100m-14 instead; concatenated parts sha256 match the zip exactly)
| `f1807780ef` | 2026-10-03T00:19:16Z | 2026-10-02 EDT | see release `build-f1807780ef` |
- `b512bcfd20` zip sha256: `6fa58940690b0b681fbc8e4e023a4823c2261e3ed3398366c1ecb6b7805940d4` (17455 files, 1.5G; manifest clean, no personal-data hits; monolithic zip upload stalled at this size on prior builds, fifteen ~100 MB parts p100m-00..p100m-14 instead; concatenated parts sha256 match the zip exactly)
| `b512bcfd20` | 2026-10-03T02:22:54Z | 2026-10-03 EDT | see release `build-b512bcfd20` |
- `5ef30c0d86` zip sha256: `f645f8815acf7c638d2ff5010ce2ad7ca8991e928eaf9a6ceddbb56f5778f8b5` (17456 files, 1.5G; manifest clean, no personal-data hits; monolithic zip upload stalled at this size on prior builds, fifteen ~100 MB parts p100m-00..p100m-14 instead; concatenated parts sha256 match the zip exactly)
| `5ef30c0d86` | 2026-10-03T05:02:26Z | 2026-10-03 EDT | see release `build-5ef30c0d86` |
| `56ea674fc0` | 2026-10-03T07:53:03Z | 2026-10-03 EDT | see release `build-56ea674fc0` |
- `56ea674fc0` zip sha256: `752006d735765a2c26e11dcd7a9acb51c90e8fe560f27b4328b5db2c2ac72499` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; concatenated parts sha256 match the zip exactly)
- `9c97d123ff` zip sha256: `d537538a6e532675faaf1eafc0ee27a2016888a1737e08c3f5870dfa04a21231` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `9c97d123ff` | 2026-10-03T12:28:48Z | 2026-10-03 EDT | see release `build-9c97d123ff` |
- `b7c5d689d9` zip sha256: `20e756e8d0186329b88042472941da84f849facda16ec4fb57a633a5e11555b8` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `b7c5d689d9` | 2026-10-03T15:20:07Z | 2026-10-03 EDT | see release `build-b7c5d689d9` |
| `12a6141da3` | 2026-10-03T17:48:16Z | 2026-10-03 EDT | see release `build-12a6141da3` |
- `12a6141da3` zip sha256: `1482abf353dea38cf4e482170bffc6e98fbb70b0e08689af3f3889ead910c8ec` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `f2b9d1cd37` | 2026-10-03T19:53:57Z | 2026-10-03 EDT | see release `build-f2b9d1cd37` |
- `f2b9d1cd37` zip sha256: `7f38e7ab4cd042411e0437209690f35547ab85281747015d4c027d4cf0f4d784` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `c53c928944` | 2026-10-04T02:56:41Z | 2026-10-04 EDT | see release `build-c53c928944` |
- `c53c928944` zip sha256: `9c3cb94edff7102d1bb3cac98b92775b3af027ad8443211f583244be9061f9b5` (17456 files, 1.5G; filename scan clean; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; monolithic upload failed with a GitHub stream error, parts uploaded clean; concatenated parts sha256 match the zip exactly)
| `3637018994` | 2026-10-04T07:34:29Z | 2026-10-04 EDT | see release `build-3637018994` |
- `3637018994` zip sha256: `f7497093c51e7429835bb5c51cbf5471bc232930379eb0fc698897475a9f0649` (17456 files, 1.5G; filename scan clean; seventeen ~100 MB parts p100m-00..p100m-16 instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `68a836d6ab` | 2026-10-04T17:10:36Z | 2026-10-04 EDT | see release `build-68a836d6ab` |
- `68a836d6ab` zip sha256: `c240662677651756c7bef0aaf92e5fa80defe5834a6e8cf8d05f74ebee1b0a25` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `ac28a8986f` | 2026-10-04T20:26:29Z | 2026-10-04 EDT | see release `build-ac28a8986f` |
- `ac28a8986f` zip sha256: `2a62080354de3fb98a9aaf7078ba6eb19601ed6cc9d0f7a92aadfb52622d72b4` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `1f8d50e25f` | 2026-10-04T23:18:44Z | 2026-10-04 EDT | see release `build-1f8d50e25f` |
- `1f8d50e25f` zip sha256: `cb223a628bf7194e670fdd491572a97680a052306045013a4fbb86bda0736b7b` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `9b13d3a12e` | 2026-10-05T02:19:15Z | 2026-10-05 EDT | see release `build-9b13d3a12e` |
- `9b13d3a12e` zip sha256: `da7e724b79172a5621f344771b105d7117456b4a9ce45a7cb6d2cd3039166dc9` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; monolithic upload failed with a GitHub stream error, parts uploaded clean; concatenated parts sha256 match the zip exactly)
| `8d61278e1f` | 2026-10-05T05:48:40Z | 2026-10-05 EDT | see release `build-8d61278e1f` |
- `8d61278e1f` zip sha256: `f20a151de7c691b2596d4cd13f2eb268c5575e4dd369b9ce8892c33cba284a2d` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; monolithic upload failed with a GitHub stream error, parts uploaded clean; concatenated parts sha256 match the zip exactly)
| `2746a87742` | 2026-10-05T08:10:33Z | 2026-10-05 EDT | see release `build-2746a87742` |
- `2746a87742` zip sha256: `1111df0324c089c29c7fdb9ad718d61d78ba83f3c82ce557a82384a79b8ae83e` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; monolithic upload skipped for the known GitHub stream error; concatenated parts sha256 match the zip exactly)
| `364c657900` | 2026-10-05T15:56:04Z | 2026-10-05 EDT | see release `build-364c657900` |
- `364c657900` zip sha256: `6083c4d77a6ef91a5571505b9677ac69ed062b2ee27ee4cd75b2c624bb0bc732` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; monolithic upload skipped for the known GitHub stream error; concatenated parts sha256 match the zip exactly)
| `916c9d67b3` | 2026-10-05T22:00:01Z | 2026-10-05 EDT | see release `build-916c9d67b3` |
- `916c9d67b3` zip sha256: `9ea65a67f224e870d8e799a9ebead4845126fcc49672f747de977cb2dd08f7c2` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; monolithic upload skipped for the known GitHub stream error; concatenated parts sha256 match the zip exactly)
| `b28c5b0249` | 2026-10-06T04:43:16Z | 2026-10-06 EDT | see release `build-b28c5b0249` |
- `b28c5b0249` zip sha256: `2a22495e786d41e5ab0564a0f005d3c49d07688e6cc7f1cdc5b5af195693ed06` (17454 files, 1.5G; manifest clean, no personal-data hits; monolithic upload clean)
| `f3c534f692` | 2026-10-06T06:45:48Z | 2026-10-06 EDT | see release `build-f3c534f692` |
- `f3c534f692` zip sha256: `6dcb2a3e164a6b466f5921b2b16655382bd3647f0a13b3291d8e6c597fb22ce5` (22335 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; monolithic upload failed with a GitHub stream error; concatenated parts sha256 match the zip exactly)
| `3b4aa3a20a` | 2026-10-06T11:17:24Z | 2026-10-06 EDT | see release `build-3b4aa3a20a` |
- `3b4aa3a20a` zip sha256: `782cd621783d00e31e5018da34a2b418d019ba0ac37072a520e59134a96dc9a0` (17455 files, 1.5G; manifest clean, no personal-data hits)
| `99c8eb41f3` | 2026-10-06T14:27:23Z | 2026-10-06 EDT | see release `build-99c8eb41f3` |
- `99c8eb41f3` zip sha256: `759cdefc72b8bc8b9ade7c6a760c4f458bb6938da893d4402bb60a5a6645e8a7` (17455 files, 1.6G; manifest clean, no personal-data hits; monolithic upload clean)
| `e6ced0b136` | 2026-10-06T15:44:59Z | 2026-10-06 EDT | see release `build-e6ced0b136` |
- `e6ced0b136` zip sha256: `25d6031d35817360e0a80e7bf830a1c7f0f01bf2f53d2ab2956580924acae5ae` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; monolithic upload failed with a GitHub stream error; concatenated parts sha256 match the zip exactly)
| `16f6e81b2ce` | 2026-10-06T17:29:49Z | 2026-10-06 EDT | see release `build-16f6e81b2ce` |
- `16f6e81b2ce` zip sha256: `56f91f55f6286bc3105aa95174940dfded3b7e43814b9bc8ace4542cdaa349c5` (17455 files, 1.5G; filename scan clean; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip; monolithic upload stalled with zero progress for ~24 min and was killed, same as builds f3c534f692 and e6ced0b136; concatenated parts sha256 match the zip exactly)
| `33c21777f2` | 2026-10-06T21:21:48Z | 2026-10-06 EDT | see release `build-33c21777f2` |
- `33c21777f2` zip sha256: `9b1a1bfda345e61a8a5c8cf067a2c9450c941a876a5bc7c29fa4ca6d2feba89b` (17404 files, 1.5G; filename scan clean; monolithic upload hit the known GitHub stream error (looping re-reads), so uploaded fifteen ~100 MB parts p100m-aa..ao instead)
| `ac424c7ab5` | 2026-10-06T23:47:00Z | 2026-10-07 EDT | see release `build-ac424c7ab5` |
- `ac424c7ab5` zip sha256: `17f5320329b73f42ceb841ad8097a8adb60be0ed8b24b517a4f4ebe419f14b2e` (17404 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip; monolithic upload stalled with zero progress for 15 min and was killed by timeout, same as builds e6ced0b136/16f6e81b2ce/33c21777f2; concatenated parts sha256 match the zip exactly)
| `2c1519b0c5` | 2026-10-07T02:44:32Z | 2026-10-07 EDT | see release `build-2c1519b0c5` |
- `2c1519b0c5` zip sha256: `0f3b6673e7519de93dfc0be73304c882a8fba0ee673e4a0447e762a9b34fc48a` (17404 files, 1.5G; filename scan clean; manifest personal-data scan clean; only node_modules files with token/secret in their own filenames, same benign pattern as prior builds; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `b07b138c86` | 2026-10-07T05:09:32Z | 2026-10-07 EDT | see release `build-b07b138c86` |
- `b07b138c86` zip sha256: `d66d8b5d4caae10137d849f372d79b008b59702dc3f8eb3850b1f1ac417e9aa2` (17397 files, 1.4G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; monolithic upload stalled with zero progress for ~10 min and was killed, same as builds e6ced0b136/16f6e81b2ce/33c21777f2/ac424c7ab5; concatenated parts sha256 match the zip exactly)
| `3ce7bb6229` | 2026-10-07T07:22:58Z | 2026-10-07 EDT | see release `build-3ce7bb6229` |
- `3ce7bb6229` zip sha256: `09f9c65294c0b8df19dd0fe3331ce1569dbf03a97177ca69a93d5559ce176c17` (17397 files, 1.4G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip; monolithic upload stalled with zero progress for ~13 min and was killed, same as builds e6ced0b136/16f6e81b2ce/33c21777f2/ac424c7ab5/b07b138c86; concatenated parts sha256 match the zip exactly)
| `2963b89331` | 2026-10-07T09:30:31Z | 2026-10-07 EDT | see release `build-2963b89331` |
- `2963b89331` zip sha256: `a4b324e929e706cb1ca31331f385333f1691af6fa5e65c1d03cad9a45aae5f0a` (17397 files, 1.4G; filename scan clean; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `c8269003fb` | 2026-10-07T11:10:34Z | 2026-10-07 EDT | see release `build-c8269003fb` |
- `c8269003fb` zip sha256: `fe74986ab260f04a98b4d98b878b9957ea3c13d3a9e4397c5870b08d1a0f0e46` (17397 files, 1.4G; filename scan clean; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `a06b011269` | 2026-10-07T14:55:58Z | 2026-10-07 EDT | see release `build-a06b011269` |
- `a06b011269` zip sha256: `b37b00511d36046a3a49306b3c5fa83172e193659a56ed2b3f2db92920eea6e0` (17398 files, 1.5G; filename scan clean; manifest personal-data scan clean; only node_modules files with token/secret in their own filenames, same benign pattern as prior builds; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `df18821260` | 2026-10-07T20:27:12Z | 2026-10-07 EDT | see release `build-df18821260` |
- `df18821260` zip sha256: `c9abe673d1405c20ea2fa25bc4de6d7f4058f4da1a0a78ebd5c5f1f25b606e18` (17398 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; fifteen ~100 MB parts p100m-aa..p100m-ao uploaded to the release instead of the monolithic zip; concatenated parts sha256 match the zip exactly)
| `d063baed68` | 2026-10-07T22:11:09Z | 2026-10-07 EDT | see release `build-d063baed68` |
| `336425023b` | 2026-10-08T01:44:34Z | 2026-10-08 EDT | release NOT created; GitHub API unreachable from VM this run (graphql context deadline exceeded on gh release list/view); local archive retained in snapshot/, upload deferred to a later run with working network |
- `336425023b` zip sha256: `550c58d75e6a055d19ac861e082ae478bd72b4c7b8423818f3ab1f2289fb56ea` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `ff1d6c5f74` | 2026-10-08T04:23:22Z | 2026-10-08 EDT | release NOT created; GitHub API unreachable from VM this run (gh token invalid, GraphQL Forbidden); local archive retained in snapshot/, upload deferred to a later run with working network. Commit fb0f688 LOCAL ONLY; push to origin/main failed this run (proxy CONNECT timeout to github.com); retry push + release upload on next run with working network |
- `ff1d6c5f74` zip sha256: `5e1672e0929f4dabcf266afa5ce9207ed9ab5853946859d8459122bd083bd895` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `ac4dcaf525` | 2026-10-08T06:14:10Z | 2026-10-08 EDT | release NOT created; GitHub API unreachable from VM this run (GraphQL Forbidden on gh release list); local archive retained in snapshot/, upload deferred to a later run with working network |
- `ac4dcaf525` zip sha256: `f37d4aed042e6aeaef5fe83a7d7a71b75a8c57940d916a6c2430da0ee39bee2e` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `d15a580998` | 2026-10-08T07:41:03Z | 2026-10-08 EDT | see release `build-d15a580998` |
- `d15a580998` zip sha256: `1860c24dd6495243f18719398e615a250172d295d6ee088961d99e467851b296` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `cc7cc90c54` | 2026-10-08T10:53:56Z | 2026-10-08 EDT | release `build-cc7cc90c54` created (page exists) but asset upload failed this run (gh exit 1 after ~25 min on the 1.5G monolithic zip, same stall pattern as prior builds); local archive retained in snapshot/, upload deferred to a later run with working network |
- `cc7cc90c54` zip sha256: `cd888befca87826b94273df5cdc7082fcc8f32b2fa05ae8eef9d1dfa3df96a96` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `c55d7c4efc` | 2026-10-08T12:20:35Z | 2026-10-08 EDT | release `build-c55d7c4efc` created (page exists) but asset upload failed this run (context deadline exceeded uploading the 1.5G monolithic zip, same stall pattern as prior builds); local archive retained in snapshot/, upload deferred to a later run with working network |
- `c55d7c4efc` zip sha256: `4100cfc9e8810070839364bf566c21ede217ed21a51693a2793e425d66a1880d` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `b0a7dd2527` | 2026-10-08T15:11:48Z | 2026-10-08 EDT | release `build-b0a7dd2527` created (page exists) but asset upload failed this run (403 Forbidden on uploads.github.com, twice; release-page API works, upload endpoint does not); local archive retained in snapshot/, upload deferred to a later run with working network |
- `b0a7dd2527` zip sha256: `10061590117804ed1be142da016cca1cd59bb8fc3e9dfe12231370503ddd7843` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `21533d58f0` | 2026-10-08T17:33:38Z | 2026-10-08 EDT | release `build-21533d58f0` created (manifest + exclusions uploaded); 1.5G zip upload exit 0 but asset missing from release after ~26 min; retried, local archive retained in snapshot/; verify + upload on next run |
- `21533d58f0` zip sha256: `39f7269dde5b708dc415914eeb1a2b87fe44d00f570fd662acdc6542d88c6d30` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `684373965f` | 2026-10-08T19:56:45Z | 2026-10-08 EDT | release `build-684373965f` created (page exists); zip upload queued this run |
- `684373965f` zip sha256: `dbe07e28e75e9ad6ee45f07d727e32b9a42e75906319b71771450397b7a779f3` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `0f3744c487` | 2026-10-09T02:04:05Z | 2026-10-09 EDT | release `build-0f3744c487` created (manifest + exclusions uploaded; zip upload in progress this run) |
| `b25683e243` | 2026-10-09T04:16:53Z | 2026-10-09 EDT | release `build-b25683e243` exists (created by earlier run 02:37 EDT; manifest + exclusions uploaded); archive assets already present locally from that run (redundant rebuild skipped this run); zip upload retried this run, local archive retained in snapshot/ until upload verified |
- `b25683e243` zip sha256: `80b6f7ae09131efe8feb07cb763762aa6b6f0c8e8138b8f6c95cbf0401f9de30` (1476781163 bytes)
| `2de5c3b889` | 2026-10-09T06:24:22Z | 2026-10-09 EDT | release `build-2de5c3b889` created; manifest + exclusions + 1.4G zip upload queued this run |
| `4db8f26109` | 2026-10-09T08:28:25Z | 2026-10-09 EDT | release `build-4db8f26109` created; manifest + exclusions uploaded; zip upload exit 0 on first attempt but asset missing from release (same stall pattern as 21533d58f0); retry in progress this run, local archive retained in snapshot/ until upload verified |
| `580e20ebc4` | 2026-10-09T09:49:53Z | 2026-10-09 EDT | release `build-580e20ebc4` exists (created by earlier run 10:37 EDT; manifest + exclusions uploaded); zip upload retried this run, local archive retained in snapshot/ until upload verified |
| `497a4794b4` | 2026-10-09T15:12:39Z | 2026-10-09 EDT | release `build-497a4794b4` created; manifest + exclusions + zip uploaded (exit 0) this run |
| `06191b3e25` | 2026-10-09T18:34:23Z | 2026-10-09 EDT | release `build-06191b3e25` created; manifest + exclusions + zip upload queued this run |
| `34001c0d79` | 2026-10-09T21:11:18Z | 2026-10-09 EDT | release `build-34001c0d79` created; manifest + exclusions uploaded (exit 0); zip upload in progress this run |
| `075d6865cb` | 2026-10-10T02:17:38Z | 2026-10-10 EDT | release `build-075d6865cb` created; manifest + exclusions + zip upload queued this run |
- `075d6865cb` zip sha256: `2fe23da010b3d3e86b73acf2cac0f348de580b10515dd6664a5ed2d9acb77baa` (1.4G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `29ff824780` | 2026-10-10T20:35:08Z | 2026-10-10 EDT | release `build-29ff824780` created; manifest + exclusions + 1.4G zip uploaded (exit 0) this run |
- `29ff824780` zip sha256: `eb291063813363f1e18f96924bd1c2d771a5d28dc13f357d4fc66eb39c3d581d` (1.4G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `5ac8cb8387` | 2026-10-11T10:03:17Z | 2026-10-11 EDT | release `build-5ac8cb8387` created; manifest + exclusions + 1.4G zip uploaded (exit 0, assets verified on release) this run |
- `5ac8cb8387` zip sha256: `2bc6d102d346df47a5a6a87ac1d69f72ac8870fd672224c2ac800d106f5fc46f` (1.4G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `5e0180d149` | 2026-10-12T02:49:58Z | 2026-10-12 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-5e0180d149) |
- `5e0180d149` zip sha256: `b67e33dee1e58910444afca0cec68bd342ec43c3177d5fedd50007d0ab33b2a3` (1.5G, 17591 files; release created 2026-10-12 05:37Z with manifest + exclusions only — zip stalled on egress and the row was never recorded; backfilled 2026-10-14 ~11:30 EDT by heartbeat via tools/chunked-release-upload.sh, 15/15 parts verified with sizes summing exactly to the local zip; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `4afddad4ff` | 2026-10-12T06:05:17Z | 2026-10-12 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-4afddad4ff) |
- `4afddad4ff` zip sha256: `27926de0889e3401081da3e9582fcaa6015403ef4cdabb07455252350e7af2dc` (1.5G, 17591 files; release created 2026-10-12 08:37Z with manifest + exclusions only — zip stalled on egress and the row was never recorded; backfilled 2026-10-14 ~11:30 EDT by heartbeat via tools/chunked-release-upload.sh, 15/15 parts verified with sizes summing exactly to the local zip; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `2911b7238e` | 2026-10-12T08:19:45Z | 2026-10-12 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-2911b7238e) |
- `2911b7238e` zip sha256: `43ba125d0c8a5f3eab363e33873c985165622a7a701e4be5fd425d750a0414bb` (1.5G, 17591 files; release created 2026-10-12 12:37Z with manifest + exclusions only — zip stalled on egress and the row was never recorded; backfilled 2026-10-14 ~11:30 EDT by heartbeat via tools/chunked-release-upload.sh, 15/15 parts verified with sizes summing exactly to the local zip; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `61a9cc60f6` | 2026-10-12T13:00:18Z | 2026-10-12 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-61a9cc60f6) |
- `61a9cc60f6` zip sha256: `b611328dde3cb61ca22fa721abaf1f5e6dc9a2f16dd78ac9010016c0633bf647` (1.5G, 17591 files; release created 2026-10-12 16:37Z with manifest + exclusions only — zip stalled on egress and the row was never recorded; backfilled 2026-10-14 ~11:30 EDT by heartbeat via tools/chunked-release-upload.sh, 15/15 parts verified with sizes summing exactly to the local zip; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `e8a1328f0c` | 2026-10-12T15:34:48Z | 2026-10-12 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-e8a1328f0c) |
- `e8a1328f0c` zip sha256: `606c3c642f708bc81095af6154b383b60c6875c8a0caa365551bd67fd1ecfad6` (1.5G, 17591 files; release created 2026-10-12 20:37Z with manifest + exclusions only — zip stalled on egress and the row was never recorded; backfilled 2026-10-14 ~11:30 EDT by heartbeat via tools/chunked-release-upload.sh, 15/15 parts verified with sizes summing exactly to the local zip; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `5ba69e5276` | 2026-10-12T20:55:53Z | 2026-10-12 EDT | release `build-5ba69e5276` created; manifest + exclusions + 1.4G zip uploaded (exit 0) this run |
| `f5920ce1a0` | 2026-10-13T01:39:32Z | 2026-10-13 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-f5920ce1a0) |
- `f5920ce1a0` zip sha256: `2f124687a8af841857119c49261f4ff8832f659e4abdf48616359be526d542c2` (1.5G; release created 2026-10-13 01:39Z with manifest + exclusions only — zip stalled on egress and the row was never recorded; backfilled 2026-10-14 ~09:06 EDT by rac-daily-self-check via tools/chunked-release-upload.sh, 15/15 parts verified with sizes summing exactly to the local zip; built-UTC shown is release-creation time, exact hatch build time unrecoverable from surviving records; manifest personal-data scan clean per 10/13 archive run)
| `a1253a8788` | 2026-10-13T05:39:38Z | 2026-10-13 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-a1253a8788) |
- `a1253a8788` zip sha256: `fd2e7333381c66767b6b08703007230be7ed07b70b869c1d18f799aaf8b9a529` (1.5G, 17591 files; release created 2026-10-13 09:37Z with manifest + exclusions only — zip stalled on egress and the row was never recorded; backfilled 2026-10-14 ~11:45 EDT by heartbeat via tools/chunked-release-upload.sh, 15/15 parts verified with sizes summing exactly to the local zip; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `bee17e6ff0` | 2026-10-13T08:04:11Z | 2026-10-13 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-bee17e6ff0) |
- `bee17e6ff0` zip sha256: `0c337cbabb5721985edd80663007d6d28c71a70aec8e5450e0a4b68e83cee12e` (1.5G, 17591 files; release created 2026-10-13 10:37Z with manifest + exclusions only — zip stalled on egress and the row was never recorded; backfilled 2026-10-14 ~11:45 EDT by heartbeat via tools/chunked-release-upload.sh, 15/15 parts verified with sizes summing exactly to the local zip; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `7183955fda` | 2026-10-13T09:33:30Z | 2026-10-13 EDT | release `build-7183955fda` created; manifest + exclusions + 1.5G zip uploaded (exit 0, assets verified on release) this run |
- `7183955fda` zip sha256: `1885e1ee29f7469588d27bb90aabadd326c9e25c3ef4412050404f54cf4b0e21` (1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly)
| `b353db1ee6` | 2026-10-13T11:46:57Z | 2026-10-13 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-b353db1ee6) |
- `b353db1ee6` zip sha256: `96fff28bd2d810e8da48c2fd64df49cd6d39321ae515b4a14f3e13a861b8b977` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `fe6b7aa74b` | 2026-10-13T12:05:58Z | 2026-10-13 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-fe6b7aa74b) |
- `fe6b7aa74b` zip sha256: `eb14da1cc1c76a64cef3e01d425c84165b9eb3ced6d24cbbf4db738922db9f3c` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `26fba473ce` | 2026-10-13T13:45:18Z | 2026-10-13 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-26fba473ce) |
- `26fba473ce` zip sha256: `625070e51a43e6932eb25c89368697074dc1386701519230ae3add94d0b06ce2` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `08fbc9ad96` | 2026-10-13T17:26:23Z | 2026-10-13 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-08fbc9ad96) |
- `08fbc9ad96` zip sha256: `c9b99ad4fcf8fd87d47b4b12ddd40867fe005bf25a42fff30e74b5cdbec094e6` (1.5G; chunked upload 15/15 parts verified on release; archive script scan initially hit the relocated dynamic_credentials.py false positive, allowlisted 2026-10-13, re-archived clean; manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `4f12cbe54f` | 2026-10-13T21:41:29Z | 2026-10-13 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-4f12cbe54f) |
- `4f12cbe54f` zip sha256: `724c5c64992845fa4ab40907188e1199144db92fba2849fbcbb595ce40e18337` (1.5G; release + 15/15 chunked zip parts created by the ~20:32 EDT run, which never recorded the row; this run verified all 15 parts present with sizes summing exactly to the local zip, applied what-changed notes vs a6404cd2a2, and recorded the row)
| `e673ca8c3c` | 2026-10-13T22:18:23Z | 2026-10-13 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-e673ca8c3c) |
- `e673ca8c3c` zip sha256: `ead662746b63a35eba7e5de44b7809573440977c059999464557552168486ccc` (1.5G; release + 15/15 chunked zip parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `f5843da50b` | 2026-10-14T03:15:37Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-f5843da50b) |
- `f5843da50b` zip sha256: `49a2ab56a09c4b8c05f3851bba6fdf8ee33ec3230d3114f7b09ab90042b3eec7` (1.5G; release + 16/16 chunked zip parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `a133d60349` | 2026-10-14T05:02:18Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-a133d60349) |
- `a133d60349` zip sha256: `71ca5677060901c3fe8a40af8c306ddd74867d98bed79727c298407972cd2f0a` (1.5G; chunked upload 16/16 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `56a65ffb0b` | 2026-10-14T06:18:34Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-56a65ffb0b) |
- `56a65ffb0b` zip sha256: `acd53033cc7e94174aef16408150dfb8b5e13e12e64af2fa06127b720aad10a4` (1.5G; chunked upload 16/16 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `d7770ee7b3` | 2026-10-14T06:45:14Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-d7770ee7b3) |
- `d7770ee7b3` zip sha256: `4e3899e29fea3e81555a3522e1d0e61104a452613512ef8a600bb60cb2b6133c` (1.5G; chunked upload 16/16 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `bec1f1db5c7` | 2026-10-14T08:59:53Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-bec1f1db5c7) |
- `bec1f1db5c7` zip sha256: `e6ddef38f07d6f235334f9f77219267dbf9b30b5be7622a4e8c0c41000bd53e6` (1.5G; chunked upload 16/16 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `6867ad2c26` | 2026-10-14T10:13:16Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-6867ad2c26) |
- `6867ad2c26` zip sha256: `28af23c7098b321b9267eb503c81a46462acaa03541a4ce9630eef6d696772df` (1.5G; chunked upload 16/16 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `b507f21a59` | 2026-10-14T10:35:25Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-b507f21a59) |
- `b507f21a59`: 16/16 chunked zip parts on release verified 2026-10-14 14:51 EDT via `gh release view --json assets` (15×104857600 + 24297967 = 1597161967 bytes ≈ 1.5G; manifest + exclusions present). Local zip already purged, so no local sha256 to record; evidence is the release-side asset inventory.
| `d16ac497f5` | 2026-10-14T13:53:56Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-d16ac497f5) |
- `d16ac497f5` zip sha256: `959d3d02a2f1e54ff14822d420e1e161bdb914cccbb194fe2d4db57004cff2b` (1.5G; chunked upload 16/16 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `519a362c8d` | 2026-10-14T15:48:27Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-519a362c8d) |
- `519a362c8d` zip sha256: `d63b756938f42c302ec9464bc263d433c69e940e54a2b67a84539678f509dbf3` (1.5G; chunked upload 16/16 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `3e4a6689d3` | 2026-10-14T18:41:53Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-3e4a6689d3) |
| `dcf9116ec3` | 2026-10-14T21:00:53Z | 2026-10-14 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-dcf9116ec3) |
| `ccfc5fa9ec` | 2026-10-15T01:22:25Z | 2026-10-15 EDT | see release `build-ccfc5fa9ec` |
- `ccfc5fa9ec` zip sha256: `92d7bbc4efdbff21917edc3cabb6885a2f1b20bed28dc318cd34b472bc9cea49` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `4f010fe3dc` | 2026-10-15T03:35:43Z | 2026-10-15 EDT | see release `build-4f010fe3dc` |
- `4f010fe3dc` zip sha256: `0230feac62bb74581fb7646b126eea2bc03335c57cc99d9b7c88e4891cd8704d` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `71a013d0a3` | 2026-10-15T05:22:43Z | 2026-10-15 EDT | see release `build-71a013d0a3` |
- `71a013d0a3` zip sha256: `177350423090f23103ecf68aa1c43fbffd66cb40c53a7b5df1fa5b3820d99399` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `3d56c8cc4d` | 2026-10-15T06:07:36Z | 2026-10-15 EDT | see release `build-3d56c8cc4d` |
| `e5fe71154e` | 2026-10-15T15:24:29Z | 2026-10-15 EDT | see release `build-e5fe71154e` |
- `e5fe71154e` zip sha256: `ef083f823aca7183909f3cbfeff1cfd3e111a497dbb73c1d2d9dfb02682cf957` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `b4bc885b2e` | 2026-10-15T16:36:05Z | 2026-10-15 EDT | see release `build-b4bc885b2e` |
- `b4bc885b2e` zip sha256: `644e75da02e2425251fb655409c6434f93e9c9d25c707ecfc75dadd9e2262afb` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `68f30130d0` | 2026-10-15T18:34:41Z | 2026-10-15 EDT | see release `build-68f30130d0` |
- `68f30130d0` zip sha256: `0892c83640fba8423a33ab92ceb3238039e065ce05442337671c159737b7f815` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `ad9d6a3ee0` | 2026-10-15T19:51:07Z | 2026-10-15 EDT | see release `build-ad9d6a3ee0` |
- `ad9d6a3ee0` zip sha256: `0c0bd12012c453e624f831471d894ab8680369597c9a0529b0d6259e2619ed11` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `60383d0c0c` | 2026-10-16T08:21:08Z | 2026-10-16 EDT | see release `build-60383d0c0c` |
- `60383d0c0c` zip sha256: `4f7a40e74f868b891178859dc001e4a37b81e16e37e1cf4167fdbb658341e6df` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `db6b809d7b` | 2026-10-16T10:48:46Z | 2026-10-16 EDT | see release `build-db6b809d7b` |
- `db6b809d7b` zip sha256: `c2cab80f40e638d168deac1c9db7fd35484d12cf565c5e2b6cc384d4adbe33ff` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `00a9d8a198` | 2026-10-16T13:01:45Z | 2026-10-16 EDT | see release `build-00a9d8a198` |
- `00a9d8a198` zip sha256: `57e1f2dc91d1b42b762012fb5b9fdbdfaa5e39cc1edb8f95f8d57ff936b81b04` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `f44ea22583` | 2026-10-16T14:53:28Z | 2026-10-16 EDT | see release `build-f44ea22583` |
| `89a110e1b8` | 2026-10-16T17:03:57Z | 2026-10-16 EDT | see release `build-89a110e1b8` |
- `89a110e1b8` zip sha256: `dd2a6196f39b10a037253f1caef033f96050e424dc2e5e0e348cadede9077567` (1.5G; chunked upload 15/15 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `e09891f9d9` | 2026-10-17T00:43:02Z | 2026-10-17 EDT | see release `build-e09891f9d9` |
- `e09891f9d9` zip sha256: `9cbb3ddfccfdcba48ae806aa611ea5c5a0705f95063a3f39d61b5cc9b740d2d7` (1.7G; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `1edbd71531` | 2026-10-17T04:40:42Z | 2026-10-17 EDT | see release `build-1edbd71531` |
- `1edbd71531` zip sha256: `36cd7d794f3957310b4da59dd47d0728c5974c5cdd8275baa7f9f2a9955045b5` (1.7G; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `09ec1ab112` | 2026-10-17T07:24:28Z | 2026-10-17 EDT | see release `build-09ec1ab112` |
- `09ec1ab112` zip sha256: `382ac7ce570805f2932927e52ba6e730da979cf0bb215cd63335118cd931680d` (1.7G; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `452007da9b` | 2026-10-17T10:24:54Z | 2026-10-17 EDT | see release `build-452007da9b` |
- `452007da9b` zip sha256: `be83218599931fa8a8ce1c0c06500bd757a9725c76c8ce8adcee6dd8b09dc47f` (1.7G; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `863b27ffab` | 2026-10-17T16:46:39Z | 2026-10-17 EDT | see release `build-863b27ffab` |
- `863b27ffab` zip sha256: `03a99f291910274455e406e4ff0324999465e9854e29dbeb845b7ab7021cd48a` (1750569117 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits)
| `5eb0f6a857` | 2026-10-17T19:58:53Z | 2026-10-17 EDT | see release `build-5eb0f6a857` |
- `5eb0f6a857` zip sha256: `b8458e57aa5a90d414fe01f75c9eb4e2f6aa447e2db279f758d713d3ffe95f08` (1750326271 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; local parts deleted after verify)
| `cd99f2e76d` | 2026-10-17T22:48:21Z | 2026-10-17 EDT | see release `build-cd99f2e76d` |
- `cd99f2e76d` zip sha256: `5431feac4b3e4001c33f989af4c51e4ffdea907997c1f368bc79364e859c0830` (1750508502 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; no mike/mzio/passwd/shadow hits; local parts deleted after verify)
| `cfa4ab70d6` | 2026-10-18T00:40:50Z | 2026-10-18 EDT | see release `build-cfa4ab70d6` |
- `cfa4ab70d6` zip sha256: `20e668abd0b1921379db326d966eaf106ed12933509f558c4c30c37c28dbac56` (1751004970 bytes; chunked upload 17/17 parts verified on release, part sizes sum to local zip; what-changed notes on release; git commit 212cbf3 pushed)
| `90791a36f8` | 2026-10-18T04:26:57Z | 2026-10-18 EDT | see release `build-90791a36f8` |
- `90791a36f8` zip sha256: `4a2522cfe27f179bda3db7cbd958c7418dd6d20852ace90ecb1a88dbb8da91ad` (1751021666 bytes; chunked upload 17/17 parts verified on release; what-changed notes on release; local parts deleted after verify)
| `cace28c471` | 2026-10-18T05:37:33Z | 2026-10-18 EDT | see release `build-cace28c471` |
- `cace28c471` zip sha256: `28e4f0ddc217e27648817a4c44695decd5ba2123fce8f55be27c40ad7b8f4163` (1751023626 bytes; chunked upload 17/17 parts verified on release; what-changed notes on release; local parts deleted after verify)
| `3303ee8d62` | 2026-10-18T08:18:46Z | 2026-10-18 EDT | see release `build-3303ee8d62` |
- `3303ee8d62` zip sha256: `c1b57ac893cf2024254eb38eea2b7d2ccdb32745ec72d78e4bebf6dccc8ad8d6` (1751122522 bytes; chunked upload 17/17 parts verified on release, part sizes sum to local zip; what-changed notes on release)

| `4480daceda` | 2026-10-18T09:35:08Z | 2026-10-18 EDT | see release `build-4480daceda` |
- `4480daceda` zip sha256: `88638eb89aa0b3728f1a50391bad673fbc102c329f9cf877960969bf50a12fca` (1751163169 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)

| `6421718da2` | 2026-10-18T10:24:11Z | 2026-10-18 EDT | see release `build-6421718da2` |
- `6421718da2` zip sha256: `aa711691167346bcdb7789565583d235ca28c2d38b6e579ac316440c88c29927` (1751331458 bytes; chunked upload 17/17 parts verified on release; what-changed notes on release)

| `a35d064db0` | 2026-10-18T15:01:54Z | 2026-10-18 EDT | see release `build-a35d064db0` |
- `a35d064db0` zip sha256: `84c288987f7a2de450e672ba93a1afca633e831a45df410cbb89a19d251f4a89` (1751357157 bytes; chunked upload 17/17 parts verified on release; what-changed notes on release)

| `d6fc430403` | 2026-10-18T16:32:28Z | 2026-10-18 EDT | see release `build-d6fc430403` |
- `d6fc430403` zip sha256: `3907504ff3ea9a76253fb688ea2b1aab0228c5edbcb9998b08700d0e83744897` (1751221975 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)

| `721eab4386` | 2026-10-18T18:03:16Z | 2026-10-18 EDT | see release `build-721eab4386` |
- `721eab4386` zip sha256: `1b999c25f376649f98637d32dbee090683af17c6422ff4df497fe8a5b9ea4b8a` (1751303262 bytes; chunked upload 17/17 parts verified on release; what-changed notes on release)

| `01e521ee52` | 2026-10-18T20:12:12Z | 2026-10-18 EDT | see release `build-01e521ee52` |
- `01e521ee52` zip sha256: `77b6799ba4c20bad91997f52082c59fb0feae7be96e085b1af6afdd6820c82dc` (1751687316 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `8fe11732af` | 2026-10-18T21:15:13Z | 2026-10-18 EDT | see release `build-8fe11732af` |
- `8fe11732af` zip sha256: `96b007beddfe82ad87ae7a28e0922dfb12c2e7e121f27dd5abe4b9e1b96700f4` (1751530460 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| \`440142b7f0\` | 2026-10-18T23:29:50Z | 2026-10-18 EDT | see release \`build-440142b7f0\` |

| `2f0d2ccca9` | 2026-10-18T23:38:38Z | 2026-10-18 EDT | see release `build-2f0d2ccca9` |
- `2f0d2ccca9` zip sha256: `37b637a52b006869134ed0c1b5f95b8083f047faaedf4d53cf3bec9d3a260693` (1751723876 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `ae43885198` | 2026-10-19T00:28:36Z | 2026-10-19 EDT | see release `build-ae43885198` |
- `ae43885198` zip sha256: `0df369184fdc34d756cf39dc37d229b059a2d6803eea8e6324facd96f0da4cdc` (1751534528 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `5633119974` | 2026-10-19T03:10:28Z | 2026-10-19 EDT | see release `build-5633119974` |
- `5633119974` zip sha256: `3269facec4cd7b30366d24bcd33726e4303e86155f051e1c4140bc58570cf7f9` (1751483049 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)

| `8d6f38fcb6` | 2026-10-19T04:03:33Z | 2026-10-19 EDT | see release `build-8d6f38fcb6` |
- `8d6f38fcb6` zip sha256: `cdcd6102df4fb8d7ebe6f38212a303a49c5717f39bb9fff41364f54a86014984` (1751472795 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)

| `67ced200e6` | 2026-10-19T05:20:57Z | 2026-10-19 EDT | see release `build-67ced200e6` |
- `67ced200e6` zip sha256: `fef6faea10f2dd8425ab8198b672a0a4fc6922cd0ac77d4492e0812a06171702` (1751474384 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)

| `8de186e2f4` | 2026-10-19T06:30:01Z | 2026-10-19 EDT | see release `build-8de186e2f4` |
- `8de186e2f4` zip sha256: `11ed6454865873f7475f23662bfb9336fe2f6e996d3d7cea7529b6e164ffc98a` (1751403611 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `cf6d9fc785` | 2026-10-19T07:16:56Z | 2026-10-19 EDT | see release `build-cf6d9fc785` |
- `cf6d9fc785` zip sha256: `1cc94ac2eca2582e7a3122269c636f08dd7913cb95d5f9fc308eecc04f2923cc` (1751483049 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)

| `44b8733f01` | 2026-10-19T09:45:08Z | 2026-10-19 EDT | see release `build-44b8733f01` |
- `44b8733f01` zip sha256: `03aad8aba5e1d6313c1897f7a6f747c7fd80123dda57d63b77ff648f01e2a500` (1751409326 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)

| `4355616f68` | 2026-10-19T12:33:21Z | 2026-10-19 EDT | see release `build-4355616f68` |
- `4355616f68` zip sha256: `8e51135b75f5f9cb0b3709f9d14f129b50ad84baf4dec3138c42f5d3f471a0ef` (1751403007 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `1ab6d90545` | 2026-10-19T12:58:51Z | 2026-10-19 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-1ab6d90545) |
| `d6f9b9c783` | 2026-10-19T14:17:38Z | 2026-10-19 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-d6f9b9c783) |
- `d6f9b9c783` zip sha256: `d5fdc1ce12ea09285998026a642a17b525804cb3ec16a2e14879fcb2b7bbf428` (1751671470 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)

| `18e89944ec` | 2026-10-19T15:34:35Z | 2026-10-19 EDT | see release `build-18e89944ec` |
- `18e89944ec` zip sha256: `f8bb3c5ebe891c4f58b08202070e79b1ac08c36425b487f375e64fb783bf544c` (1751649558 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `e803a8c58b` | 2026-10-19T17:50:46Z | 2026-10-19 EDT | see release `build-e803a8c58b` |
- `e803a8c58b` zip sha256: `dffac7a9035f4f80af246454b1f30bfda50e0d0eda2fa2b7eeeefda2a7d3b6bd` (1751658938 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `0c8e9d2d08` | 2026-10-19T20:15:20Z | 2026-10-19 EDT | see release `build-0c8e9d2d08` |
- `0c8e9d2d08` zip sha256: `fb79aa7dd1e35c6df2490f20aeb5259978c9d43b8eff808ed1c322c095cddaa3` (1752456115 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `098bf5c481` | 2026-10-19T22:31:23Z | 2026-10-19 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-098bf5c4814) |
| `115589f45b` | 2026-10-19T23:39:43Z | 2026-10-19 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-115589f45b) |
- `115589f45b` zip sha256: `9160f4f4002ba96515585f1ee088c75d0efe2ad0c3f5a0e4016c4285da7e4902` (1752941410 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `1f81876ac3` | 2026-10-20T00:44:50Z | 2026-10-19 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-1f81876ac3) |
- `1f81876ac3` zip sha256: `def556c1cc5cd7fc2443589f6f09bc48325db5d0a880c60b6d07f4fcea4b3b62` (1753120047 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `7b97ff7b69` | 2026-10-20T01:21:53Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-7b97ff7b69) |
- `7b97ff7b69` zip sha256: `b25141995290d2fed6848b24bba2fa0cbc0b65655c7abf7d859c5e65286981ec` (1753720603 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `c92d6ba285` | 2026-10-20T01:21:21Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-c92d6ba285) |
- `c92d6ba285` zip sha256: `10552df5ef42ea19d09b2c130588600ac62894048e5e9cc766141e226c569025` (1753709429 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `f6ab5d2b1c` | 2026-10-20T03:58:48Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-f6ab5d2b1c) |
- `f6ab5d2b1c` zip sha256: `fb47d3de42e1f93f397ae5db5db1758a91dd0a03819466aa0a1a65d10bdc7354` (1754525044 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `b72a54c450` | 2026-10-20T04:23:58Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-b72a54c450) |
- `b72a54c450` zip sha256: `03852e1b15d07be384199f0f1b71c54a07595e3ebd3c02804ab31260b9848623` (1754557628 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `013a9e1a1c` | 2026-10-20T05:14:20Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-013a9e1a1c) |
- `013a9e1a1c` zip sha256: `68c7031f3341432ba1ee46430648ec01f2a5721450cd30d6d2c0ef87fd0528ec` (1754427376 bytes; chunked upload 17/17 parts verified on release; archive script exit 0 on retry after a VM-restart kill interrupted the first attempt's zip step; manifest personal-data scan clean; what-changed notes on release)
| `1d39f11dc5` | 2026-10-20T06:59:12Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-1d39f11dc5) |
- `1d39f11dc5` zip sha256: `bfd6c299509923b445a1488f378a7b59c7f5e37f6049b1799f617f42d7d5b867` (1754435007 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `5811edc446` | 2026-10-20T07:11:31Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-5811edc446) |
- `5811edc446` zip sha256: `8896e46717f275e2917a8732a770838683f0448cd3b2a1c74d62749542fba186` (1754481196 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `f005f10ced` | 2026-10-20T07:53:19Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-f005f10ced) |
- `f005f10ced` zip sha256: `8ca865d9392cea1f78617cc4824ac9ea986ddc5a3cb63976a41fdcfc0e9e40bb` (1754643144 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `e1bfbe55e1` | 2026-10-20T08:32:51Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-e1bfbe55e1) |
- `e1bfbe55e1` zip sha256: `5814f73c7136e9ca42c83e9201c7ae3eaf597d14d211e376a4157bcd3b736065` (1775512104 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `768f23fe50` | 2026-10-20T10:22:40Z | 2026-10-20 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-768f23fe50) |
- `768f23fe50` zip sha256: `df7880cb747f6fa0de2061da91b14de9c1a21f5466074d94e19aadc59795fd25` (1775513375 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `e3eef6add0` | 2026-10-20T11:53:32Z | 2026-10-20 11:31 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-e3eef6add0) |
- `e3eef6add0` zip sha256: `23d0d16e2b4830c3914e401e68b4f5e6ec61531880efb9326dbaf00fe859b47c` (1775510026 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `6a6bf271c4` | 2026-10-20T18:20:05Z | 2026-10-20 18:29 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-6a6bf271c4) |
- `6a6bf271c4` zip sha256: `f2a7fca5b1980ccd56a3d7044c5975788a3a889400d177e3b562be76e444fd81` (1777274727 bytes; chunked upload 17/17 parts verified on release; archive script exit 0 on prior run, manifest personal-data scan clean; what-changed notes on release)
| `7521ff50ec` | 2026-10-20T20:09:27Z | 2026-10-20 19:55 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-7521ff50ec) |
- `7521ff50ec` zip sha256: `46915b47465172464115127c349844a1c7faedf05beb0315c5169343b775c1bb` (1777572998 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `f4e71f55b5` | 2026-10-20T23:18:52Z | 2026-10-20 22:51 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-f4e71f55b5) |
- `f4e71f55b5` zip sha256: `fb2d62ed4d0ffbdc65a50d322be5fbdde6f3e1cd333e3f531e99b5d2da8319c8` (1777912250 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `88d4d027d8` | 2026-10-21T01:46:14Z | 2026-10-21 01:29 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-88d4d027d8) |
- `88d4d027d8` zip sha256: `09bc72c6cb16c5b5fa4e0cadea0ae02f8a9ff4637af4f0e056c915e223c87625` (1778929706 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `80ada07dcc` | 2026-10-21T03:53:45Z | 2026-10-21 02:29 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-80ada07dcc) |
- `80ada07dcc` zip sha256: `d68aa9ac28792611ca8192782d7ff29f7b4105ee0f886652133f18e0bdaa5703` (1778414513 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `7d04916af8` | 2026-10-21T08:34:23Z | 2026-10-21 07:51 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-7d04916af8) |
- `7d04916af8` zip sha256: `e3a9ec67d7ee3e28d5c50125e3874e7a9d9960dbe1714227c2d28f289e9f620b` (1781457763 bytes; chunked upload 17/17 parts verified on release; archive script exit 0 after two repairs (overlay-mount chown fix + .stagged-uploads exclusion), manifest personal-data scan clean; what-changed notes on release)
| `1d1c171fb0` | 2026-10-21T10:32:34Z | 2026-10-21 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-1d1c171fb0) |
- `1d1c171fb0` zip sha256: `519434713b6d8e4ee56a77188d4db8edee7f99cde795274afacaa38050a5cad7` (1781243144 bytes; chunked upload 17/17 parts verified on release; manifest personal-data scan clean; what-changed notes on release)
| `486064ea8d` | 2026-10-21T11:47:53Z | 2026-10-21 10:30 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-486064ea8d) |
- `486064ea8d` zip sha256: `f1aa76e70e5bb69079835e549a55408ee0cf6eb0154593e50ed6a78ea639299d` (1781221030 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `deaba5214f` | 2026-10-21T13:14:48Z | 2026-10-21 12:52 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-deaba5214f) |
- `deaba5214f` zip sha256: `fade19604f8be13eccd47bc6bb29b807df8e496b0d15c9a784cb806eb03769e6` (1781003180 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `e904e1f885` | 2026-10-21T14:54:59Z | 2026-10-21 15:30 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-e904e1f885) |
- `e904e1f885` zip sha256: `4a2e0df4bb30b818ed7d6afe18f644c693545f9f1a8462b76b0d7240f6a70e3d` (1781057218 bytes; chunked upload 17/17 parts verified on release; archive + release + what-changed notes completed by prior 14:32 EDT run, builds.md row written this run)
| `0279d5bc8b` | 2026-10-21T17:47:09Z | 2026-10-21 17:51 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-0279d5bc8b) |
| `955c893682` | 2026-10-21T18:38:41Z | 2026-10-21 18:51 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-955c893682) |
- `955c893682` zip sha256: `e989c8c328f70a6d97c02661d4aa1a49035ed92265b4a1e4339d3c7edd5f96df` (1782522663 bytes; chunked upload 17/17 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `8f5a4fa6cb` | 2026-10-21T23:15:42Z | 2026-10-21 22:29 EDT | [Release](https://github.com/mikezio/muse-runtime/releases/tag/build-8f5a4fa6cb) |
- `8f5a4fa6cb` zip sha256: `b1089d5b4d0698110c3d48eeff58b9234a64c154da43a7963bdaae416b7d9a22` (1784328490 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `994ca06e2d` | 2026-10-22T00:25:39Z | 2026-10-22 EDT | see release `build-994ca06e2d` |
- `994ca06e2d` zip sha256: `3b23b8bb74efdcc688f291fc6cb8670d440dca8fff4253b0355f89f53ad435c1` (1787201963 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `5990826e25` | 2026-10-22T03:44:10Z | 2026-10-22 EDT | see release `build-5990826e25` |
- `5990826e25` zip sha256: `6f371f304023560495c4094a29ee0003db92a290f0c3d9ca251e92f9121f2ac2` (1788717627 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `8b82da8f82` | 2026-10-22T05:06:41Z | 2026-10-22 EDT | see release `build-8b82da8f82` |
- `8b82da8f82` zip sha256: `8b4b8e202d9f24ba1dc6aad60c5dd9cd69588076347c54e7acc6ed37c1909582` (1789473100 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `064233055c` | 2026-10-22T06:35:12Z | 2026-10-22 EDT | see release `build-064233055c` |
- `064233055c` zip sha256: `2e5375fb4d5644aa3e848cb24bb65ce95c3d54a7f8a2fd2c26e11c5bef5e8377` (1789703704 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `5367b57283` | 2026-10-22T08:46:40Z | 2026-10-22 EDT | see release `build-5367b57283` |
- `5367b57283` zip sha256: `f23e68ea2ec3afb8b3ff83c0321f596a33c5f63ed3be87ce2727ed46693a9aab` (1789780769 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `1b3b809b8b` | 2026-10-22T11:27:56Z | 2026-10-22 EDT | see release `build-1b3b809b8b` |
- `1b3b809b8b` zip sha256: `c7ea65b235d1d77723b51ef03f5095a6c0176fc3a5a3fa2d377dc6bf8e794d6e` (1789780666 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `5f4bb5f79f` | 2026-10-22T13:09:27Z | 2026-10-22 EDT | see release `build-5f4bb5f79f` |
- `5f4bb5f79f` zip sha256: `25fa109e090a428d4e26ff46f08f1c829570d6393005264723311e1cf080013c` (1790788835 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `89b873f3ec` | 2026-10-22T14:32:08Z | 2026-10-22 EDT | see release `build-89b873f3ec` |
- `89b873f3ec` zip sha256: `b00c573aaddf7194b7e533273c5f5c3905e2bc0ce78172c3c29c7c3f80e6eb4a` (1790805822 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `940f1a8368` | 2026-10-22T16:31:47Z | 2026-10-22 EDT | see release `build-940f1a8368` |
- `940f1a8368` zip sha256: `833a6c39506fab2abf57238da3e600049b84f987c3d787c3d67e92ccbb4163b9` (1791126376 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `f181c0d811` | 2026-10-22T18:57:22Z | 2026-10-22 EDT | see release `build-f181c0d811` |
- `f181c0d811` zip sha256: `f770d9c4774e9be876f93326fc248952087f13ac412c49a999ff8b7eecc30d96` (1790931287 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `9a4eb56798` | 2026-10-22T20:30:23Z | 2026-10-22 EDT | see release `build-9a4eb56798` |
- `9a4eb56798` zip sha256: `c878ac292f71954ae4d9a64fc6aa5f3985f7ca7fd7ca3ee2d5ada2fa6a377c65` (1791047583 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `92c304f261` | 2026-10-23T02:07:45Z | 2026-10-23 EDT | see release `build-92c304f261` |
- `92c304f261` zip sha256: `fb54e911ea59786ee824280d78d38233f16ff4a9839fefca1a974716addb277f` (1792303122 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `babff4e47e` | 2026-10-23T02:05:44Z | 2026-10-23 EDT | see release `build-babff4e47e` |
- `babff4e47e` zip sha256: `c5d8bf37ae8ff5444bde3ba25dba347c2d656d563a0a32ba5da89d2b34715e04` (1792323486 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `c6187b72fc` | 2026-10-23T07:11:06Z | 2026-10-23 EDT | see release `build-c6187b72fc` |
- `c6187b72fc` zip sha256: `b5c2170482825d05c5a9c4de0a03e4a4b3e380d5deb8c2bdeb2774d7e708ae1c` (1793424007 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `0bf1debf76` | 2026-10-23T07:21:49Z | 2026-10-23 EDT | see release `build-0bf1debf76` |
- `0bf1debf76` zip sha256: `b83b692ac5b790c3f5eafed875eb9917b02683cf3e3e70de876ced1fc620c26d` (1793516060 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
| `3983555078` | 2026-10-23T09:19:48Z | 2026-10-23 EDT | see release `build-3983555078` |
- `3983555078` zip sha256: `ac97bcad478cd7c46ca0d05adeae29e1bbdd72be5e48e066e4e19b604b5418ab` (1793512314 bytes; chunked upload 18/18 parts verified on release; archive script exit 0, manifest personal-data scan clean; what-changed notes on release)
