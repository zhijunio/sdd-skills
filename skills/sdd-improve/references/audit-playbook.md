# Audit Playbook

Condensed read-only checklist per category (standard = categories **1–8**).

**Sources (summarized, not copied):** [shadcn/improve](https://github.com/shadcn/improve) (MIT); [addyosmani/agent-skills `code-review-and-quality`](https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality) (five-axis review checklist).

**No step named Simplify** — readability, duplication, and over-engineering are **category 5** findings. **交付审** spec/AC compliance, Simplify pass, and **delivery verdict** belong in **`sdd-review`**, not here. Pairing: [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation).

## 1 correctness

Does the code behave as implemented — not “does it match an approved spec” (that is delivery review).

- Happy path only — error paths missing or swallowed exceptions
- Wrong defaults; silent failures; unchecked return values
- Edge cases: empty, null, boundary, off-by-one
- Async hazards: missing `await`, race windows, stale closures, state inconsistencies
- Data consistency across reads/writes; partial updates without rollback story

## 2 security

Evidence-based only — cite `file:line` and credential **type**; never reproduce secret values.

- Auth gaps; missing authorization on mutations
- User input in queries, shell, paths, or file operations without validation
- SQL string concatenation — prefer parameterized queries
- Output encoding for XSS where user content is rendered
- Secrets in repo, logs, or client bundles
- External data (APIs, config, user content, webhooks) treated as **untrusted** until validated at boundaries
- Known-vulnerable dependencies (cross-check category 6; cite once)

## 3 performance

- N+1 queries; unbounded loops or fetches
- List endpoints or UI lists without pagination where data can grow
- Hot-path synchronous or blocking work that should be async
- Unnecessary re-renders or recomputation in UI hot paths
- Large object allocation in hot paths; missing indexes or caches on frequent queries

## 4 test coverage

Review tests for **behavior**, not as a substitute for reading production code.

- Missing tests on critical paths, auth, money, or data-loss surfaces
- Tests assert implementation detail instead of observable behavior
- Weak assertions that would not catch regressions
- Bug-fix areas without regression tests
- Test names do not express intent; duplicated arrange/assert blocks (category 5 candidate)

## 5 tech-debt & architecture

Absorbs legacy `sdd-architect` signals plus agent-skills **readability** and **architecture** axes (no separate readability category).

**Structure & patterns**

- New pattern without justification vs existing conventions
- Circular dependencies; dependencies flowing the wrong direction
- Shallow modules, leaky seams, pass-through layers
- **Deletion test** — deleting the module scatters complexity → may earn its keep; complexity vanishes → pass-through noise
- **Depth / seam** vocabulary where useful
- Strength: `Strong`, `Worth exploring`, `Speculative`

**Readability & duplication** (not named Simplify)

- Unclear names (`temp`, `data`) vs project conventions; nested or clever control flow
- Abstractions not yet justified (generalize on third use case, not first)
- **Over-engineering** — layers without reuse; **duplication** — parallel APIs, 5+ line repeated blocks, copy-paste UI
- Dead code: unreachable paths, legacy shims, no-op variables left after refactors
- Oversized modules/files without domain justification (signal only — change-sizing gates live in **`sdd-review`**)

## 6 dependencies & migrations

**Before treating a new dependency as acceptable:**

- Could the existing stack or stdlib solve this?
- Bundle/install size impact (apps and frontends)
- Maintenance signal: recent releases, open critical issues
- License compatible with the project
- `npm audit` / ecosystem equivalent failures; unpinned risky versions

**Migrations**

- Lockfile drift; half-finished migrations; deprecated API still in primary paths

## 7 experience & tooling

- Local setup unclear or multi-step without documented one-liner
- Missing scripts for test, lint, or common maintainer tasks
- Slow CI without proportionate value; flaky jobs
- Cannot run the standard verification story locally (test/lint/typecheck as documented in repo guidance)

## 8 docs

- README drift; stale examples; missing docs for public APIs
- Domain terms in code undefined in README, CONTEXT, or ADR
- Change traceability weak: commit messages or CHANGELOG entries that do not stand alone (e.g. “Fix bug”, “Patch”) without what/why
- Anti-pattern: moving code with no rationale in history when grep cannot explain intent

## 9 direction

Only when user asks roadmap / next steps. Evidence-grounded; 2–4 items max; open trade-offs → `sdd-grill`.

## Branch scope

When scope is branch vs merge-base, tag each finding `introduced` or `pre-existing` in touched files.

## Limits

On large repos, record what was **not** fully read (hotspot-weighted scan per Profile). Do not invent findings to fill gaps.
