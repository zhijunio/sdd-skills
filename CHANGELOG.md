# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-06-09

Third validated release. Consumer third loop (**`sdd-architect`**) completed in [todo-web](https://github.com/zhijunio/todo-web). **`sdd-zoom`** ships in this release without a separate consumer gate — see [runbook-0.2.0.md](docs/design/consumer-loops/runbook-0.2.0.md) footnote.

### Added

- Optional satellite skill **`sdd-architect`** for architecture deepening (Matt `improve-codebase-architecture` adapted; conversation deliverable)
- Optional satellite skill **`sdd-zoom`** for territory map (modules, callers, domain vocabulary) before spec, grill, architect, or build; default Mermaid relationship diagram when three or more units interact

### Changed

- **`SOURCES.md` / `CHANGELOG` / `project-decisions`**: remove links to retired maintainer **`sdd-lite`** repo; attribute absorbed patterns inline
- **`using-sdd`**: optional satellite routing for **`sdd-zoom`** (territory map) and **`sdd-architect`** (deepening); consolidated **Routing matrix**; pre-spec priority when territory and trade-offs both open (zoom first, then grill)
- **`tests/check.py`**: auto-discover skills under `skills/*/SKILL.md`; require core seven present
- **`using-sdd` / `sdd-review` / `sdd-architect` / README**: clarify **Review vs architect** — delivery diff review vs pre-spec architecture opportunity scan
- **README** / **SOURCES** / **project-decisions**: seven core stages + optional satellites; consumer loop evidence under `docs/design/consumer-loops/`; Workflow Mermaid diagram
- **Consumer loop docs** moved to `docs/design/consumer-loops/` (`runbook-<gate>.md`, `<project>-<gate>.md`)
- **`sdd-review`**: plan Acceptance mapping, large-diff triage, standards lens, finding tags (agent-skills + maintainer prior review patterns; verification still in `sdd-ship`)
- **`sdd-build`**: read repository guidance and match existing code conventions in touched areas; TDD red discipline and review-fix scope (maintainer prior patterns); fallback to spec/plan + touched code when AGENTS/README silent
- **`AGENTS.md` / `project-decisions`**: maintainer Git workflow — `main` integrates via PR only; branch protection enabled

### Renamed

- **`sdd-deepen`** → **`sdd-architect`** (optional satellite; disambiguate from `sdd-review` delivery review)

## [0.1.1] - 2026-06-09

### Changed

- `using-sdd`: optional routing announcement before recommending the next skill
- `sdd-spec` / `sdd-plan`: inline self-review checklist before user approval (maintainer prior lightweight SDD patterns)
- `plan-template.md`: optional Risks / Dependencies section (comment-only; omit when not needed)

## [0.1.0] - 2026-06-09

First validated release. Consumer second loop completed in [todo-web](https://github.com/zhijunio/todo-web) (delete-confirmation increment).

### Added

- Seven platform-neutral SDD skills: `using-sdd`, `sdd-grill`, `sdd-spec`, `sdd-plan`, `sdd-build`, `sdd-review`, `sdd-ship`
- Bundled `spec-template.md` and `plan-template.md` with writing guides
- `python3 tests/check.py` for skill and template validation
- Design docs under `docs/design/` (methodology, project decisions, second-loop runbook)
- README installation for Cursor, Codex, and Claude Code via the [skills CLI](https://github.com/vercel-labs/skills)
- Pinned install example: `npx skills@latest add zhijunio/sdd-skills@v0.1.0`

### Changed

- Merged `sdd-brainstorm` into `sdd-grill` (eight skills → seven)
- `sdd-spec` supports in-place revision with an append-only revision log

### Fixed

- `project-decisions.md` timeline and version-gate wording after release review

[Unreleased]: https://github.com/zhijunio/sdd-skills/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.2.0
[0.1.1]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.1.1
[0.1.0]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.1.0
