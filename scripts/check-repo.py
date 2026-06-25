#!/usr/bin/env python3
"""Maintainer pre-merge checks: skill count and relative Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = 10
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def check_skill_count() -> bool:
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    count = len(skills)
    if count != EXPECTED_SKILLS:
        print(f"FAIL: expected {EXPECTED_SKILLS} skills, found {count}")
        for skill in skills:
            print(f"  - {skill.parent.name}")
        return False
    print(f"OK: {count} skills")
    return True


def check_links() -> bool:
    broken: list[tuple[Path, str, str]] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK_PATTERN.finditer(text):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                broken.append((path, target, "outside repo"))
                continue
            if not resolved.exists():
                broken.append((path, target, "missing"))

    if broken:
        for path, target, reason in broken:
            print(f"FAIL: {path.relative_to(ROOT)} -> {target} ({reason})")
        return False

    print("OK: relative markdown links")
    return True


def main() -> int:
    ok = check_skill_count() and check_links()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
