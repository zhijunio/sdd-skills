# Closing the Loop — SDD follow-through

Route selected findings after present — not in-scan implementation. **Advisor never edits source during the scan.** Follow-up: SDD loop or user **direct edit**. Finding format: [report.md](report.md); lenses: [map.md](map.md).

## After present

**Present** scopes follow-up — **not** a build trigger. No product edits in the improve session.

| User intent | Next |
| --- | --- |
| New/changed **behavior** / AC not written | **`sdd-spec`** → **`sdd-plan`** → **`sdd-build`** |
| **Approved spec**; plan/build only | **`sdd-plan`** or **`sdd-build`** |
| **Mechanical** follow-up — boundaries clear; user **waives** spec | **`sdd-build`** if plan exists; else thin **`sdd-plan`** |
| Trade-offs / direction open | **`sdd-grill`** |
| Increment built; check diff | **`sdd-review`** → **`sdd-build`** → **`sdd-ship`** |
| **Handoff** — zero session context | **`sdd-spec`** + **`sdd-plan`** (`docs/sdd/*`) |
| Implement **during scan** | Decline; route below or **direct edit** after Stop |
| **Ad-hoc fix** — no SDD skills | **Stop** — **direct edit**; optional later **`sdd-review`** |

Respect **P0/P1/P2** order from the report. **Default when unclear:** **`sdd-spec`**.

## Reconcile

| User says | Route |
| --- | --- |
| "Finished finding #3?" | **`sdd-review`** / **`sdd-ship`** if increment exists; else re-run **`sdd-improve`** or check persisted `docs/sdd/*` |
| "Plan drifted / blocked" | **`sdd-plan`** or **`sdd-build`** |
| "Sync watchlist / tag" | **`sdd-ship`** |

Loop shorthand: `sdd-improve → sdd-spec → sdd-plan → sdd-build → sdd-review → sdd-ship`. **Direct edit** valid: `sdd-improve → (user edits) → verify`.

## Optional durable artifact

Only when asked: `docs/sdd/YYYY-MM-DD-<topic>-improve.md` — reconcile aid, not spec/plan substitute.
