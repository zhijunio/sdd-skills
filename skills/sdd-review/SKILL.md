---
name: sdd-review
description: Use when a scoped diff needs an independent, read-only review before delivery, after implementation, or when the user asks for a review. Always includes a mandatory simplify pass for DRY/KISS opportunities in the scoped diff.
---

# SDD Review

## Goal

Find actionable defects and behavior-preserving simplification opportunities in a defined diff without modifying product, test, or plan files.

## When to Use

Use before delivery, after implementation, or when the user asks for a review.

It can run with only a diff. Missing spec or plan reduces traceability and must be disclosed.

Skip when the user wants **机会扫描** (whole-repo or branch health check) without a delivery increment — use **`sdd-improve`**.

### Disambiguation vs **机会扫描** `sdd-improve`

**交付审** (this skill) vs **机会扫描** — normative table in [using-sdd — Disambiguation](../using-sdd/SKILL.md#disambiguation).

| | **机会扫描** `sdd-improve` | **交付审** `sdd-review` |
| --- | --- | --- |
| Outcome | **Findings report** | **Delivery verdict** (pass / must-fix / should-fix) |
| Scope | Whole repo or branch vs merge-base | **Increment diff** only (defined range; default `merge-base…HEAD`) |

Dimension checklists: [review-dimensions.md](references/review-dimensions.md). Ambiguous review/审查 without increment diff → **`using-sdd`** asks which skill.

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

### Large diffs

When the diff is roughly **30+ files** or **>300 lines**, triage **high-risk areas first**: auth, secrets, migrations, public API, money or data-loss paths. Sample or defer the rest; record **Limits** (what was not fully read) in **Assumptions & Gaps**. Prose-only diffs: prioritize spec/plan traceability and clarity.

### Pre-existing code

Issues in code **outside** the scoped diff may be noted as **out-of-scope observations**. Do not classify them as `must-fix` or `should-fix` for this increment unless the scoped diff reintroduces, exposes, or worsens them.

Fresh command output and full acceptance evidence belong in `sdd-ship`, not here.

## Review Dimensions

Walk dimensions on the **scoped diff only**. Detailed checklists: [review-dimensions.md](references/review-dimensions.md) (agent-skills five-axis summary + SDD delivery gate).

### Core (always)

- **Spec / plan compliance** — AC mapping; Non-goals; disclose missing artifacts.
- **Correctness and regressions** — logic, error paths, edge cases, concurrency, data consistency.
- **Tests** — behavior vs implementation; regression value; review test changes before implementation.
- **Docs and traceability** — spec/plan paths, CHANGELOG, standalone commit/PR descriptions.

### Conditional (when the diff touches them)

- **Standards** — repository guidance and CI-gated linters.
- **Architecture** — modules, boundaries, patterns, duplication **introduced or worsened by this diff** only.
- **Security** — authz, input boundaries, injection/XSS, secrets, untrusted external data.
- **Performance** — N+1, unbounded work, pagination, hot-path cost in changed code.
- **Readability** — naming, control flow, dead code introduced in the diff.
- **Dependencies** — new/upgraded packages: necessity, audit, license, lockfile (when manifest files change).
- **Simplify (mandatory on code diffs)** — behavior-preserving DRY/KISS in the diff; see checklist below. Pre-existing duplication → out-of-scope only.

Skip conditional dimensions the diff does not touch (e.g. docs-only → skip security and performance). **Never skip Simplify** on non-trivial code diffs.

## Process

1. State scope using the output template below (`Scope` table).
2. Read the **complete** scoped diff before judging correctness — or triage per **Large diffs** and disclose **Limits**.
3. Read the spec and plan when available; map Acceptance when a plan exists.
4. Review test changes first: coverage, edge cases, regression value.
5. Walk implementation against core and applicable conditional dimensions.
6. **Simplify pass (mandatory for code diffs)** — after correctness, run the checklist below on the full scoped diff. Record each hit as `suggestion` or `should-fix` when the duplication is large, migration is half-done, or the slice is harder to maintain than a small extract would cost. If nothing applies, write `None.` under **### simplify** and say `simplify: pass` in **Dimension Coverage**.
7. Report findings before summary, ordered by severity; end with verdict.

### Simplify pass checklist

Scan the scoped diff for behavior-preserving simplifications. Prefer `file:line — [simplify] — …` in findings.

| Signal | Look for |
| ------ | -------- |
| **Parallel APIs** | Two entry points doing the same job (e.g. `foo` vs `fooIds`, overload vs new method) where one path or a thin wrapper would suffice |
| **Repeated blocks** | Same 5+ line pattern in multiple files (resolve/filter/build-param helpers, private methods that differ only by type) — candidate for shared util or base method |
| **Copy-paste UI** | Identical or near-identical components, hooks, form fields, Cascader/search wiring repeated across screens |
| **Field or param bloat** | New fields that duplicate an existing one (`areaId` + `areaIds`) without a documented compatibility reason; merge at Query/DTO boundary when safe |
| **Layer noise** | Extra indirection, pass-through methods, or abstractions added in the same increment without reuse |
| **Half migration** | Old path still called beside new path; staged but uncommitted pieces of the same refactor; dead code left after switch |
| **Dead code introduced** | Unreachable branches, legacy shims, or no-op variables added or left in the diff after a switch |
| **Test duplication** | Same arrange/assert copied across tests — table-driven or shared fixture candidate |

**Severity:** `should-fix` when half-migration or large duplication blocks maintainability or risks drift; otherwise `suggestion`. Do not mark `must-fix` solely for simplify unless the diff clearly violates an agreed Non-goal (e.g. “no dual API”) from the plan.

**Out of scope:** pre-existing duplication untouched by the diff — note under **Assumptions & Gaps**, not `must-fix`.

Prefer `file:line — [spec|standards] — issue` in findings when the lens matters. On auth, secrets, migrations, or public API, label **inferred** claims as such; do not state inference as fact.

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
- Finishing review without the **Simplify pass** on a non-trivial code diff.
- Treating DRY/KISS only as optional style nits — duplication introduced or left half-migrated by the diff belongs in **### simplify** or **should-fix**.

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

List only in-scope issues. Use `file:line` references; optional `[spec]` or `[standards]` tags.

### must-fix

…

### should-fix

…

### suggestion

…

### simplify

Behavior-preserving DRY/KISS opportunities from the mandatory simplify pass. Tag lines with `[simplify]` when helpful.

…

If a severity subsection has no items, write `None.`

## Dimension Coverage

Brief pass, fail, or skip for each dimension examined: spec/plan (including Acceptance mapping when a plan exists), correctness, tests, docs, **simplify (mandatory on code diffs)**, and any conditional dimensions reviewed (standards, architecture, security, performance, readability, dependencies).

## Assumptions & Gaps

What was assumed, not run, or observed outside scope. Label out-of-scope notes and **Limits** (sampled or unread areas on large diffs) explicitly.

## Verdict

**`sdd-build`** or **`sdd-ship`** — one or two sentences of reason.
```

Do not update the plan; accepted risks are recorded later by the user or `sdd-build`.

## Stop Conditions

With blocking findings, recommend `sdd-build` and stop. Without blocking findings, recommend `sdd-ship` and stop.
