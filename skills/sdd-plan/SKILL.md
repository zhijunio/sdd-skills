---
name: sdd-plan
description: Use when an approved specification needs to be decomposed into testable vertical slices before implementation begins.
---

# SDD Plan

## Goal

Turn an approved specification into small, observable, verifiable implementation slices.

## When to Use

Use after the user approves a specification source and before implementation starts.

Do not use to clarify product behavior or to implement code.

## Prerequisites

Require an approved specification at `docs/sdd/YYYY-MM-DD-<topic>-spec.md`. Read repository conventions and inspect the affected code before proposing tasks.

## Process

1. Start from [plan-template.md](plan-template.md).
2. Record the **Spec** path at the top of the plan.
3. Map every acceptance criterion to at least one vertical slice.
4. Prefer slices that deliver observable behavior, usually completable in 15 to 60 minutes.
5. A small increment may use a single slice; do not drop slice structure for a separate plan format.
6. Record dependencies, the failing test or alternative proof, implementation outline, verification command, and completion condition for each slice.
7. Keep local reversible choices in the plan.
8. Return public interface, persistent data, security boundary, or cross-module dependency changes to `sdd-spec`.
9. Present the written plan for user approval.

During `sdd-build`, append only factual results to each slice **Done** field: command outcome and material deviation. Do not record commit hashes.

## Red Flags

- Tasks split only by file or technical layer.
- Unmapped acceptance criteria.
- Commit hashes, status machines, or redundant traceability tables.
- Starting implementation before approval.

## Verification

Confirm all acceptance criteria are covered and each slice can be verified independently.

## Output

Write `docs/sdd/YYYY-MM-DD-<topic>-plan.md`.

## Stop Conditions

Stop after the user approves the plan. Recommend `sdd-build`.
