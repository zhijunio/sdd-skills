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

Require a defined diff range before reviewing code. Determine scope using **Scope** below.

## Scope

Determine the diff range in this order:

1. User-specified files, PR, commit range, branch pair, or baseline.
2. Scope recorded by the current task or plan.
3. Staged changes only when the user or task explicitly limits review to staged work.
4. Task-related uncommitted changes that belong to the same increment.
5. Merge-base diff against the real integration branch: `merge-base(<integration-base>, HEAD)...HEAD`.

### Integration base

- Prefer the repository's default integration branch (`origin/HEAD`, or the branch named in repository guidance).
- Use the branch the user names when it differs from defaults.
- **Never assume `main`**, `master`, or any branch name without evidence.

### Default range

When nothing more specific applies, review the **full** merge-base diff for the current branch, not the entire repository history and not an arbitrary subset of files.

Include task-related **uncommitted** changes in the same review when they complete the increment (for example fixes still sitting in the working tree).

### Narrow or split scope

Ask before reviewing when:

- The user gives a repository path but no commit range, PR, or baseline.
- Unrelated dirty files would pollute the diff.
- The integration branch is unknown or ambiguous.
- One diff mixes multiple independent topics or increments.
- The range is too large to review reliably in one pass.

When the user names a subset, honor it and record what was excluded.

### Pre-existing code

Issues in code **outside** the scoped diff may be noted as **out-of-scope observations**. Do not classify them as `must-fix` or `should-fix` for this increment unless the scoped diff reintroduces, exposes, or worsens them.

Fresh command output and full acceptance evidence belong in `sdd-ship`, not here.

## Review Dimensions

### Core (always)

- **Spec / plan compliance** — acceptance criteria, out-of-scope boundaries; disclose when spec or plan is missing.
- **Correctness and regressions** — logic, edge cases, concurrency, data consistency.
- **Tests** — gaps, behavior vs implementation focus, assertions that would catch regressions.
- **Docs and traceability** — spec/plan paths, CHANGELOG, commit messages vs diff.

### Conditional (when the diff touches them)

- **Architecture** — new modules, cross-layer calls, shared APIs, duplication **introduced or worsened by this diff**. Whole-codebase deepening opportunities outside the diff belong in optional **`sdd-architect`**, not here; note those only as out-of-scope observations.
- **Security** — auth, user input, secrets in repo or logs, SQL or untrusted external data.
- **Performance** — N+1 queries, unbounded loops or fetches, hot paths, heavy synchronous work.
- **Readability and change size** — naming, control flow, unnecessary complexity; flag when a single increment is roughly **>300 lines** or one file grows substantially without justification.

Skip conditional dimensions the diff does not touch (for example, docs-only diffs skip security and performance).

## Process

1. State scope using the output template below (`Scope` table).
2. Read the **complete** scoped diff before judging correctness.
3. Read the spec and plan when available.
4. Review test changes first: coverage, edge cases, regression value.
5. Walk implementation against core and applicable conditional dimensions.
6. Report findings before summary, ordered by severity; end with verdict.

Use a fresh agent or subagent when available; otherwise reread the baseline before reviewing.

Optional two-pass review when the plan is large: spec/plan compliance first, then code quality. Default is one pass.

## Red Flags

- Editing while reviewing.
- Reviewing only staged files when the task includes unstaged increment work.
- Defaulting the baseline to `main` or `master` without evidence.
- Reviewing the whole repository without a commit range.
- Treating a directory path alone as scope.
- Expanding scope to pre-existing code not in the scoped diff and marking it `must-fix`.
- Claiming specification compliance without a specification.
- Running full verification or updating the plan during review.

## Verification

Classify findings:

- `must-fix`: blocks delivery within the scoped increment.
- `should-fix`: normally fixed; only the user accepts the risk.
- `suggestion`: non-blocking improvement.

## Output

Use this heading structure. Do not rename top-level sections.

```markdown
# SDD Review

## Scope

| Item | Content |
| ---- | ------- |
| Baseline | integration branch or commit |
| Range | `merge-base...HEAD`, PR, commits, or user-specified span |
| Included | commits, files, staged/unstaged task changes |
| Excluded | unrelated changes, out-of-scope areas |
| Spec / Plan | paths used, or disclosure when missing |

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

Brief pass, fail, or skip for each dimension examined: spec/plan, correctness, tests, docs, and any conditional dimensions reviewed.

## Assumptions & Gaps

What was assumed, not run, or observed outside scope. Label out-of-scope notes explicitly.

## Verdict

**`sdd-build`** or **`sdd-ship`** — one or two sentences of reason.
```

Do not update the plan; accepted risks are recorded later by the user or `sdd-build`.

## Stop Conditions

With blocking findings, recommend `sdd-build` and stop. Without blocking findings, recommend `sdd-ship` and stop.
