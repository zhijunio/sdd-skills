# Finding Format

**Maintainers:** List-block skeleton is shared with **`sdd-review`** `finding-format.md`. When changing shared rules (severity groups, axes, Coverage subsections), update **both** files in the same PR.

## Opportunity scan report

**Outcome:** conversation **findings report** — not a **delivery verdict**. Follow-ups: [closing-the-loop.md](closing-the-loop.md).

**Report skeleton:** **Context → Findings → Coverage → Follow-up** (same section order as **`sdd-review`**; content differs below).

```markdown
# SDD Improve

## Context

### Recon

Read-only territory facts. Skips belong here — not in Scope.

| Item | Summary |
| --- | --- |
| **Type** | e.g. skills-only repo, Python app, monorepo |
| **Verification** | exact command + last result, e.g. `python3 tests/check.py` ✅ |
| **CI** | workflow file + job name, or "none" |
| **HEAD** | `git rev-parse --short HEAD` + branch name |
| **Working tree** | clean / N modified / ahead M of origin |
| **Hotspots** | paths or areas with recent churn or focus |
| **Not audited** | categories or areas skipped + project-specific reason |

### Scope

Profile (optional) merges here — **no `## Profile` heading**. **In-scope only.**

- **Effort:** standard
- **Range:** whole repo
- **Categories:** correctness, security, tests, architecture, dependencies, experience, docs

## Findings

**List blocks only — no findings table.** Group under **`### 🔴 must-fix`**, **`### 🟡 should-fix`**, **`### 🟢 suggestion`**. Number within each group (1, 2, …). Order groups must-fix → should-fix → suggestion; within a group, by leverage. Empty group → `None.`

**Follow-up priority only** — does **not** gate **`sdd-ship`**. (Delivery review uses the same labels with a different meaning — [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation).)

| Severity | Use when |
| --- | --- |
| **🔴 must-fix** | HIGH-confidence correctness, security, or data-loss risk; missing verification baseline; unblocker |
| **🟡 should-fix** | Maintainability or test gap on important paths; MED+ confidence |
| **🟢 suggestion** | Docs/DX polish, LOW investigate, speculative architecture, awareness |

**Per-finding axes:**

| Axis | Values |
| --- | --- |
| **Confidence** | ✅ HIGH · ⚠️ MED · ❓ LOW |
| **Effort** (fix) | S · M · L |
| **Risk** (fix) | 🔴 HIGH · 🟡 MED · 🟢 LOW |
| **Strength** (category 5) | 🟢 Strong · 🟡 Worth exploring · ⚪ Speculative |

### 🔴 must-fix

**1. architecture · introduced** — Pass-through layer adds indirection without reuse.

- **Evidence:** `skills/foo.md:12` — thin wrapper re-exports parent with no added invariant
- **Impact:** Callers pay indirection cost; no shared reuse at the seam
- **Effort:** M
- **Confidence:** ✅ HIGH
- **Risk:** 🟢 LOW
- **Strength:** 🟡 Worth exploring

### 🟡 should-fix

**1. docs** — Install pin documents a tag that predates `sdd-improve`.

- **Evidence:** `README.md:90-94` — `@v0.2.1` example; tag predates satellite
- **Impact:** New consumers miss `sdd-improve` when installing from tag only
- **Effort:** S
- **Confidence:** ✅ HIGH
- **Risk:** 🟢 LOW

### 🟢 suggestion

None.

## Coverage

Process meta — **not** findings. Same two subsections as **`sdd-review`**; content differs.

### Examined

What was walked: categories per **Context — Scope** (narrative or brief ✅/⏭️ list — format may differ from delivery review). Skips stay in **Context — Recon — Not audited** only — do not repeat here.

### Limits

**Verify** output: considered and rejected (by-design, mis-attributed evidence, duplicate). No credible findings → state what was examined. Large-repo sampling limits here if applicable.

## Follow-up

**Required:** **`### Next stage`** on every report — even when Findings are empty (none found → **`sdd-grill`** if trade-offs open, else stop with explicit none-actionable). Do not end **Present** with Confirm only.

### Next stage

One **route** — [closing-the-loop.md](closing-the-loop.md). Name it and one-line why:

- **`sdd-spec`** / **`sdd-plan`** / **`sdd-build`** — via **`using-sdd`** when a skill adds value (default **`sdd-spec`** when AC missing)
- **`sdd-grill`** — trade-offs still open
- **`direct edit`** — user fixes ad-hoc **outside** SDD skills; improve **Stop**s; user verifies (e.g. `./mvnw test`); optional later **`sdd-review`**

**Not in-session implementation:** improve never edits product code. **SDD skills optional** for follow-up — not every finding needs spec, plan, or **`sdd-build`**.

### Direction

Optional — category 9 only; before **Next stage** when present; 2–4 bullets with **Evidence**.

### Dependency order

Optional — when ≥2 follow-ups; one line: `#1 → #5`. Omit when ≤1 actionable finding.
```

### Finding block fields

**Title:** `**{n}. {category} · {tag}** — {summary}` — omit `· {tag}` unless branch scope (`introduced` / `pre-existing`).

**Body:** **Evidence** (required), **Impact**, **Effort**, **Confidence**, **Risk**; category 5 adds **Strength**. ADR conflicts: note on **Evidence**.

**Prioritization:** impact ÷ effort, discounted by confidence and fix-risk.

### Verify rules

Re-read every cited location before **Present**; rejections → **Coverage — Limits**.

## Disambiguation vs **delivery review**

Normative pairing — [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation). Same report skeleton and **🔴/🟡/🟢** labels; **meaning differs** — opportunity-scan severities rank follow-up priority only and **do not** gate **`sdd-ship`**.
