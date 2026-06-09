# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Optional satellite skill **`sdd-architect`** for architecture deepening (Matt `improve-codebase-architecture` adapted; conversation deliverable)

### Changed

- **`using-sdd`**: optional satellite routing for deepening / mud-ball intent
- **`using-sdd` / `sdd-review` / `sdd-architect` / README**: clarify **Review vs architect** — delivery diff review vs pre-spec architecture opportunity scan
- **README** / **SOURCES** / **project-decisions**: seven core stages + optional `sdd-architect`; consumer loop evidence under `docs/design/consumer-loops/`
- **Consumer loop docs** moved to `docs/design/consumer-loops/` (`runbook-<gate>.md`, `<project>-<gate>.md`)
- **`sdd-review`**: plan Acceptance mapping, large-diff triage, standards lens, finding tags (sdd-lite / agent-skills adapted; verification still in `sdd-ship`)
- **`sdd-build`**: read repository guidance and match existing code conventions in touched areas; TDD red discipline and review-fix scope (sdd-lite adapted)

### Renamed

- **`sdd-deepen`** → **`sdd-architect`** (optional satellite; disambiguate from `sdd-review` delivery review)

## [0.1.1] - 2026-06-09

### Changed

- `using-sdd`: optional routing announcement before recommending the next skill
- `sdd-spec` / `sdd-plan`: inline self-review checklist before user approval (adapted from sdd-lite)
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

[0.1.1]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.1.1
[0.1.0]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.1.0
