#!/usr/bin/env python3
"""Validate the minimal repository contract without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_CORE_SKILLS = frozenset(
    {
        "sdd-grill",
        "sdd-spec",
        "sdd-plan",
        "sdd-build",
        "sdd-review",
        "sdd-ship",
    }
)
SKILL_BODY_MIN_CHARS = 40
LOCAL_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)")

# Optional satellite skills: bundled references and SKILL.md size caps.
SKILL_REFERENCE_BUNDLES: dict[str, tuple[str, ...]] = {
    "sdd-improve": (
        "references/audit-dimensions.md",
        "references/finding-format.md",
        "references/closing-the-loop.md",
        "references/profile-guide.md",
    ),
    "sdd-review": (
        "references/review-dimensions.md",
        "references/finding-format.md",
        "references/scope.md",
    ),
}
SATELLITE_SKILL_MAX_LINES: dict[str, int] = {
    "sdd-improve": 90,
}
DEPRECATED_SATELLITE_FILES: dict[str, tuple[str, ...]] = {
    "sdd-improve": ("references/audit-playbook.md",),
}

# Template content requirements: each template must contain these headings/anchors.
TEMPLATE_REQUIREMENTS = {
    "spec-template.md": ["Goal", "Scope", "Non-goals", "Requirements", "Acceptance Criteria"],
    "plan-template.md": ["Slice", "Goal", "Acceptance", "Verification"],
}


def discover_skills() -> list[str]:
    if not SKILLS_DIR.is_dir():
        return []

    names: list[str] = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").is_file():
            names.append(skill_dir.name)
    return names


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
    skill_dir = SKILLS_DIR / name
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

    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            body = text[end + 5 :]
    if len(body.strip()) < SKILL_BODY_MIN_CHARS:
        errors.append(
            f"skills/{name}/SKILL.md: body too short after frontmatter "
            f"(need at least {SKILL_BODY_MIN_CHARS} characters)"
        )

    errors.extend(check_local_links(skill_file, text))
    return errors


def check_skill_reference_bundle(name: str) -> list[str]:
    if name not in SKILL_REFERENCE_BUNDLES:
        return []

    errors: list[str] = []
    skill_dir = SKILLS_DIR / name
    skill_file = skill_dir / "SKILL.md"

    for rel in SKILL_REFERENCE_BUNDLES[name]:
        if not (skill_dir / rel).is_file():
            errors.append(f"skills/{name}: missing bundled reference {rel}")

    for rel in DEPRECATED_SATELLITE_FILES.get(name, ()):
        if (skill_dir / rel).is_file():
            errors.append(f"skills/{name}: deprecated file must not exist: {rel}")

    max_lines = SATELLITE_SKILL_MAX_LINES.get(name)
    if max_lines is not None and skill_file.is_file():
        line_count = len(skill_file.read_text(encoding="utf-8").splitlines())
        if line_count > max_lines:
            errors.append(
                f"skills/{name}/SKILL.md: {line_count} lines exceeds satellite cap {max_lines}"
            )

    if skill_file.is_file():
        text = skill_file.read_text(encoding="utf-8")
        if "audit-playbook" in text:
            errors.append(
                f"skills/{name}/SKILL.md: must link audit-dimensions.md, not audit-playbook"
            )

    return errors


def check_template(template: Path) -> list[str]:
    errors: list[str] = []
    if not template.is_file():
        return [f"missing template: {template.relative_to(ROOT)}"]

    text = template.read_text(encoding="utf-8")
    if len(text.strip()) < 100:
        errors.append(f"{template.relative_to(ROOT)}: too short ({len(text)} bytes), add writing guidance")

    name = template.name
    if name in TEMPLATE_REQUIREMENTS:
        for required in TEMPLATE_REQUIREMENTS[name]:
            if required not in text:
                errors.append(f"{template.relative_to(ROOT)}: missing required content '{required}'")

    return errors


def main() -> int:
    errors: list[str] = []
    skills = discover_skills()

    if not skills:
        errors.append("no skills discovered under skills/*/SKILL.md")

    missing_core = sorted(REQUIRED_CORE_SKILLS - set(skills))
    if missing_core:
        errors.append(f"missing core skills: {', '.join(missing_core)}")

    for skill in skills:
        errors.extend(check_skill(skill))
        errors.extend(check_skill_reference_bundle(skill))

    templates = (
        SKILLS_DIR / "sdd-spec" / "spec-template.md",
        SKILLS_DIR / "sdd-plan" / "plan-template.md",
    )
    for template in templates:
        errors.extend(check_template(template))

    for markdown_file in ROOT.rglob("*.md"):
        if ".git" in markdown_file.parts:
            continue
        text = markdown_file.read_text(encoding="utf-8")
        errors.extend(check_local_links(markdown_file, text))

    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Repository checks passed: {len(skills)} skills discovered, "
        f"{len(templates)} templates validated."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
