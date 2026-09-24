#!/bin/bash
# Regenerates snapshot/home-tree.txt and snapshot/runtime-info.json from the
# live instance. Sanitized: names only, personal subtrees pruned to their
# top-level directory. Safe to run on a schedule and commit the result.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SNAP_DIR="$REPO_DIR/snapshot"
HOME_DIR="$HOME"

{
  echo "# Sanitized home-directory map of a live Muse instance"
  echo "# Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ) (UTC)"
  echo "# Names only. Personal subtrees are pruned to their top directory."
  echo ""
  find "$HOME_DIR" -maxdepth 3 \
    \( -path "$HOME_DIR/.ssh" \
    -o -path "$HOME_DIR/workspace/user" \
    -o -path "$HOME_DIR/workspace/your_files" \
    -o -path "$HOME_DIR/workspace/profile-images" \
    -o -path "$HOME_DIR/memory/people" \
    -o -path "$HOME_DIR/memory/groups" \
    -o -path "$HOME_DIR/channels" \
    -o -path "$HOME_DIR/subscriptions" \
    -o -path "$HOME_DIR/data" \
    -o -path "$HOME_DIR/dreams" \
    -o -path "$HOME_DIR/workspace/memory" \
    \) -prune \
    -o -not -path '*/venv*' -not -path '*/node_modules*' -not -path '*/__pycache__*' \
       -not -name '*.cookies' -not -name '.storage*' -not -name '*.lock' \
       -print 2>/dev/null \
    | sed "s|$HOME_DIR|~|" | sort
} > "$SNAP_DIR/home-tree.txt"

{
  echo "{"
  echo "  \"snapshot_utc\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\","
  echo "  \"repo\": \"muse-runtime\","
  echo "  \"kind\": \"sanitized-observational-snapshot\","
  echo "  \"notes\": \"directory names only; personal subtrees pruned; no file contents, no credentials, no personal data\""
  echo "}"
} > "$SNAP_DIR/runtime-info.json"

echo "snapshot regenerated: $SNAP_DIR"
