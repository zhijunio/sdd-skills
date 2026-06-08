---
name: using-sdd
description: Use when a software task needs routing to the appropriate SDD stage, especially when it is unclear whether to brainstorm, specify, plan, build, review, or ship.
---

# Using SDD

## Goal

Choose one appropriate SDD skill from current facts without maintaining workflow state.

## When to Use

Use at the start of an unfamiliar task or when the next stage is ambiguous.

Do not use when the user already named the stage skill.

## Prerequisites

None. Read the request, repository guidance, relevant SDD documents, and current diff when available.

## Process

1. Identify the active, independently testable increment.
2. Assess uncertainty, impact, reversibility, and verification cost.
3. Route to one skill:
   - unclear goal or costly trade-off: `sdd-brainstorm`
   - no confirmed specification: `sdd-spec`
   - confirmed specification without a plan: `sdd-plan`
   - approved plan with unfinished work: `sdd-build`
   - implementation ready for independent review: `sdd-review`
   - review passed and final evidence is needed: `sdd-ship`
4. Explain any skipped stage briefly.

## Red Flags

- Inventing a persistent status.
- Defaulting every task to the full workflow.
- Routing multiple unrelated increments together.
- Calling the next skill automatically.

## Verification

Confirm the recommendation matches the available artifacts and repository state.

## Output

State the active increment, recommended path, skipped stages, reason, and one next skill.

## Stop Conditions

Stop after the routing recommendation. The user loads the next skill.

