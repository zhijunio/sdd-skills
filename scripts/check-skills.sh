#!/usr/bin/env bash
# Validate the skill package and stable documentation contracts.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

fail=0
checked=0

skill_files=()
while IFS= read -r f; do skill_files+=("$f"); done < <(find skills -mindepth 2 -maxdepth 2 -name SKILL.md -print | sort)
actual="${#skill_files[@]}"
echo "OK   skill count=$actual (derived from skills/)"

for doc in README.md AGENTS.md; do
  if grep -qF "当前 **$actual** 个" "$doc" || grep -qF "当前 $actual 个" "$doc"; then
    echo "OK   $doc declares $actual skills"
  else
    echo "MISS $doc does not declare $actual skills"
    fail=1
  fi
done

# Every published skill is listed in the human-facing README.
for f in "${skill_files[@]}"; do
  dir="$(basename "$(dirname "$f")")"
  if grep -qF "](skills/$dir/SKILL.md)" README.md; then
    echo "OK   README lists $dir"
  else
    echo "MISS README does not list $dir"
    fail=1
  fi
done

# Retired ids must not reappear as discoverable skill directories.
for name in sdd-ship sdd-verify git-release sdd-audit repo-audit-full repo-audit sdd-grill; do
  if [ -e "skills/$name" ]; then
    echo "MISS retired skill exists: skills/$name"
    fail=1
  fi
done

# Explicit prompt/skill pairs. Other prompts are standalone by design.
pairs=(
  "explain-code:docs/prompts/explain-code.prompt.md"
  "generate-java-test:docs/prompts/generate-java-tests.prompt.md"
  "onboarding-plan:docs/prompts/onboarding-plan.prompt.md"
  "sdd-review:docs/prompts/review-code.prompt.md"
)
for pair in "${pairs[@]}"; do
  skill="${pair%%:*}"
  prompt="${pair#*:}"
  if [ ! -f "skills/$skill/SKILL.md" ] || [ ! -f "$prompt" ]; then
    echo "MISS prompt pair: $skill <-> $prompt"
    fail=1
  else
    echo "OK   prompt pair: $skill"
    for marker in "Locale (hard rule)" "Stop"; do
      if grep -qF "$marker" "$prompt"; then
        echo "OK   prompt contract $skill contains '$marker'"
      else
        echo "MISS prompt contract $prompt contains '$marker'"
        fail=1
      fi
    done
  fi
done

# Every runtime skill must preserve the package-wide Present/Stop contract.
for f in "${skill_files[@]}"; do
  for marker in "Locale (hard rule)" "Stop"; do
    if grep -qF "$marker" "$f"; then
      echo "OK   skill contract $f contains '$marker'"
    else
      echo "MISS skill contract $f contains '$marker'"
      fail=1
    fi
  done
done

# Validate cross-skill routing links.
while IFS= read -r f; do
  src="$(basename "$(dirname "$f")")"
  refs=$(grep -oE '\.\./[A-Za-z0-9._-]+/SKILL\.md' "$f" 2>/dev/null | sort -u || true)
  [ -z "$refs" ] && continue
  while IFS= read -r ref; do
    name="${ref#../}"; name="${name%/SKILL.md}"
    checked=$((checked + 1))
    if [ -f "skills/$name/SKILL.md" ]; then echo "OK   route $src -> $name"; else echo "MISS route $src -> $name"; fail=1; fi
  done <<< "$refs"
done < <(printf '%s\n' "${skill_files[@]}")

# Keep the stable cross-skill behavior contract text present without snapshotting prose.
for requirement in "skills/sdd-review/SKILL.md:## When" "skills/sdd-review/SKILL.md:## Skip" "skills/sdd-improve/SKILL.md:- **Standards**" "skills/sdd-improve/SKILL.md:Correctness" "skills/sdd-improve/SKILL.md:Structure" "skills/sdd-improve/SKILL.md:Verification" "skills/sdd-improve/SKILL.md:Traceability" "skills/generate-java-test/SKILL.md:default to" "skills/generate-java-test/SKILL.md:not measured" "docs/prompts/generate-java-tests.prompt.md:default to" "docs/prompts/generate-java-tests.prompt.md:not measured"; do
  file="${requirement%%:*}"; text="${requirement#*:}"
  if grep -qF -- "$text" "$file"; then echo "OK   contract $file contains '$text'"; else echo "MISS contract $file contains '$text'"; fail=1; fi
