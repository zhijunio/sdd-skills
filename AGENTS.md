# Repository Guidelines

Platform-neutral **SDD stage skills** for consumer projects. Runtime contracts: `skills/<name>/SKILL.md` and [SOURCES.md](docs/design/SOURCES.md). Design rationale: [README — Core principles](README.md#core-principles), [engineering-rationale §1.0](docs/design/engineering-rationale.md#10-核心原则).

## Core principles (six)

**Shape** — minimal & neutral · explicit stages. **Delivery** — verifiable slices · test and prove. **Governance** — borrow don't rebuild · no empty ceremony.

## Layout

- **Ten skills** under `skills/*/SKILL.md` — six core loop + optional **`sdd-worktree`** (pre-loop), **`sdd-publish`** (post-loop), **`sdd-audit`**, and **`sdd-zoom`**.
- Self-contained per skill; bundled `references/` only inside that skill directory.
- Default consumer artifacts: `docs/sdd/*-spec.md` and `docs/sdd/*-plan.md` only — no central routing doc, runtime state files, hooks, slash commands, or platform manifests in this repo.

## Authoring `SKILL.md`

- Frontmatter **description** — triggering conditions only, not workflow summary.
- Instructions **English**; upstream pins: borrowed prose verbatim @ pin ([SOURCES.md](docs/design/SOURCES.md)) + minimal **SDD:** tail (routing, throws). No fixed section template — short like upstream.
- **Present** hard rule in every skill: deliverables in the **user's language** (latest user turn when unclear) — do not default to English. Keep literal: `AC-n`, skill ids, category lens ids, `file:line`, git literals, 🔴/🟡/🟢.
- One stage output → **Stop** → hand off; user **`@`** the next skill — no auto-chaining or in-session next-stage work.
- **Codebase audit** (`sdd-audit`) vs **delivery review** (`sdd-review`): **When/Skip** cross-links only — do not duplicate pairing tables elsewhere.

## Maintainer changes

- Update [SOURCES.md](docs/design/SOURCES.md) and [THIRD_PARTY_NOTICES.md](docs/design/THIRD_PARTY_NOTICES.md) when upstream-derived behavior changes.
- **No** `tests/check.py` or repo CI (no `.github` workflows).
- Before merge: run `python3 scripts/check-repo.py` (ten skills + relative Markdown links); **`sdd-audit`** / **`sdd-review`** references intact.
- **Material** skill or behavior changes: try in conversation or maintainer self-trial; note user-visible friction in PR or [CHANGELOG.md](CHANGELOG.md) `[Unreleased]`.
- Do not add core stages, state fields, or ceremony without consumer evidence.
- `main` integrates via PR; preserve third-party notices.
