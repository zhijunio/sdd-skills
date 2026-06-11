# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Optional satellite skill **`sdd-improve`** — read-only multi-category codebase audit; conversation findings report; Matt architect vocabulary in category 5

### Changed

- **`using-sdd`**: **opportunity scan** / **delivery review** canonical pair; routing heuristic; normative Disambiguation table
- **`sdd-improve`**: **🔴/🟡/🟢** Findings groups + emoji grading; `audit-dimensions.md` (renamed from `audit-playbook.md`, pairs with **`sdd-review`** `review-dimensions.md`)
- **`sdd-review`**: **Architecture** absorbs Simplify + readability; **Diff kind** (`code` / `prose/docs-only`) with classification signals + Scope field; list-block Findings + **🔴/🟡/🟢** (delivery gate semantics); no **Strengths** section
- **`sdd-improve` / `sdd-review`**: clarify **🔴/🟡/🟢** meaning differs (follow-up priority vs delivery gate); improve cat 5 **half migration** signal
- **`sdd-review`**: Security 按信号必审；Dependencies 补 lockfile/迁移；prose/docs-only **reference integrity**；条件维 **observability / a11y / ops**
- **`sdd-improve`**: cat 3/5/7 补 observability、a11y、ops；cat 5 与 review **Architecture** 同透镜（结构 + duplication 表）
- **`sdd-review`**: Architecture 补 deletion test、seam/depth；与 improve cat 5 对称
- **docs/design**: 完善 `software-engineering-rationale`、`upstream-engineering-rationale`（直白中文 + [shadcn/improve](https://github.com/shadcn/improve) 专节）；**删除** `project-decisions.md`、`context-adr-workflow.md`
- **`sdd-review` / `sdd-zoom`**: route whole-repo health → **`sdd-improve`**
- **Removed** optional satellite **`sdd-architect`** — superseded by **`sdd-improve`** (breaking rename; reinstall with `-s sdd-improve`)
- **`README`**: install note — **`v0.2.1` tag** predates **`sdd-improve`**; use branch or `-s sdd-improve` until next tag
- **`spec-template` / README**: drop `CONTEXT-MAP.md`; multi-domain uses `docs/context/<domain>/CONTEXT.md`; spec **Current Context** stays increment facts (link shared terms from CONTEXT)
- **`AGENTS.md`**: maintainer PR 按主题合并，避免频繁 micro-PR
- **`consumer-loops`**: grill 共识 — 下一 tag **`v0.3.0`**；第四次 loop gate **`sdd-improve`** only（trial Pass 后 ship）
- **`tests/check.py`**: **`sdd-review`** 卫星 bundle 校验（与 **`sdd-improve`** 对称）
- **`sdd-improve`**: Present 强制 **`Follow-up` → `Next stage`**（`SKILL.md` / `finding-format.md`）
- **consumer-loops**: 第四次 loop trial Pass — [todo-web-0.3.0](docs/design/consumer-loops/todo-web-0.3.0.md)（improve → WebMvcTest 切片）

## [0.2.1] - 2026-06-09

Maintainer patch: CI gate on `main` and stale consumer-loop status fixes after **`v0.2.0`** ship.

### Added

- GitHub Actions workflow **`check`** — runs `python3 tests/check.py` on pull requests and pushes to `main`

### Fixed

- **`runbook-0.2.0.md`** / **`todo-web-0.2.0.md`**: **`v0.2.0` tag** status synced to shipped (was stale「待 ship」)

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

[Unreleased]: https://github.com/zhijunio/sdd-skills/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.2.1
[0.2.0]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.2.0
[0.1.1]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.1.1
[0.1.0]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.1.0
