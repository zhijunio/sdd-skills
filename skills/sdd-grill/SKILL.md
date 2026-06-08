---
name: sdd-grill
description: Use when an existing spec, plan, or design draft needs stress-testing before approval, or when the user says "grill me".
---

# SDD Grill

## Goal

Reach shared understanding by challenging every aspect of an existing plan or design until all decision-tree branches align.

## When to Use

Use when a spec, plan, or design draft already exists and needs stress-testing before approval, or when the user mentions "grill me".

**Requires an existing artifact** (spec draft, plan draft, design document, or a pasted summary). If no artifact exists and goals are still unclear, use `sdd-brainstorm` first.

Do not use when multiple directions are still open — use `sdd-brainstorm` first.

If the user provides a scope hint (e.g., "grill the database migration only"), limit grilling to that scope; do not expand into unrelated subsystems.

## Prerequisites

Read the existing artifact and repository guidance. Explore the codebase and documentation before asking the user — do not ask for facts that can be discovered locally.

## Process

1. Confirm the subject (pasted text, file path, or summary from the current thread).
2. List the major decision branches (briefly; no long essay).
3. Walk branches in dependency order: prerequisites first, then downstream questions.
4. **One question at a time**; wait for an answer before the next.
5. Each question includes a recommended answer with a short rationale.
6. Record resolved decisions, accepted trade-offs, and items explicitly deferred by the user.

Stop when open items are zero or all remaining items are marked deferred.

**Hard rules:**
- Do not write or edit any files — no spec, plan, design docs, or product code.
- If the user wants artifacts on disk after grilling, suggest `sdd-spec`, `sdd-plan`, or `sdd-brainstorm`; the user must switch explicitly.

## Red Flags

- Asking the user questions the repository can answer.
- Writing or editing spec, plan, or product code in this skill.
- Treating grill as mandatory before every spec or plan.
- Expanding scope beyond what the user provided without asking.

## Verification

Confirm all decision-tree branches are either resolved or explicitly accepted/deferred before stopping.

## Output

Shared understanding reached, open branches resolved, and the recommended next SDD skill.

## Stop Conditions

Stop after shared understanding. Recommend one next skill only; do not invoke it automatically:

- direction still unset → `sdd-brainstorm`
- spec needs work → `sdd-spec`
- plan needs work → `sdd-plan`
