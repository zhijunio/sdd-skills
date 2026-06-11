# sdd-improve Satellite Implementation Plan

**Spec:** `docs/sdd/2026-06-11-sdd-improve-spec.md`

**Status:** complete (2026-06-11)

## Slices

| Slice | Goal | Verification |
| --- | --- | --- |
| 1 | Publish `skills/sdd-improve/` + references | ~~`python3 tests/check.py`~~ *(obsolete — see spec revision log 2026-06-11)* |
| 2 | improve/review/zoom **When/Skip** cross-links | cross-links present; no central routing doc |
| 3 | README, SOURCES, CHANGELOG, engineering-rationale | docs updated |
| 4 | Consumer loop Pass | [todo-web-0.3.0.md](../design/consumer-loops/todo-web-0.3.0.md) |

> **Note:** Slices 1–3 originally cited `tests/check.py`; maintainer verify removed — acceptance per [spec revision log](./2026-06-11-sdd-improve-spec.md#revision-log) and consumer loop evidence.

## Ship

- Maintainer review + `sdd-ship` slice → **`v0.3.0`** tag when ready.
