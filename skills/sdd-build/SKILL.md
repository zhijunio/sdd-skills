---
name: sdd-build
description: Use when an approved SDD plan is ready for test-first implementation or when review findings must be fixed without changing accepted behavior.
---

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

RED → GREEN → REFACTOR per slice. Watch the test fail. Minimal code to pass. **Vertical slices** — one test → one implementation; not horizontal "all tests then all code." Tests verify behavior through public interfaces, not implementation details.

**When:** planned implementation; fixes from `sdd-review` (listed findings only — no scope expansion). **Not when:** AC or major constraints still need revision.

Require approved spec + plan. Read `AGENTS.md`, README, linters when present; else follow spec/plan and touched-code patterns. Exclude unrelated dirty files.

**Slice loop:**

1. Select one unfinished slice (already satisfied → mark done, next).
2. Failing test for **intended behavior**; observe expected failure (not compile-only unless slice requires).
3. Minimum change to pass.
4. Refactor; keep tests green.
5. Run slice verification.
6. Append only result, command outcome, material deviation to plan.
7. Repeat.

**Stop and route back:**

- Criterion undeliverable without changing it → record deviation → invoke `sdd-spec`.
- Slice boundary change (merge/split/reorder) → record → invoke `sdd-plan`.
- Spec open question blocks implementation → record → invoke `sdd-spec`.

**Alternative proof** when no reasonable test entry (docs, config, mechanical): deterministic, rerunnable command or observable check (curl JSON, rendered HTML, CLI output).

**Red flags:** "small change" / "tests later"; production before red failure; scope expansion on review fixes; tests locking implementation; unrelated dirty files; commit hashes or invented state; quiet slice/AC changes; claiming merge-ready or invoking `sdd-ship` before `sdd-review`.

**SDD:** User's language for narration. Local reversible deviation may continue. Stop when all slices done → invoke `sdd-review` (not `sdd-ship`). Escalation → invoke `sdd-plan` or `sdd-spec`. Commits only when user authorizes.
