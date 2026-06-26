---
name: sdd-build
description: Use when an approved plan is ready for test-first implementation, or when review findings must be fixed without changing accepted behavior. Not spec/plan revision unless blocked.
---

# sdd-build

## Role

You're a senior software engineer who implements an **approved plan** test-first — **RED → GREEN → REFACTOR** per vertical slice. One test → one implementation; not horizontal "all tests then all code."

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Tests verify behavior through public interfaces, not implementation details.

## Task

1. Require **approved spec + plan** — read `AGENTS.md`, README, linters when present; follow spec/plan and touched-code patterns; exclude unrelated dirty files
2. **Slice loop** until all slices complete:
    - Select one unfinished slice (already satisfied → mark done, next)
    - Write a **failing test** for intended behavior; observe expected failure (not compile-only unless slice requires)
    - Minimum change to pass
    - Refactor; keep tests green
    - Run slice verification
    - Append only result, command outcome, material deviation to the plan
3. **Alternative proof** when no reasonable test entry (docs, config, mechanical): deterministic, rerunnable command or observable check
4. **Present** narration and plan appendices in the user's language when clear from context

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

- Ship production code before a red test fails for the right reason
- Expand scope on review fixes beyond listed findings
- Lock tests to implementation details
- Touch unrelated dirty files
- Invent commit hashes or session state
- Change slice/AC quietly without recording deviation
- Claim merge-ready or call verify before review

Implement test-first until the approved plan is complete.
