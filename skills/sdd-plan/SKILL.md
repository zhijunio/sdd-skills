---
name: sdd-plan
description: Use when an approved specification needs to be decomposed into testable vertical slices before implementation begins.
---

Decompose work into small, verifiable tasks with explicit acceptance criteria. Every task small enough to implement, test, and verify in one focused session.

**When:** after user-approved spec, before implementation. **Not for:** clarifying product behavior or writing code.

Require approved spec. Read repository conventions; inspect affected code before proposing tasks.

**Process** — [plan-template.md](plan-template.md):

1. Map every spec AC to at least one vertical slice.
2. Prefer **15–60 minute** slices with observable behavior — not file/layer splits.
3. Per slice: dependencies, failing test or alternative proof, implementation outline, verification command, completion condition.
4. **Risks / Dependencies** when they affect order, verification, or rollback (omit when none).
5. Keep local reversible choices in the plan.
6. Public interface, persistent data, security boundary, or cross-module dependency changes → `sdd-spec`.
7. **Self-review:** no placeholders; every AC mapped; concrete risks when present; each slice independently verifiable.
8. **Present** for user approval.

**Present:** Write the plan in the **user's language** (latest user turn when unclear) — do not default to English. Keep literal: `AC-n`, skill ids, verification commands.

**Red flags:** layer-only splits; unmapped AC; commit hashes or status machines; implementation before approval.

**SDD:** thrown superpowers `docs/superpowers/plans/` default path. Write `docs/sdd/YYYY-MM-DD-<topic>-plan.md`. Layout flexible. User approval before build. Stop → invoke `sdd-build`.
