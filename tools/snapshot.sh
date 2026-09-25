#!/bin/bash
# Regenerates snapshot/home-tree.txt and snapshot/runtime-info.json from the
# live instance, using the same sanitized staging as archive-runtime.sh.
# The tree is derived from the staged (sanitized) files, so it can only list
# what would ship in an archive. Safe to run on a schedule and commit.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"

bash "$REPO_DIR/tools/archive-runtime.sh" --tag "snapshot-$(date +%F)" \
  --out "$REPO_DIR/snapshot" --snapshot-only

echo "snapshot regenerated: $REPO_DIR/snapshot"
