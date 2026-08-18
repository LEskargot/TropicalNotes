#!/usr/bin/env bash
# Point this repo's hooks at scripts/hooks/ so they are version-controlled.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
git config core.hooksPath scripts/hooks
echo "core.hooksPath -> scripts/hooks"
echo "hooks active:"
for h in scripts/hooks/*; do
  [ -x "$h" ] && [ "$(basename "$h")" != "install.sh" ] && echo "  - $(basename "$h")"
done
