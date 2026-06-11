# Repository Guidelines

Platform-neutral **SDD stage skills** for consumer projects. Runtime contracts: `skills/<name>/SKILL.md` and [SOURCES.md](SOURCES.md). Design rationale: [README — Core principles](README.md#core-principles), [engineering-rationale §1.0](docs/design/engineering-rationale.md#10-核心原则).

## Core principles (six)

**Shape** — minimal & neutral · explicit stages. **Delivery** — verifiable slices · test and prove. **Governance** — borrow don't rebuild · no empty ceremony.

## Layout

- **Eight skills** under `skills/*/SKILL.md` — six core loop + optional **`sdd-improve`** and **`sdd-zoom`**.
- Self-contained per skill; bundled `references/` only inside that skill directory.
- Default consumer artifacts: `docs/sdd/*-spec.md` and `docs/sdd/*-plan.md` only — no central routing doc, runtime state files, hooks, slash commands, or platform manifests in this repo.

## Authoring `SKILL.md`

- Frontmatter **description** — triggering conditions only, not workflow summary.
- Instructions **English**; upstream pins: borrowed prose verbatim @ pin ([SOURCES.md](SOURCES.md)) + minimal **SDD:** tail (routing, throws). No fixed section template — short like upstream.
- **Present** hard rule in every skill: deliverables in the **user's language** (latest user turn when unclear) — do not default to English. Keep literal: `AC-n`, skill ids, category lens ids, `file:line`, git literals, 🔴/🟡/🟢.
- One stage output → **Stop** → hand off; user **`@`** the next skill — no auto-chaining or in-session next-stage work.
- **Opportunity scan** (`sdd-improve`) vs **delivery review** (`sdd-review`): **When/Skip** cross-links only — do not duplicate pairing tables elsewhere.

## Maintainer changes

- Update [SOURCES.md](SOURCES.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) when upstream-derived behavior changes.
- **No** `tests/check.py`. Minimal CI job **`validate`** (`.github/workflows/check.yml`) counts eight skills on PRs to `main` — branch protection only, not skill-behavior validation.
- **Material** skill or behavior changes: spot-check in a **consumer repo** (reinstall pinned tag, run one increment). Note user-visible friction in PR or [CHANGELOG.md](CHANGELOG.md) `[Unreleased]`.
- Before merge: eight skills present; **`sdd-improve`** / **`sdd-review`** references intact; spot-check Markdown links you edit. Details: [README — Maintainer verification](README.md#maintainer-verification).
- Do not add core stages, state fields, or ceremony without consumer evidence.
- `main` integrates via PR; preserve third-party notices.
