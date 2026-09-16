#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
pdf="$repo_root/sources/raw/manas-ms-old911-current90-full.pdf"
work="${MANAS_OLD911_WORK:-/tmp/manas-old911}"
images="$work/images"
ocr="$work/ocr"
mkdir -p "$images" "$ocr"

# Render once. Existing pages are retained so interrupted OCR can resume.
if [[ $(find "$images" -name 'page-*.jpg' | wc -l) -lt 302 ]]; then
  nix shell nixpkgs#poppler-utils -c pdftoppm \
    -scale-to 1800 -jpeg -jpegopt quality=90 \
    "$pdf" "$images/page"
fi

export ocr
find "$images" -name 'page-*.jpg' -print0 | sort -z | \
  xargs -0 -P "${MANAS_OLD911_JOBS:-8}" -n 1 bash -c '
    image="$1"
    name="$(basename "${image%.jpg}")"
    output="$ocr/$name"
    [[ -s "$output.txt" ]] || tesseract "$image" "$output" -l eng --psm 6 2>/dev/null
  ' _

python "$repo_root/scripts/summarize-manas-old911-ocr.py" "$work"
