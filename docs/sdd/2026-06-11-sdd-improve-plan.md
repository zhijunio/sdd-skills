# sdd-improve Satellite Implementation Plan

**Spec:** `docs/sdd/2026-06-11-sdd-improve-spec.md`

**Plan approved** 2026-06-11. Spec and plan committed with implementation branch.

## Risks / Dependencies

- **Breaking rename:** `sdd-architect` → `sdd-improve`; CHANGELOG + README migration note.
- **Third-party:** condensed `audit-dimensions.md` (from shadcn/improve audit-playbook, MIT).
- **Retired:** `sdd-architect` removed in Slice 4 (user-confirmed). Routing: **only `sdd-improve`**.
- **Naming:** no **Simplify** anywhere in skill text or references.

## Slice 1: Publish the sdd-improve skill package

- Goal: Valid satellite; `check.py` passes with both skills on disk.
- Acceptance: AC-1, AC-2, AC-3, AC-4, AC-5, AC-8, AC-12, AC-13, AC-15, AC-16, AC-17, AC-10
- Depends on: None
- Test or proof:
  - `SKILL.md` — eight sections; **Disambiguation** vs `sdd-review`; deliverable = **conversation findings report**; workflow **Profile (optional) → Audit → Verify → Present → Confirm → Stop**.
  - **No** step/category/block named Simplify.
  - Category 5 covers over-engineering, duplication, deletion test, depth/seam.
  - `standard` scans categories **1–8** by default.
  - References: `profile-guide.md`, `audit-dimensions.md`, `finding-format.md`, `closing-the-loop.md`.
  - Natural-language scope inference (AC-16); internal labels only — users need not type `quick` / `branch` / `next`.
  - v1: standard (1–8) + architecture intent from natural language; branch/quick/deep polish later.
- Implementation outline:
  - Create `skills/sdd-improve/` and three reference files.
  - Slice 1 only: leave `skills/sdd-architect/` on disk until Slice 4 retirement.
- Verification: `python3 tests/check.py` — **passed** (10 skills — architect + improve coexistence)
- Done: true

## Slice 2: Wire routing and cross-skill boundaries

- Goal: Route only to `sdd-improve`; review diff boundary clear.
- Acceptance: AC-6, AC-7, AC-9, AC-17, AC-18
- Depends on: Slice 1
- Test or proof:
  - `using-sdd` — no `sdd-architect` in routing matrix; ambiguous 「review」without diff → ask improve vs review.
  - `sdd-architect/SKILL.md` — optional one-line deprecation pointer (Slice 2; removed Slice 4).
  - `sdd-review` — Disambiguation vs improve (delivery gate / diff only); whole-repo or branch health → improve.
  - `sdd-zoom` — refactor findings → improve.
  - `sdd-improve/SKILL.md` — Disambiguation section per spec.
- Verification: `python3 tests/check.py` — **passed**; `rg sdd-architect skills/using-sdd/` — **empty**
- Done: true

## Slice 3: Repository docs

- Goal: README, SOURCES, decisions, CHANGELOG updated.
- Acceptance: AC-11
- Depends on: Slice 2
- Verification: `python3 tests/check.py` — **passed**; README + SOURCES + CHANGELOG + `docs/design/engineering-rationale.md` updated
- Done: true

## Slice 4: Retire sdd-architect (user-confirmed only)

- Goal: Remove architect after user confirms post-trial.
- Acceptance: AC-14
- Depends on: Slice 3; user confirmation
- Trial checklist (natural language):
  - 「帮我体检一下这个仓库」→ categories 1–8
  - 「看看架构有没有泥球」→ category 5
  - Category 5 findings include over-engineering/duplication with evidence
- Verification: `python3 tests/check.py` — **passed** (9 skills); `rg sdd-architect skills/` — **empty**
- Done: true

## Final Review and Ship

- Maintainer **opportunity scan** trials (2026-06-11): report format (Recon/Scope, **🔴/🟡/🟢** Findings, `closing-the-loop`); **`sdd-review`** `finding-format.md` aligned; no **Strengths** section.
- `sdd-review` → `sdd-build` fixes → `sdd-ship`; no semver tag this increment until consumer friction recorded.
