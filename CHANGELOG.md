# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- [`docs/adr/0001-sdd-skill-pack-shape.md`](docs/adr/0001-sdd-skill-pack-shape.md) — pack shape: three-stage loop + independent review/improve
- [`CONTEXT.md`](CONTEXT.md) — ubiquitous language for Spec/Plan/Build and independent Delivery Review / Improve Pass
- [`skills/sdd-review/references/`](skills/sdd-review/references/) — shared Standards baselines (four dimensions + Fowler smells)
- Design principle docs — [`docs/design/design.md`](docs/design/design.md), 33 framework-neutral principles extracted and deduplicated from Spring Boot conventions
- [`java-test`](skills/java-test/SKILL.md) / [`generate-java-tests.prompt.md`](docs/prompts/generate-java-tests.prompt.md) — Java unit/integration tests for class, package, module, or project scopes; defaults to `both`, preserves existing coverage policy, reports `not measured` when no coverage tool exists, and stops on non-Java scopes instead of becoming a generic audit

### Changed

- `scripts/check-skills.sh` now derives the eleven-skill inventory from `skills/` and validates frontmatter structure, the README inventory, routing, prompt pairs, behavior-contract markers, and local Markdown files/anchors.
- Removed local `skills-lock.json` and ignored `.agents/`/`skills-lock.json`; machine-specific skills CLI state is not a portable package artifact.
- Completed the package-wide Present contract for runtime skills and paired prompts: user-language output followed by explicit Stop, without automatic chaining.
- Expanded `.github/workflows/check.yml` path filters so every Markdown change runs the package contract checker.
- Pack shape — core loop **`sdd-spec` → `sdd-plan` → `sdd-build` → Stop**; [`sdd-review`](skills/sdd-review/SKILL.md) and [`sdd-improve`](skills/sdd-improve/SKILL.md) are **independent** (usable without Spec/Plan/Build)
- [`sdd-spec`](skills/sdd-spec/SKILL.md) / [`sdd-plan`](skills/sdd-plan/SKILL.md) / [`sdd-build`](skills/sdd-build/SKILL.md) (+ templates) — conversational Approval, AC-only binding, thin plans OK, close-out verification on build, review-fix path
- [`sdd-review`](skills/sdd-review/SKILL.md) — Matt-style two-axis report; missing fixed point → `origin/HEAD` (not hard-coded `main`); Spec Present **(a)/(b)/(c)**; Standards Present **(a)/(b)** + 🔴/🟡/🟢; bucket routing (Verification → Standards (a) first; no double-file); lean Summary + Verdict gate; no hard route to loop skills
- [`ponytail-audit`](skills/ponytail-audit/SKILL.md) — hotspot-aware scope, Top cut, disambiguation vs `sdd-improve` / `sdd-review`; stays one-shot over-engineering cuts only
- [`sdd-improve`](skills/sdd-improve/SKILL.md) — Structure cuts may use ponytail tags (`delete`/`stdlib`/`native`/`yagni`/`shrink`) + optional `net` / Largest Structure cut; four dimensions unchanged
- Present chrome — **Approval Present** / **Report Present**; restore **Present locale** hard rule (user language, not English by default); review Matt-shaped buckets + short Summary/Verdict; improve optional sections default off; terms in [`CONTEXT.md`](CONTEXT.md)
- [`docs/prompts/review-code.prompt.md`](docs/prompts/review-code.prompt.md) — aligned with four Standards dimensions + Spec
- [`README.md`](README.md) / [`AGENTS.md`](AGENTS.md) — skill tables, install examples, and validation commands match the ten-skill pack
- [`skills/create-readme/SKILL.md`](skills/create-readme/SKILL.md) and [`skills/create-agentsmd/SKILL.md`](skills/create-agentsmd/SKILL.md) — Present locale + confirm-before-write; `create-agentsmd`: **primary**/**also OK**, **stable vs ephemeral**, inventory→manifest, optional docs without invented ceremony, convention-conflict ask before write; `create-readme`: stack-agnostic, inventory→manifest, setup **primary**/**also OK**, evidenced architecture/deploy, illustrative diagrams, external URL provenance, AGENTS cross-link, **P3** rearrange-OK; paired prompts aligned

### Removed

- **`sdd-ship`** / **`sdd-verify`** / **`git-release`** (+ prompt) — close-out lives in build; git/PR out of pack
- **`sdd-audit`** / **`repo-audit-full`** — use **`sdd-improve`**
- **`repo-audit`** — merged into **`sdd-review`**
- **`docs/design/sdd-skill-design.md`** — superseded by ADR-0001
- **`sdd-grill`** / **`sdd-zoom`** / local design-interview prompt — use upstream skills or ad hoc as noted in AGENTS

## [0.3.1] - 2026-06-11

Governance and Present-locale hardening after `v0.3.0`.

### Removed

- **`docs/design/consumer-loops/`** — maintainer runbook/evidence archive; verification simplified to README checklist + consumer repo spot-check

### Changed

