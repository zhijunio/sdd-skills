# Closing the Loop — SDD follow-through

The advisor's job doesn't end at the findings report. This file covers routing selected findings through the **SDD skill loop** and reconciling progress later — not default `plans/` factories, executor dispatch, or in-scan implementation.

The founding rule survives unchanged: **the advisor never edits source code during the scan.** Follow-up may use the SDD loop (**`sdd-build`** on an approved plan) **or** the user may edit directly **outside** any SDD skill — improve only routes; it does not mandate **`sdd-build`**.

---

## Advisor, not implementer

- **This skill:** understand, vet, prioritize, present findings.
- **Not this skill:** edit product code, write default on-disk plans, dispatch executors, or merge/push. During the scan: **no mutating commands** on the user's tree — [audit-dimensions — Read-only rules](audit-dimensions.md#read-only-rules).

**Strong / weak split (SDD):**

| Role | Skills |
| --- | --- |
| Judge + specify | **`sdd-improve`**, **`sdd-grill`**, **`sdd-spec`**, **`sdd-plan`** |
| Execute | **`sdd-build`** (test-first on approved plan) |
| Review verdict | **`sdd-review`** (increment diff) |
| Ship evidence | **`sdd-ship`** |

---

## After **Confirm** — next route

**Confirm** selects which findings scope the next increment. It is **not** a build trigger — do not edit product code in the improve session.

| User intent | Next |
| --- | --- |
| New or changed **behavior** / AC not yet written | **`sdd-spec`** → **`sdd-plan`** → **`sdd-build`** |
| Finding already covered by an **approved spec**; only plan/build left | **`sdd-plan`** or **`sdd-build`** |
| **Mechanical** follow-up (tests, refactor) — boundaries clear, verification obvious; user **waives** a new spec | **`sdd-build`** on approved plan if one exists; else **`sdd-plan`** (thin slice) — consumer discipline, not improve implementing in-session |
| Trade-offs or direction still open | **`sdd-grill`** |
| Increment already built; check diff vs spec/plan | **`sdd-review`** → **`sdd-build`** (fixes) → **`sdd-ship`** |
| **Handoff** for another agent with zero session context | **`sdd-spec`** + **`sdd-plan`** (`docs/sdd/*`) — self-contained AC, slices, verification commands |
| User asks to **implement during the scan** | Decline; pick a row below or **direct edit** after Stop |
| User will **fix ad-hoc** — no spec/plan/build skills | **Stop** — **direct edit** (no SDD skill). User edits + runs repo verification; optional later **`sdd-review`** on the diff |

Respect **Dependency order** from the report when multiple findings are selected.

**Default when unclear:** **`sdd-spec`**. **Not mandatory:** spec, plan, **`sdd-build`**, or any SDD skill — never edit product code **inside** the improve session.

---

## Reconcile — keep follow-ups alive

Process what happened since the last scan:

| User says | Route |
| --- | --- |
| "Did we finish finding #3 from the last scan?" | If spec/plan exists → **`sdd-review`** / **`sdd-ship`** on the increment; else re-run **`sdd-improve`** or check **`docs/sdd/*`** if the user asked to persist |
| "Plan drifted / blocked" | Refresh **`docs/sdd/*-plan.md`** via **`sdd-plan`** or fix via **`sdd-build`** |
| "Sync watchlist / tag" | **`sdd-ship`** + project docs as applicable |

**SDD loop (recommended when you want a durable contract):**

```text
sdd-improve → sdd-spec → sdd-plan → sdd-build → sdd-review → sdd-ship
```

**Direct edit** after improve is valid consumer practice — shorthand: `sdd-improve → (user edits) → verify`. No skill invocation required.

---

## Optional durable artifact

Only when the user explicitly asks: `docs/sdd/YYYY-MM-DD-<topic>-improve.md` — findings summary for later reconcile, not a substitute for spec/plan.