done

# Validate the limited skill frontmatter schema and local Markdown links/anchors.
if ! python3 - <<'PY'
from pathlib import Path
from urllib.parse import unquote
import re
import sys

root = Path('.')
failed = False

def miss(message):
    global failed
    print(f"MISS {message}")
    failed = True

def validate_frontmatter(source):
    lines = source.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0] != '---':
        miss(f"frontmatter opening: {source}")
        return
    try:
        closing = lines.index('---', 1)
    except ValueError:
        miss(f"frontmatter closing: {source}")
        return

    fields = {}
    current = None
    for line in lines[1:closing]:
        if not line.strip():
            continue
        match = re.fullmatch(r'([A-Za-z][A-Za-z0-9_-]*):\s*(.*)', line)
        if match:
            key, value = match.groups()
            if key in fields:
                miss(f"duplicate frontmatter key '{key}': {source}")
                return
            fields[key] = [] if value in {'>', '|'} else [value]
            current = key
        elif line[:1].isspace() and current:
            fields[current].append(line.strip())
        else:
            miss(f"frontmatter syntax: {source}:{line}")
            return

    if set(fields) != {'name', 'description'}:
        miss(f"frontmatter keys: {source} (found {sorted(fields)})")
        return
    name = ' '.join(fields['name']).strip()
    description = ' '.join(fields['description']).strip()
    expected = source.parent.name
    if name != expected:
        miss(f"frontmatter name: {source} (found '{name}', expected '{expected}')")
        return
    if not description:
        miss(f"frontmatter description: {source}")
        return
    print(f"OK   frontmatter {expected}")

def heading_anchors(text):
    anchors = set()
    counts = {}
    for line in text.splitlines():
        match = re.match(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', line)
        if not match:
            continue
        heading = re.sub(r'<[^>]+>', '', match.group(1))
        heading = re.sub(r'!?(?:\[([^\]]*)\])\([^)]*\)', r'\1', heading)
        heading = re.sub(r'[`*_~]', '', heading).lower()
        slug = re.sub(r'[^\w\- ]', '', heading, flags=re.UNICODE)
        slug = re.sub(r'\s+', '-', slug.strip())
        if not slug:
            continue
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(slug if count == 0 else f"{slug}-{count}")
    return anchors

for source in sorted(Path('skills').glob('*/SKILL.md')):
    validate_frontmatter(source)

for source in root.rglob('*.md'):
    if any(part in {'.git', '.agents'} for part in source.parts):
        continue
    text = source.read_text(encoding='utf-8')
    for raw_target in re.findall(r'!?(?:\[[^\]]*\])\(([^)]+)\)', text):
        target = raw_target.strip().strip('<>')
        if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', target):
            continue
        location, _, fragment = target.partition('#')
        location = location.split('?', 1)[0]
        path = (source if not location else source.parent / unquote(location)).resolve()
        if not path.exists():
            miss(f"markdown link: {source}:{raw_target}")
            continue
        if fragment and path.suffix.lower() == '.md':
            anchors = heading_anchors(path.read_text(encoding='utf-8'))
            anchor = unquote(fragment).lower()
            if anchor not in anchors:
                miss(f"markdown anchor: {source}:{raw_target}")
if failed:
    sys.exit(1)
print('PASS frontmatter and Markdown relative links/anchors')
PY
then
  fail=1
fi

echo "---"
echo "checked=$checked routing links"
if [ "$fail" -ne 0 ]; then echo "FAIL: skill package contract checks failed"; exit 1; fi
echo "PASS: skill package contract checks passed"
