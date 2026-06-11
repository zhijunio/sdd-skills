---
name: sdd-review
description: Use when a scoped diff needs an independent, read-only review before delivery, after implementation, or when the user asks for a review. Classifies code diff vs prose/docs-only; mandatory architecture walk on code diffs only.
---

# SDD Review

## Goal

You are a **read-only reviewer, not an implementer**. Find actionable defects and behavior-preserving simplification opportunities in a defined **increment diff**; deliver a **delivery review report** with evidence — without modifying product, test, or plan files.

## When to Use

Use before delivery, after implementation, or when the user asks for a review.

It can run with only a diff. Missing spec or plan reduces traceability and must be disclosed.

Skip when the user wants **opportunity scan** (whole-repo or branch health check) without a delivery increment — use **`sdd-improve`**.

### Disambiguation vs **opportunity scan** `sdd-improve`

**This skill:** **delivery verdict** · increment diff only. **Not** whole-repo audit — pairing table: [using-sdd — Disambiguation](../using-sdd/SKILL.md#disambiguation). Ambiguous "review" without increment diff → **`using-sdd`** asks which skill.

Report structure: [finding-format.md](references/finding-format.md). Dimension checklists: [review-dimensions.md](references/review-dimensions.md).

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

When the diff is roughly **30+ files** or **>300 lines**, triage **high-risk areas first**: auth, secrets, migrations, public API, money or data-loss paths. Sample or defer the rest; record **Limits** (what was not fully read) in **Coverage — Limits**. Prose-only diffs: prioritize spec/plan traceability and clarity.

### Pre-existing code

Issues in code **outside** the scoped diff may be noted as **out-of-scope observations**. Do not classify them as `must-fix` or `should-fix` for this increment unless the scoped diff reintroduces, exposes, or worsens them.

Fresh command output and full acceptance evidence belong in `sdd-ship`, not here.

### Diff kind

Classify from changed paths **before** dimension walk; record in **Context — Scope**.

| Kind | Rule of thumb | Architecture |
| --- | --- | --- |
| **Code diff** | Any executable source, test code, CI/build script, or behavior-changing config | **Mandatory** → `architecture: pass` or findings |
| **Prose/docs-only** | Only markdown, docs, comments-only, or metadata with no runtime behavior | **Skip** → `architecture: skip` |

Any code path in the diff → **code diff** (even one `tests/check.py` beside ten `.md` files). Full signals and edge cases: [review-dimensions.md — Diff kind](references/review-dimensions.md#diff-kind).

## Review Dimensions

Walk dimensions on the **scoped diff only**. Detailed checklists: [review-dimensions.md](references/review-dimensions.md) (agent-skills five-axis summary + SDD delivery gate).

### Core (always)

- **Spec / plan compliance** — AC mapping; Non-goals; disclose missing artifacts.
- **Correctness and regressions** — logic, error paths, edge cases, concurrency, data consistency.
- **Tests** — behavior vs implementation; regression value; review test changes before implementation.
- **Docs and traceability** — spec/plan paths, CHANGELOG, commit/PR descriptions; **reference integrity** on renames (especially **prose/docs-only**).

### Mandatory on code diffs

- **Architecture** — structure insight **and** duplication/DRY/KISS in the diff (same lenses as **`sdd-improve`** category 5; scope differs). **Skip** on **prose/docs-only**. Checklist: [review-dimensions.md — Architecture](references/review-dimensions.md#architecture).

### Conditional (when signals apply)

- **Standards** — repository guidance and CI-gated linters.
- **Security** — external I/O, auth/session, data access, security-sensitive deps. [Security](references/review-dimensions.md#security).
- **Performance** — N+1, unbounded work, pagination, hot-path cost.
- **Dependencies** — manifest/lockfile/migration changes. [Dependencies](references/review-dimensions.md#dependencies).
- **Observability** — logging, metrics, tracing, alerting changes. [Observability](references/review-dimensions.md#observability).
- **Accessibility** — UI/components/forms/markup changes. [Accessibility](references/review-dimensions.md#accessibility).
- **Operations** — CI/CD, deploy, runbooks, rollout config. [Operations](references/review-dimensions.md#operations).

Skip conditionals with no matching signal (`*: skip` in **Coverage — Examined**). **Prose/docs-only** → skip **Architecture**; still walk **docs — reference integrity**. **Never skip Architecture** on **code** diffs.

## Process

1. State **Context — Scope** per [finding-format.md](references/finding-format.md) — include **Diff kind** (`code` / `prose/docs-only`).
2. Read the **complete** scoped diff before judging correctness — or triage per **Large diffs** and disclose **Limits**.
3. Read the spec and plan when available; map Acceptance when a plan exists.
4. Review test changes first: coverage, edge cases, regression value.
5. Walk core dimensions; on **code** diffs walk **architecture** (skip on prose/docs-only); walk applicable conditionals. Record architecture hits under **🟡/🟢** per [finding-format.md](references/finding-format.md). **`architecture: pass`** or **`architecture: skip`** in **Coverage — Examined**.
6. **Present** — **Context → Findings → Coverage → Follow-up** per [finding-format.md](references/finding-format.md).

Use **Evidence** bullets and lens tags (`[spec]`, `[standards]`, `[security]`) per [finding-format.md](references/finding-format.md). On auth, secrets, migrations, or public API, label **inferred** claims as such; do not state inference as fact.

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
- Finishing a **code** diff review without walking **Architecture**.
- Walking **Architecture** on a **prose/docs-only** diff.
- Treating DRY/KISS only as optional style nits — duplication introduced or left half-migrated belongs in **🟡 should-fix** or **🟢 suggestion**.
- Findings as one-line `file:line` lists without **Evidence** / emoji grading when [finding-format.md](references/finding-format.md) applies.

## Verification

Confirm deliverable matches [finding-format.md](references/finding-format.md): **Context → Findings → Coverage → Follow-up**.

- **🔴 must-fix** — blocks delivery of **this increment** (delivery gate — not the same meaning as opportunity-scan 🔴).
- **🟡 should-fix** — fix unless the user accepts the risk.
- **🟢 suggestion** — non-blocking.

## Output

**Delivery review report** — skeleton per [finding-format.md](references/finding-format.md). Default **no** durable file.

Do not update the plan; accepted risks are recorded later by the user or **`sdd-build`**.

## Stop Conditions

With blocking findings, recommend `sdd-build` and stop. Without blocking findings, recommend `sdd-ship` and stop.
