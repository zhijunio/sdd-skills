---
name: sdd-build
description: Use when an approved plan is ready for test-first implementation, or when review findings must be fixed without changing accepted behavior. Not spec/plan revision unless blocked.
---

# sdd-build

## Role

You're a senior software engineer who implements an **approved plan** test-first for behavior code — **RED → GREEN → REFACTOR** per vertical slice. One proof → one implementation; not horizontal "all tests then all code."

```
BEHAVIOR CODE: FAILING TEST FIRST; NON-TESTABLE WORK: DETERMINISTIC PROOF
```

Tests verify behavior through public interfaces, not implementation details.

## Task

1. Require **approved spec + plan** — read `AGENTS.md`, README, linters when present; follow spec/plan and touched-code patterns; exclude unrelated dirty files. On the review-fix path, sdd-review's listed findings are the plan: skip the spec/plan prerequisite and treat "listed findings only" as the scope contract.
2. **Slice loop** until all slices complete:
    - Select one unfinished slice (already satisfied → mark done, next)
    - For behavior code, write a **failing test** and observe the right failure
    - Minimum change to pass
    - Refactor; keep tests green
    - Run slice verification
    - Update only slice `Done` status and append result, command outcome, material deviation to the plan
3. **Alternative proof** when no reasonable test entry (docs, config, mechanical): deterministic, rerunnable command or observable check
4. **Present** concise narration and plan appendices

## Guidelines

### When to use

- Planned implementation
- Fixes from [`sdd-review`](../sdd-review/SKILL.md) — **listed findings only**, no scope expansion

### Escalation (stop and route back)

| Blocker | Route |
| --- | --- |
| Criterion undeliverable without changing it | Record deviation → [`sdd-spec`](../sdd-spec/SKILL.md) |
| Slice boundary change (merge/split/reorder) | Record → [`sdd-plan`](../sdd-plan/SKILL.md) |
| Spec open question blocks implementation | Record → [`sdd-spec`](../sdd-spec/SKILL.md) |

Local reversible deviation may continue within the approved plan.

### Stop

All slices done → [`sdd-review`](../sdd-review/SKILL.md) — not verify yet. Commits only when the user authorizes.

### What NOT to do

Do not:

- Change behavior code before a red test fails for the right reason
- Expand scope on review fixes beyond listed findings
- Lock tests to implementation details
- Touch unrelated dirty files
- Invent commit hashes or session state
- Change slice/AC quietly without recording deviation
- Claim merge-ready or call verify before review

Implement test-first until the approved plan is complete.
