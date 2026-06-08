---
name: sdd-brainstorm
description: Use when a software change has an unclear goal, boundary, acceptance criteria, or costly design trade-off that should be resolved before writing a specification.
---

# SDD Brainstorm

## Goal

Resolve the decisions that block a reliable specification.

## When to Use

Use for ambiguous intent, multiple viable directions, irreversible choices, or unclear acceptance criteria **when no spec, plan, or design draft exists yet**.

Skip when behavior and boundaries are already explicit — route directly to `sdd-spec` or `sdd-grill`.

## Prerequisites

Read repository guidance and explore facts that can be answered from code or documentation before asking the user.

## Process

1. Ask one decision question at a time.
2. Provide a recommended answer with each question.
3. Walk dependent branches in order.
4. Compare two or three viable approaches when a real choice exists.
5. Converge on a recommended direction and explicit boundaries.
6. Record rejected approaches and why they were rejected.

Create `docs/sdd/YYYY-MM-DD-<topic>-brainstorm.md` only when complex decisions must survive the conversation.

## Red Flags

- Asking the user questions the repository can answer.
- Exploring implementation details before the goal is stable.
- Treating brainstorming as mandatory.
- Writing the formal specification in this skill.

## Verification

Confirm no unresolved question prevents writing observable acceptance criteria.

## Output

Provide the recommended direction, rationale, rejected alternatives, boundaries, and remaining specification questions.

## Stop Conditions

Recommend `sdd-spec` and stop. Do not write the formal specification automatically.

