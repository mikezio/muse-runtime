# Turn the runtime archives into useful evidence

The [release assets](https://github.com/mikezio/muse-runtime/releases) let you
compare shipped tools, skill instructions, schemas and binaries between builds.
Start with the small manifests. Download a full archive only when a changed file
is relevant to the question you are investigating.

These archives capture a **live instance**, including some installed additions.
A file appearing in an archive does not establish that Meta shipped it, that it
was enabled for the account, or that the running daemon used it.

## What each artifact tells you

| Artifact | What it contains | Useful for |
|---|---|---|
| [builds.md](../builds.md) | Observed build IDs, build timestamps, release references and upload notes | Finding two builds to compare |
| [snapshot/runtime-info.json](../snapshot/runtime-info.json) | Current snapshot time, archive tag, build ID, build time and regular-file count | Linking the checked-in tree to one capture |
| [snapshot/home-tree.txt](../snapshot/home-tree.txt) | Names of staged paths, including `home/` and `opt/` | Finding likely components without downloading their contents |
| `*.manifest.txt` release asset | One SHA256, byte count and relative path per regular file | Detecting additions, removals and content changes |
| `*.exclusions.txt` release asset | Excluded paths and reasons for that capture | Understanding missing evidence |
| `*.zip` or `*.zip.part-*` release assets | Staged file contents rooted at `runtime/` | Reading relevant scripts, skills, schemas and binary metadata |
| [snapshot/files/](../snapshot/files/) | A few curated, redacted example files | Reading examples directly on GitHub |

`runtime/home/` corresponds to the instance's home directory; `runtime/opt/`
corresponds to `/opt/hatch/`. It is **not** a copy of all of `/opt/`.
The archiver omits `/opt/hatch-image` and several personal, credential and working
directories. Check each release's exclusions rather than assuming completeness.
The checked-in tree lists directories as well as files, so its line count will
not match the manifest's regular-file count.

The snapshot time is when the capture ran. The build time describes the runtime
build. Neither is necessarily the release publication time. Prefer those fields
over row order in `builds.md`, whose entries may have been backfilled.

## Compare two builds without downloading their ZIPs

The following commands run from the repository root. Set the two release tags
to the builds you want to inspect. GitHub CLI (`gh`) is only needed for downloading;
the comparison script itself uses Python's standard library.

```sh
old_tag=build-49d7dfcc81f
new_tag=build-1eefe22acda
compare_dir=$(mktemp -d "${TMPDIR:-/tmp}/muse-compare.XXXXXX")
mkdir "$compare_dir/old" "$compare_dir/new"
gh release download "$old_tag" --repo mikezio/muse-runtime \
  --pattern '*.manifest.txt' --pattern '*.exclusions.txt' --dir "$compare_dir/old"
gh release download "$new_tag" --repo mikezio/muse-runtime \
  --pattern '*.manifest.txt' --pattern '*.exclusions.txt' --dir "$compare_dir/new"
python3 tools/compare-manifests.py \
  "$compare_dir/old"/*.manifest.txt "$compare_dir/new"/*.manifest.txt
```

Use an empty directory for each download and confirm it contains exactly one
manifest. The tool takes exactly two paths, with the older manifest first.

Narrow the output to a component or produce JSON for another script:

```sh
python3 tools/compare-manifests.py OLD.manifest.txt NEW.manifest.txt \
  --prefix opt/skills --limit 30
python3 tools/compare-manifests.py OLD.manifest.txt NEW.manifest.txt \
  --json --limit 0 > counts.json
```

The output includes added, removed, changed and unchanged counts, total file
bytes and their difference. Paths are sorted. By default, at most 20 paths per
category are displayed, including in JSON; omitted counts remain visible.
`--limit 0` gives totals only. `--prefix` matches a complete path or directory
boundary, so `opt/skills` will not also match `opt/skills-old`.
All counts and byte totals refer to the selected prefix if one is supplied.
Exit status is `0` for a successful comparison even when files changed, and `2`
for invalid input or unreadable files.

For the two releases in the download example, the manifests contain 17,209 and
17,210 files. Comparison found 16 added, 15 removed and 85 changed files. Under
`opt/skills`, only one file was added and four changed: a much smaller reading
list than the complete 1.2 GB archive. These are observations from those two
captures, not an attribution of every change to the runtime update.

### Manifest format and limits

The format written by [archive-runtime.sh](../tools/archive-runtime.sh) is:

```text
<64 hexadecimal SHA256 characters>  <size in bytes>  ./opt/skills/example/SKILL.md
```

The fields use two spaces. Spaces within a path are supported. The comparison
tool rejects malformed rows, duplicate normalized paths, absolute paths,
traversal components, control characters and backslash-escaped filenames. It
only reads the two manifests; it does not follow their paths, extract files,
run archive contents or contact the network.

The current archive script's line-oriented hash pipeline is not a lossless
encoding for every possible Unix filename. Backslash and newline names require
an archiver format change, not guessing during comparison. Empty manifests are
valid inputs to represent an empty set of files.

A changed hash proves a difference in recorded file contents. It does not
explain the behavior change. Changes may reflect a local addition or a revised
exclusion policy. File permissions, ownership, timestamps, directories and
symlink targets are not represented by this regular-file manifest. A rename
appears as a removal plus an addition. Compare the exclusions alongside the
manifest before writing a release analysis.

## Reassemble a split archive

Some releases contain one ZIP; others contain six pieces because long uploads
failed. Parts use either numeric (`part-00` … `part-05`) or alphabetic
(`part-aa` … `part-af`) suffixes. Inspect the assets for the specific release;
do not assume every release uses the same names, date suffix or part count.

For the numeric six-part release `build-1eefe22acda`, after downloading all six
parts into a new directory, concatenate their exact filenames in order:

```sh
base=runtime-archive-1eefe22acda-20260927.zip
cat "$base.part-00" "$base.part-01" "$base.part-02" \
    "$base.part-03" "$base.part-04" "$base.part-05" > "$base"
sha256sum "$base"
unzip -t "$base"
```

Use `aa` through `af` instead for an alphabetic six-part release. Check that all
expected parts are present with the expected sizes before concatenating.
Explicit part names avoid accidentally mixing builds or including stale parts.

### Two different SHA256 checks

**The ZIP checksum** checks the complete downloaded or reassembled ZIP. Compare
`sha256sum "$base"` with the ZIP digest published for that exact build in its
release notes or `builds.md`. For the example above, `builds.md` records
`462b6398aede5a390e7e8034a105d904372d626b2cf86e3bb05eb5ab63408e0a`.
If no independent ZIP digest is published, ZIP integrity testing is still
possible, but a trusted whole-archive SHA256 comparison is not.

**The per-file manifest** checks individual regular-file contents inside
`runtime/`. It does **not** contain the ZIP's checksum. Its additional size
column also means it is not directly compatible with `sha256sum -c`.
The comparison tool compares recorded digests; it does not verify ZIP contents
against them. `unzip -t` checks ZIP integrity, not the publisher's identity or
the runtime's behavior.

## Inspect the useful files first

List paths and print selected text files without running anything from the
archive:

```sh
unzip -Z1 "$base" | rg '^runtime/opt/(skills|bin|runtime-cell)/' | head -40
unzip -p "$base" runtime/opt/skills/spaces/SKILL.md | head -100
```

Choose the exact path from the listing; an example path may be absent in an
older build. Prefer skill instructions and schemas for interface questions,
scripts for configuration-loading questions, and binary metadata or strings
only when readable source is unavailable. A string in a binary can describe
retired, gated or unreachable code.

If extraction is necessary, inspect member names and link entries first and
use a fresh disposable directory. Do not unpack into a live runtime or execute
archived binaries merely to identify them. Extract only the files you need.

## Write findings with provenance

For each useful discovery, record:

- **Question:** what you were trying to determine.
- **Build and capture:** full release tag, build ID and snapshot timestamp.
- **Evidence:** exact archive member path and per-file hash, or the specific
  read-only runtime endpoint and observation time.
- **Observation:** what the file or response actually says.
- **Interpretation and limits:** what follows from it, and what still requires
  a live test, account entitlement or provider metadata.

For example, a new model ID in a compiled catalog is evidence that the string
exists in that build. Successful selection requires a separate runtime test;
a completed response requires another; the provider's actual model identity
may still be unavailable. Preserve those distinctions when updating the
architecture and model documentation.

Keep personal prompts, conversations, account IDs, cookies, tokens and private
device information out of contributed evidence. The archiver's filename
exclusions and post-stage scan are a backstop, not a complete content audit.
Do not run the archiver on an unrelated workstation: it stages that machine's
`$HOME` and `/opt/hatch`.

## Provenance of this guide and tool

Reviewed on 2026-09-28 against the checked-in archiver, `builds.md`, current
snapshot metadata, and the release manifest for `build-1eefe22acda`
(`runtime-archive-1eefe22acda-20260927.manifest.txt`). The parser was tested on
that real manifest, a comparison with `build-49d7dfcc81f`, and small fixtures for paths with spaces, added/removed/
changed files, output limits, directory boundaries and malformed input.
No full runtime archive was downloaded or executed for that validation.

Run the fixture tests with:

```sh
python3 -m unittest discover -s tools -p 'test_compare_manifests.py' -v
```
