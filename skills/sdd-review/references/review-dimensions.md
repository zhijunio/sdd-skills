# Review Dimensions

**Delivery review** checklist — **increment diff** only. Whole repo / branch → **`sdd-improve`** [`When/Skip`](../../sdd-improve/SKILL.md). Attribution: **`SOURCES.md`** / **`THIRD_PARTY_NOTICES.md`**.

## Diff kind

Classify **before** walking dimensions. Record in **Scope** — [finding-format.md](finding-format.md).

1. List every changed path.
2. **Code diff** if **any** path is executable logic or test code.
3. **Prose/docs-only** only when **every** path is prose, docs, or non-behavior config.
4. **Mixed** → **code diff** — architecture on code paths; prose still gets spec/docs review.

**Do not** skip **Architecture** on code diffs by size or “trivial rename”. Empty walk → `architecture: pass`.

| → **Code diff** | → **Prose/docs-only** |
| --- | --- |
| Source: `.py`, `.js`, `.ts`, `.go`, `.rs`, `.java`, … | Markdown, `README`, `CHANGELOG`, `skills/**`, `references/**` |
| Tests: `tests/**`, `*_test.*`, `*.spec.*` | Comment/whitespace-only |
| CI/build when steps change; migrations; lockfiles when deps/codegen change | `docs/**`, `LICENSE`, notices; metadata-only config |
| Runtime-behavior config | Typo-only prose |

**Skills-only repos:** `skills/**` / `docs/**` usually **prose/docs-only**; repo verify scripts help classify. **Ambiguous** → default **code diff**; note in **Coverage — Limits**.

| Diff kind | Architecture |
| --- | --- |
| **Code diff** | **Mandatory** — structure + DRY/KISS **in changed code** |
| **Prose/docs-only** | **Skip** — `architecture: skip`; prioritize spec/plan + **reference integrity** |

Pre-existing outside diff → **Coverage — Limits**, not **Findings**.

## Core (always)

### Spec / plan compliance

- Map plan **Acceptance** → `met` / `partial` / `missing` / `unclear`
- Diff outside **Non-goals** → at least **should-fix**
- Disclose missing spec/plan; label **inferred** claims

### Correctness and regressions

- Matches task/spec intent for **this increment**
- Error paths; edge cases; async/state/data consistency
- Bug fixes need regression coverage (see Tests)

### Tests

- Review **test changes first**
- Behavior-focused assertions; names express intent
- TDD signal when plan expected tests to lead

### Docs and traceability

- Spec/plan paths when they exist; CHANGELOG when convention requires
- Flag vague commit messages as **suggestion**

**Reference integrity** (primary when **architecture** skipped):

- Stale links after renames/deletes (`SKILL.md`, `references/**`, `README`, `SOURCES`, `docs/**`)
- Install pins, skill lists, routing tables match tree
- Terminology consistent across skills touched in increment

## Mandatory on code diffs

### Architecture

**Diff-introduced or worsened only.** MECE lenses **A1–A6**, **C1** — [lens-map.md](lens-map.md). Full anti-pattern table → [`sdd-improve` playbook § Anti-patterns](../sdd-improve/references/playbook.md#anti-patterns) (apply to changed paths only).

- New modules, patterns, circular deps, shallow modules, pass-through layers
- **Deletion test** on new modules in diff
- Layer noise; oversized increment (~**>300 lines**) without justification → **suggestion** or **should-fix**

| Signal | Look for |
| --- | --- |
| **Parallel APIs** | Two entry points for same job |
| **Repeated blocks** | Same 5+ line pattern — shared util candidate |
| **Copy-paste UI** | Identical components/hooks/forms |
| **Half migration** | Old + new path; dead code after switch |
| **Dead code introduced** | Unreachable branches, shims, no-ops in diff |
| **Test duplication** | Copied arrange/assert — table-driven candidate |
| **Naming & control flow** | `temp`/`data`; nested ternaries |

**Severity:** half-migration / large duplication → **should-fix**; DRY/KISS alone usually **suggestion**. Whole-repo patterns → **`sdd-improve`** or **Limits**.

## Conditional (when diff touches them)

Walk when signals apply; else `*: skip` in **Coverage — Examined**.

### Standards

Repository guidance (`AGENTS.md`, README, CI linters). Skip style nits CI already gates unless bypassed.

### Security

| Signal | Examples |
| --- | --- |
| External I/O | HTTP, webhooks, shell, SSRF surfaces |
| Auth/session | Login, tokens, guards on mutations |
| Data access | Queries, migrations, serializers across trust boundaries |
| Security deps | Crypto, JWT, HTML/SQL parsers in manifest |

When walking: authZ on mutations; input validation; parameterized SQL; XSS encoding; no secrets in code/logs/docs — cite `file:line` + type only.

### Performance

Queries, loops, lists, hot paths: N+1; unbounded fetches; missing pagination; blocking sync work; hot-path allocations/re-renders.

### Dependencies

Manifest, lockfile, vendor, schema migrations: necessity; size/license/vulns; lockfile consistency; half migrations; breaking upgrades; deploy/rollback story.

### Observability

Logging/metrics/tracing changes: actionable context; critical paths covered; no PII in logs.

### Accessibility

UI/markup changes: keyboard path; accessible names; alt text; focus traps; form errors associated.

### Operations

CI/CD, deploy, infra, flags: rollback story; health probes; migration order; runbook updates.

Triage and sizing: [scope.md](scope.md). Severity semantics: [finding-format.md](finding-format.md).
