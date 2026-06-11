# Review Dimensions (diff-scoped)

Detailed checklists for **delivery review** **`sdd-review`** — **increment diff** only. **Opportunity scan** (whole-repo or branch) → **`sdd-improve`**. Pairing table: [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation).

**Sources (summarized):** [addyosmani/agent-skills `code-review-and-quality`](https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality); aligned with **`sdd-improve`** `audit-playbook.md` where lenses overlap.

## Core (always)

### Spec / plan compliance

- Map each plan **Acceptance** item to `met` / `partial` / `missing` / `unclear` against diff and tests
- Diff outside plan **Non-goals** → at least **should-fix**
- Disclose missing spec or plan; do not claim compliance without artifacts
- Infer **inferred** when judging from code alone; do not state inference as fact

### Correctness and regressions

- Change matches stated task/spec intent for **this increment**
- Error paths handled — not happy-path only
- Edge cases: empty, null, boundary, off-by-one
- Concurrency, async (`await`), state consistency, data consistency across reads/writes
- Bug fixes include regression coverage (see Tests)

### Tests

- Review **test changes first** — they reveal intent
- Behavior-focused assertions; not locked to implementation detail
- Edge cases and failure paths covered where the diff touches them
- Test names express intent; assertions would catch regressions
- TDD signal when the plan expected tests to lead the slice

### Docs and traceability

- Spec/plan paths referenced when they exist
- CHANGELOG updated when repo convention requires user-visible notes
- Commit messages / PR description stand alone (imperative subject + what/why) — flag “Fix bug” / “Patch” with no context as **suggestion**

## Conditional (when the diff touches them)

### Standards

- Repository guidance (`AGENTS.md`, README, linters in CI)
- Skip style nits CI already gates unless the diff bypasses or disables checks

### Architecture

**Only** what this diff **introduces or worsens:**

- New modules, cross-layer calls, shared APIs
- New pattern vs existing conventions — justified?
- Circular dependencies or wrong dependency direction introduced
- Duplication introduced or left half-migrated (also **Simplify**)
- Oversized increment (~**>300 lines** or one file grows substantially) without justification — **suggestion** or **should-fix** per risk

Whole-codebase patterns outside the diff → out-of-scope observation or **`sdd-improve`**.

### Security

When the diff touches auth, input, data access, or dependencies:

- Auth **and** authorization on new mutations
- Input validated/sanitized at boundaries
- Parameterized queries — no SQL string concatenation
- XSS: encode output where user content renders
- No secrets in code, logs, or client bundles — cite `file:line` and type only
- External APIs, config, webhooks treated as untrusted until validated

### Performance

When the diff touches queries, loops, lists, or hot paths:

- N+1 queries; unbounded fetches or loops
- Missing pagination on growing lists
- Blocking/sync work where async is expected
- Unnecessary re-renders or large allocations on hot paths

### Readability

Within the scoped diff:

- Names vs project conventions; avoid context-free `temp` / `data`
- Straightforward control flow — flag nested ternaries or clever one-liners
- Comments only where intent is non-obvious
- Dead code introduced: unreachable branches, legacy shims, no-op vars after refactor → **Simplify** or **suggestion**

### Dependencies

When the diff adds or upgrades packages:

- Necessity — could stdlib or existing stack suffice?
- Size, maintenance, license, known vulnerabilities (`npm audit` or equivalent)
- Lockfile consistency

### Simplify (mandatory on code diffs)

Behavior-preserving reductions **in the diff** — see SKILL **Simplify pass checklist**. Never skip on non-trivial code diffs.

Record hits under **`### 🟡 should-fix`** or **`### 🟢 suggestion`** — **`[simplify]`** lens + **Evidence** bullets per [finding-format.md](finding-format.md); no separate simplify heading.

Pre-existing duplication untouched by the diff → **Assumptions & Gaps**, not **must-fix**.

## Severity (delivery gate)

Aligned with **`sdd-improve`** list-block shape — [finding-format.md](finding-format.md).

| Class | Meaning |
| --- | --- |
| **🔴 must-fix** | Blocks delivery of this increment |
| **🟡 should-fix** | Fix unless user explicitly accepts risk |
| **🟢 suggestion** | Non-blocking; includes most readability and small simplify wins |

Do not use agent-skills Nit/FYI labels here — map to **suggestion**. Reserve **must-fix** for correctness, security, spec/AC gaps, and agreed Non-goal violations.

## Change sizing (signal)

| Size | Guidance |
| --- | --- |
| ~100 lines | Ideal review size |
| ~300 lines | Acceptable for one logical increment |
| ~1000 lines | Ask to split; triage per **Large diffs** and record **Limits** |

Separate refactoring-only diffs from feature work when the author can still split.
