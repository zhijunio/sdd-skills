# Finding Format

## Conversation findings report

**Opportunity scan** outcome — not a **delivery review** verdict. **List blocks** (not a findings table); follow-ups via the **SDD loop** — see [closing-the-loop.md](closing-the-loop.md).

```markdown
# SDD Improve

## Recon

Always — map the territory before findings. Read-only facts only.

| Item | Summary |
| --- | --- |
| **Type** | e.g. skills-only repo, Python app, monorepo |
| **Verification** | exact command + last result, e.g. `python3 tests/check.py` ✅ |
| **CI** | workflow file + job name, or "none" |
| **HEAD** | `git rev-parse --short HEAD` + branch name |
| **Working tree** | clean / N modified / ahead M of origin |
| **Hotspots** | paths or areas with recent churn or this increment's focus |
| **Not audited** | categories or areas skipped + project-specific reason |

## Scope

Profile (optional) merges here — **no separate Profile heading**. **In-scope only** — skips and audit limits belong in **Recon — Not audited**, not here.

- **Effort:** standard
- **Range:** whole repo
- **Categories:** correctness, security, tests, architecture, dependencies, experience, docs

## Findings

**List blocks only — no findings table.** Group under **`### 🔴 must-fix`**, **`### 🟡 should-fix`**, **`### 🟢 suggestion`** (same labels as **`sdd-review`**, different meaning — see below). Number findings **within each group** (1, 2, …). Order groups: must-fix → should-fix → suggestion; within a group, order by leverage (high first).

**Not a delivery verdict:** these severities rank **follow-up priority** for the user to **select** — they do **not** gate **`sdd-ship`** on their own.

| Severity | Use when |
| --- | --- |
| **🔴 must-fix** | HIGH-confidence correctness, security, or data-loss risk; missing verification baseline that blocks safe change; unblocker other findings depend on |
| **🟡 should-fix** | Clear maintainability or test gap on important paths; MED+ confidence; worth addressing in the next increment the user is likely to take |
| **🟢 suggestion** | Docs/DX polish, LOW-confidence investigate, speculative architecture, pre-existing debt surfaced for awareness |

**Per-finding axes** (bullets under each item):

| Axis | Values |
| --- | --- |
| **Confidence** | ✅ HIGH · ⚠️ MED · ❓ LOW |
| **Effort** (fix) | S · M · L |
| **Risk** (fix) | 🔴 HIGH · 🟡 MED · 🟢 LOW |
| **Strength** (architecture, cat. 5) | 🟢 Strong · 🟡 Worth exploring · ⚪ Speculative |

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

## Direction

Only when category 9 ran — **after Findings**, not ranked against bugs. Bullet list, 2–4 items. Each item: short title + **Evidence** + grading bullets; **Impact** = product/user value; **Confidence** = how grounded the evidence is.

## Dependency order

When **two or more** findings are plausible follow-ups (or user may multi-select), list recommended fix order — unblockers first, then leverage. One line per step; cite finding numbers.

```text
#1 → #5 → #6
```

Omit this section when zero or one actionable finding.

## Considered and rejected

Brief list of candidates dropped during **Verify** (by-design, mis-attributed evidence, duplicate).

## Suggested next stage

One skill via **using-sdd** — see [closing-the-loop.md](closing-the-loop.md). Default **sdd-spec** when AC needed; **sdd-grill** when trade-offs open.
```

### Finding block fields

**Placement:** under the matching severity heading (`🔴 must-fix` / `🟡 should-fix` / `🟢 suggestion`). Shared block shape with **`sdd-review`** — see [finding-format.md](../../sdd-review/references/finding-format.md).

**Title:** `**{n}. {category} · {tag}** — {one-line summary}` — omit `· {tag}` when not branch scope (`introduced` / `pre-existing`).

**Body:** one-line **summary** (imperative or plain), then **required bullets**:

- **Evidence** — `` `file:line` — what is there `` (repeat for 2–5 strongest sites; note "~N similar" if widespread). **Required** — do not fold evidence only into the summary line.
- **Impact** — concrete consequence
- **Effort** — S / M / L for the fix including tests
- **Confidence** — ✅ HIGH / ⚠️ MED / ❓ LOW
- **Risk** — 🔴 HIGH / 🟡 MED / 🟢 LOW + one line why

**Architecture (category 5):** add **Strength** — 🟢 Strong / 🟡 Worth exploring / ⚪ Speculative.

ADR conflicts: extra bullet or note on **Evidence**.

**Prioritization:** leverage = impact ÷ effort, discounted by confidence and fix-risk. Tiebreakers: unblockers first; HIGH-confidence security above equal leverage; prefer fixes with a clean verification story.

## Verify rules

- Re-read every cited location before presenting.
- Downgrade, correct, or reject false positives.
- No credible findings → explicit **none found** with what was examined (Recon **Not audited** still lists skips).

## Disambiguation vs **delivery review** `sdd-review`

Normative pair: **opportunity scan** vs **delivery review** — full table in [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation).

| | **Opportunity scan** `sdd-improve` | **Delivery review** `sdd-review` |
| --- | --- | --- |
| Question | Opportunities / problems? | Increment meets spec/plan and ship? |
| Range | Whole repo or branch vs merge-base | Increment diff only |
| Outcome | **Findings report** | **Delivery verdict** |
| Overlap | correctness, security, performance, tests, architecture | Same lenses **on diff only**; plus AC gate |
| Not in delivery review | experience (7), direction (9), branch pre-existing tags | — |
| Not in opportunity scan | — | Spec/plan AC mapping, Simplify pass, ship gate |
| Report format | [finding-format.md](finding-format.md) (this file) | [sdd-review finding-format.md](../../sdd-review/references/finding-format.md) |
