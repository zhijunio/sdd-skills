# Finding Format

**Maintainers:** Sync **severity semantics**, **Report locale**, and **Verify** rules with **`sdd-improve`** `finding-format.md` when those change. **Layout need not match** opportunity scan.

## Report locale

Skill instructions **English**. Report prose in the **user's language** (latest user turn when unclear).

- **Format:** any clear structure — tables, prose, or lists; **no** mandatory shared markdown skeleton across skills.
- **Keep literal:** category lens ids (e.g. `architecture`); skill ids; `file:line`; git literals; **🔴/🟡/🟢** (group titles may translate).

## Delivery review report

**Outcome:** **delivery verdict** on an **increment diff** only. Checklists: [review-dimensions.md](review-dimensions.md).

**Required content** (substance, not heading names):

1. **Scope** — diff range, **Diff kind** (`code` / `prose/docs-only`).
2. **Findings** — **Evidence**; **🔴/🟡/🟢** **delivery gate** (blocks **`sdd-build`** / **`sdd-ship`** for this increment).
3. **Coverage** — dimensions walked; `architecture: pass` or `skip`; limits / pre-existing.
4. **Verdict** — pass, or must-fix / should-fix → route.

**Example layout (optional):**

```markdown
# SDD Review

## Context

### Scope

| Item | Content |
| --- | --- |
| **Baseline** | integration branch or commit |
| **Range** | `merge-base...HEAD`, PR, commits, or user-specified span |
| **Diff kind** | `code` or `prose/docs-only` — per [review-dimensions — Diff kind](review-dimensions.md#diff-kind); drives architecture walk |
| **Included** | commits, files, staged/unstaged task changes |
| **Excluded** | unrelated changes, out-of-scope areas |
| **Spec / Plan** | paths used, or disclosure when missing |

## Findings

One option: group under **🔴 / 🟡 / 🟢** severity (titles may translate). Each finding needs **Evidence**. Empty severity group → state none.

**Delivery gate** — decides **`sdd-build`** 🔧 vs **`sdd-ship`** ✅. (Opportunity scan uses the same labels for follow-up priority — [`sdd-improve` — When/Skip](../../sdd-improve/SKILL.md).)

| Severity | Use when |
| --- | --- |
| **🔴 must-fix** | Blocks delivery of **this increment** — correctness, security, spec/AC gap, Non-goal violation |
| **🟡 should-fix** | Fix unless user accepts risk — large duplication, half-migration, test gaps on changed paths |
| **🟢 suggestion** | Non-blocking — docs, small DRY/KISS, readability in the diff |

**Per-finding axes:**

| Axis | Values |
| --- | --- |
| **Confidence** | ✅ HIGH · ⚠️ MED · ❓ LOW |
| **Effort** (fix) | S · M · L |
| **Risk** (fix) | 🔴 HIGH · 🟡 MED · 🟢 LOW |

**Lens** (in title): `[spec]` · `[standards]` · `[security]` — omit for **architecture** when dimension is obvious.

### 🔴 must-fix

**1. spec · [spec]** — AC unmapped; no test proof in diff.

- **Evidence:** `tests/check.py` — no assertion for stated AC
- **Impact:** Increment ships without verification for agreed AC
- **Effort:** S
- **Confidence:** ✅ HIGH
- **Risk:** 🟢 LOW

### 🟡 should-fix

**1. architecture** — Half migration in the same increment.

- **Evidence:** `skills/foo/handoff.md` — deleted; replacement untracked in diff
- **Impact:** Partial rename breaks consumers on commit
- **Effort:** S
- **Confidence:** ✅ HIGH
- **Risk:** 🟡 MED

### 🟢 suggestion

None.

## Coverage

Process meta — **not** findings. Same two subsections as **`sdd-improve`**; **Examined** uses ✅/❌/⏭️ per dimension here (opportunity scan may use narrative category list).

### Examined

Brief ✅ pass / ❌ fail / ⏭️ skip per dimension: spec/plan, correctness, tests, docs (**reference integrity**), **architecture** (**code** diffs mandatory; prose → `architecture: skip`), and conditionals when signals apply — **security**, **performance**, **dependencies**, **observability**, **accessibility**, **operations** (else `*: skip`). **`architecture: pass`** when the walk found nothing.

### Limits

Assumed, not run, or out-of-scope observations. Large-diff **Limits** (sampled/unread areas). Pre-existing duplication untouched by diff — here, not in **Findings**.

## Follow-up

### Next stage

**`sdd-build`** 🔧 or **`sdd-ship`** ✅ — one or two sentences. Optional one positive in the same paragraph — no separate Strengths section.
```

### Finding fields (when numbered)

Per item: dimension/lens, summary, **Evidence** (required); optional Impact (this increment), Effort, Confidence, Risk.

**Architecture (DRY/KISS in diff):** under **🟡** or **🟢** only — checklist in [review-dimensions.md](review-dimensions.md).

**Prioritization:** severity class first; within class, impact ÷ effort discounted by confidence.

## Disambiguation vs **opportunity scan**

Normative pairing — [`sdd-improve` — When/Skip](../../sdd-improve/SKILL.md). Shared **🔴/🟡/🟢** labels only; **meaning differs** — delivery severities **gate** **`sdd-build`** / **`sdd-ship`** for **this increment**.
