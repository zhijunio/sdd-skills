---
name: using-sdd
description: Use when a software task needs routing to the appropriate SDD stage, especially when it is unclear whether to clarify, specify, plan, build, review, or ship.
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
   - unclear goal, costly trade-off, or stress-test a plan or design: `sdd-grill`
   - no confirmed specification: `sdd-spec`
   - confirmed specification without a plan: `sdd-plan`
   - approved plan with unfinished work: `sdd-build`
   - implementation ready for independent review: `sdd-review`
   - review passed and final evidence is needed: `sdd-ship`
4. Explain any skipped stage briefly.

## Routing examples

Use one next skill only. Do not invoke it automatically.

**Pre-spec**

| Situation | Route | Skip |
| --- | --- | --- |
| Goals, boundaries, trade-offs, or plan/design still need decisions | `sdd-grill` | — |
| Boundaries clear; small reversible change | `sdd-spec` | grill |

**Core loop**

| Situation | Route |
| --- | --- |
| No user-approved spec | `sdd-spec` |
| Spec approved; no plan | `sdd-plan` |
| Plan approved; slices unfinished | `sdd-build` |
| Build done; diff ready | `sdd-review` |
| No must-fix; should-fix fixed or accepted | `sdd-ship` |

**Review loop**

| Review verdict | Route |
| --- | --- |
| must-fix or should-fix to address | `sdd-build` |
| pass | `sdd-ship` |

**Escalation from build**

| Change type | Route |
| --- | --- |
| Local slice detail only | stay in `sdd-build` |
| Slice boundaries or verification changed | `sdd-plan` |
| Acceptance or constraints changed | `sdd-spec` (revise in place; log; re-approve if AC or constraints change) |

**User named a stage**

Honor it. Do not route through `using-sdd` again unless the named stage is wrong for the artifacts in hand.

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
