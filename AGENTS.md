# Repository Guidelines

Operating guide for AI agents in **zhijunio/sdd-skills** — a Markdown-only skill pack, not an application repo. Human overview: [README.md](README.md). Runtime contracts: `skills/<name>/SKILL.md`. Upstream pins: [docs/design/SOURCES.md](docs/design/SOURCES.md).

## Context

- Maintain **fourteen** platform-neutral SDD skills: six-stage delivery loop plus optional satellites (see [README — Skills](README.md#skills)).
- Write skill instructions in **English**; **Present** deliverables in the **user's language** (every `SKILL.md`).
- Finish one stage → **Stop** → wait for the user to **`@`** the next skill. Never auto-chain stages in one session.
- Do not add hooks, slash commands, agent manifests, central routing docs, or runtime state files unless the user asks.

**Nested AGENTS.md:** not needed — skills are self-contained under `skills/`; one root file is enough.

## Structure

| Path | Purpose |
| --- | --- |
| `skills/<name>/SKILL.md` | Skill runtime contract |
| `skills/<name>/references/` | Bundled templates/checklists for that skill only |
| `.github/prompts/*.prompt.md` | Cursor prompts paired with meta/exploration skills |
| `.github/workflows/check.yml` | CI job **`validate`** |
| `docs/design/` | Maintainer design — `engineering-rationale.md`, `SOURCES.md`, `THIRD_PARTY_NOTICES.md` |
| `docs/sdd/` | SDD specs/plans for this repo's own increments |
| `CHANGELOG.md` | User-visible release notes |

**Skill groups**

| Group | Members |
| --- | --- |
| Core loop | `sdd-grill`, `sdd-spec`, `sdd-plan`, `sdd-build`, `sdd-review`, `sdd-verify` |
| Loop satellites | `sdd-worktree`, `sdd-publish` |
| Exploration | `sdd-zoom`, `sdd-audit` |
| Meta | `sdd-readme`, `sdd-agents`, `sdd-explain`, `sdd-onboard` |

Consumer projects use `docs/sdd/*-spec.md` and `docs/sdd/*-plan.md` by convention — not required in this maintainer repo.

## Commands

No build, lint, format, or test runner exists here. Run these before opening a PR — they mirror [`.github/workflows/check.yml`](.github/workflows/check.yml):

```bash
test "$(find skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l)" -eq 14
test ! -e skills/sdd-ship
test -f skills/sdd-verify/SKILL.md
```

Spot-check relative Markdown links in files you edit. Preserve cross-skill links under `sdd-audit/references/` and `sdd-review/references/`.

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
- Borrow upstream prose verbatim @ pin ([SOURCES.md](docs/design/SOURCES.md)) + minimal **SDD:** tail; keep bodies short; put detail in `references/`.
- Preserve literals: `AC-n`, skill ids, lens ids, `file:line`, git literals, 🔴/🟡/🟢.
- Pair **`sdd-audit`** vs **`sdd-review`** via **When/Skip** cross-links in each skill — do not add pairing tables to AGENTS, README, or design docs.
- When adding or renaming a skill, update `check.yml` assertions and README skill tables if user-visible.
- When upstream-derived behavior changes, update [docs/design/SOURCES.md](docs/design/SOURCES.md) and [docs/design/THIRD_PARTY_NOTICES.md](docs/design/THIRD_PARTY_NOTICES.md).

## Agent notes

**Do**

- Read the target `SKILL.md` and its `references/` before editing.
- Self-trial **material** behavior changes; note user-visible friction in the PR or CHANGELOG.
- Link [README.md](README.md) for onboarding — do not duplicate it here.

**Do not**

- Treat **`sdd-audit`** as a delivery gate or substitute for **`sdd-review`**.
- Chain review → verify → publish without explicit user `@`.
- Add core stages, state fields, or ceremony without evidence.
- Babysit failing CI, merge on red checks, or run mutating `git`/`gh` unless the user scopes **`sdd-publish`**.
- Reintroduce retired ids: `sdd-ship` (use **`sdd-verify`**), `sdd-improve` (use **`sdd-audit`**).
