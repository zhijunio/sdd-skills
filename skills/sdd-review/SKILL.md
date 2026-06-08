---
name: sdd-review
description: Use when a scoped diff needs an independent, read-only review before delivery, after implementation, or when the user asks for a review.
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

Default scope is the full merge-base diff (`integration-base...HEAD`), not the whole repository unless the user gives an explicit commit range or PR.

Never assume `main`. Ask when unrelated changes, an unknown integration branch, multiple topics, an oversized diff, or a repo path without a commit range makes the scope ambiguous.

Pre-existing issues outside the scoped diff may be noted as out-of-scope observations; do not classify them as `must-fix` for this increment.

## Review Dimensions

### Core (always)

- **Spec / plan compliance** — acceptance criteria, out-of-scope boundaries; disclose when spec or plan is missing.
- **Correctness and regressions** — logic, edge cases, concurrency, data consistency.
- **Tests** — gaps, behavior vs implementation focus, assertions that would catch regressions.
- **Docs and traceability** — glossary/domain docs, ADR/plan paths, CHANGELOG, commit messages vs diff.

### Conditional (when the diff touches them)

- **Architecture** — new modules, cross-layer calls, shared APIs, duplication.
- **Security** — auth, user input, secrets in repo/logs, SQL or untrusted external data.
- **Performance** — N+1 queries, unbounded loops or fetches, hot paths, heavy sync work.
- **Readability and change size** — naming, control flow, unnecessary complexity; warn when a single increment is roughly >300 lines or one file grows substantially.

Skip conditional dimensions that the diff does not touch (for example, docs-only diffs skip security and performance).

Fresh command output and full acceptance evidence belong in `sdd-ship`, not here.

## Process

1. State `Scope`, `Included`, and `Excluded`.
2. Read the complete scoped diff.
3. Read the spec and plan when available; use domain glossary (for example `CONTEXT.md`) as a lightweight spec when no separate spec exists.
4. Review test changes first: coverage, edge cases, regression value.
5. Walk implementation against core and applicable conditional dimensions.
6. Report using the output template below. Findings first, ordered by severity; end with verdict.

Use a fresh agent or subagent when available; otherwise reread the baseline before reviewing.

Optional two-pass review when plan is large: spec/plan compliance first, then code quality. Default is one pass.

## Red Flags

- Editing while reviewing.
- Reviewing only staged files when the task includes unstaged work.
- Defaulting the baseline to `main`.
- Claiming specification compliance without a specification.
- Expanding scope to pre-existing code not in the scoped diff.
- Treating a repository path alone as scope without a commit range or baseline.
- Running full verification or updating the plan during review.

## Verification

Classify findings:

- `must-fix`: blocks delivery.
- `should-fix`: normally fixed; only the user accepts the risk.
- `suggestion`: non-blocking improvement.

## Output

Use this heading structure. Do not rename top-level sections.

```markdown
# SDD Review

## Scope

| Item | Content |
| ---- | ------- |
| Baseline | … |
| Included | commits, files, or unstaged task changes |
| Excluded | … |
| Spec / Plan | sources used, or disclosure when missing |

## Strengths

Optional. One to three specific positives.

## Findings

List only in-scope issues. Use `file:line` references.

### must-fix

…

### should-fix

…

### suggestion

…

If a severity has no items, write `None.`

## Dimension Coverage

Brief pass/fail (or skip) for each reviewed dimension: spec/plan, correctness, tests, docs, and any conditional dimensions examined.

## Assumptions & Gaps

What was assumed, not run, or observed outside scope. Label out-of-scope notes explicitly.

## Verdict

**`sdd-build`** or **`sdd-ship`** — one or two sentences of reason.
```

Do not update the plan; accepted risks are recorded later by the user or `sdd-build`.

## Stop Conditions

With blocking findings, recommend `sdd-build` and stop. Without blocking findings, recommend `sdd-ship` and stop.
