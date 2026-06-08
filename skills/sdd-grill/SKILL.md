---
name: sdd-grill
description: Use when the user wants to stress-test a plan or design, get grilled, or says "grill me", before locking the next SDD stage.
---

# SDD Grill

## Goal

Reach shared understanding by grilling every aspect of the current plan or design.

## When to Use

Use when the user wants to stress-test a plan, get grilled on their design, or mentions "grill me".

Do not use when multiple directions are still open — use `sdd-brainstorm` first.

## Prerequisites

Read repository guidance. If a question can be answered by exploring the codebase, explore the codebase instead of asking the user.

## Process

Interview the user relentlessly about every aspect of this plan until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

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
