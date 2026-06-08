#!/usr/bin/env python3
"""Validate the minimal repository contract without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "using-sdd",
    "sdd-brainstorm",
    "sdd-spec",
    "sdd-plan",
    "sdd-build",
    "sdd-review",
    "sdd-ship",
)
REQUIRED_SECTIONS = (
    "Goal",
    "When to Use",
    "Prerequisites",
    "Process",
    "Red Flags",
    "Verification",
    "Output",
    "Stop Conditions",
)
LOCAL_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}

    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def check_local_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for target in LOCAL_LINK.findall(text):
        link_path = target.split("#", 1)[0]
        if link_path and not (path.parent / link_path).exists():
            errors.append(f"{path.relative_to(ROOT)}: missing link target {target}")
    return errors


def check_skill(name: str) -> list[str]:
    errors: list[str] = []
    skill_dir = ROOT / "skills" / name
    skill_file = skill_dir / "SKILL.md"

    if not skill_dir.is_dir():
        return [f"missing skill directory: skills/{name}"]
    if not skill_file.is_file():
        return [f"missing skill file: skills/{name}/SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    if frontmatter.get("name") != name:
        errors.append(f"skills/{name}/SKILL.md: frontmatter name must be {name}")

    description = frontmatter.get("description", "")
    if not description.startswith("Use when "):
        errors.append(
            f"skills/{name}/SKILL.md: description must start with 'Use when '"
        )

    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in text:
            errors.append(f"skills/{name}/SKILL.md: missing section '{section}'")

    errors.extend(check_local_links(skill_file, text))
    return errors


def main() -> int:
    errors: list[str] = []
    for skill in SKILLS:
        errors.extend(check_skill(skill))

    for template in (
        ROOT / "skills" / "sdd-spec" / "spec-template.md",
        ROOT / "skills" / "sdd-plan" / "plan-template.md",
    ):
        if not template.is_file():
            errors.append(f"missing template: {template.relative_to(ROOT)}")

    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository checks passed: {len(SKILLS)} skills validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
