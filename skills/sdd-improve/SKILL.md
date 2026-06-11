---
name: sdd-improve
description: Use when the user wants a read-only codebase audit or health check—correctness, security, architecture debt, tests, or branch exploration—outside the delivery loop. Optional satellite; not delivery review of a scoped diff.
---

Senior advisor, not implementer. Read-only multi-category audit → conversation **findings report** with evidence. Optional satellite — not mandatory before `sdd-ship`.

**When:** audit, health check, improve pass, architecture/debt scan (repo or branch). **Skip:** delivery review of increment diff → [`sdd-review`](../sdd-review/SKILL.md); map only → `sdd-zoom`; open trade-offs → `sdd-grill`; direct implementation during scan → decline, hand off after Stop. **Opportunity scan** — not delivery verdict. Ambiguous "review" without increment diff → ask vs [`sdd-review`](../sdd-review/SKILL.md).

Read repository guidance, README, optional `CONTEXT.md` / `docs/adr/` / `docs/sdd/*`. **Read-only:** no installs, commits, formatters, mutating builds — [audit-dimensions.md — Read-only rules](references/audit-dimensions.md#read-only-rules).

**Recon → Profile (optional) → Audit → Verify → Present → Confirm → Stop**

1. **Recon** — README/AGENTS, verify command, CI, `HEAD`, working tree, hotspots → **Context — Recon** ([finding-format.md](references/finding-format.md)).
2. **Profile** (optional) — effort/scope ambiguous → merges into **Context — Scope** ([profile-guide.md](references/profile-guide.md); effort table there; default **standard**).
3. **Audit** — read-only; never Simplify ([audit-dimensions.md](references/audit-dimensions.md)). Depth per effort (`quick`/`standard`/`deep`). Name skipped categories in Recon **Not audited**.
4. **Verify** — re-read cited code; reject false positives → **Coverage — Limits**. ADR conflicts → mark + follow-up.
5. **Present** — Context → Findings → Coverage → Follow-up per [finding-format.md](references/finding-format.md). **`### Next stage`** required before Confirm ([closing-the-loop.md](references/closing-the-loop.md)).
6. **Confirm** — which findings enter Next stage increment. **Not** approval to edit product code — Confirm ≠ `sdd-build`.
7. **Stop** — name **Next stage** per [closing-the-loop.md](references/closing-the-loop.md); **hand off** — load that skill or **direct edit** on continuation. No in-session product edits.

Branch scope: tag findings `introduced` or `pre-existing` in touched files.

**Red flags:** ship gate or delivery-review substitute; mutating commands; editing product/spec/plan/CONTEXT/ADR (except user-requested `docs/sdd/*-improve.md`); Confirm as implement permission; default on-disk reports; invented findings; reproducing secrets.

**SDD:** 🔴🟡🟢 = follow-up priority only — **not** `sdd-ship` gate (delivery gate = `sdd-review`). User's language; layout flexible. Default no durable file; persist only when user asks.
