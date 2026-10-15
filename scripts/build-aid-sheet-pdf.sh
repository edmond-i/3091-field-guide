#!/usr/bin/env bash
# Rebuilds aid-sheet.pdf from aid-sheet.html using headless Chrome (macOS path below;
# change CHROME for Linux/Windows). Checks that the result is exactly one page.
set -euo pipefail
cd "$(dirname "$0")/.."

# Any Chromium-based browser works. Set CHROME=/path/to/browser to override.
if [ -z "${CHROME:-}" ]; then
  for c in \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
    "/Applications/Chromium.app/Contents/MacOS/Chromium" \
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
    "$(command -v google-chrome 2>/dev/null)" "$(command -v chromium 2>/dev/null)" "$(command -v chromium-browser 2>/dev/null)"; do
    if [ -n "$c" ] && [ -x "$c" ]; then CHROME="$c"; break; fi
  done
fi
[ -n "${CHROME:-}" ] || { echo "No Chromium-based browser found; set CHROME=/path/to/browser" >&2; exit 1; }

"$CHROME" --headless --disable-gpu --no-sandbox \
  --print-to-pdf="aid-sheet.pdf" --no-pdf-header-footer \
  --run-all-compositor-stages-before-draw --virtual-time-budget=5000 \
  "file://$PWD/aid-sheet.html" 2>/dev/null

if command -v pdfinfo >/dev/null; then
  pages=$(pdfinfo aid-sheet.pdf | awk '/^Pages:/{print $2}')
  echo "aid-sheet.pdf: $pages page(s)"
  [ "$pages" = "1" ] || { echo "ERROR: aid sheet must fit on ONE page" >&2; exit 1; }
fi
