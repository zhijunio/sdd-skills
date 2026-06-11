---
name: sdd-zoom
description: Use when unfamiliar territory needs a map of modules, callers, and domain vocabulary before spec or other stages, or the user says zoom out. Not delivery review or refactor findings.
---

I don't know this area of code well. Go up a layer of abstraction. Give me a map of all the relevant modules and callers, using the project's domain glossary vocabulary.

**Skip:** refactor findings → `sdd-improve`; open trade-offs → `sdd-grill`; delivery diff review → `sdd-review`; territory known, need contract → `sdd-spec`.

**Diagram:** when ≥3 interacting units — Mermaid flowchart/graph or ASCII; show call/depend direction.

**Output:** `Territory:` (scoped + excluded); `Map:` (diagram + role/inbound/outbound per unit); `Glossary & Gaps:`; `Suggested next:` (one skill + reason). Default no durable file. Then name one next skill; **hand off** — no in-session next-stage work. Common: territory clear → `sdd-spec`; trade-offs → `sdd-grill`; findings wanted → `sdd-improve`; approved plan in area → `sdd-build`.

**Red flags:** mandatory before every spec/ship; duplicating improve or review; raw tree without roles/callers/vocabulary; prose-only map when diagram would clarify; writing spec, plan, or product code in-session.
