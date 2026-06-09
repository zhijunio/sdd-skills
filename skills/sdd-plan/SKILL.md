---
name: sdd-plan
description: Use when an approved specification needs to be decomposed into testable vertical slices before implementation begins.
---

# SDD Plan

## Goal

Turn an approved specification into small, observable, verifiable implementation slices.

## When to Use

Use after the user approves a specification and before implementation starts.

Do not use to clarify product behavior or to implement code.

## Prerequisites

Require an approved specification. Read repository conventions and inspect the affected code before proposing tasks.

## Process

1. Start from [plan-template.md](plan-template.md).
2. Map every acceptance criterion to at least one vertical slice.
3. Prefer slices that deliver observable behavior, usually completable in 15 to 60 minutes.
4. Record dependencies, the failing test or alternative proof, implementation outline, verification command, and completion condition.
5. Record **Risks / Dependencies** when they affect slice order, verification, or rollback (omit when none).
6. Keep local reversible choices in the plan.
7. Return public interface, persistent data, security boundary, or cross-module dependency changes to `sdd-spec`.
8. **Self-review** the draft before user approval:
   - no placeholders in slices or verification commands
   - every spec acceptance criterion maps to at least one slice
   - risks and dependencies are concrete when present
   - each slice is independently verifiable
9. Present the written plan for user approval.

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

