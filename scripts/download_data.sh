#!/usr/bin/env bash
# Download version 1 of the Kaggle dataset into data/raw/<platform>/<table>.csv
# and check that all 21 expected files are there.
#
# Usage (from the repo root, with the gaming-ds env active; on Windows use Git Bash):
#   bash scripts/download_data.sh           # skips the download if all files already exist
#   bash scripts/download_data.sh --force   # downloads again and overwrites
#
# No Kaggle account is needed: the Kaggle CLI downloads public datasets anonymously.
# It still prints an "Authentication required" notice first; the download goes on.
set -euo pipefail

# Pinned to version 1 so everyone analyses the same data, even if the author publishes a new version
DATASET="artyomkruglov/gaming-profiles-2025-steam-playstation-xbox/1"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="$REPO_ROOT/data/raw"

# Same layout as TABLES in src/config.py
COMMON_TABLES=(games achievements players history purchased_games prices)
EXPECTED=()
for platform in steam playstation xbox; do
  for table in "${COMMON_TABLES[@]}"; do
    EXPECTED+=("$platform/$table.csv")
  done
done
EXPECTED+=(steam/reviews.csv steam/friends.csv steam/private_steamids.csv)

missing_files() {
  for f in "${EXPECTED[@]}"; do
    [[ -f "$RAW_DIR/$f" ]] || echo "$f"
  done
}

FORCE=0
case "${1:-}" in
  "") ;;
  --force) FORCE=1 ;;
  *)
    echo "Usage: bash scripts/download_data.sh [--force]" >&2
    exit 2
    ;;
esac

if [[ $FORCE -eq 0 && -z "$(missing_files)" ]]; then
  echo "All ${#EXPECTED[@]} files are already in data/raw; nothing to download (use --force to download again)."
  exit 0
fi

if ! command -v kaggle >/dev/null 2>&1; then
  echo "kaggle CLI not found. Activate the env first: conda activate gaming-ds" >&2
  exit 1
fi

mkdir -p "$RAW_DIR"
echo "Downloading $DATASET into data/raw (about 4 GB once unzipped) ..."
kaggle datasets download "$DATASET" -p "$RAW_DIR" --unzip

missing="$(missing_files)"
if [[ -n "$missing" ]]; then
  echo "Download incomplete. Missing files in data/raw:" >&2
  echo "$missing" >&2
  exit 1
fi

echo
echo "All ${#EXPECTED[@]} files are in data/raw (size on disk):"
for f in "${EXPECTED[@]}"; do
  printf '%8s  data/raw/%s\n' "$(du -h "$RAW_DIR/$f" | cut -f1)" "$f"
done