- **All skills**: **Present** locale hard rule (deliverables in user's language, not English by default)
- **`sdd-improve` / `sdd-review`**: compressed `finding-format.md` + `review-dimensions.md`; README/AGENTS CI narrative aligned
- **`AGENTS.md`**: regenerated maintainer guidelines; **`SOURCES.md`**: per-skill **Present** / **Stop** aligned with `SKILL.md`
- **`engineering-rationale.md`**: governance aligned to consumer spot-check; expanded prose (CONTEXT L0–L3, stage heuristics, review/improve diff kind, §3 upstream four-source synthesis)
- **`README.md`**: workflow diagram fix; review vs improve table; Present/AGENTS/engineering-rationale links

## [0.3.0] - 2026-06-11

Fourth validated release. Consumer fourth loop completed in an external consumer repo.

### Added

- Optional satellite skill **`sdd-improve`** — read-only multi-category codebase audit; conversation findings report; Matt architect vocabulary in category 5

### Removed

- **`using-sdd`** skill and central routing docs/templates
- **`docs/sdd/2026-06-09-sdd-architect-{spec,plan}.md`** — superseded by **`sdd-improve`**
- **`tests/check.py`** and full GitHub Actions **`check`** workflow — maintainer verification via README checklist + consumer repo trials

### Changed

- **Eight skills** — six core loop + optional **`sdd-improve`** and **`sdd-zoom`**; user **`@`** stage skills directly; no routing skill or central routing doc
- **Core principles** (six, three layers: shape / delivery / governance) — dedupe nine → six: minimal & neutral, explicit stages, verifiable slices, test and prove, borrow don't rebuild, no empty ceremony; README, engineering-rationale §1.0, AGENTS, SOURCES (removed in a later release)
- **`SKILL.md`** — concise bodies with semantic preservation; hand off at Stop; improve/review **When/Skip** cross-links
- **`sdd-improve`**: **🔴/🟡/🟢** Findings groups; `audit-dimensions.md` (pairs with **`sdd-review`** `review-dimensions.md`); **`Follow-up` → `Next stage`**
- **`sdd-review`**: **Architecture** absorbs Simplify + readability; **Diff kind** (`code` / `prose/docs-only`); list-block Findings + **🔴/🟡/🟢** (delivery gate); `references/scope.md`
- **`sdd-improve` / `sdd-review`**: **🔴/🟡/🟢** meaning differs (follow-up priority vs delivery gate)
- **docs/design** (removed in a later release): engineering-rationale.md（直白中文 + [shadcn/improve](https://github.com/shadcn/improve) 专节）
- **`spec-template` / README**: multi-domain `docs/context/<domain>/CONTEXT.md`; spec **Current Context** stays increment facts
- Fourth consumer trial（improve → WebMvcTest 切片）
- **`sdd-grill`** / **`sdd-zoom`**: upstream single-source bodies + minimal SDD tails; doc drift cleanup (`tests/check.py` references; improve spec **AC-10** withdrawn)
- **`sdd-improve`**: `SKILL.md` one-line Process + minimal tail; workflow detail in `references/`
- **`sdd-improve`**: `finding-format.md` minimal optional report skeleton; required content unchanged
- **Maintainer verification** — README checklist; no `tests/check.py`; README recommends **`v0.3.0`** for eight skills

## [0.2.1] - 2026-06-09

Maintainer patch: CI gate on `main` and stale gate-doc status fixes after **`v0.2.0`** ship.

### Added

- GitHub Actions workflow **`check`** — runs `python3 tests/check.py` on pull requests and pushes to `main`

### Fixed

- **`v0.2.0` tag** status synced to shipped in maintainer docs (was stale「待 ship」)

## [0.2.0] - 2026-06-09

Third validated release. Consumer third loop completed in an external consumer repo.

### Added

- Optional satellite skill **`sdd-architect`** for architecture deepening (Matt `improve-codebase-architecture` adapted; conversation deliverable)
- Optional satellite skill **`sdd-zoom`** for territory map (modules, callers, domain vocabulary) before spec, grill, architect, or build; default Mermaid relationship diagram when three or more units interact

### Changed

- **`SOURCES.md` / `CHANGELOG` / `project-decisions`**: remove links to retired maintainer **`sdd-lite`** repo; attribute absorbed patterns inline
- **`using-sdd`**: optional satellite routing for **`sdd-zoom`** (territory map) and **`sdd-architect`** (deepening); consolidated **Routing matrix**; pre-spec priority when territory and trade-offs both open (zoom first, then grill)
- **`tests/check.py`**: auto-discover skills under `skills/*/SKILL.md`; require core seven present
- **`using-sdd` / `sdd-review` / `sdd-architect` / README**: clarify **Review vs architect** — delivery diff review vs pre-spec architecture opportunity scan
- **README** / **SOURCES** / **project-decisions**: seven core stages + optional satellites; Workflow Mermaid diagram
- **Consumer loop docs** under `docs/design/consumer-loops/` (`runbook-<gate>.md`, `<project>-<gate>.md`)
- **`sdd-review`**: plan Acceptance mapping, large-diff triage, standards lens, finding tags (agent-skills + maintainer prior review patterns; verification still in `sdd-verify`)
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

First validated release. Consumer second loop completed in an external consumer repo (delete-confirmation increment).

### Added

- Seven platform-neutral SDD skills: `using-sdd`, `sdd-grill`, `sdd-spec`, `sdd-plan`, `sdd-build`, `sdd-review`, `sdd-verify`
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

[Unreleased]: https://github.com/zhijunio/sdd-skills/compare/v0.3.1...HEAD
[0.3.1]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.3.1
[0.3.0]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.3.0
[0.2.1]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.2.1
[0.2.0]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.2.0
[0.1.1]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.1.1
[0.1.0]: https://github.com/zhijunio/sdd-skills/releases/tag/v0.1.0
