#!/usr/bin/env bash
# archive-runtime.sh - sanitized per-build archive of the entire Muse runtime.
#
# Stages the live instance into a sanitized tree and zips it as a GitHub
# release asset. Archives are NEVER committed to git (see .gitignore).
#
# SCOPE - the entire runtime minus personal files/info:
#   runtime/home  <- $HOME, personal subtrees excluded (see EXCLUDES_HOME)
#   runtime/opt   <- /opt/hatch (bin, skills, assets, runtime-cell)
# NOT included, with reasons (also written to the .exclusions.txt artifact):
#   /opt/hatch-image  - host image; includes ~1.3G model weights, not
#                       redistributable, not part of the per-build runtime
#   ~/workspace       - instance working state; heavily mixed personal
#                       content. Curated redacted copies live in
#                       snapshot/files/ instead.
#   This archives the LIVE instance running a given build, not a pristine
#   Meta image. Live-instance additions are not distinguished from
#   fresh-image files.
#
# Usage:
#   bash archive-runtime.sh --tag <tag> [--out DIR]
#       [--build-commit <c>] [--build-built-at <ts>] [--snapshot-only]
# Output (in --out):
#   runtime-archive-<tag>.zip
#   runtime-archive-<tag>.manifest.txt    (sha256, size_bytes, path)
#   runtime-archive-<tag>.exclusions.txt  (documented exclusion list)
#   (always refreshes snapshot/home-tree.txt + snapshot/runtime-info.json)
#
# FAILS LOUDLY: tar aborts on any error other than "file changed as we read
# it" (exit 1, expected on a live home dir). The post-stage filename scan
# aborts on any high-confidence personal/secret name. Review the manifest
# before publishing.

set -euo pipefail

OUT_DIR="."
TAG=""
BUILD_COMMIT=""
BUILD_BUILT_AT=""
SNAPSHOT_ONLY=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --out) OUT_DIR="$2"; shift 2 ;;
    --tag) TAG="$2"; shift 2 ;;
    --build-commit) BUILD_COMMIT="$2"; shift 2 ;;
    --build-built-at) BUILD_BUILT_AT="$2"; shift 2 ;;
    --snapshot-only) SNAPSHOT_ONLY=1; shift ;;
    *) echo "unknown arg: $1" >&2; exit 1 ;;
  esac
done
[[ -n "$TAG" ]] || TAG="$(date +%F)"

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SNAP_DIR="$REPO_DIR/snapshot"
OUT_DIR="$(cd "$OUT_DIR" && pwd)"   # absolute: subshell cd's later must not break it
STAGE="$OUT_DIR/.stage-runtime-$TAG"
rm -rf "$STAGE"
trap 'rm -rf "$STAGE"' EXIT
mkdir -p "$STAGE/runtime/home" "$STAGE/runtime/opt"

ARCHIVE_BASENAME="runtime-archive-$TAG"

