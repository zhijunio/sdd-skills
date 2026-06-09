---
name: sdd-build
description: Use when an approved SDD plan is ready for test-first implementation or when review findings must be fixed without changing accepted behavior.
---

# SDD Build

## Goal

Implement the approved plan incrementally while preserving scope and verification evidence.

## When to Use

Use for planned implementation and fixes returned from `sdd-review`.

When fixing review findings, address only the listed findings; do not expand scope.

Do not use when acceptance criteria or major constraints still need revision.

## Prerequisites

Require an approved spec and plan. Read repository guidance (`AGENTS.md`, README, linters) when present; when style or architecture rules are absent, follow the approved spec/plan and patterns in touched code. Inspect the current diff and exclude unrelated changes.

## Process

1. Select one unfinished slice. If the slice is already satisfied and verified, mark it done in the plan and pick the next.
2. Write a failing test for the **intended behavior** and observe the expected failure — not compile-only unless the slice requires it.
3. Implement the minimum change that passes.
4. Refactor while keeping relevant tests green.
5. Run the slice verification.
6. Append only the result, command outcome, and material deviation to the plan.
7. Repeat for the next slice.

**Fallback rules — stop immediately and route back when:**
- A slice cannot deliver its acceptance criterion without changing the criterion: record the deviation, stop, and return to `sdd-spec`.
- A slice boundary must change (merge, split, or reorder slices): record the change, stop, and return to `sdd-plan`.
- An open question from the spec is discovered to block implementation: record it, stop, and return to `sdd-spec`.

Documentation, pure configuration, mechanical changes, or projects without a reasonable automated test entry may use a **repeatable alternative proof** — a command or observable check that verifies the slice's goal without a unit or integration test (for example: a curl request returning expected JSON, a rendered HTML file containing expected text, or a CLI command producing correct output). The proof must be deterministic and rerunnable.

## Red Flags

- "The change is small" or "tests later" as an exception.
- Production changes before the intended red failure.
- Fixing review findings while expanding scope beyond those findings.
- Tests that lock implementation details instead of observable behavior.
- Editing unrelated dirty files.
- Recording commit hashes or inventing workflow state.
- Quietly changing slice boundaries, verification, or acceptance.
- Claiming merge-ready or invoking `sdd-ship` before `sdd-review`.

## Verification

Report each command and outcome. A local reversible deviation may continue; changed slice boundaries return to `sdd-plan`; changed acceptance or constraints return to `sdd-spec`.

## Output

Produce code, tests, and minimal factual plan updates. Follow repository Git conventions only when the user authorizes commits.

## Stop Conditions

Stop when all slices are implemented or a plan/spec revision is required. Recommend `sdd-review` when implementation is ready. Do not invoke `sdd-ship` or claim merge-ready from this skill.

