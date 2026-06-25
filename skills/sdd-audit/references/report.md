# Report

**Delivery: chat only** — post the full report in the conversation.

**No disk by default** — do **not** create or update audit files in the target repo (including findings JSON, dot-folders, or report Markdown) unless the user **explicitly** asks to persist a baseline or export.

**Report body:** user's language. **Section headings** follow the user's language too (use English headings below when the user writes in English). Literals: paths, lens ids, git refs, **severity emojis** (below).

## Severity emoji

Use emoji **with** the level text in the findings table — not instead of rubric. **Roadmap phases use text only** (`P0` / `P1` / `P2` — no emoji).

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

## Finding table

```markdown
| severity | lens | title | files | evidence | evidence_type | confidence | impact | effort | fix_risk | attribution | structural_fix |
```

**snapshot / 快照:** ≤5 rows. **standard / deep / 标准 / 深度:** max **20** rows. Zero → `NO_FINDINGS` + patterns searched.

### Columns

| Col | Rule |
|-----|------|
| severity | 🚨 Critical · 🔴 High · 🟡 Medium · 🟢 Low (+ localized label) |
| lens | **A1–A6**, **C0–C3**, **S1**, **V1–V2**, **D1**, **O1** — `map.md` |
| files | `path:line` comma-separated |
| evidence | ≤3 lines or call-path |
| evidence_type | `observed` \| `inferred` |
| attribution | `—` \| `introduced` / `pre-existing` (English branch audit) \| 本分支引入 / 既有问题 (Chinese branch audit) |
| structural_fix | Systemic move — not typo fix |

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

Finding table above. Branch audits: use **attribution** column or split sections.

## Strengths

Evidence-backed **systemic** positives — not the inverse of findings, not a delivery pass. Omit the section when nothing durable applies (do not invent praise).

2–5 bullets: pattern or shape that is healthy; cite `path`, layer, or contract. **snapshot / 快照:** ≤3 bullets.

Localized heading examples: **Strengths** (English) · **健康面** / **做得好的地方** (Chinese).

## Roadmap

| Phase | Systemic move | Depends on |
| P0 | … | … |
| P1 | … | … |
| P2 | … | … |

Simplicity audits: roadmap rows should favor **delete / merge / collapse** over extract-and-wrap.

## Direction notes (optional)

2–4 options with trade-offs — not ranked vs findings.

## Rejected findings (optional)

| title | reason |

Vetted out of **Findings** — not **Coverage — Limits** alone.

## Suggested next steps

**Always last section.** Pick **one** route — handoff table in [`SKILL.md`](../SKILL.md) **Stop**. Also: follow-up deep pillar when a single lens needs another pass.
```
