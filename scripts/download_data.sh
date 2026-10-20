#!/usr/bin/env bash
# Download the Kaggle dataset into data/raw/ and print the row count of every
# downloaded file.
#
# Usage (with the gaming-ds env active):
#   bash scripts/download_data.sh
set -euo pipefail

DATASET="artyomkruglov/gaming-profiles-2025-steam-playstation-xbox"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="$REPO_ROOT/data/raw"
KAGGLE_DIR="$HOME/.kaggle"

# kaggle.json is the classic (legacy) API key; newer Kaggle tokens live in
# ~/.kaggle/access_token or $KAGGLE_API_TOKEN, so those count too.
if [[ ! -f "$KAGGLE_DIR/kaggle.json" && ! -f "$KAGGLE_DIR/access_token" && -z "${KAGGLE_API_TOKEN:-}" ]]; then
  cat >&2 <<EOF
Kaggle API credentials not found at: $KAGGLE_DIR/kaggle.json

Setup:
  1. Sign in at https://www.kaggle.com and open https://www.kaggle.com/settings/api
  2. Create a credential, either:
       - legacy API key: the browser downloads kaggle.json, then
       
           mkdir -p ~/.kaggle
           mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
           chmod 600 ~/.kaggle/kaggle.json
       - new API token ("Generate New Token"): save the token text to
           ~/.kaggle/access_token
  3. Re-run: bash scripts/download_data.sh
EOF
  exit 1
fi

if ! command -v kaggle >/dev/null 2>&1; then
  echo "kaggle CLI not found. Activate the env first: conda activate gaming-ds" >&2
  exit 1
fi

mkdir -p "$RAW_DIR"

echo "Downloading $DATASET into $RAW_DIR ..."
kaggle datasets download "$DATASET" -p "$RAW_DIR" --unzip

echo
echo "Files in data/raw (line count via wc -l, header line included):"
find "$RAW_DIR" -type f ! -name '.gitkeep' | sort | while IFS= read -r f; do
  printf '%12d  %s\n' "$(wc -l < "$f")" "${f#"$REPO_ROOT"/}"
done
