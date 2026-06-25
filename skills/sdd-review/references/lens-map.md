# Lens map — delivery review

**Scope:** **increment diff only**. Whole repo / branch codebase audit → [`sdd-audit`](../sdd-audit/SKILL.md) (`map.md` there).

Map each finding to **one lens** id. Full MECE rules and anti-patterns → [`sdd-audit/references/map.md`](../sdd-audit/references/map.md) and `playbook.md` § Anti-patterns (diff-introduced signals only here).

## Review dimension → lens

| Review dimension | Lens ids |
| --- | --- |
| Spec / plan compliance | `—` (use `[spec]` tag; no pillar lens) |
| Correctness / regressions | **C0** |
| Tests | **V1** |
| Docs / reference integrity | **D1** (README/links) or `—` if spec-only |
| Architecture (diff) | **A1–A6**, **C1** |
| Security | **S1** |
| Performance | **C3** |
| Dependencies | **D1** |
| Observability | **C2** |
| Accessibility | **A1** |
| Operations (CI/deploy in diff) | **V2**, **O1** |

## Diff architecture (mandatory on code diffs)

Walk **diff-introduced or worsened** signals only. Pre-existing → **Coverage — Limits**.

| Signal in diff | Lens |
| --- | --- |
| New pass-through / shallow module | **A6** |
| Parallel APIs / duplication in changed files | **C1** |
| Half migration / dead code in diff | **A5**, **C1** |
| Layer breach / new cycle | **A1** |
| Oversized increment (~>300 lines) without justification | **C1** or **A5** |

Anti-pattern names and vet bar → `sdd-audit/references/playbook.md` § Anti-patterns, § Vet — apply only to **changed** paths.

## Overlap (one row)

| Topic | Lens |
| --- | --- |
| CVE in lockfile (diff) | **D1** |
| Unsafe API call in diff | **S1** |
| Missing test for changed behavior | **V1** |
| N+1 in new code | **C3** |
| PII in new logs | **S1** |
