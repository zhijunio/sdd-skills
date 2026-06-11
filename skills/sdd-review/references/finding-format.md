# Finding Format

## Delivery review report

**Delivery review** outcome — **delivery verdict** on an **increment diff** only. **List blocks** (not a findings table). Pairing: [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation). Dimension checklists: [review-dimensions.md](review-dimensions.md).

```markdown
# SDD Review

## Scope

| Item | Content |
| --- | --- |
| **Baseline** | integration branch or commit |
| **Range** | `merge-base...HEAD`, PR, commits, or user-specified span |
| **Included** | commits, files, staged/unstaged task changes |
| **Excluded** | unrelated changes, out-of-scope areas |
| **Spec / Plan** | paths used, or disclosure when missing |

## Findings

**List blocks only — no findings table.** Group under **`### 🔴 must-fix`**, **`### 🟡 should-fix`**, **`### 🟢 suggestion`**. Number findings **within each group** (1, 2, …). Order groups: must-fix → should-fix → suggestion.

**Delivery gate:** these severities decide **`sdd-build`** vs **`sdd-ship`** — unlike **`sdd-improve`** follow-up priority.

| Severity | Use when |
| --- | --- |
| **🔴 must-fix** | Blocks delivery of **this increment** — correctness, security, spec/AC gap, agreed Non-goal violation |
| **🟡 should-fix** | Fix unless user explicitly accepts risk — large **[simplify]** hits, half-migration, test gaps on changed paths |
| **🟢 suggestion** | Non-blocking — docs, small DRY/KISS, readability |

**Per-finding axes** (bullets under each item):

| Axis | Values |
| --- | --- |
| **Confidence** | ✅ HIGH · ⚠️ MED · ❓ LOW |
| **Effort** (fix) | S · M · L |
| **Risk** (fix) | 🔴 HIGH · 🟡 MED · 🟢 LOW |

**Lens** (in title after dimension): `[spec]` · `[standards]` · `[simplify]` · `[security]` — optional; use **`[simplify]`** for all Simplify-pass hits.

### 🔴 must-fix

**1. spec · [spec]** — AC-10 unmapped; no test proof in diff.

- **Evidence:** `tests/check.py` — no assertion for new skill contract
- **Impact:** Increment ships without verification gate for stated AC
- **Effort:** S
- **Confidence:** ✅ HIGH
- **Risk:** 🟢 LOW

### 🟡 should-fix

**1. architecture · [simplify]** — Half migration: new file untracked while old file deleted.

- **Evidence:** `skills/foo/references/handoff.md` — deleted; `closing-the-loop.md` untracked
- **Impact:** Partial rename breaks install on commit
- **Effort:** S
- **Confidence:** ✅ HIGH
- **Risk:** 🟡 MED — easy to ship broken tree

### 🟢 suggestion

None.

## Dimension Coverage

Brief ✅ pass / ❌ fail / ⏭️ skip per dimension: spec/plan (AC mapping when plan exists), correctness, tests, docs, **simplify (mandatory on code diffs)**, and any conditional dimensions reviewed. Write **`simplify: pass`** when the Simplify pass found nothing.

## Assumptions & Gaps

What was assumed, not run, or observed outside scope. Label **Limits** (sampled unread areas on large diffs) explicitly.

## Verdict

**`sdd-build`** 🔧 or **`sdd-ship`** ✅ — one or two sentences of reason. Optional: one concrete positive in the same paragraph — **no separate Strengths section** (aligned with **`sdd-improve`**).
```

### Finding block fields

**Placement:** under the matching severity heading (`🔴 must-fix` / `🟡 should-fix` / `🟢 suggestion`).

**Title:** `**{n}. {dimension} · [{lens}]** — {one-line summary}` — omit `· [{lens}]` when obvious from dimension alone.

**Body:** required bullets (same shape as **`sdd-improve`** [finding-format.md](../../sdd-improve/references/finding-format.md)):

- **Evidence** — `` `file:line` — what is there `` (**required**)
- **Impact** — concrete consequence for **this increment**
- **Effort** — S / M / L
- **Confidence** — ✅ HIGH / ⚠️ MED / ❓ LOW
- **Risk** — 🔴 HIGH / 🟡 MED / 🟢 LOW + one line why

**Simplify pass:** record under **🟡 should-fix** or **🟢 suggestion** only; always include **`[simplify]`** in the title. No separate simplify heading.

**Prioritization:** severity class first; within a class, order by impact ÷ effort discounted by confidence.

## Disambiguation vs **opportunity scan** `sdd-improve`

Normative pair — full table in [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation). Report shape shared with **`sdd-improve`**; meaning of **must-fix** / **should-fix** / **suggestion** differs (delivery gate vs follow-up priority). See **`sdd-improve`** [finding-format.md](../../sdd-improve/references/finding-format.md).
