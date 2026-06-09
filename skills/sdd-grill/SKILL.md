---
name: sdd-grill
description: Use when a software change has unclear goals, boundaries, or trade-offs before specification, when the user wants to stress-test a plan or design, or mentions "grill me". Works within SDD or standalone.
---

# SDD Grill

## Goal

Resolve blocking decisions and reach shared understanding before writing or revising a specification or plan.

## When to Use

Use for ambiguous intent, multiple viable directions, irreversible choices, unclear acceptance criteria, or when the user wants to stress-test a plan or design and says "grill me".

The subject may be a file, a pasted summary, or the plan as stated in the conversation. A disk artifact is not required.

Use within the SDD workflow or standalone for any decision.

Skip when behavior and boundaries are already explicit — route directly to `sdd-spec`.

## Prerequisites

Read repository guidance and explore facts that can be answered from code or documentation before asking the user.

If a question can be answered by exploring the codebase, explore the codebase instead of asking the user.

## Process

Ask one decision question at a time. Provide a recommended answer with each question. Walk dependent branches in order.

**Explore** — when multiple viable directions are still open:

1. Compare two or three approaches when a real choice exists.
2. Converge on a recommended direction and explicit boundaries.
3. Record rejected approaches and why they were rejected.

**Challenge** — when a plan or design is already on the table:

1. Interview the user about every aspect until shared understanding is reached.
2. Resolve dependencies between decisions one-by-one.

Create `docs/sdd/YYYY-MM-DD-<topic>-clarify.md` only when complex decisions must survive the conversation.

Both phases may appear in one session. Start with explore when directions are still open; shift to challenge once a direction or artifact is stable enough to stress-test.

## Red Flags

- Asking the user questions the repository can answer.
- Exploring implementation details before the goal is stable.
- Treating grill as mandatory before every spec or plan.
- Writing or editing spec, plan, design docs, or product code in this skill.

## Verification

Confirm no unresolved question prevents writing observable acceptance criteria or continuing the plan under discussion.

## Output

Provide the recommended direction, rationale, rejected alternatives when applicable, boundaries, shared understanding reached, and remaining specification or plan questions.

## Stop Conditions

Stop after shared understanding. Recommend one next skill only; do not invoke it automatically:

- ready for a behavior contract → `sdd-spec`
- plan needs work → `sdd-plan`
