# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[0.1.0]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.1.0
