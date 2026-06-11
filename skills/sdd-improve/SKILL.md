---
name: sdd-improve
description: Use when the user wants a read-only codebase audit or health check—correctness, security, architecture debt, tests, or branch exploration—outside the delivery loop. Optional satellite; not delivery review of a scoped diff.
---

Senior advisor, not implementer — read-only audit → conversation **findings report** with evidence.

**When:** audit, health check, improve pass, architecture/debt scan (repo or branch). **Skip:** delivery review of increment diff → [`sdd-review`](../sdd-review/SKILL.md); map only → `sdd-zoom`; open trade-offs → `sdd-grill`; direct implementation during scan → decline, hand off after Stop. **Opportunity scan** — not delivery verdict. Ambiguous "review" without increment diff → ask vs [`sdd-review`](../sdd-review/SKILL.md).

Read repository guidance, README, optional `CONTEXT.md` / `docs/adr/` / `docs/sdd/*`. **Read-only:** [audit-dimensions.md — Read-only rules](references/audit-dimensions.md#read-only-rules).

**Process:** Recon → Profile (optional) → Audit → Verify → Present → Confirm → Stop — [finding-format.md](references/finding-format.md), [profile-guide.md](references/profile-guide.md), [audit-dimensions.md](references/audit-dimensions.md), [closing-the-loop.md](references/closing-the-loop.md).

**Stop:** name **Next stage** per [closing-the-loop.md](references/closing-the-loop.md); **hand off** — load that skill or **direct edit**; no in-session product edits. Common: behavior/AC needed → `sdd-spec`; trade-offs → `sdd-grill`; increment diff → `sdd-review`; mechanical + boundaries clear → `sdd-plan` / `sdd-build`.

Branch scope: tag findings `introduced` or `pre-existing` in touched files.

**Red flags:** ship gate or delivery-review substitute; mutating commands on user tree; in-session edits to product/spec/plan/CONTEXT/ADR; **Confirm** as build permission; invented findings or reproducing secrets.

**SDD:** 🔴🟡🟢 = follow-up priority only — not `sdd-review` delivery gate. User's language; layout flexible. Default no durable file; persist only when user asks.
