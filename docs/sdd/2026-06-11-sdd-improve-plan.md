# sdd-improve Satellite Implementation Plan

**Spec:** `docs/sdd/2026-06-11-sdd-improve-spec.md`

**Status:** complete (2026-06-11)

## Slices

| Slice | Goal | Verification |
| --- | --- | --- |
| 1 | Publish `skills/sdd-improve/` + references | `python3 tests/check.py` — eight skills |
| 2 | improve/review/zoom **When/Skip** cross-links | `check.py`; no central routing doc |
| 3 | README, SOURCES, CHANGELOG, engineering-rationale | `check.py` |
| 4 | Consumer loop Pass | [todo-web-0.3.0.md](../design/consumer-loops/todo-web-0.3.0.md) |

## Ship

- Maintainer review + `sdd-ship` slice → **`v0.3.0`** tag when ready.
