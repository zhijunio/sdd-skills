---
name: sdd-spec
description: Use when a software change needs a durable behavior contract, scope, acceptance criteria, and necessary technical constraints before implementation planning.
---

# SDD Spec

## Goal

Write a concise specification that defines what must be true without prescribing file-by-file implementation.

## When to Use

Use for a new project, feature, bug fix, migration, or meaningful behavior change whose intent is sufficiently clear.

Use also when an approved specification needs in-place revision because acceptance criteria or constraints changed during planning, build, or review.

Do not use to explore unresolved design directions or to write implementation tasks.

## Prerequisites

Read repository guidance, relevant code and docs, and any clarify outcome from `sdd-grill`. Ask only for decisions that cannot be discovered locally.

## Process

### New specification

1. Start from [spec-template.md](spec-template.md).
2. Define the goal, scope, and non-goals.
3. Record only repository facts that constrain the change.
4. Write requirements and necessary compatibility, migration, security, or interface constraints.
5. Give each observable acceptance criterion a stable identifier such as `AC-1`.
6. Remove irrelevant template sections.
7. Present the written specification for user approval.

### Revision

Revise the same `docs/sdd/YYYY-MM-DD-<topic>-spec.md` in place. Do not create a second spec file or a `-v2` copy.

1. Make the needed edits to Requirements, Acceptance Criteria, or Constraints.
2. Append one **Revision log** entry with: date, reason, changed AC IDs (or `none — clarification`), and plan impact (`yes` / `no` with brief note).
3. **Clarification only** — wording, background, or scope/non-goals that do not change any pass/fail outcome: log the entry and stop. No re-approval. Continue the stage that triggered the edit (`sdd-plan`, `sdd-build`, or `sdd-review`).
4. **AC or constraint change** — any criterion or constraint whose pass/fail or limit changes: present the updated specification for user re-approval.
5. After re-approval: recommend `sdd-plan` only when slice boundaries or verification steps change; otherwise return to the prior stage.

Examples:

- Clarification: reword AC-2 for readability without changing when it passes or fails → log only, no re-approval.
- AC change: AC-3 response-time limit changes from 200ms to 500ms → re-approve; if plan slices are unchanged, return to `sdd-build`.

## Red Flags

- Hiding implementation steps inside acceptance criteria.
- Copying the grill or clarify transcript verbatim.
- Leaving open questions that block planning.
- Treating file existence as user approval.
- Creating a new spec file instead of revising in place.
- Skipping re-approval after an acceptance criterion or constraint change.

## Verification

Check that every criterion has a clear pass/fail result and that no requirement depends on an undefined term.

## Output

Write `docs/sdd/YYYY-MM-DD-<topic>-spec.md`.

## Stop Conditions

Stop after the user approves a new specification. Recommend `sdd-plan`.

For a clarification-only revision, stop after logging. Do not recommend a stage change.

For a revised specification after AC or constraint change, stop after user re-approval. Recommend `sdd-plan` when plan impact is yes; otherwise name the prior stage to resume (`sdd-build` or `sdd-review`).

