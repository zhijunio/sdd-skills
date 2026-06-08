---
name: sdd-grill
description: Use when the user wants to stress-test a plan or design, get grilled on their design, or mentions "grill me". Works within SDD or standalone.
---

# SDD Grill

## Goal

Reach shared understanding by grilling every aspect of the plan or design under discussion.

## When to Use

Use when the user wants to stress-test a plan, get grilled on their design, or mentions "grill me".

The subject may be a file, a pasted summary, or the plan as stated in the conversation. A disk artifact is not required.

Use within the SDD workflow or standalone for any decision.

Skip when the user still needs to choose between multiple unexplored directions and wants options compared — use `sdd-brainstorm` first.

## Prerequisites

Read repository guidance and any subject the user gave.

If a question can be answered by exploring the codebase, explore the codebase instead of asking the user.

## Process

Interview the user relentlessly about every aspect of this plan until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

## Red Flags

- Asking the user questions the repository can answer.
- Writing or editing spec, plan, design docs, or product code in this skill.
- Treating grill as mandatory before every spec or plan.

## Verification

Confirm open branches are resolved or explicitly accepted before stopping.

## Output

Shared understanding reached and the recommended next step.

## Stop Conditions

Stop after shared understanding. Recommend one next skill only; do not invoke it automatically:

- still choosing between directions → `sdd-brainstorm`
- spec needs work → `sdd-spec`
- plan needs work → `sdd-plan`
