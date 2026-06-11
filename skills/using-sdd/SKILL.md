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

When routing, you may state briefly that you are checking the SDD stage and name the recommended skill. Do not invoke that skill automatically.

1. Identify the active, independently testable increment.
2. Assess uncertainty, impact, reversibility, and verification cost.
3. Route to **one** skill using the **Routing matrix** below.
4. Explain any skipped stage briefly.

## Routing matrix

Normative routing for this skill. Recommend **one** skill only; do not invoke automatically.

**Optional satellites** (`sdd-zoom`, `sdd-improve`) are not part of the mandatory core loop before `sdd-ship`. After **`sdd-improve`**, hand off per **Next stage** — SDD skill via **`using-sdd`** (default **`sdd-spec`** when AC needed) or **direct edit** (no skill); see **`sdd-improve`** [closing-the-loop.md](../sdd-improve/references/closing-the-loop.md).

### Disambiguation

**Canonical pair:** **opportunity scan** (`sdd-improve`) vs **delivery review** (`sdd-review`). Same lenses can overlap; **scope**, **outcome**, and **timing** differ.

| | **Opportunity scan** `sdd-improve` | **Delivery review** `sdd-review` |
| --- | --- | --- |
| Question | What opportunities or problems exist? | Does this **increment** meet spec/plan and ship? |
| Scope | **Whole repo** or **branch** vs merge-base | **Increment diff** only (defined range; default `merge-base…HEAD`) |
| Criteria | Leverage, categories 1–9 | Spec / plan / **AC** |
| Outcome | **Findings report** — user selects follow-ups | **Delivery verdict** — pass / must-fix / should-fix → ship |
| Timing | Exploratory — health check, pre-increment | After **`sdd-build`**, before ship |
| Branch | Tags `introduced` and `pre-existing` | Only defects **introduced or worsened** by diff |
| Unique | experience (7) incl. **ops**; direction (9); cat 5 = structure **+** DRY signals | AC mapping; **architecture** on **code** diffs; conditionals incl. **observability / a11y / ops** when signals apply |

**Routing heuristic** — when intent is unclear, apply in order:

| Cue | Route |
| --- | --- |
| PR, plan, AC, ship, merge, deliver, ready to merge | **delivery review** `sdd-review` |
| health check, audit, architecture debt, roadmap — **no** delivery context | **opportunity scan** `sdd-improve` |
| before PR + compare to plan / ship / AC | **delivery review** `sdd-review` |
| before PR + risks / opportunities (no delivery gate) | **opportunity scan** `sdd-improve` |
| "review" **without** increment diff **and** delivery context | **Ask** — delivery review vs opportunity scan; do not route silently |

| User says / means | Route |
| --- | --- |
| "zoom out", "big picture", unfamiliar territory — **map**, not findings | `sdd-zoom` |
| Unfamiliar territory **and** open trade-offs | **`sdd-zoom` first** — then **`using-sdd`** → **`sdd-grill`** if decisions remain |
| Goals, boundaries, trade-offs still open | `sdd-grill` |

### Pre-spec

| Situation | Route | Skip |
| --- | --- | --- |
| Unfamiliar territory; need map before spec, grill, or build | `sdd-zoom` | — |
| Goals, boundaries, trade-offs, or plan/design still need decisions | `sdd-grill` | — |
| **Opportunity scan** before spec (audit, architecture, health check); not **delivery review** | `sdd-improve` | — |
| Boundaries clear; small reversible change | `sdd-spec` | grill |

### Core loop

| Situation | Route |
| --- | --- |
| No user-approved spec | `sdd-spec` |
| Spec approved; no plan | `sdd-plan` |
| Plan approved; slices unfinished | `sdd-build` |
| Build done; diff ready | `sdd-review` |
| No must-fix; should-fix fixed or accepted | `sdd-ship` |

### Review loop

| Review verdict | Route |
| --- | --- |
| must-fix or should-fix to address | `sdd-build` |
| pass | `sdd-ship` |

### Escalation from build

| Change type | Route |
| --- | --- |
| Local slice detail only | stay in `sdd-build` |
| Slice boundaries or verification changed | `sdd-plan` |
| Acceptance or constraints changed | `sdd-spec` (revise in place; log; re-approve if AC or constraints change) |

### User named a stage

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
