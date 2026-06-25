# Finding Format

**Maintainers:** Delivery **verdict** semantics stay here; MECE **lens** ids and severity emoji rubric align with [`sdd-audit`](../sdd-audit/references/report.md) — **different job**: ship gate vs codebase audit.

## Report locale

Skill instructions **English**. Report prose in the **user's language**. Keep literal: lens ids; skill ids; `file:line`; git literals; delivery groups **🔴/🟡/🟢 must-fix / should-fix / suggestion**.

## Required content

**Delivery verdict** on an **increment diff** only. Checklists: [review-dimensions.md](review-dimensions.md). Lenses: [lens-map.md](lens-map.md).

1. **Scope** — diff range, **Diff kind** (`code` / `prose/docs-only`).
2. **Findings** — **Evidence**; grouped by **delivery gate** (below).
3. **Coverage** — dimensions walked; `architecture: pass` or `skip`; limits / pre-existing.
4. **Verdict** — pass, or must-fix / should-fix → route.

## Delivery gate (group headers)

**Blocks `sdd-build` / `sdd-ship` for this increment** — not the same as `sdd-audit` severity emoji.

| Group | Use when |
| --- | --- |
| **🔴 must-fix** | Blocks delivery — correctness, security, spec/AC gap, Non-goal violation |
| **🟡 should-fix** | Fix unless user accepts risk — duplication, half-migration, test gaps on changed paths |
| **🟢 suggestion** | Non-blocking — docs, small DRY/KISS, readability in the diff |

Do not use Nit/FYI labels — map to **suggestion**. Reserve **must-fix** for correctness, security, spec/AC gaps, Non-goal violations — not DRY/KISS alone.

## Per-finding fields

**Evidence** required. **Lens** column or title suffix: **A1–A6**, **C0–C3**, **S1**, **V1–V2**, **D1**, **O1**, or `—` for pure spec compliance — [lens-map.md](lens-map.md).

Optional **impact** (not delivery gate): severity emoji per improve rubric — `🚨 Critical` · `🔴 High` · `🟡 Medium` · `🟢 Low` — when it helps rank within a group.

Optional: Confidence (✅ HIGH · ⚠️ MED · ❓ LOW), Effort (S/M/L), Risk. Prioritize: delivery group first; then impact ÷ effort.

## Example (optional)

```markdown
## Context

### Scope
| Baseline | `main` |
| Range | `abc1234..def5678` |
| Diff kind | `code` |
| Spec / Plan | `docs/sdd/...-spec.md` or missing — disclosed |

## Findings

### 🔴 must-fix
**1. AC unmapped** — `[spec]` · lens `—`
- **Evidence:** `npm test` — no assertion for stated AC
- **Impact:** 🔴 High · **Confidence:** ✅ HIGH

**2. SQL concat in new handler** — `[security]` · lens **S1**
- **Evidence:** `src/api/user.ts:42`
- **Impact:** 🚨 Critical

### 🟡 should-fix
**3. Duplicate mapper in diff** — lens **C1**
- **Evidence:** `src/foo.ts:10`, `src/bar.ts:88`

### 🟢 suggestion
None.

## Coverage
**Examined:** spec/plan ✅ · correctness ✅ · tests ✅ · docs ✅ · architecture ✅ · security ⏭️
**Limits:** Pre-existing N+1 in `legacy/` — not in diff.

## Follow-up
### Verdict
**`sdd-build`** 🔧 — one 🔴 must-fix on spec/AC traceability.
```

## Verify

Re-read every cited location before **Present**; rejections and pre-existing outside diff → **Coverage — Limits**, not **Findings**. Vet rules → `sdd-audit/references/playbook.md` § Vet.
