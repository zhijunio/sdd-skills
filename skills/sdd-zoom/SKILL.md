---
name: sdd-zoom
description: Use when the user says zoom out or needs the big picture—unfamiliar code needs a higher-level map of modules, callers, and domain vocabulary before spec, grill, improve, or build—not delivery review or refactor findings.
---

# SDD Zoom

## Goal

Produce a read-only territory map of relevant modules and callers at one layer of abstraction above the code, using the project's domain vocabulary. Add broader context only when it clarifies how the territory fits the wider system—without prescribing refactors, writing specs, or reviewing a delivery diff.

This is **orientation**, not architecture opportunity scanning and not delivery review.

## When to Use

Use when the user says zoom out, needs the big picture, or is unfamiliar with a section of the codebase before choosing the next SDD stage.

Use when `using-sdd` routes here because the active increment's territory is unclear but goals may already be known.

Skip when the user wants **refactor findings** (shallow modules, seams, mud-ball) — use **`sdd-improve`**.

Skip when goals, boundaries, or trade-offs are still unclear — use **`sdd-grill`**.

Skip when the task is **delivery review** of a defined diff — use **`sdd-review`**.

Skip when the user already knows the territory and needs a behavior contract — use **`sdd-spec`**.

This is an **optional satellite**. It is not part of the mandatory core loop before `sdd-ship`.

## Prerequisites

Read repository guidance and existing SDD artifacts (`docs/sdd/*-spec.md`, `*-plan.md`) when present.

When the consumer repo has optional domain docs, read them before mapping:

- `CONTEXT.md` or linked domain glossary files referenced from repository guidance
- `docs/adr/` for terms and boundaries that constrain how modules are described

When those files are absent, infer vocabulary from code, README, and SDD artifacts only. Do not require or create them in this skill.

When the user names a focus area (path, feature, module, or ticket), scope the map to that territory plus immediate callers and dependencies.

## Process

1. Identify the **territory**: user-named focus, or the increment implied by the task and any open SDD artifacts.
2. Read enough code and docs to map **modules**, **callers**, and **callees** at one abstraction layer—not every file line.
3. Prefer **domain terms** from CONTEXT, ADR, spec, or repository guidance over raw path lists alone.
4. Draw a **relationship diagram** for the map (default deliverable—not optional when three or more units interact):
   - Prefer **Mermaid** `flowchart` or `graph` with domain labels on nodes and edges.
   - Use **ASCII** when Mermaid is unavailable or the map is tiny (two units).
   - Show **call / depend** direction; group optional satellites or maintainer layers when they clarify the territory.
5. For each mapped unit, note briefly (table or bullets under the diagram):
   - **Role** — what responsibility it holds in domain language
   - **Inbound** — who calls or depends on it
   - **Outbound** — what it calls or depends on
6. Call out **boundaries** and **glossary gaps** (terms used in code but undefined in docs, or ambiguous names).
7. End with one next-step recommendation through **`using-sdd`**. Common paths:
   - territory clear, behavior change next → **`sdd-spec`**
   - trade-offs still open → **`sdd-grill`**
   - structural friction visible and user wants findings → **`sdd-improve`**
   - approved plan, coding in mapped area → **`sdd-build`**

Do not propose refactor findings, recommendation strength, or deepening directions — that belongs in **`sdd-improve`**.

Do not write product code, tests, spec, plan, CONTEXT, ADR, or durable map files unless the user explicitly asks for one.

## Red Flags

- Treating this skill as mandatory before every spec or ship.
- Duplicating **`sdd-improve`** with refactor or deepening findings.
- Duplicating **`sdd-review`** on a scoped diff.
- Dumping a raw directory tree without roles, callers, or domain vocabulary.
- **Map as table or prose only** when three or more units interact and a relationship diagram would clarify callers (contrast **`sdd-improve`**, which does not require diagram deliverables).
- Auto-invoking **`sdd-spec`**, **`sdd-grill`**, **`sdd-improve`**, or **`sdd-build`**.

## Verification

Confirm the map names the scoped territory, includes a **relationship diagram** when the territory has multiple interacting units, lists modules with inbound/outbound relationships, uses domain vocabulary where available, and notes glossary gaps or assumptions explicitly.

## Output

Deliver a conversation report with this structure:

```markdown
# SDD Zoom

## Territory

What area was mapped and what was excluded.

## Map

Relationship diagram (Mermaid or ASCII) using domain labels—required when three or more units interact.

Then a short table or bullets: role, inbound, outbound per unit (domain terms first).

## Glossary & Gaps

Terms used; missing or ambiguous definitions.

## Suggested next stage

One skill via **`using-sdd`** and one sentence of reason.
```

Default durable artifact: **none**. Do not require a zoom report file on disk.

## Stop Conditions

Stop after the conversation deliverable and one routing recommendation.

Recommend **`using-sdd`** only; do not invoke the next skill automatically.
