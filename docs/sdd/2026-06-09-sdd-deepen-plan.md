# sdd-deepen Satellite Implementation Plan

**Spec:** `docs/sdd/2026-06-09-sdd-deepen-spec.md`

Commit the approved spec and this plan before Slice 1.

## Slice 1: Publish the sdd-deepen skill contract

- Goal: The repository contains a valid eighth skill that defines optional deepening behavior and passes repository checks.
- Acceptance: AC-1, AC-2, AC-3, AC-4, AC-5, AC-7
- Depends on: None
- Test or proof:
  - Add `sdd-deepen` to `tests/check.py` `SKILLS` tuple before or with the new skill file so validation covers eight skills.
  - Confirm `skills/sdd-deepen/SKILL.md` includes satellite wording, conversation deliverable, optional CONTEXT/ADR read rules, ADR conflict handling, and stop → `using-sdd` with default `sdd-spec` when a candidate needs acceptance criteria.
- Implementation outline:
  - Create `skills/sdd-deepen/SKILL.md` using the standard eight sections and a `Use when` description covering deepening, shallow modules, seams, and mud-ball architecture concerns.
  - Embed concise depth / seam / deletion-test guidance in Process and Output without HTML or subagent requirements.
  - Update `tests/check.py` to include `sdd-deepen`.
- Verification:

  ```bash
  python3 tests/check.py
  ```

- Done: true
- Result:
  - Added `skills/sdd-deepen/SKILL.md` and registered the skill in `tests/check.py`.
  - Verified `python3 tests/check.py` reports eight skills passing.

## Slice 2: Wire optional satellite routing and repository docs

- Goal: Readers and routers can discover and reach `sdd-deepen` without making it part of the mandatory core loop.
- Acceptance: AC-6, AC-8
- Depends on: Slice 1
- Test or proof:
  - `using-sdd` lists optional satellites and routes mud-ball / deepening intent to `sdd-deepen` without auto-invocation.
  - README distinguishes **seven core stages** from the optional **`sdd-deepen`** satellite and updates install examples where needed.
  - `SOURCES.md` records Matt inspiration and local decisions for the satellite.
  - `docs/design/project-decisions.md` records the 8th-skill satellite decision and `v0.2.0` gate.
  - `CHANGELOG.md` `[Unreleased]` notes the new optional skill.
- Implementation outline:
  - Extend `skills/using-sdd/SKILL.md` Process or a short **Optional satellites** subsection with triggers and handoff to `using-sdd` after `sdd-deepen`.
  - Update README skills table, workflow note, and install copy (`seven core` + optional satellite).
  - Update SOURCES (`sdd-deepen` section + Why seven skills footnote), project-decisions timeline/watchlist, and CHANGELOG.
  - Scan other docs for stale “exactly seven skills only” wording; update only where the new satellite must be disclosed.
- Verification:

  ```bash
  python3 tests/check.py
  ```

  Manual read: README Skills section, `using-sdd` satellite routing, SOURCES local decisions.

- Done: true
- Result:
  - Updated `using-sdd`, README, SOURCES, project-decisions, and CHANGELOG.
  - Verified `python3 tests/check.py` passes.

## Final Review and Ship

- Run `sdd-review` against the `sdd-deepen` increment diff on `feat/sdd-deepen`.
- Fix blocking findings through `sdd-build`, then rerun `sdd-review`.
- Run `sdd-ship` with `python3 tests/check.py` and a manual spot-check that core-loop wording still shows seven mandatory stages.
- Do **not** create `v0.2.0` in this increment.
