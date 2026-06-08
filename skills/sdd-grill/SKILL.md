---
name: sdd-grill
description: Use when an existing plan, design, or draft needs stress-testing before committing to it, or when the user says "grill me". Works within SDD or standalone.
---

# SDD Grill

## Goal

Reach shared understanding by challenging every aspect of an existing plan or design until all decision-tree branches align.

## When to Use

Use when a plan, design, or draft already exists and needs stress-testing before approval, or when the user mentions "grill me". Can be used within the SDD workflow or standalone for any decision.

**Requires an existing artifact** (a written plan, design document, draft, or a pasted summary). If no artifact exists and goals are still unclear, use `sdd-brainstorm` first.

Do not use when multiple directions are still open — use `sdd-brainstorm` first.

If the user provides a scope hint (e.g., "grill the database migration only"), limit grilling to that scope; do not expand into unrelated subsystems.

## Prerequisites

Read the existing artifact and relevant context. Explore available facts before asking the user — do not ask for information that can be discovered locally.

## Process

1. Confirm the subject (pasted text, file path, or summary from the current thread).
2. List the major decision branches (briefly; no long essay).
3. Walk branches in dependency order: prerequisites first, then downstream questions.
4. **One question at a time**; wait for an answer before the next.
5. Each question includes a recommended answer with a short rationale.
6. Record resolved decisions, accepted trade-offs, and items explicitly deferred by the user.

Stop when open items are zero or all remaining items are marked deferred.

**Hard rules:**
- Do not write or edit any files — no design docs, no plans, no product code.
- If the user wants artifacts on disk after grilling, suggest writing them down; the user must request it explicitly.

## Red Flags

- Asking the user questions that can be answered from available context.
- Writing or editing plans, designs, or product code in this skill.
- Treating grill as mandatory before every decision.
- Expanding scope beyond what the user provided without asking.

## Verification

Confirm all decision-tree branches are either resolved or explicitly accepted/deferred before stopping.

## Output

Shared understanding reached, open branches resolved, and a recommended next step:

- direction still unset → suggest `sdd-brainstorm`
- plan needs writing or rewriting → suggest writing it down
- good enough to proceed → say so and stop
- within SDD flow → recommend the next SDD stage (`sdd-spec`, `sdd-plan`, etc.) if applicable

## Stop Conditions

Stop after shared understanding. Recommend one next step only; do not invoke it automatically.
