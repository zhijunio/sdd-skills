# Audit Dimensions

**Opportunity scan** checklist — whole repo or **branch** vs merge-base. Increment diff → **`sdd-review`** [`When/Skip`](../../sdd-review/SKILL.md). Standard = categories **1–8**. No **Simplify** step — readability/duplication → category **5**. Attribution: **`SOURCES.md`** / **`THIRD_PARTY_NOTICES.md`**.

## Read-only rules

**Advisor, not implementer** during the scan:

- **Never** edit product code, consumer spec/plan, or `CONTEXT.md` / `docs/adr/` during the audit.
- **Never** run commands that **mutate the user's working tree** — no package installs, no `git commit`, no formatters, no builds that write artifacts outside standard ignored dirs.
- **Allowed:** read, search, repo-documented verify commands, `tsc --noEmit`, lint in check mode, ecosystem audit in check mode, test suites that are cheap and side-effect free.
- **Durable write (explicit user request only):** `docs/sdd/YYYY-MM-DD-<topic>-improve.md` — not a substitute for spec/plan. Implementation → SDD loop — [closing-the-loop.md](closing-the-loop.md).

## Parallel audit (optional)

When the host supports read-only subagents, fan out by category (or cluster). Subagent caps and coverage: [profile-guide.md — Effort levels](profile-guide.md#effort-levels).

Subagent prompt: path to this file + [finding-format.md](finding-format.md); recon facts; **findings only**. **Vet** leads before **Present**. No subagents → category-priority order. Monorepos → scope to **packages**.

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

**Observability** (when backend/service — tag findings `architecture` or `performance` as fits)

- Errors swallowed or returned without structured logs on critical paths
- Money, auth, or data-loss paths without metrics, tracing, or alert hooks
- New failure modes invisible in production (no dashboard, no SLO signal)
- Logs leak PII/secrets or lack correlation IDs across requests

## 4 test coverage

Review tests for **behavior**, not as a substitute for reading production code.

- Missing tests on critical paths, auth, money, or data-loss surfaces
- Tests assert implementation detail instead of observable behavior
- Weak assertions that would not catch regressions
- Bug-fix areas without regression tests
- Test names do not express intent; duplicated arrange/assert blocks (category 5 candidate)

## 5 architecture

Structure + duplication/DRY (whole repo or branch — not diff-only). Same lenses as **`sdd-review`** Architecture.

- New pattern without justification vs existing conventions
- Circular dependencies; dependencies flowing the wrong direction
- Shallow modules, leaky seams, pass-through layers
- **Deletion test** — deleting the module scatters complexity → may earn its keep; complexity vanishes → pass-through noise
- **Depth / seam** vocabulary where useful
- Strength: `Strong`, `Worth exploring`, `Speculative`

| Signal | Look for |
| --- | --- |
| **Parallel APIs** | Two entry points for the same job where one path would suffice |
| **Repeated blocks** | Same 5+ line pattern — shared util or base method candidate |
| **Copy-paste UI** | Identical components, hooks, or form fields across screens |
| **Over-engineering** | Layers without reuse; abstractions before third use case |
| **Half migration** | Old path still called beside new; staged pieces of same refactor |
| **Dead code** | Unreachable paths, legacy shims, no-op variables after refactors |
| **Naming & control flow** | `temp` / `data` vs conventions; nested ternaries or clever one-liners |

Oversized modules/files without domain justification (signal only).

**Accessibility** (UI — tag `architecture`)

- Interactive controls without keyboard path or accessible name
- Meaningful images/icons without text alternative
- Modals/focus traps without escape; state conveyed by color alone
- Forms without labels/errors associated for assistive tech

## 6 dependencies & migrations

**Before treating a new dependency as acceptable:**

- Could the existing stack or stdlib solve this?
- Bundle/install size impact (apps and frontends)
- Maintenance signal: recent releases, open critical issues
- License compatible with the project
- `npm audit` / ecosystem equivalent failures; unpinned risky versions

**Migrations**

- Lockfile drift; half-finished migrations; deprecated API still in primary paths

## 7 experience

- Local setup unclear or multi-step without documented one-liner
- Missing scripts for test, lint, or common maintainer tasks
- Slow CI without proportionate value; flaky jobs
- Cannot run the standard verification story locally (test/lint/typecheck as documented in repo guidance)

**Operations** (tag findings `experience`)

- Deploy, rollback, or incident runbook missing/stale for changed surfaces
- New services without health/readiness probes or documented on-call path
- Risky launches without feature flags, kill switches, or staged rollout notes
- CI/CD gaps: migration order, blue/green, or backout not documented when needed

## 8 docs

- README drift; stale examples; missing docs for public APIs
- Domain terms in code undefined in README, CONTEXT, or ADR
- Change traceability weak: commit messages or CHANGELOG entries that do not stand alone (e.g. “Fix bug”, “Patch”) without what/why
- Anti-pattern: moving code with no rationale in history when grep cannot explain intent

## 9 direction

User asks roadmap / next steps only. Evidence-grounded; 2–4 items; trade-offs → `sdd-grill`.

## Limits

On large repos, record what was **not** fully read (hotspot-weighted scan per Profile). Do not invent findings to fill gaps.
