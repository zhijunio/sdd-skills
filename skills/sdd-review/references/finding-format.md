# Finding Format

## Delivery review report

**Outcome:** **delivery verdict** on an **increment diff** only. Checklists: [review-dimensions.md](review-dimensions.md).

**Report skeleton:** **Context → Findings → Coverage → Follow-up** (same section order as **`sdd-improve`**; content differs below).

```markdown
# SDD Review

## Context

### Scope

| Item | Content |
| --- | --- |
| **Baseline** | integration branch or commit |
| **Range** | `merge-base...HEAD`, PR, commits, or user-specified span |
| **Included** | commits, files, staged/unstaged task changes |
| **Excluded** | unrelated changes, out-of-scope areas |
| **Spec / Plan** | paths used, or disclosure when missing |

## Findings

**List blocks only — no findings table.** Group under **`### 🔴 must-fix`**, **`### 🟡 should-fix`**, **`### 🟢 suggestion`**. Number within each group (1, 2, …). Order groups must-fix → should-fix → suggestion; within a group, by leverage. Empty group → `None.`

**Delivery gate** — decides **`sdd-build`** 🔧 vs **`sdd-ship`** ✅. (Opportunity scan uses the same labels for follow-up priority — [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation).)

| Severity | Use when |
| --- | --- |
| **🔴 must-fix** | Blocks delivery of **this increment** — correctness, security, spec/AC gap, Non-goal violation |
| **🟡 should-fix** | Fix unless user accepts risk — large **[simplify]**, half-migration, test gaps on changed paths |
| **🟢 suggestion** | Non-blocking — docs, small DRY/KISS, readability |

**Per-finding axes:**

| Axis | Values |
| --- | --- |
| **Confidence** | ✅ HIGH · ⚠️ MED · ❓ LOW |
| **Effort** (fix) | S · M · L |
| **Risk** (fix) | 🔴 HIGH · 🟡 MED · 🟢 LOW |

**Lens** (in title): `[spec]` · `[standards]` · `[simplify]` · `[security]` — **required `[simplify]`** for Simplify-pass hits.

### 🔴 must-fix

**1. spec · [spec]** — AC unmapped; no test proof in diff.

- **Evidence:** `tests/check.py` — no assertion for stated AC
- **Impact:** Increment ships without verification for agreed AC
- **Effort:** S
- **Confidence:** ✅ HIGH
- **Risk:** 🟢 LOW

### 🟡 should-fix

**1. architecture · [simplify]** — Half migration in the same increment.

- **Evidence:** `skills/foo/handoff.md` — deleted; replacement untracked in diff
- **Impact:** Partial rename breaks consumers on commit
- **Effort:** S
- **Confidence:** ✅ HIGH
- **Risk:** 🟡 MED

### 🟢 suggestion

None.

## Coverage

Process meta — **not** findings. Same two subsections as **`sdd-improve`**; content differs.

### Examined

Brief ✅ pass / ❌ fail / ⏭️ skip per dimension: spec/plan (AC mapping when plan exists), correctness, tests, docs, **simplify** (mandatory on code diffs), and conditionals reviewed. **`simplify: pass`** when Simplify pass found nothing.

### Limits

Assumed, not run, or out-of-scope observations. Large-diff **Limits** (sampled/unread areas). Pre-existing duplication untouched by diff — here, not in **Findings**.

## Follow-up

### Next stage

**`sdd-build`** 🔧 or **`sdd-ship`** ✅ — one or two sentences. Optional one positive in the same paragraph — no separate Strengths section.
```

### Finding block fields

**Title:** `**{n}. {dimension} · [{lens}]** — {summary}` — omit `· [{lens}]` when obvious.

**Body:** **Evidence** (required), **Impact** (for **this increment**), **Effort**, **Confidence**, **Risk**.

**Simplify pass:** under **🟡** or **🟢** only; **`[simplify]`** in title — checklist in **`sdd-review` SKILL.md**.

**Prioritization:** severity class first; within class, impact ÷ effort discounted by confidence.

## Disambiguation vs **opportunity scan**

Normative pairing — [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation). Same report skeleton and **🔴/🟡/🟢** labels; **`sdd-improve`** severities rank follow-up priority only.
