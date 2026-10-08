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
- `c53c928944` zip sha256: `9c3cb94edff7102d1bb3cac98b92775b3af027ad8443211f583244be9061f9b5` (17456 files, 1.5G; filename scan clean; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip — monolithic upload failed with a GitHub stream error, parts uploaded clean; concatenated parts sha256 match the zip exactly)
| `3637018994` | 2026-10-04T07:34:29Z | 2026-10-04 EDT | see release `build-3637018994` |
- `3637018994` zip sha256: `f7497093c51e7429835bb5c51cbf5471bc232930379eb0fc698897475a9f0649` (17456 files, 1.5G; filename scan clean; seventeen ~100 MB parts p100m-00..p100m-16 instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `68a836d6ab` | 2026-10-04T17:10:36Z | 2026-10-04 EDT | see release `build-68a836d6ab` |
- `68a836d6ab` zip sha256: `c240662677651756c7bef0aaf92e5fa80defe5834a6e8cf8d05f74ebee1b0a25` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `ac28a8986f` | 2026-10-04T20:26:29Z | 2026-10-04 EDT | see release `build-ac28a8986f` |
- `ac28a8986f` zip sha256: `2a62080354de3fb98a9aaf7078ba6eb19601ed6cc9d0f7a92aadfb52622d72b4` (17456 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `1f8d50e25f` | 2026-10-04T23:18:44Z | 2026-10-04 EDT | see release `build-1f8d50e25f` |
- `1f8d50e25f` zip sha256: `cb223a628bf7194e670fdd491572a97680a052306045013a4fbb86bda0736b7b` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip; concatenated parts sha256 match the zip exactly)
| `9b13d3a12e` | 2026-10-05T02:19:15Z | 2026-10-05 EDT | see release `build-9b13d3a12e` |
- `9b13d3a12e` zip sha256: `da7e724b79172a5621f344771b105d7117456b4a9ce45a7cb6d2cd3039166dc9` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip — monolithic upload failed with a GitHub stream error, parts uploaded clean; concatenated parts sha256 match the zip exactly)
| `8d61278e1f` | 2026-10-05T05:48:40Z | 2026-10-05 EDT | see release `build-8d61278e1f` |
- `8d61278e1f` zip sha256: `f20a151de7c691b2596d4cd13f2eb268c5575e4dd369b9ce8892c33cba284a2d` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip — monolithic upload failed with a GitHub stream error, parts uploaded clean; concatenated parts sha256 match the zip exactly)
| `2746a87742` | 2026-10-05T08:10:33Z | 2026-10-05 EDT | see release `build-2746a87742` |
- `2746a87742` zip sha256: `1111df0324c089c29c7fdb9ad718d61d78ba83f3c82ce557a82384a79b8ae83e` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip — monolithic upload skipped for the known GitHub stream error; concatenated parts sha256 match the zip exactly)
| `364c657900` | 2026-10-05T15:56:04Z | 2026-10-05 EDT | see release `build-364c657900` |
- `364c657900` zip sha256: `6083c4d77a6ef91a5571505b9677ac69ed062b2ee27ee4cd75b2c624bb0bc732` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..ao instead of monolithic zip — monolithic upload skipped for the known GitHub stream error; concatenated parts sha256 match the zip exactly)
| `916c9d67b3` | 2026-10-05T22:00:01Z | 2026-10-05 EDT | see release `build-916c9d67b3` |
- `916c9d67b3` zip sha256: `9ea65a67f224e870d8e799a9ebead4845126fcc49672f747de977cb2dd08f7c2` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip — monolithic upload skipped for the known GitHub stream error; concatenated parts sha256 match the zip exactly)
| `b28c5b0249` | 2026-10-06T04:43:16Z | 2026-10-06 EDT | see release `build-b28c5b0249` |
- `b28c5b0249` zip sha256: `2a22495e786d41e5ab0564a0f005d3c49d07688e6cc7f1cdc5b5af195693ed06` (17454 files, 1.5G; manifest clean, no personal-data hits; monolithic upload clean)
| `f3c534f692` | 2026-10-06T06:45:48Z | 2026-10-06 EDT | see release `build-f3c534f692` |
- `f3c534f692` zip sha256: `6dcb2a3e164a6b466f5921b2b16655382bd3647f0a13b3291d8e6c597fb22ce5` (22335 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip — monolithic upload failed with a GitHub stream error; concatenated parts sha256 match the zip exactly)
| `3b4aa3a20a` | 2026-10-06T11:17:24Z | 2026-10-06 EDT | see release `build-3b4aa3a20a` |
- `3b4aa3a20a` zip sha256: `782cd621783d00e31e5018da34a2b418d019ba0ac37072a520e59134a96dc9a0` (17455 files, 1.5G; manifest clean, no personal-data hits)
| `99c8eb41f3` | 2026-10-06T14:27:23Z | 2026-10-06 EDT | see release `build-99c8eb41f3` |
- `99c8eb41f3` zip sha256: `759cdefc72b8bc8b9ade7c6a760c4f458bb6938da893d4402bb60a5a6645e8a7` (17455 files, 1.6G; manifest clean, no personal-data hits; monolithic upload clean)
| `e6ced0b136` | 2026-10-06T15:44:59Z | 2026-10-06 EDT | see release `build-e6ced0b136` |
- `e6ced0b136` zip sha256: `25d6031d35817360e0a80e7bf830a1c7f0f01bf2f53d2ab2956580924acae5ae` (17455 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip — monolithic upload failed with a GitHub stream error; concatenated parts sha256 match the zip exactly)
| `16f6e81b2ce` | 2026-10-06T17:29:49Z | 2026-10-06 EDT | see release `build-16f6e81b2ce` |
- `16f6e81b2ce` zip sha256: `56f91f55f6286bc3105aa95174940dfded3b7e43814b9bc8ace4542cdaa349c5` (17455 files, 1.5G; filename scan clean; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip — monolithic upload stalled with zero progress for ~24 min and was killed, same as builds f3c534f692 and e6ced0b136; concatenated parts sha256 match the zip exactly)
| `33c21777f2` | 2026-10-06T21:21:48Z | 2026-10-06 EDT | see release `build-33c21777f2` |
- `33c21777f2` zip sha256: `9b1a1bfda345e61a8a5c8cf067a2c9450c941a876a5bc7c29fa4ca6d2feba89b` (17404 files, 1.5G; filename scan clean; monolithic upload hit the known GitHub stream error (looping re-reads), so uploaded fifteen ~100 MB parts p100m-aa..ao instead)
| `ac424c7ab5` | 2026-10-06T23:47:00Z | 2026-10-07 EDT | see release `build-ac424c7ab5` |
- `ac424c7ab5` zip sha256: `17f5320329b73f42ceb841ad8097a8adb60be0ed8b24b517a4f4ebe419f14b2e` (17404 files, 1.5G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip — monolithic upload stalled with zero progress for 15 min and was killed by timeout, same as builds e6ced0b136/16f6e81b2ce/33c21777f2; concatenated parts sha256 match the zip exactly)
| `2c1519b0c5` | 2026-10-07T02:44:32Z | 2026-10-07 EDT | see release `build-2c1519b0c5` |
- `2c1519b0c5` zip sha256: `0f3b6673e7519de93dfc0be73304c882a8fba0ee673e4a0447e762a9b34fc48a` (17404 files, 1.5G; filename scan clean; manifest personal-data scan clean — only node_modules files with token/secret in their own filenames, same benign pattern as prior builds; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip — concatenated parts sha256 match the zip exactly)
| `b07b138c86` | 2026-10-07T05:09:32Z | 2026-10-07 EDT | see release `build-b07b138c86` |
- `b07b138c86` zip sha256: `d66d8b5d4caae10137d849f372d79b008b59702dc3f8eb3850b1f1ac417e9aa2` (17397 files, 1.4G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip — monolithic upload stalled with zero progress for ~10 min and was killed, same as builds e6ced0b136/16f6e81b2ce/33c21777f2/ac424c7ab5; concatenated parts sha256 match the zip exactly)
| `3ce7bb6229` | 2026-10-07T07:22:58Z | 2026-10-07 EDT | see release `build-3ce7bb6229` |
- `3ce7bb6229` zip sha256: `09f9c65294c0b8df19dd0fe3331ce1569dbf03a97177ca69a93d5559ce176c17` (17397 files, 1.4G; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip — monolithic upload stalled with zero progress for ~13 min and was killed, same as builds e6ced0b136/16f6e81b2ce/33c21777f2/ac424c7ab5/b07b138c86; concatenated parts sha256 match the zip exactly)
| `2963b89331` | 2026-10-07T09:30:31Z | 2026-10-07 EDT | see release `build-2963b89331` |
- `2963b89331` zip sha256: `a4b324e929e706cb1ca31331f385333f1691af6fa5e65c1d03cad9a45aae5f0a` (17397 files, 1.4G; filename scan clean; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-00..p100m-14 instead of monolithic zip — concatenated parts sha256 match the zip exactly)
| `c8269003fb` | 2026-10-07T11:10:34Z | 2026-10-07 EDT | see release `build-c8269003fb` |
- `c8269003fb` zip sha256: `fe74986ab260f04a98b4d98b878b9957ea3c13d3a9e4397c5870b08d1a0f0e46` (17397 files, 1.4G; filename scan clean; manifest clean, no personal-data hits; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip — concatenated parts sha256 match the zip exactly)
| `a06b011269` | 2026-10-07T14:55:58Z | 2026-10-07 EDT | see release `build-a06b011269` |
- `a06b011269` zip sha256: `b37b00511d36046a3a49306b3c5fa83172e193659a56ed2b3f2db92920eea6e0` (17398 files, 1.5G; filename scan clean; manifest personal-data scan clean — only node_modules files with token/secret in their own filenames, same benign pattern as prior builds; fifteen ~100 MB parts p100m-aa..p100m-ao instead of monolithic zip — concatenated parts sha256 match the zip exactly)
| `df18821260` | 2026-10-07T20:27:12Z | 2026-10-07 EDT | see release `build-df18821260` |
- `df18821260` zip sha256: `c9abe673d1405c20ea2fa25bc4de6d7f4058f4da1a0a78ebd5c5f1f25b606e18` (17398 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; fifteen ~100 MB parts p100m-aa..p100m-ao uploaded to the release instead of the monolithic zip — concatenated parts sha256 match the zip exactly)
| `d063baed68` | 2026-10-07T22:11:09Z | 2026-10-07 EDT | see release `build-d063baed68` |
| `336425023b` | 2026-10-08T01:44:34Z | 2026-10-08 EDT | release NOT created — GitHub API unreachable from VM this run (graphql context deadline exceeded on gh release list/view); local archive retained in snapshot/, upload deferred to a later run with working network |
- `336425023b` zip sha256: `550c58d75e6a055d19ac861e082ae478bd72b4c7b8423818f3ab1f2289fb56ea` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean — no mike/mzio/passwd/shadow hits)
| `ff1d6c5f74` | 2026-10-08T04:23:22Z | 2026-10-08 EDT | release NOT created — GitHub API unreachable from VM this run (gh token invalid, GraphQL Forbidden); local archive retained in snapshot/, upload deferred to a later run with working network. Commit fb0f688 LOCAL ONLY — push to origin/main failed this run (proxy CONNECT timeout to github.com); retry push + release upload on next run with working network |
- `ff1d6c5f74` zip sha256: `5e1672e0929f4dabcf266afa5ce9207ed9ab5853946859d8459122bd083bd895` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean — no mike/mzio/passwd/shadow hits)
| `ac4dcaf525` | 2026-10-08T06:14:10Z | 2026-10-08 EDT | release NOT created — GitHub API unreachable from VM this run (GraphQL Forbidden on gh release list); local archive retained in snapshot/, upload deferred to a later run with working network |
- `ac4dcaf525` zip sha256: `f37d4aed042e6aeaef5fe83a7d7a71b75a8c57940d916a6c2430da0ee39bee2e` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean — no mike/mzio/passwd/shadow hits)
| `d15a580998` | 2026-10-08T07:41:03Z | 2026-10-08 EDT | see release `build-d15a580998` |
- `d15a580998` zip sha256: `1860c24dd6495243f18719398e615a250172d295d6ee088961d99e467851b296` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean — no mike/mzio/passwd/shadow hits)
| `cc7cc90c54` | 2026-10-08T10:53:56Z | 2026-10-08 EDT | release `build-cc7cc90c54` created (page exists) but asset upload failed this run (gh exit 1 after ~25 min on the 1.5G monolithic zip, same stall pattern as prior builds); local archive retained in snapshot/, upload deferred to a later run with working network |
- `cc7cc90c54` zip sha256: `cd888befca87826b94273df5cdc7082fcc8f32b2fa05ae8eef9d1dfa3df96a96` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean — no mike/mzio/passwd/shadow hits)
| `c55d7c4efc` | 2026-10-08T12:20:35Z | 2026-10-08 EDT | release `build-c55d7c4efc` created (page exists) but asset upload failed this run (context deadline exceeded uploading the 1.5G monolithic zip, same stall pattern as prior builds); local archive retained in snapshot/, upload deferred to a later run with working network |
- `c55d7c4efc` zip sha256: `4100cfc9e8810070839364bf566c21ede217ed21a51693a2793e425d66a1880d` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean — no mike/mzio/passwd/shadow hits)
| `b0a7dd2527` | 2026-10-08T15:11:48Z | 2026-10-08 EDT | release `build-b0a7dd2527` created (page exists) but asset upload failed this run (403 Forbidden on uploads.github.com, twice; release-page API works, upload endpoint does not); local archive retained in snapshot/, upload deferred to a later run with working network |
- `b0a7dd2527` zip sha256: `10061590117804ed1be142da016cca1cd59bb8fc3e9dfe12231370503ddd7843` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean — no mike/mzio/passwd/shadow hits)
| `21533d58f0` | 2026-10-08T17:33:38Z | 2026-10-08 EDT | release `build-21533d58f0` created (manifest + exclusions uploaded); 1.5G zip upload exit 0 but asset missing from release after ~26 min — retried, local archive retained in snapshot/; verify + upload on next run |
- `21533d58f0` zip sha256: `39f7269dde5b708dc415914eeb1a2b87fe44d00f570fd662acdc6542d88c6d30` (17397 files, 1.5G; archive script exits non-zero on tar errors or scan hits and this archive completed cleanly; manifest personal-data scan clean — no mike/mzio/passwd/shadow hits)
