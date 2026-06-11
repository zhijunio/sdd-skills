# Review Dimensions (diff-scoped)

Detailed checklists for **delivery review** **`sdd-review`** — **increment diff** only. **Opportunity scan** (whole-repo or branch) → **`sdd-improve`**. Pairing table: [`sdd-improve` — When/Skip](../../sdd-improve/SKILL.md).

**Sources (summarized):** [addyosmani/agent-skills `code-review-and-quality`](https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality). Lenses overlap opportunity-scan **architecture** (category 5) where scope allows — **diff only** here.

## Diff kind

Classify **before** walking dimensions. Record **Diff kind** in **Context — Scope** (see [finding-format.md](finding-format.md)).

### How to classify

1. List every changed path in the scoped diff.
2. **Code diff** if **any** path is primarily **executable logic or test code** (see signals below).
3. **Prose/docs-only** only when **every** changed path is prose, docs, or non-behavior config.
4. **Mixed** (code + prose) → **code diff** — walk **Architecture** on the code paths; prose paths still get spec/docs review.

**Do not** use diff size or “trivial rename” to skip **Architecture** on a **code diff**. Small code diffs still get the walk; empty result → `architecture: pass`.

### Signals

| → **Code diff** | → **Prose/docs-only** |
| --- | --- |
| Source: `.py`, `.js`, `.ts`, `.go`, `.rs`, `.java`, … | Markdown: `.md`, `.txt`, `README`, `CHANGELOG`, `skills/**/SKILL.md`, `references/**` |
| Tests with assertions: `tests/**`, `*_test.*`, `*.spec.*` | Comment-only or whitespace-only edits in any file |
| CI/build scripts: `.github/workflows/**`, `Makefile`, `Dockerfile` when steps change | Pure docs trees: `docs/**`, `LICENSE`, notices |
| Migrations, generated code, lockfiles **when deps or codegen behavior change** | Frontmatter / metadata-only JSON/YAML/TOML (no runtime behavior) |
| Config that changes runtime behavior (feature flags, env templates consumed by app code) | Typo fixes in prose with no structural doc refactor |

**Skills-only repos (e.g. this collection):** `skills/**` and `docs/**` edits are usually **prose/docs-only**; repo-declared verify scripts (if any) help classify **code diff** vs prose-only.

**Ambiguous** (e.g. workflow tweak, lockfile-only, rename across code + docs): default **code diff** when unsure; note assumption in **Coverage — Limits**.

### Architecture walk

| Diff kind | Architecture |
| --- | --- |
| **Code diff** | **Mandatory** — structure, readability, duplication, DRY/KISS **in changed code** |
| **Prose/docs-only** | **Skip** — `architecture: skip` in **Coverage — Examined**; prioritize spec/plan, **docs/traceability — Reference integrity** |

Pre-existing duplication outside the diff → **Coverage — Limits**, not **Findings**.

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

**Reference integrity** — especially on **prose/docs-only** diffs (primary substitute when **Architecture** is skipped):

- **Renames / deletes** — grep for stale inbound links (`SKILL.md`, `references/**`, `README`, `SOURCES`, `docs/**`, disambiguation tables)
- **Cross-doc pointers** — relative links and skill names still resolve; no orphan anchors after heading moves
- **Consumer-facing examples** — install pins, skill lists, and routing tables match the tree after adds/removes/renames
- **Terminology** — dimension/category names and Disambiguation rows consistent across skills touched in the same increment

## Mandatory on code diffs

### Architecture

**Only** what this diff **introduces or worsens.** Same lenses as opportunity-scan **architecture** (category 5) — **structure insight and duplication/DRY signals**; scope here is **increment diff** only. Never skip on **code** diffs; pre-existing duplication untouched → **Coverage — Limits**, not **must-fix**.

**Structure & patterns**

- New modules, cross-layer calls, shared APIs
- New pattern vs existing conventions — justified?
- Circular dependencies or wrong dependency direction introduced
- Shallow modules, leaky seams, pass-through layers introduced in the diff
- **Deletion test** — new module in diff: deleting it scatters complexity (may earn its keep) or complexity vanishes (pass-through noise)
- **Depth / seam** vocabulary where useful for new boundaries
- Layer noise: extra indirection, pass-through methods, abstractions without reuse in the same increment
- Oversized increment (~**>300 lines** or one file grows substantially) without justification — **suggestion** or **should-fix** per risk

**Readability & duplication** (diff-only)

| Signal | Look for |
| --- | --- |
| **Parallel APIs** | Two entry points for the same job where one path or thin wrapper would suffice |
| **Repeated blocks** | Same 5+ line pattern in multiple files — shared util or base method candidate |
| **Copy-paste UI** | Identical or near-identical components, hooks, form fields repeated across screens |
| **Field or param bloat** | New fields duplicating an existing one without documented compatibility reason |
| **Half migration** | Old path still called beside new path; staged but uncommitted pieces; dead code after switch |
| **Dead code introduced** | Unreachable branches, legacy shims, no-op variables in the diff |
| **Test duplication** | Same arrange/assert copied — table-driven or shared fixture candidate |
| **Naming & control flow** | Context-free `temp` / `data` vs conventions; nested ternaries or clever one-liners |

