#!/usr/bin/env bash
# Rebuilds aid-sheet.pdf from aid-sheet.html using headless Chrome (macOS path below;
# change CHROME for Linux/Windows). Checks that the result is exactly one page.
set -euo pipefail
cd "$(dirname "$0")/.."

CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

"$CHROME" --headless --disable-gpu --no-sandbox \
  --print-to-pdf="aid-sheet.pdf" --no-pdf-header-footer \
  --run-all-compositor-stages-before-draw --virtual-time-budget=5000 \
  "file://$PWD/aid-sheet.html" 2>/dev/null

if command -v pdfinfo >/dev/null; then
  pages=$(pdfinfo aid-sheet.pdf | awk '/^Pages:/{print $2}')
  echo "aid-sheet.pdf: $pages page(s)"
  [ "$pages" = "1" ] || { echo "ERROR: aid sheet must fit on ONE page" >&2; exit 1; }
fi
