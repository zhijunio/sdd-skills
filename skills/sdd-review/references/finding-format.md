# Finding Format

**Maintainers:** Sync **severity semantics**, **Report locale**, and **Verify** with **`sdd-improve`** `finding-format.md`. Layout need not match opportunity scan.

## Report locale

Skill instructions **English**. Report prose in the **user's language** (latest user turn when unclear) — hard rule at **Present** in `SKILL.md`.

- Layout: tables, prose, or lists — no mandatory shared skeleton.
- Keep literal: category lens ids; skill ids; `file:line`; git literals; **🔴/🟡/🟢** (group titles may translate).

## Required content

**Delivery verdict** on an **increment diff** only. Checklists: [review-dimensions.md](review-dimensions.md).

1. **Scope** — diff range, **Diff kind** (`code` / `prose/docs-only`).
2. **Findings** — **Evidence**; **🔴/🟡/🟢** **delivery gate** (blocks **`sdd-build`** / **`sdd-ship`** for this increment).
3. **Coverage** — dimensions walked; `architecture: pass` or `skip`; limits / pre-existing.
4. **Verdict** — pass, or must-fix / should-fix → route.

## Severity

**Delivery gate** for **this increment** — same labels as **`sdd-improve`**; meaning differs — follow-up priority there only.

| Severity | Use when |
| --- | --- |
| **🔴 must-fix** | Blocks delivery — correctness, security, spec/AC gap, Non-goal violation |
| **🟡 should-fix** | Fix unless user accepts risk — duplication, half-migration, test gaps on changed paths |
| **🟢 suggestion** | Non-blocking — docs, small DRY/KISS, readability in the diff |

Do not use Nit/FYI labels — map to **suggestion**. Reserve **must-fix** for correctness, security, spec/AC gaps, Non-goal violations — not DRY/KISS alone.

## Per-finding fields

**Evidence** required. Optional: Impact (this increment), Confidence (✅ HIGH · ⚠️ MED · ❓ LOW), Effort (S/M/L), Risk (🔴/🟡/🟢). **Lens** in title: `[spec]` · `[standards]` · `[security]` — omit for **architecture** when obvious. Architecture (DRY/KISS in diff): **🟡** or **🟢** only — [review-dimensions.md](review-dimensions.md). Prioritize: severity class first; impact ÷ effort discounted by confidence.

## Example (optional)

Not mandatory.

```markdown
## Context

### Scope
| Baseline | `main` |
| Range | `abc1234..def5678` |
| Diff kind | `code` |
| Spec / Plan | `docs/sdd/...-spec.md` or missing — disclosed |

## Findings

### 🔴 must-fix
**1. spec · [spec]** — AC unmapped; no test proof in diff.
- **Evidence:** `npm test` — no assertion for stated AC
- **Confidence:** ✅ HIGH · **Effort:** S · **Risk:** 🟢 LOW

### 🟡 should-fix
None.

### 🟢 suggestion
None.

## Coverage
**Examined:** spec/plan ✅ · correctness ✅ · tests ✅ · docs ✅ · architecture ✅ · security ⏭️
**Limits:** Large diff — sampled `src/` hotspots only.

## Follow-up
### Verdict
**`sdd-build`** 🔧 — one 🔴 must-fix on spec/AC traceability.
```

## Verify

Re-read every cited location before **Present**; rejections and pre-existing outside diff → **Coverage — Limits**, not **Findings**.
