#!/usr/bin/env bash
# Verify every cross-skill routing link (../<name>/SKILL.md) referenced in a
# SKILL.md points to an existing skills/<name>/SKILL.md. Guards the review ->
# build / improve / spec routing graph against rename/delete drift.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

fail=0
checked=0

while IFS= read -r f; do
  src="$(basename "$(dirname "$f")")"
  refs=$(grep -oE '\.\./[A-Za-z0-9._-]+/SKILL\.md' "$f" 2>/dev/null | sort -u || true)
  [ -z "$refs" ] && continue
  while IFS= read -r ref; do
    name="${ref#../}"
    name="${name%/SKILL.md}"
    checked=$((checked + 1))
    if [ -f "skills/$name/SKILL.md" ]; then
      echo "OK   $src -> $name"
    else
      echo "MISS $src -> $name  (skills/$name/SKILL.md not found)"
      fail=1
    fi
  done <<< "$refs"
done < <(find skills -mindepth 2 -maxdepth 2 -name SKILL.md | sort)

echo "---"
echo "checked=$checked routing links"
if [ "$fail" -ne 0 ]; then
  echo "FAIL: unresolved cross-skill routing links"
  exit 1
fi
echo "PASS: all cross-skill routing links resolve"