**Severity:** **should-fix** when half-migration or large duplication blocks maintainability or risks drift; otherwise **suggestion**. Reserve **must-fix** for Non-goal violations (e.g. “no dual API”), not DRY/KISS alone.

Whole-codebase patterns outside the diff → out-of-scope observation or opportunity scan via **`sdd-improve`**.

## Conditional (when the diff touches them)

### Standards

- Repository guidance (`AGENTS.md`, README, linters in CI)
- Skip style nits CI already gates unless the diff bypasses or disables checks

### Security

**Walk when any signal below** — even if changed paths are not obviously “security” files (helpers and wrappers count):

| Signal | Examples |
| --- | --- |
| **New/changed external I/O** | HTTP/RPC clients, webhooks, file or network reads, subprocess/shell, user-controlled URLs (SSRF) |
| **New/changed auth/session** | Login, tokens, cookies, session stores, guards, permission checks on mutations |
| **New/changed data access** | Queries, ORM/repository layers, migrations/schema, serializers across trust boundaries |
| **Security-sensitive deps** | Crypto, auth, JWT/OAuth, HTML/SQL parsers added or upgraded in manifest/lockfile |

If none apply (typical **prose/docs-only** without secret examples) → `security: skip` in **Coverage — Examined**.

**When walking:**

- Auth **and** authorization on new mutations
- Input validated/sanitized at boundaries
- Parameterized queries — no SQL string concatenation
- XSS: encode output where user content renders
- No secrets in code, logs, client bundles, or docs examples — cite `file:line` and type only
- External APIs, config, webhooks treated as untrusted until validated

### Performance

When the diff touches queries, loops, lists, or hot paths:

- N+1 queries; unbounded fetches or loops
- Missing pagination on growing lists
- Blocking/sync work where async is expected
- Unnecessary re-renders or large allocations on hot paths

### Dependencies

**Walk when** manifest, lockfile, vendor tree, or **schema/data migration** files change.

- Necessity — could stdlib or existing stack suffice?
- Size, maintenance, license, known vulnerabilities (`npm audit` or equivalent)
- **Lockfile consistency** — manifest and lockfile updated together; no unexplained drift between them
- **Half-finished migrations** — deprecated API still on primary paths; old and new package versions both required without plan note
- **Breaking upgrades** — major semver or API removal: migration steps, rollback story, or plan **Non-goals** respected
- **Schema/data migrations** — backward compatibility, deploy order, nullable/default strategy for existing rows

### Observability

**Walk when** logging, metrics, tracing, alerting, or error-reporting changes:

- New/changed failure paths logged with actionable context (correlation IDs, safe user messages)
- Critical, money, or auth paths missing metrics/traces after change
- PII/secrets in logs; log volume or cardinality risks in hot paths

If none apply → `observability: skip` in **Coverage — Examined**.

### Accessibility

**Walk when** UI components, forms, styles, or user-facing markup change:

- Keyboard focus order and visible focus; interactive elements have accessible names
- Meaningful images/icons have text alternatives; state not conveyed by color alone
- Modals/traps have escape; form errors associated with fields
- Automated a11y CI gates exist → skip style nits already gated; flag bypasses or disabled checks

If none apply → `accessibility: skip` in **Coverage — Examined**.

### Operations

**Walk when** CI/CD, deploy, infra, runbooks, feature flags, or rollout config change:

- Rollback or forward-fix story documented for the increment
- Health/readiness probes for new runtime surfaces
- Deploy/migration order aligns with **Dependencies** and plan
- On-call/runbook updated when incident response path changes

If none apply → `operations: skip` in **Coverage — Examined**.

## Severity (delivery gate)

Same **🔴/🟡/🟢** labels as opportunity scan — [finding-format.md](finding-format.md) (layout need not match). **Meaning differs** — pairing: [`sdd-improve` — When/Skip](../../sdd-improve/SKILL.md).

| Class | Meaning |
| --- | --- |
| **🔴 must-fix** | Blocks delivery of this increment |
| **🟡 should-fix** | Fix unless user explicitly accepts risk |
| **🟢 suggestion** | Non-blocking; includes most readability and small DRY/KISS wins in the diff |

Do not use agent-skills Nit/FYI labels here — map to **suggestion**. Reserve **must-fix** for correctness, security, spec/AC gaps, and agreed Non-goal violations.

## Change sizing (signal)

| Size | Guidance |
| --- | --- |
| ~100 lines | Ideal review size |
| ~300 lines | Acceptable for one logical increment |
| ~1000 lines | Ask to split; triage per **Large diffs** and record **Limits** |

Separate refactoring-only diffs from feature work when the author can still split.
