---
name: sdd-improve
description: Use when the user wants a read-only codebase audit or health check outside the delivery loop — MECE pillars (A/C/S/V/D/O), P0/P1/P2 roadmap, snapshot/standard/deep. Opportunity scan; not delivery review of a scoped diff.
---

# SDD Improve — opportunity scan

**Role:** Optional **satellite** — read-only **MECE** multi-pillar health assessment. **Not** a delivery stage; **not** [`sdd-review`](../sdd-review/SKILL.md).

**Produces (chat only):** boundary map, findings (one lens per row), P0/P1/P2 roadmap, optional direction notes, **Next stage** (SDD handoff).

**Does not produce:** `plans/`, product edits, spec/plan files, or delivery verdict. **🔴🟡🟢 in findings severity** = impact rubric per `report.md` — **not** `sdd-review` ship gate.

**When:** audit, health check, architecture/debt scan (repo or branch). **Skip:** increment diff delivery review → `sdd-review`; map only → `sdd-zoom`; trade-offs → `sdd-grill`; implement during scan → decline, hand off after Stop.

Ambiguous **"review"** without increment diff → ask vs `sdd-review`.

**Present:** User's language. Literals: lens ids, `file:line`, git refs, severity emojis per `report.md`.

## Hard rules

1. **Read-only** on user tree — [playbook.md](references/playbook.md) § Recon SDD context.
2. **Systemic first** — pattern-class findings; pillar boundaries in `map.md`.
3. **Vet before report** — re-read 🚨/🔴 cites; ADRs by-design unless contradicted.
4. **No secret values** — `file:line` + credential type only.
5. **MECE** — one lens per row.

## Workflow

1. `map.md` → 2. `playbook.md` (Recon → pillars → Vet) → 3. `report.md` → 4. **Next stage** per [closing-the-loop.md](references/closing-the-loop.md) → **Stop** — hand off; no in-session next-stage work.

`deep` → `deep-parallel.md`. Effort, variants, Chinese triggers → `references/map.md` and `references/playbook.md`.

## Self-check

Lenses A1–A6, C0–C3, S1, V1–V2, D1, O1. Skipped pillars stated. **Stop** names one next skill or direct edit — user **`@`** it separately.

## References

`references/map.md` · `references/playbook.md` · `references/report.md` · `references/closing-the-loop.md`

**Provenance:** MECE audit playbooks adapted from [zhijunio/zhijunio-skills `codebase-audit`](https://github.com/zhijunio/zhijunio-skills/tree/main/codebase-audit) — see [SOURCES.md](../../SOURCES.md).
