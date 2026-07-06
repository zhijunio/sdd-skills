# Repository Guidelines

Operating guide for AI agents in **zhijunio/sdd-skills** — a Markdown-only skill pack, not an application repo. Human overview: [README.md](README.md). Runtime contracts: `skills/<name>/SKILL.md`.

## Context

- Maintain **eleven** platform-neutral skills: **six SDD** (`sdd-spec`, `sdd-plan`, `sdd-build`, `sdd-review`, `sdd-ship`, `sdd-audit`) plus **five independent** utilities (see [README — Skills](README.md#skills)).
- Write skill instructions in **English**.
- Finish one SDD stage → **Stop** → wait for the user to **`@`** the next skill. Never auto-chain stages in one session.
- Independent skills (`create-readme`, `create-agentsmd`, `explain-code`, `onboarding-plan`, `ponytail-audit`) are **not** SDD loop stages — do not route SDD handoffs to them.
- Do not add hooks, slash commands, agent manifests, central routing docs, or runtime state files unless the user asks.

**Nested AGENTS.md:** not needed — skills are self-contained under `skills/`; one root file is enough.

## Structure

| Path | Purpose |
| --- | --- |
| `skills/<name>/SKILL.md` | Skill runtime contract |
| `skills/<name>/references/` | Bundled templates/checklists for that skill only |
| `docs/prompts/*.prompt.md` | Cursor prompt files — content aligned with paired skills; independent files (see README — Skills) |
| `docs/design/` | Maintainer design notes |
| `CHANGELOG.md` | User-visible release notes |

**Skill groups**

| Group | Members |
| --- | --- |
| SDD core loop | `sdd-spec`, `sdd-plan`, `sdd-build`, `sdd-review`, `sdd-ship` |
| SDD optional | `sdd-audit` |
| Independent (not SDD) | `create-readme`, `create-agentsmd`, `explain-code`, `onboarding-plan`, `ponytail-audit` |

Consumer projects use `docs/sdd/*-spec.md` and `docs/sdd/*-plan.md` by convention — not required in this maintainer repo.

## Commands

No build, lint, format, or test runner exists here. Run these before opening a PR:

```bash
test "$(find skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l)" -eq 11
test ! -e skills/repo-audit
test ! -e skills/repo-audit-full
test ! -e skills/sdd-grill
test ! -e skills/git-release
test -f skills/sdd-ship/SKILL.md
```

Spot-check relative Markdown links in files you edit. Preserve cross-skill links in `sdd-review` and any skill-local references that still exist.

Optional — trial install into an agent:

```bash
npx skills@latest add zhijunio/sdd-skills --list
npx skills@latest add zhijunio/sdd-skills -a cursor -y
```

Do not run or invent `npm test`, `pytest`, `mvn verify`, or similar — they are not part of this repository.

## Commit & PR

- Branch from `main` using `feature/`, `fix/`, or `docs/` + topic; merge via PR only — do not push new work to `main`.
- One logical change per commit; use `feat:` / `fix:` / `docs:` / `chore:` / `refactor:` (or project convention).
- Record user-visible skill changes in [CHANGELOG.md](CHANGELOG.md) `[Unreleased]`.
- Ensure CI **`validate`** passes — branch protection requires it on `main`.
- Do not force-push `main`, change git config, or skip hooks unless the user explicitly asks.

**When editing `SKILL.md`**

- Keep frontmatter **`description`** to triggering conditions only — not a workflow summary.
- Borrow upstream ideas in skill bodies; keep bodies short; put bulky detail in `references/` only when the skill still needs progressive disclosure.
- Preserve literals: `AC-n`, skill ids, lens ids, `file:line`, git literals, 🔴/🟡/🟢.
- Pair **`sdd-audit`** vs **`sdd-review`** via **When/Skip** cross-links in each skill — skill ↔ prompt pairing table lives in README only.
- Keep **`sdd-audit` Standards** and **`sdd-review` Standards** dimensions synchronized; only scope and Spec handling should differ.
- When adding or renaming a skill, update `check.yml` assertions and README skill tables if user-visible.
- When a skill has a paired `docs/prompts/*.prompt.md`, keep **content aligned** but **no cross-links** between the two files; update both in the same change.
- When upstream-derived behavior changes materially, note attribution in the PR or [CHANGELOG.md](CHANGELOG.md).

## Agent notes

**Do**

- Read the target `SKILL.md` and any existing skill-local references before editing.
- Self-trial **material** behavior changes; note user-visible friction in the PR or CHANGELOG.
- Link [README.md](README.md) for onboarding — do not duplicate it here.

**Do not**

- Treat **`sdd-audit`** as a delivery gate or substitute for **`sdd-review`**.
- Treat `sdd-review` as a repo-wide health scan; use **`sdd-audit`** for whole-repo / module / area audits.
- Chain SDD stages (review → verify) without explicit user `@`.
- Route SDD **Stop** handoffs to independent skills (`create-readme`, etc.).
- Add core stages, state fields, or ceremony without evidence.
- Babysit failing CI, merge on red checks, or run mutating `git`/`gh` unless the user scopes **`sdd-ship`**.
- Reintroduce retired ids: `sdd-grill` (use an upstream design-interview skill), `git-release` (use **`sdd-ship`**), `repo-audit` (merged into **`sdd-review`**), `repo-audit-full` (merged into **`sdd-audit`**), `sdd-improve` (use **`sdd-audit`**), **`sdd-zoom`** (removed).
