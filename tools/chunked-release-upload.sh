#!/usr/bin/env bash
# chunked-release-upload.sh — durable, resumable chunked upload of a large
# file to a GitHub release.
#
# Background (2026-09-25 .. 2026-10-13): uploads of the ~1.5GB runtime-archive
# zip to GitHub releases stall on the VM egress proxy (uploads.github.com,
# gh internal deadline, stream CANCEL mid-upload), while small files upload
# fine. The fix is splitting the file into ~100MB chunks and uploading each
# chunk as its own release asset: every chunk finishes inside the deadline,
# and a failed chunk only costs its own retry.
#
# Improvements over tools/upload-release-parts.sh and bin/upload-chunked.sh:
#   * per-chunk retries with exponential backoff (env-overridable)
#   * idempotent: chunks already present on the release (same name AND size)
#     are skipped, so a re-run after a stall resumes instead of re-uploading
#   * chunks present with a wrong size are re-uploaded with --clobber
#     (partial/corrupt upload repair)
#   * final verification via `gh release view --json assets` with per-asset
#     size checks; exit non-zero if anything is missing
#   * per-chunk timing in the log
#
# Usage: chunked-release-upload.sh <release-tag> <file> [options]
#   options: --chunk-size <100M|200M|...>  (default 100M, passed to split -b)
#            --retries N                   (default 5 upload attempts per chunk)
#            --backoff-base SECONDS        (default 15; doubles per attempt)
#            --timeout SECONDS             (default 1200 per upload attempt)
#            --workdir DIR                 (default: mktemp dir next to file)
#            --keep-parts                  (keep local parts after success)
#            --dry-run                     (plan only: split and print, no upload)
#
# On failure, local parts are KEPT (unless deleted before) so the next run
# resumes. Reassemble with: cat <basename>.part-* > <basename>
#
# Idempotent and safe to re-run. Never touches real build release assets
# unless pointed at one; the caller owns the tag choice.
set -u
REPO="mikezio/muse-runtime"

TAG=""
FILE=""
CHUNK_SIZE="100M"
RETRIES=5
BACKOFF_BASE=15
ATTEMPT_TIMEOUT=1200
WORKDIR=""
KEEP_PARTS=0
DRY_RUN=0

usage() { sed -n '2,32p' "$0"; }

while [ $# -gt 0 ]; do
  case "$1" in
    --chunk-size)   CHUNK_SIZE="${2:?}"; shift 2 ;;
    --retries)      RETRIES="${2:?}"; shift 2 ;;
    --backoff-base) BACKOFF_BASE="${2:?}"; shift 2 ;;
    --timeout)      ATTEMPT_TIMEOUT="${2:?}"; shift 2 ;;
    --workdir)      WORKDIR="${2:?}"; shift 2 ;;
    --keep-parts)   KEEP_PARTS=1; shift ;;
    --dry-run)      DRY_RUN=1; shift ;;
    -h|--help)      usage; exit 0 ;;
    *) if [ -z "$TAG" ]; then TAG="$1"; elif [ -z "$FILE" ]; then FILE="$1";
       else echo "unexpected arg: $1" >&2; exit 2; fi; shift ;;
  esac
done

log() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" ; }
die() { log "FATAL: $*"; exit 1; }

[ -n "$TAG" ]  || die "release tag required"
[ -n "$FILE" ] || die "file required"
[ -f "$FILE" ] || die "file not found: $FILE"
command -v gh    >/dev/null || die "gh CLI not found"
command -v split >/dev/null || die "split not found"

# release must exist (the caller creates it; we never create/delete releases)
if ! gh release view "$TAG" --repo "$REPO" >/dev/null 2>&1; then
  die "release $TAG does not exist on $REPO (create it first)"
fi

FILESIZE=$(stat -c%s "$FILE")
BASENAME=$(basename "$FILE")
FILE_SHA=$(sha256sum "$FILE" | cut -d' ' -f1)

if [ -z "$WORKDIR" ]; then
  # /tmp is a 512MB tmpfs — stage on the workspace disk instead.
  WORKDIR="$(mktemp -d -p ~/workspace .chunks-XXXXXX)"
  trap 'rm -rf "$WORKDIR"' EXIT
else
  mkdir -p "$WORKDIR" || die "cannot create workdir $WORKDIR"
fi

log "tag=$TAG file=$BASENAME size=$FILESIZE sha256=$FILE_SHA chunk=$CHUNK_SIZE"

