# Report

**Delivery: chat only** — post the full report in the conversation.

**No disk by default** — do **not** create or update audit files in the target repo (including findings JSON, dot-folders, or report Markdown) unless the user **explicitly** asks to persist a baseline or export.

**Report body:** user's language. **Section headings** follow the user's language too (use English headings below when the user writes in English). Literals: paths, lens ids, git refs, **severity emojis** (below).

## Severity emoji

Use emoji **with** the level text in each finding — not instead of rubric. **Roadmap phases use text only** (`P0` / `P1` / `P2` — no emoji).

| Emoji | Level | When |
|-------|-------|------|
| 🚨 | **Critical** | Systematic contract break; secrets on hot path; auth bypass class; diverging sources of truth |
| 🔴 | **High** | Boundary violation; missing authZ on mutations; critical CVE on path |
| 🟡 | **Medium** | Duplication tax; missing boundary tests; observability gaps |
| 🟢 | **Low** | Non-critical drift; minor smell without pattern |

Cell format: `🚨 Critical` / `🚨 严重` — emoji + localized label.

**Executive summary:** optional severity counts — e.g. `🚨×1 🔴×3 🟡×2`.

## Roadmap phases (text only)

| Phase | When |
|-------|------|
| **P0** | Unblockers first — verify baseline, secrets, contract breaks before structural work |
| **P1** | High-leverage systemic fixes after P0 |
| **P2** | Polish, DX, low-urgency drift |

Cell format: `P0` · `P1` · `P2` only — **no emoji**. Severity and scheduling are independent (e.g. `🟡 Medium` finding may appear under **P0**).

## Finding format

**Do not** use a wide markdown table (too many columns hurt readability). Use **severity groups + numbered cards** below.

**snapshot / 快照:** ≤5 findings. **standard / 标准 / deep / 深度:** max **20** cards. Zero → `NO_FINDINGS` + patterns searched; simplicity audits with no cuts end `Lean already — ship.`

### Group order

`🚨 Critical` → `🔴 High` → `🟡 Medium` → `🟢 Low`. Omit empty groups.

### Per-finding card

```markdown
**{n}. {title}** — lens **{id}**
- **Evidence:** ≤3 lines or call-path · `{observed|inferred}`
- **Location:** `path:line`, …
- **Fix:** {structural_fix — systemic move, not typo}
- **Meta (optional, one line):** confidence · effort S/M/L · fix risk · branch: introduced / pre-existing
```

| Field | Rule |
|-------|------|
| title | Short pattern name |
| lens | **A1–A6**, **C0–C3**, **S1**, **V1–V2**, **D1**, **O1** — `map.md` |
| Evidence | Required; tag `observed` or `inferred` inline |
| Location | `path:line` comma-separated |
| Fix | **structural_fix** — systemic move |
| Meta | Optional tail: confidence (HIGH/MED/LOW), effort (S/M/L), fix risk, **attribution** on branch audits (`introduced` / `pre-existing` · 本分支引入 / 既有问题) |

**snapshot / 快照** may add a slim index (≤5 rows) **after** the cards for quick scan:

```markdown
| severity | lens | title | location |
```

Four columns only — no evidence or meta in the index.

## Report template

**snapshot / 快照** → Scope + summary + ≤5 findings. **standard / deep / 标准 / 深度** → full below.

**Section order:** `Scope` → `Executive summary` → `Boundary map` (if in scope) → `Coverage` → `Findings` → `Strengths` (optional) → `Roadmap` → `Direction notes` (optional) → `Rejected findings` (optional) → **`Suggested next steps` last**.

**Parallel to [`sdd-review` Coverage](../../sdd-review/references/finding-format.md):** examination boundary **before** findings; rejected items **after** roadmap, not before the handoff.

```markdown
# Codebase Audit — {Project}

> Date · Target · Effort · Range

## Scope

| Field | Value |
|-------|-------|
| HEAD | `{sha}` |
| Shape / Stack | … |
| Effort | snapshot / standard / deep |
| Range | whole-repo · branch:`<name>` vs merge-base |

## Executive summary

2–4 sentences: healthy / drifting / at risk; top risks (optional `🚨`/`🔴`/`🟡` counts); next move.

## Boundary map (architecture)

When in scope — Mermaid or ASCII (example):

    [layer] → modules → notes

Skip when user narrowed to a single pillar without shape walk.

## Coverage

**Examined:** pillars / lenses walked (e.g. A1–A6 architecture-only · full A/C/S/V/D/O)

**Skipped:** pillars or lenses out of scope — state explicitly

**Verification:** commands — ok / partial / none

**Limits:** branch scope, triage omissions, cheap checks not run — not **Findings**

Localized heading: **Coverage** · **审查覆盖**

## Findings

Severity groups + numbered cards (see **Finding format** above). Branch audits: put attribution in **Meta** or split `### 本分支引入` / `### 既有问题` subsections.

Example:

```markdown
### 🔴 High

**1. Domain imports infrastructure adapter** — lens **A1**
- **Evidence:** `OrderService` constructs `PrismaOrderRepo` directly · `observed`
- **Location:** `src/orders/order-service.ts:42`
- **Fix:** Introduce port in domain; inject adapter at composition root
- **Meta:** confidence HIGH · effort M · branch: introduced
```

## Strengths

Evidence-backed **systemic** positives — not the inverse of findings, not a delivery pass. Omit the section when nothing durable applies (do not invent praise).

2–5 bullets: pattern or shape that is healthy; cite `path`, layer, or contract. **snapshot / 快照:** ≤3 bullets.

Localized heading examples: **Strengths** (English) · **健康面** / **做得好的地方** (Chinese).

## Roadmap

| Phase | Systemic move | Depends on |
| P0 | … | … |
| P1 | … | … |
| P2 | … | … |

Simplicity audits: roadmap rows should favor **delete / merge / collapse** over extract-and-wrap. End with net-removal estimate: `net: -<N> lines, -<M> deps possible.` — `0` when a finding simplifies without removing lines.

## Direction notes (optional)

2–4 options with trade-offs — not ranked vs findings.

## Rejected findings (optional)

| title | reason |

Vetted out of **Findings** — not **Coverage — Limits** alone.

## Suggested next steps

**Always last section.** Pick **one** route — handoff table in [`SKILL.md`](../SKILL.md) **Stop**. Also: follow-up deep pillar when a single lens needs another pass.
```
