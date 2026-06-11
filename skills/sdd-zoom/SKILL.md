---
name: sdd-zoom
description: Use when the user says zoom out or needs the big picture—unfamiliar code needs a higher-level map of modules, callers, and domain vocabulary before spec, grill, improve, or build—not delivery review or refactor findings.
---

I don't know this area of code well. Go up a layer of abstraction. Give me a map of all the relevant modules and callers, using the project's domain glossary vocabulary.

Read-only **orientation** — not architecture opportunity scan (`sdd-improve`) or delivery review (`sdd-review`). Optional satellite; not mandatory before `sdd-ship`.

**When:** zoom out, big picture, unfamiliar territory before `@` a stage skill. **Skip:** refactor findings → `sdd-improve`; open trade-offs → `sdd-grill`; delivery diff review → `sdd-review`; territory known, need contract → `sdd-spec`.

Read repository guidance and `docs/sdd/*` when present. Optional `CONTEXT.md`, `docs/adr/` — infer from code/README when absent; do not require or create. Scope to user-named focus + immediate callers/deps.

**Process:**

1. Identify territory (user focus or increment from task/SDD artifacts).
2. Map modules, callers, callees at one abstraction layer — not every line.
3. Domain terms from CONTEXT/ADR/spec over raw paths.
4. **Relationship diagram** when ≥3 interacting units (Mermaid flowchart/graph or ASCII for tiny maps); call/depend direction.
5. Per unit: **Role**, **Inbound**, **Outbound** (table or bullets under diagram).
6. Boundaries; glossary gaps (undefined/ambiguous terms).
7. Suggest one next skill — common: territory clear → `sdd-spec`; trade-offs → `sdd-grill`; friction + findings wanted → `sdd-improve`; approved plan in area → `sdd-build`.

No refactor findings, recommendation strength, or deepening directions. No product code, tests, spec, plan, CONTEXT, ADR, or durable map files unless user asks.

**Red flags:** mandatory before every spec/ship; duplicating improve or review; raw tree without roles/callers/vocabulary; prose-only map when diagram would clarify; next-stage work in-session without stopping.

**Output (required content — layout flexible):** Territory (scoped + excluded); Map (diagram + role/inbound/outbound); Glossary & Gaps; Suggested next stage (one skill + reason). Default no durable file.

**SDD:** User's language. Stop after deliverable — name one next skill; **hand off**, no in-session next-stage work.
