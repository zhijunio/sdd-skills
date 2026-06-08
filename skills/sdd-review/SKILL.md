---
name: sdd-review
description: Use when a diff needs an independent, read-only review for correctness, regressions, test gaps, specification compliance, or plan compliance.
---

# SDD Review

## Goal

Find actionable defects in a defined diff without modifying product, test, or plan files.

## When to Use

Use before delivery, after implementation, or when the user asks for a review.

It can run with only a diff. Missing spec or plan reduces traceability and must be disclosed.

## Prerequisites

Determine scope in this order:

1. User-specified files, PR, commit, branch, or baseline.
2. Scope recorded by the current task or plan.
3. Staged changes.
4. Task-related uncommitted changes.
5. Merge-base diff against the real integration branch.

Never assume `main`. Ask when unrelated changes, an unknown integration branch, multiple topics, or an oversized diff make the scope ambiguous.

## Process

1. State `Scope`, `Included`, and `Excluded`.
2. Read the complete scoped diff.
3. Read the spec and plan when available.
4. Check acceptance and plan compliance where evidence exists.
5. Check correctness, regressions, test gaps, and unnecessary complexity.
6. Report findings before summary, ordered by severity.

Use a fresh agent or subagent when available; otherwise reread the baseline before reviewing.

## Red Flags

- Editing while reviewing.
- Reviewing only staged files when the task includes unstaged work.
- Defaulting the baseline to `main`.
- Claiming specification compliance without a specification.

## Verification

Classify findings:

- `must-fix`: blocks delivery.
- `should-fix`: normally fixed; only the user accepts the risk.
- `suggestion`: non-blocking improvement.

## Output

Provide file and line references, findings, assumptions, and residual verification gaps. Do not update the plan; accepted risks are recorded later by the user or `sdd-build`.

## Stop Conditions

With blocking findings, recommend `sdd-build` and stop. Without blocking findings, recommend `sdd-ship` and stop.

