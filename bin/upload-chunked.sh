#!/bin/bash
# Upload a large release asset to a GitHub release in chunks.
# Root cause (2026-09-25): uploads through the sandbox egress proxy fail with
# "unexpected EOF" on single files ~1GB+, while small files upload fine.
# So we split into 200MB parts and upload those instead.
# Usage: upload-chunked.sh <release-tag> <file> [chunk-size]
set -euo pipefail
TAG="${1:?release tag required}"
FILE="${2:?file required}"
CHUNK="${3:-200M}"
REPO="mikezio/muse-runtime"

BASENAME="$(basename "$FILE")"
# NOTE: /tmp is a 512MB tmpfs, too small for GB-scale chunks. Stage on the
# workspace disk instead (trap cleans up on exit).
WORKDIR="$(mktemp -d -p ~/workspace .chunks-XXXXXX)"
trap 'rm -rf "$WORKDIR"' EXIT

echo "splitting $FILE into $CHUNK chunks..."
split -b "$CHUNK" -d --suffix-length=2 "$FILE" "$WORKDIR/$BASENAME.part-"

echo "uploading parts to $TAG..."
for part in "$WORKDIR"/$BASENAME.part-*; do
  pname="$(basename "$part")"
  echo "  $pname ($(du -h "$part" | cut -f1))"
  gh release upload "$TAG" --repo "$REPO" "$part" --clobber
done

echo "done. reassemble with: cat $BASENAME.part-* > $BASENAME"
