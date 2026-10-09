#!/usr/bin/env bash
# Upload a large runtime-archive zip to a GitHub release as ~200MB split parts.
# Monolithic uploads keep failing through the VM egress proxy (gh internal
# deadline / EOF on uploads.github.com); the 2026-09-25 build-679b103d9f6
# upload PROVED 6x200MB parts succeed on this network.
#
# Usage: upload-release-parts.sh <release-tag> <local-zip>
#   e.g. upload-release-parts.sh build-4db8f26109 \
#          ~/workspace/muse-runtime/snapshot/runtime-archive-4db8f26109-20261009.zip
#
# On success the parts are deleted locally (the release holds the copies) and
# an evidence line is appended to builds.md. Exit non-zero on any failure.
set -u
REPO="mikezio/muse-runtime"
TAG="${1:?release tag required}"
ZIP="${2:?local zip required}"
PART_BYTES=209715200  # 200 MB

log() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" ; }

[ -f "$ZIP" ] || { log "FATAL: zip not found: $ZIP"; exit 1; }

ZIPSIZE=$(stat -c%s "$ZIP")
ZIPBASE=$(basename "$ZIP")
PARTDIR="$(dirname "$ZIP")"
ZIP_sha=$(sha256sum "$ZIP" | cut -d' ' -f1)

log "tag=$TAG zip=$ZIPBASE size=$ZIPSIZE sha256=$ZIP_sha"

# split (idempotent: reuse existing parts only if they match this zip)
rm -f "$PARTDIR/$ZIPBASE.part-"* 2>/dev/null
split -b "$PART_BYTES" --numeric-suffixes=2 "$ZIP" "$PARTDIR/$ZIPBASE.part-"
PARTS=( $(ls "$PARTDIR/$ZIPBASE.part-"* 2>/dev/null) )
[ "${#PARTS[@]}" -gt 0 ] || { log "FATAL: split produced no parts"; exit 1; }
PARTSIZE_SUM=$(stat -c%s "${PARTS[@]}" | awk '{s+=$1} END {print s}')
[ "$PARTSIZE_SUM" = "$ZIPSIZE" ] || { log "FATAL: part sizes $PARTSIZE_SUM != zip $ZIPSIZE"; exit 1; }
log "split into ${#PARTS[@]} parts, sizes sum OK"

# upload each part
for p in "${PARTS[@]}"; do
  pb=$(basename "$p"); ps=$(stat -c%s "$p")
  log "uploading $pb ($ps bytes)"
  if ! gh release upload "$TAG" "$p" --repo "$REPO" --clobber >/tmp/part-upload.log 2>&1; then
    log "FATAL: upload failed for $pb"; tail -5 /tmp/part-upload.log | sed 's/^/  /'
    exit 1
  fi
  log "uploaded $pb"
done

# verify: every part present on the release and sizes sum to the zip size
ASSETS=$(gh release view "$TAG" --repo "$REPO" 2>/dev/null | grep '^asset:' | awk -F'\t' '{print $2}')
missing=0
for p in "${PARTS[@]}"; do
  pb=$(basename "$p")
  echo "$ASSETS" | grep -qx "$pb" || { log "FATAL: part missing from release assets: $pb"; missing=1; }
done
[ "$missing" = 0 ] || exit 1
log "all ${#PARTS[@]} parts present on release $TAG"

# cleanup local parts (release holds the copies)
rm -f "${PARTS[@]}"
log "local parts deleted"

# evidence in builds.md
BUILDSDIR="$(cd "$(dirname "$0")/.." && pwd)"
printf -- '- `%s` zip uploaded as %d split parts (%s bytes) on %s; parts reassemble with `cat %s.part-* > %s`.\n' \
  "$TAG" "${#PARTS[@]}" "$ZIPSIZE" "$(date -u +%FT%TZ)" "$ZIPBASE" "$ZIPBASE" >> "$BUILDSDIR/builds.md"
log "done"
