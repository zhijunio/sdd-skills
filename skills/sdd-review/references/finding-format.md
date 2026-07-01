# Finding Format

**Maintainers:** Delivery **verdict** semantics stay here; MECE **lens** ids and optional impact emoji align with [`sdd-audit`](../../sdd-audit/references/report.md) — **different job**: **delivery gate** vs codebase follow-up priority.

**Delivery: chat only** — post the full review in the conversation. No durable file unless the user asks.

## Report locale

Skill instructions **English**. Report prose and **section headings** in the **user's language** (English headings below when the user writes in English). Keep literal: lens ids; skill ids; `file:line`; git literals; delivery groups **🔴/🟡/🟢 must-fix / should-fix / suggestion**.

Checklists: [review-dimensions.md](review-dimensions.md). Lenses: [lens-map.md](lens-map.md).

## Delivery gate (group headers)

**Blocks `sdd-build` / `sdd-ship` for this increment** — not the same as `sdd-audit` severity emoji or P0/P1/P2.

| Group | Use when |
| --- | --- |
| **🔴 must-fix** | Blocks delivery — correctness, security, spec/AC gap, Non-goal violation |
| **🟡 should-fix** | Fix unless user accepts risk — duplication, half-migration, test gaps on changed paths |
| **🟢 suggestion** | Non-blocking — docs, small DRY/KISS, readability in the diff |

Do not use Nit/FYI labels — map to **suggestion**. Reserve **must-fix** for correctness, security, spec/AC gaps, Non-goal violations — not DRY/KISS alone.

**Strengths do not override Verdict** — 🔴 must-fix still blocks even when Strengths are present.

## Per-finding fields

**Evidence** required. **Lens** column or title suffix: **A1–A6**, **C0–C3**, **S1**, **V1–V2**, **D1**, **O1**, or `—` for pure spec compliance — [lens-map.md](lens-map.md).

Optional **impact** (not delivery gate): severity emoji per `sdd-audit` rubric — `🚨 Critical` · `🔴 High` · `🟡 Medium` · `🟢 Low` — when it helps rank within a group.

Optional: Confidence (✅ HIGH · ⚠️ MED · ❓ LOW), Effort (S/M/L), Risk, **structural_fix** (systemic move in the diff). Prioritize: delivery group first; then impact ÷ effort.

## Report template

**Section order** (aligned with [`sdd-audit` report.md](../../sdd-audit/references/report.md); review-specific sections marked):

`Scope` → `Executive summary` → `Diff shape` (optional) → `Coverage` → `Findings` → `Strengths` (optional) → `Verdict` → `Rejected / deferred` (optional) → **`Suggested next steps` last**

```markdown
# Delivery Review — {Project}

> Date · Diff range · Diff kind

## Scope

| Field | Value |
| --- | --- |
| Baseline | `main` / user-specified |
| Range | `abc1234..def5678` or staged/unstaged — disclosed |
| Diff kind | `code` / `prose/docs-only` |
| Spec / Plan | path or missing — disclosed |

## Executive summary

2–4 sentences: pass or blocked; optional **🔴/🟡/🟢** counts; one-line next move. Not a substitute for **Verdict**.

## Diff shape (optional)

Code diffs with ≥3 changed units — Mermaid or ASCII of **changed** modules only (example):

    [changed module] → role in this increment

Skip on small prose/docs-only diffs.

## Coverage

**Examined:** spec/plan · correctness · tests · docs · architecture (`pass` / `skip`) · conditionals walked or `*: skip`

**Limits:** pre-existing outside diff; triage omissions — not **Findings**

Localized heading: **Coverage** · **审查覆盖**

## Findings

Grouped by **delivery gate** (not audit severity). Number within each group.

### 🔴 must-fix

**1. {title}** — `[dimension]` · lens **{id}**
- **Evidence:** …
- **Impact:** optional 🚨/🔴/🟡/🟢 · **Confidence:** optional

### 🟡 should-fix

…

### 🟢 suggestion

… or `None.`

## Strengths

Evidence-backed positives **in the diff** — not a delivery pass. Omit when nothing applies (do not invent praise).

2–5 bullets; cite `path:line` or pattern in changed files.

Localized heading examples: **Strengths** · **健康面** / **做得好的地方**

## Verdict

**pass** — no unresolved 🔴 must-fix (🟡 may remain if user accepts risk).

**blocked** — list 🔴 ids/titles; increment must not proceed to **`sdd-ship`** until fixed.

Review-specific — **not** `sdd-audit` Roadmap P0/P1/P2.

## Rejected / deferred (optional)

| title | reason |

Pre-existing / out-of-scope items vetted out of **Findings**.

## Suggested next steps

**Always last section.** Name **one** route — user **`@`** that skill; no auto-chain.

| Verdict | Typical route |
| --- | --- |
| **blocked** (🔴 must-fix) | **`sdd-build`** |
| **pass** | **`sdd-ship`** |
| Whole-repo follow-up (optional note) | **`sdd-audit`** — not a substitute for Verdict |

Also: open trade-offs → **`sdd-grill`**; spec/AC gap needs contract change → **`sdd-spec`**.
```

## Verify

Re-read every cited location before **Present**; rejections and pre-existing outside diff → **Coverage — Limits** or **Rejected / deferred**, not **Findings**. Vet rules → `sdd-audit/references/playbook.md` § Vet.
