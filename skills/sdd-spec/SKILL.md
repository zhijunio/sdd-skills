---
name: sdd-spec
description: Use when a software change needs a durable behavior contract, scope, acceptance criteria, and necessary technical constraints before implementation planning.
---

Write a structured specification before writing any code. The spec is the shared source of truth — what we're building, why, and how we'll know it's done. Concise; no file-by-file implementation prescription.

**When:** new feature, bug fix, migration, or meaningful behavior change with sufficiently clear intent; or in-place revision when AC/constraints change during plan/build/review. **Skip:** open design directions (`sdd-grill`); implementation tasks.

Read repository guidance, relevant code/docs, and any `sdd-grill` Stop summary from the conversation. Ask only for decisions not discoverable locally.

**New spec** — [spec-template.md](spec-template.md):

1. Goal, scope, non-goals.
2. Repository facts that constrain the change only.
3. Requirements; compatibility, migration, security, or interface constraints as needed.
4. Each observable criterion → stable `AC-n`.
5. Remove irrelevant template sections.
6. **Self-review:** no `TBD`/`TODO`/vague AC; sections agree; scope matches non-goals; pass/fail unambiguous; no hidden implementation tasks.
7. Present for user approval.

**Revision** — same `docs/sdd/YYYY-MM-DD-<topic>-spec.md` in place (no `-v2` copy):

1. Edit Requirements, AC, or Constraints.
2. Append **Revision log**: date, reason, changed AC IDs (or `none — clarification`), plan impact (`yes`/`no` + note).
3. Self-review (same checks as new).
4. **Clarification only** (wording/background; pass/fail unchanged) → log, stop — no re-approval; continue triggering stage (`sdd-plan`, `sdd-build`, `sdd-review`).
5. **AC or constraint change** → present for re-approval.
6. After re-approval: `sdd-plan` only when slice boundaries or verification change; else return to prior stage.

Examples: reword AC-2 without changing pass/fail → log only. AC-3 limit 200ms→500ms → re-approve; unchanged slices → return to `sdd-build`.

**Red flags:** implementation steps inside AC; verbatim grill transcript; open questions blocking planning; file existence as approval; new spec file instead of revise; skipping re-approval after AC/constraint change.

**SDD:** `docs/sdd/YYYY-MM-DD-<topic>-spec.md`. User's language; layout flexible. New spec approved → invoke `sdd-plan`. Clarification-only → no stage change. AC change re-approved → invoke `sdd-plan` if plan impact yes, else prior stage.
