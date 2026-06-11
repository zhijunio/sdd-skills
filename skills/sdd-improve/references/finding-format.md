# Finding Format

## Conversation findings report

**机会扫描** outcome — not a **交付审** delivery verdict. Aligns with [shadcn/improve](https://github.com/shadcn/improve) recon + vetted findings shape; uses **list blocks** (not a findings table) and SDD routing — **no `plans/`** by default.

```markdown
# SDD Improve

## Recon

Always — map the territory before findings (improve Phase 1). Read-only facts only.

| 项 | 结论 |
| --- | --- |
| **类型** | e.g. skills-only repo, Python app, monorepo |
| **验证** | exact command + last result, e.g. `python3 tests/check.py` ✅ |
| **CI** | workflow file + job name, or "none" |
| **HEAD** | `git rev-parse --short HEAD` + branch name |
| **工作区** | clean / N modified / ahead M of origin |
| **活跃区** | paths or areas with recent churn or this increment's focus |
| **未审** | categories or areas skipped + project-specific reason |

## Scope

Profile (optional) merges here — **no separate Profile heading**.

- **Effort:** standard
- **Range:** whole repo
- **Categories:** correctness, security, performance, tests, architecture, dependencies, experience, docs
- **Skipped:** performance — no runtime hot paths

## Findings

Ordered by leverage (high first). **List blocks only — no findings table.** One `###` per finding.

**Grading legend (use in every finding):**

| Axis | Values |
| --- | --- |
| **Leverage** (title) | 🔴 high · 🟡 medium · 🟢 low |
| **Confidence** | ✅ HIGH · ⚠️ MED · ❓ LOW |
| **Effort** (fix) | S · M · L |
| **Risk** (fix) | 🔴 HIGH · 🟡 MED · 🟢 LOW |
| **Strength** (architecture) | 🟢 Strong · 🟡 Worth exploring · ⚪ Speculative |

### 1. 🔴 architecture · introduced

Pass-through layer adds indirection without reuse.

- **Evidence:** `skills/foo.md:12` — thin wrapper re-exports parent with no added invariant
- **Impact:** Callers pay indirection cost; no shared reuse at the seam
- **Effort:** M
- **Confidence:** ✅ HIGH
- **Risk:** 🟢 LOW
- **Strength:** 🟡 Worth exploring

### 2. 🟡 docs

Install pin documents a tag that predates `sdd-improve`.

- **Evidence:** `README.md:90-94` — `@v0.2.1` example; tag predates satellite
- **Impact:** New consumers miss `sdd-improve` when installing from tag only
- **Effort:** S
- **Confidence:** ✅ HIGH
- **Risk:** 🟢 LOW

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

One skill via **using-sdd** — see [handoff.md](handoff.md) (SDD loop vs **shadcn/improve** `plans/` / `execute` / `reconcile`). Default **sdd-spec** when AC needed; **sdd-grill** when trade-offs open. No in-repo `plans/` unless the user explicitly asks.
```

### Finding block fields

**Title:** `{n}. {leverage-emoji} {category} · {tag}` — leverage emoji required; omit `· {tag}` when not branch scope (`introduced` / `pre-existing`).

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
- No credible findings → explicit **none found** with what was examined (Recon **未审** still lists skips).

## Disambiguation vs **交付审** `sdd-review`

Normative pair: **机会扫描** vs **交付审** — full table in [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation).

| | **机会扫描** `sdd-improve` | **交付审** `sdd-review` |
| --- | --- | --- |
| Question | Opportunities / problems? | Increment meets spec/plan and ship? |
| Range | Whole repo or branch vs merge-base | Increment diff only |
| Outcome | **Findings report** | **Delivery verdict** |
| Overlap | correctness, security, performance, tests, architecture | Same lenses **on diff only**; plus AC gate |
| Not in 交付审 | experience (7), direction (9), branch pre-existing tags | — |
| Not in 机会扫描 | — | Spec/plan AC mapping, Simplify pass, ship gate |
