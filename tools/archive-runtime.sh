#!/usr/bin/env bash
# archive-runtime.sh - build a sanitized zip of the Muse runtime.
#
# Copies the instance's home directory and built-in skills into a staging
# area, excluding personal data, then zips it. The result approximates what
# ships with a fresh runtime: structure, tooling and skills, no user content.
#
# Usage: bash archive-runtime.sh [--out DIR]
# Output: runtime-archive-YYYY-MM-DD.zip + runtime-archive-YYYY-MM-DD.manifest.txt
#
# ALWAYS review the manifest before sharing the zip.

set -euo pipefail

OUT_DIR="."
while [[ $# -gt 0 ]]; do
  case "$1" in
    --out) OUT_DIR="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 1 ;;
  esac
done

DATE="$(date +%F)"
STAGE="$OUT_DIR/.stage-runtime-$DATE"
rm -rf "$STAGE"
trap 'rm -rf "$STAGE"' EXIT
mkdir -p "$STAGE/runtime/home" "$STAGE/runtime/skills"

# never archive our own staging area (it's inside the tree we're copying)
STAGE_REL="${STAGE#$HOME/}"
OUT_REL="${OUT_DIR#$HOME/}"

echo "staging home directory (excluding personal paths)..."

# tar handles live/unusual files better than rsync here. Excludes are
# relative to $HOME. When in doubt, exclude: a missing runtime file is a
# smaller diff; a leaked personal file is a breach.
tar -cf - \
  --exclude='./memory' \
  --exclude='./dreams' \
  --exclude='./agents' \
  --exclude='./channels' \
  --exclude='./subscriptions' \
  --exclude='./data' \
  --exclude='./user' \
  --exclude='./workspace/user' \
  --exclude='./workspace/your_files' \
  --exclude='./workspace/goals' \
  --exclude='./workspace/personal' \
  --exclude='./workspace/profile-images' \
  --exclude='./workspace/media_library' \
  --exclude='./workspace/*backup*' \
  --exclude='./.ssh' \
  --exclude='./.xurl' \
  --exclude='./.claude-server-commander' \
  --exclude='./.codex' \
  --exclude='./.cache' \
  --exclude='./.npm' \
  --exclude='./.config' \
  --exclude='./.local/share' \
  --exclude='./.mozilla' \
  --exclude='./.pki' \
  --exclude='./MEMORY.md' \
  --exclude='./USER.md' \
  --exclude='./SOUL.md' \
  --exclude='./IDENTITY.md' \
  --exclude='./AGENTS.md' \
  --exclude='./HEARTBEAT.md' \
  --exclude='./PROACTIVE_PREFERENCES.md' \
  --exclude='./TOOLS.md' \
  --exclude='./*.before-*' \
  --exclude='./*.log' \
  --exclude='./logs' \
  --exclude='./node_modules' \
  --exclude='./venv' \
  --exclude='./.venv' \
  --exclude='./__pycache__' \
  --exclude='./*.pyc' \
  --exclude='./.git' \
  --exclude='./*.sqlite' \
  --exclude='./*.sqlite-journal' \
  --exclude='./*.db' \
  --exclude='./*credential*' \
  --exclude='./*Credential*' \
  --exclude='./*secret*' \
  --exclude='./*Secret*' \
  --exclude='./*token*' \
  --exclude='./*Token*' \
  --exclude='./*cookie*' \
  --exclude='./*Cookie*' \
  --exclude='./*.pem' \
  --exclude='./*.key' \
  --exclude='./.desktop-commander-app' \
  --exclude='./.desktop-commander-device' \
  --exclude='./.gitconfig' \
  --exclude='./hooks/archive' \
  --exclude='./workspace' \
  --exclude="./$STAGE_REL" \
  --exclude="./$OUT_REL/runtime-archive-*" \
  -C "$HOME" . 2>/dev/null | tar -xf - -C "$STAGE/runtime/home" 2>/dev/null || true

echo "staging built-in skills..."
if [[ -d /opt/hatch/skills ]]; then
  tar -cf - \
    --exclude='./node_modules' \
    --exclude='./venv' \
    --exclude='./.venv' \
    --exclude='./__pycache__' \
    --exclude='./spaces/ts-runtime' \
    --exclude='./*credential*' \
    --exclude='./*secret*' \
    --exclude='./*token*' \
    -C /opt/hatch/skills . 2>/dev/null | tar -xf - -C "$STAGE/runtime/skills" 2>/dev/null || true
fi

echo "writing manifest..."
( cd "$STAGE" && find runtime -type f | sort > "$OUT_DIR/runtime-archive-$DATE.manifest.txt" )

echo "zipping..."
( cd "$STAGE" && zip -qr "$OUT_DIR/runtime-archive-$DATE.zip" runtime )

FILES="$(wc -l < "$OUT_DIR/runtime-archive-$DATE.manifest.txt")"
SIZE="$(du -h "$OUT_DIR/runtime-archive-$DATE.zip" | cut -f1)"

echo "done: $OUT_DIR/runtime-archive-$DATE.zip ($SIZE, $FILES files)"
echo "manifest: $OUT_DIR/runtime-archive-$DATE.manifest.txt"
echo ""
echo "REVIEW THE MANIFEST BEFORE SHARING. Search it for personal data:"
echo "  grep -iE 'mike|@|/home/[a-z]' $OUT_DIR/runtime-archive-$DATE.manifest.txt | head"