# ---------------------------------------------------------------------------
# Exclusion lists. Every entry has a reason; the reasons ship in the
# .exclusions.txt artifact next to the zip.
# ---------------------------------------------------------------------------
# Personal subtrees + identity files + secret/config dirs + risky patterns.
EXCLUDES_HOME=(
  # --- personal subtrees (memory, relationships, comms, user data) ---
  ./memory ./dreams ./agents ./channels ./subscriptions ./data ./user
  # --- instance working state (mixed personal; curated copies in snapshot/files/) ---
  ./workspace
  # --- identity / standing files ---
  ./MEMORY.md ./USER.md ./SOUL.md ./IDENTITY.md ./AGENTS.md ./HEARTBEAT.md
  ./PROACTIVE_PREFERENCES.md ./TOOLS.md ./ALIGNMENT_STATE.yaml
  ./*.before-*
  # --- secret / credential / session state ---
  ./.ssh ./.xurl ./.codex ./.claude-server-commander ./.gnupg ./.aws ./.netrc
  ./.gitconfig ./.desktop-commander-app ./.desktop-commander-device
  ./.config ./.local ./.mozilla ./.pki
  # --- vnc session state (includes a password file) ---
  ./.vnc
  # --- caches, logs, build junk ---
  ./.cache ./.npm ./logs ./*.log
  ./.Xauthority ./.xsession-errors
  ./node_modules ./venv ./.venv ./__pycache__ ./*.pyc
  # --- databases, key/secret-like names (backstop; scan below also checks) ---
  ./*.sqlite* ./*.db
  ./*credential* ./*Credential* ./*secret* ./*Secret*
  ./*token* ./*Token* ./*cookie* ./*Cookie*
  ./*.pem ./*.key
  ./.git ./hooks/archive
)
# /opt/hatch is Meta-shipped (no personal data expected); drop only build junk.
EXCLUDES_OPT=(
  ./node_modules ./venv ./.venv ./__pycache__ ./*.pyc
)

# tar exit codes: 0 ok, 1 = files changed during read (live system, fine),
# 2+ = real failure. Never blanket-suppress with || true.
run_tar() {
  local src="$1" dest="$2"; shift 2
  local excludes=("$@")
  local args=(-cf - --warning=no-file-changed)
  local e; for e in "${excludes[@]}"; do args+=(--exclude="$e"); done
  # never archive our own staging area or the output archives
  args+=(--exclude="./$(basename "$STAGE")*" --exclude="./$ARCHIVE_BASENAME*")
  args+=(-C "$src" .)
  set +e
  tar "${args[@]}" 2>"$STAGE/tar-errors.log" | tar -xf - -C "$dest" 2>>"$STAGE/tar-errors.log"
  local rc=${PIPESTATUS[0]}
  set -e
  if (( rc >= 2 )); then
    echo "FATAL: tar failed with exit $rc staging $src" >&2
    tail -20 "$STAGE/tar-errors.log" >&2
    exit 1
  fi
  if (( rc == 1 )); then
    echo "note: some files changed during read of $src (live system, continuing)"
  fi
}

echo "staging home directory (personal paths excluded)..."
run_tar "$HOME" "$STAGE/runtime/home" "${EXCLUDES_HOME[@]}"

echo "staging /opt/hatch (bin, skills, assets, runtime-cell)..."
if [[ -d /opt/hatch ]]; then
  run_tar /opt/hatch "$STAGE/runtime/opt" "${EXCLUDES_OPT[@]}"
else
  echo "WARNING: /opt/hatch not present" >&2
fi

# ---------------------------------------------------------------------------
# Post-stage filename scan. High-confidence personal/secret names abort the
# build. This is a backstop for exclusion mistakes, not a content audit.
# ALLOWLIST holds exact staged paths that matched a scan pattern but were
# verified benign (reviewed source, no secrets). Keep it short and exact.
ALLOWLIST=(
  ./opt/skills/skill-creator/bin/dynamic_credentials.py
)
# ---------------------------------------------------------------------------
echo "scanning staged filenames..."
SCAN_HITS="$(cd "$STAGE/runtime" && find . -type f | grep -iE \
  -e 'mike' -e 'mzio' \
  -e 'id_ed25519' -e 'id_rsa' \
  -e '\.pem$' -e '/\.key$' \
  -e 'credential' -e 'passwd' -e 'shadow' \
  -e '\.sqlite(-journal)?$' \
  -e '(^|/)\.ssh(/|$)' -e '(^|/)\.gnupg(/|$)' \
  -e 'memory\.md$' -e '(^|/)USER\.md$' -e '(^|/)SOUL\.md$' \
  || true)"
for allowed in "${ALLOWLIST[@]}"; do
  SCAN_HITS="$(printf '%s\n' "$SCAN_HITS" | grep -vFx -- "$allowed" || true)"
done
if [[ -n "$SCAN_HITS" ]]; then
  echo "FATAL: staged tree contains suspicious filenames (aborting):" >&2
  echo "$SCAN_HITS" | head -30 >&2
  exit 1
fi
echo "filename scan clean."

# ---------------------------------------------------------------------------
# Manifest (sha256, size, path), exclusions doc, snapshot files.
# ---------------------------------------------------------------------------
echo "writing manifest..."
( cd "$STAGE/runtime" && find . -type f -print0 | sort -z | xargs -0 sha256sum > "$STAGE/sha.list" )
( cd "$STAGE/runtime" && while read -r sum path; do
    size="$(stat -c%s "$path")"
    printf '%s  %s  %s\n' "$sum" "$size" "$path"
  done < "$STAGE/sha.list" | sort -k3 > "$OUT_DIR/$ARCHIVE_BASENAME.manifest.txt" )

cat > "$OUT_DIR/$ARCHIVE_BASENAME.exclusions.txt" <<'EOF'
# Exclusions for this archive, with reasons.
#
# From $HOME (runtime/home):
#   memory dreams agents channels subscriptions data user
#     -> personal subtrees: memories, relationships, comms, user data
#   workspace
#     -> instance working state, mixed personal content; curated redacted
#        copies are published in snapshot/files/ instead
#   MEMORY.md USER.md SOUL.md IDENTITY.md AGENTS.md HEARTBEAT.md
#   PROACTIVE_PREFERENCES.md TOOLS.md ALIGNMENT_STATE.yaml *.before-*
#     -> identity and standing files about the operator
#   .ssh .xurl .codex .claude-server-commander .gnupg .aws .netrc
#   .gitconfig .desktop-commander-app .desktop-commander-device
#   .config .local .mozilla .pki
#     -> secrets, credentials, session state, client config
#   .vnc -> vnc session state including a password file
#   .cache .npm logs *.log node_modules venv .venv __pycache__ *.pyc
#     -> caches, logs, build junk
#   .Xauthority .xsession-errors
#     -> X session cookie and session error log
#   *.sqlite* *.db *credential* *secret* *token* *cookie* *.pem *.key
#   .git hooks/archive
#     -> databases and secret-like names (backstop)
#
# From /opt/hatch (runtime/opt):
#   node_modules venv .venv __pycache__ *.pyc -> build junk only
#
# Not staged at all:
#   /opt/hatch-image -> host image; includes ~1.3G model weights which are
#                      not redistributable and not part of the per-build runtime
#
# What this archive IS: a sanitized snapshot of the live instance running one
# build. It is not a pristine Meta image; live-instance additions are not
# distinguished from fresh-image files.
EOF

FILES="$(wc -l < "$OUT_DIR/$ARCHIVE_BASENAME.manifest.txt")"
echo "refreshing snapshot/home-tree.txt + runtime-info.json from staged tree..."
( cd "$STAGE/runtime" && find . | sort | sed 's|^\./||' > "$SNAP_DIR/home-tree.txt" )
{
  echo "{"
  echo "  \"snapshot_utc\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\","
  echo "  \"repo\": \"muse-runtime\","
  echo "  \"kind\": \"sanitized-observational-snapshot\","
  echo "  \"archive_tag\": \"$TAG\","
  echo "  \"build_commit\": \"$BUILD_COMMIT\","
  echo "  \"build_built_at\": \"$BUILD_BUILT_AT\","
  echo "  \"files\": $FILES,"
  echo "  \"notes\": \"file list of the sanitized per-build archive; personal subtrees pruned; no file contents in this listing; filenames scanned for personal/secret names before release\""
  echo "}"
} > "$SNAP_DIR/runtime-info.json"

if (( SNAPSHOT_ONLY )); then
  echo "snapshot-only: wrote $SNAP_DIR/home-tree.txt + runtime-info.json ($FILES files)"
  exit 0
fi

echo "zipping..."
( cd "$STAGE" && zip -qr "$OUT_DIR/$ARCHIVE_BASENAME.zip" runtime )
SIZE="$(du -h "$OUT_DIR/$ARCHIVE_BASENAME.zip" | cut -f1)"

echo ""
echo "done: $OUT_DIR/$ARCHIVE_BASENAME.zip ($SIZE, $FILES files)"
echo "manifest:   $OUT_DIR/$ARCHIVE_BASENAME.manifest.txt"
echo "exclusions: $OUT_DIR/$ARCHIVE_BASENAME.exclusions.txt"
echo ""
echo "REVIEW THE MANIFEST BEFORE PUBLISHING:"
echo "  grep -iE 'mike|mzio|passwd|shadow' $OUT_DIR/$ARCHIVE_BASENAME.manifest.txt | head"
