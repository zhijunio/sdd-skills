---
name: sdd-grill
description: Use when an existing spec, plan, or design draft needs stress-testing before approval, or when the user says "grill me".
---

# SDD Grill

## Goal

Reach shared understanding by challenging every aspect of an existing plan or design.

## When to Use

Use when a spec, plan, or design draft already exists and needs stress-testing before approval, or when the user mentions "grill me".

**Requires an existing artifact** (spec draft, plan draft, or design document). If no artifact exists and goals are still unclear, use `sdd-brainstorm` first.

Do not use when multiple directions are still open — use `sdd-brainstorm` first.

## Prerequisites

Read repository guidance. If a question can be answered by exploring the codebase, explore the codebase instead of asking the user.

## Process

1. Read the existing artifact (spec, plan, or design) and repository context.
2. Identify weak points: missing edge cases, unstated assumptions, dependency risks, or unclear boundaries.
3. Ask one focused question at a time about each weak point.
4. Provide a recommended answer with each question.
5. Walk down each branch of the decision tree, resolving dependencies one-by-one.
6. Record resolved decisions, accepted trade-offs, and remaining open items.

Do not write or edit the spec, plan, or product code during this skill.

## Red Flags

- Asking the user questions the repository can answer.
- Writing or editing spec, plan, or product code in this skill.
- Treating grill as mandatory before every spec or plan.

## Verification

Confirm unresolved branches are either resolved or explicitly accepted before stopping.

## Output

Shared understanding reached, open branches resolved, and the recommended next SDD skill.

## Stop Conditions

Stop after shared understanding. Recommend one next skill only; do not invoke it automatically:

- direction still unset → `sdd-brainstorm`
- spec needs work → `sdd-spec`
- plan needs work → `sdd-plan`