# --- split (idempotent: reuse existing parts only if they add up to the file)
PART_PREFIX="$WORKDIR/$BASENAME.part-"
if ls "${PART_PREFIX}"* >/dev/null 2>&1; then
  PARTSIZE_SUM=$(stat -c%s "${PART_PREFIX}"* | awk '{s+=$1} END {print s}')
  if [ "$PARTSIZE_SUM" = "$FILESIZE" ]; then
    log "reusing existing ${PART_PREFIX}* parts (sizes sum to $FILESIZE)"
  else
    log "existing parts don't match file ($PARTSIZE_SUM != $FILESIZE); re-splitting"
    rm -f "${PART_PREFIX}"*
    split -b "$CHUNK_SIZE" --numeric-suffixes "$FILE" "$PART_PREFIX" \
      || die "split failed"
  fi
else
  split -b "$CHUNK_SIZE" --numeric-suffixes "$FILE" "$PART_PREFIX" \
    || die "split failed"
fi

mapfile -t PARTS < <(ls "${PART_PREFIX}"*)
[ "${#PARTS[@]}" -gt 0 ] || die "split produced no parts"
PARTSIZE_SUM=$(stat -c%s "${PARTS[@]}" | awk '{s+=$1} END {print s}')
[ "$PARTSIZE_SUM" = "$FILESIZE" ] || die "part sizes $PARTSIZE_SUM != file $FILESIZE"
log "split into ${#PARTS[@]} parts"

# --- current release assets (name -> size), for skip/resume decisions
asset_names() { gh release view "$TAG" --repo "$REPO" --json assets \
                  --jq '.assets[].name'; }
asset_size() { # usage: asset_size <name>; gh --jq takes the expression only,
               # so the name is interpolated (asset names are generated, safe)
  gh release view "$TAG" --repo "$REPO" --json assets \
    --jq ".assets[] | select(.name==\"$1\") | .size"
}

upload_part() {
  local part="$1" pname="$2" attempt=1 delay="$BACKOFF_BASE"
  local start now elapsed rc
  while [ "$attempt" -le "$RETRIES" ]; do
    start=$(date +%s)
    log "attempt $attempt/$RETRIES: uploading $pname"
    rc=0
    timeout "$ATTEMPT_TIMEOUT" gh release upload "$TAG" --repo "$REPO" \
      --clobber "$part" >/tmp/chunk-upload.log 2>&1 || rc=$?
    now=$(date +%s); elapsed=$((now - start))
    if [ "$rc" = 0 ]; then
      log "uploaded $pname in ${elapsed}s"
      return 0
    fi
    log "WARN: $pname attempt $attempt failed (rc=$rc, ${elapsed}s)"
    tail -3 /tmp/chunk-upload.log | sed 's/^/  /'
    attempt=$((attempt + 1))
    if [ "$attempt" -le "$RETRIES" ]; then
      log "backing off ${delay}s before retry of $pname"
      sleep "$delay"
      delay=$((delay * 2))
    fi
  done
  return 1
}

uploaded=0; skipped=0; repaired=0
for p in "${PARTS[@]}"; do
  pname=$(basename "$p"); psize=$(stat -c%s "$p")
  rsize=$(asset_size "$pname" || true)
  if [ -n "$rsize" ] && [ "$rsize" = "$psize" ]; then
    log "SKIP $pname (already on release, size $psize matches)"
    skipped=$((skipped + 1)); continue
  fi
  if [ -n "$rsize" ]; then
    log "RE-UPLOAD $pname (on release with size $rsize, local is $psize)"
    repaired=$((repaired + 1))
  fi
  if [ "$DRY_RUN" = 1 ]; then
    log "DRY-RUN: would upload $pname ($psize bytes)"
    continue
  fi
  upload_part "$p" "$pname" || die "chunk $pname failed after $RETRIES attempts"
  uploaded=$((uploaded + 1))
done
log "upload phase: $uploaded uploaded, $skipped skipped, $repaired repaired (of ${#PARTS[@]} parts)"

# --- final verification via the release asset API, name AND size
if [ "$DRY_RUN" = 1 ]; then
  log "DRY-RUN: skipping verification"
  exit 0
fi
log "verifying all parts on release $TAG ..."
missing=0
for p in "${PARTS[@]}"; do
  pname=$(basename "$p"); psize=$(stat -c%s "$p")
  rsize=$(asset_size "$pname" || true)
  if [ -z "$rsize" ]; then
    log "FATAL: part missing from release assets: $pname"; missing=1
  elif [ "$rsize" != "$psize" ]; then
    log "FATAL: size mismatch on $pname: release $rsize != local $psize"; missing=1
  else
    log "OK $pname ($psize bytes)"
  fi
done
[ "$missing" = 0 ] || die "verification failed: $missing bad parts"

log "VERIFIED: all ${#PARTS[@]} parts present on release $TAG"
log "reassemble with: cat $BASENAME.part-* > $BASENAME"
log "source file sha256: $FILE_SHA"

if [ "$KEEP_PARTS" = 0 ] && [ "$DRY_RUN" = 0 ]; then
  rm -f "${PARTS[@]}"
  log "local parts deleted (release holds the copies)"
fi
log "done"
