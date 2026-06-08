---
name: sdd-build
description: Use when an approved SDD plan is ready for test-first implementation or when review findings must be fixed without changing accepted behavior.
---

# SDD Build

## Goal

Implement the approved plan incrementally while preserving scope and verification evidence.

## When to Use

Use for planned implementation and fixes returned from `sdd-review`.

Do not use when acceptance criteria or major constraints still need revision.

## Prerequisites

Require an approved spec and plan. Read repository guidance, inspect the current diff, and exclude unrelated changes.

## Process

1. Select one unfinished slice.
2. Write a failing test and observe the expected failure.
3. Implement the minimum change that passes.
4. Refactor while keeping relevant tests green.
5. Run the slice verification.
6. Append only the result, command outcome, and material deviation to the plan.
7. Repeat for the next slice.

Documentation, pure configuration, mechanical changes, or projects without a reasonable automated test entry may use repeatable alternative proof.

## Red Flags

- "The change is small" or "tests later" as an exception.
- Editing unrelated dirty files.
- Recording commit hashes or inventing workflow state.
- Quietly changing slice boundaries, verification, or acceptance.

## Verification

Report each command and outcome. A local reversible deviation may continue; changed slice boundaries return to `sdd-plan`; changed acceptance or constraints return to `sdd-spec`.

## Output

Produce code, tests, and minimal factual plan updates. Follow repository Git conventions only when the user authorizes commits.

## Stop Conditions

Stop when all slices are implemented or a plan/spec revision is required. Recommend `sdd-review` when implementation is ready.

