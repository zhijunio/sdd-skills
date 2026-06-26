# Review Scope

**Delivery review** — **increment diff** only. Determine range before walking dimensions.

## Range (in order)

1. User-specified files, PR, commit range, branch pair, or baseline.
2. Scope from current task or plan.
3. Staged only when user/task limits to staged work.
4. Task-related uncommitted changes in the same increment.
5. Merge-base diff: `merge-base(<integration-base>, HEAD)...HEAD`.

## Integration base

- Prefer `origin/HEAD` or branch in repository guidance.
- Use user-named branch when it differs.
- **Never assume `main`**, `master`, or any branch without evidence.

Default: **full** merge-base diff for current branch + task-related uncommitted work — not whole repo history.

## Ask before reviewing

- Path only, no commit range / PR / baseline.
- Unrelated dirty files in diff.
- Unknown integration branch.
- Multiple independent topics in one diff.
- Range too large for one pass.

## Large diffs

~**30+ files** or **>300 lines**: triage auth, secrets, migrations, public API, data-loss paths first; record **Limits**. Prose-only: spec/plan traceability first.

## Pre-existing

Issues **outside** scoped diff → out-of-scope observations only — not `must-fix`/`should-fix` unless diff reintroduces or worsens them.

Full verification evidence → **`sdd-verify`**, not here.

## Diff kind

Record in report scope. Any code path → **code diff** (mandatory **architecture** walk). Markdown/docs/comments-only → **prose/docs-only** (skip architecture). Details: [review-dimensions.md — Diff kind](review-dimensions.md#diff-kind).
