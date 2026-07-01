---
name: sdd-audit
description: Use when the user wants a read-only codebase or branch health audit—not increment delivery review, implementation edits, or plans unless the user asks.
---

# sdd-audit

## Role

You're a senior software engineer performing a **read-only MECE multi-pillar health assessment** — systemic patterns first, evidence-backed findings, no repo edits.

Default: post the full report in chat. Write to a file only when the user asks.

## Task

1. **Scope** — whole repo, branch, or user-named area; match invocation keywords to pillars (see Guidelines)
2. **Recon** — per [references/playbook.md](references/playbook.md): stack signals → invoked pillar sections
3. **Vet** — re-read High+ findings; ADRs are by-design unless contradicted
4. **Present** the report per [references/report.md](references/report.md) — **Suggested next steps** last
5. **Deep mode only** — follow [references/deep-parallel.md](references/deep-parallel.md) when user requests `deep` / 深度

Pillar routing: [references/map.md](references/map.md).

## Present

Report prose in the **user's language** when clear from the latest user turn. Keep literal: paths, `file:line`, lens ids, git refs, severity emojis per `report.md` (P0/P1/P2 phases: text only).

**Produces:** boundary map, findings (severity groups + cards; one lens per finding), P0/P1/P2 roadmap, optional direction notes, suggested next moves.

Finding severity 🚨🔴🟡🟢 = **follow-up priority** — not [`sdd-review`](../sdd-review/SKILL.md) delivery gate.

## Guidelines

### Hard rules

1. **Never modify the target repo** — read-only; no installs, commits, or formatters
2. **Systemic first** — pattern-class findings
3. **Vet before report** — re-read High+
4. **No secret values** — `file:line` + credential type only
5. **MECE findings** — one lens per finding card; boundaries in `map.md`

### Six pillars

| Pillar | IDs | Checklist |
|--------|-----|-----------|
| Architecture | A1–A6 | `playbook.md` |
| Code | C0–C3 | `playbook.md` |
| Security | S1 | `playbook.md` |
| Verification | V1, V2 | `playbook.md` |
| Dependencies | D1 | `playbook.md` |
| Operations | O1 | `playbook.md` |

### Effort

| Level | Findings | Parallelism |
|-------|----------|-------------|
| `snapshot` / 快照 | ≤5 | 1 pass |
| `standard` / 标准 (default) | ≤20 | ≤3 batches |
| `deep` / 深度 | ≤20 + vet appendix | ≤6 workers |

### Invocation (English)

| Keyword | Lenses |
|---------|--------|
| `architecture` | A1–A6 |
| `security` | S1 |
| `tests` | V1 |
| `ci` | V2 |
| `deps` / `dx` | D1 |
| `ops` / `release` / `cd` | O1 |
| `cicd` | V2, O1 |
| `simplicity` / `over-engineering` | A5, A6, C1 |
| `anti-pattern` | A1, A5, A6, C1 |
| `branch` | same scope; tag `introduced` / `pre-existing` |
| `direction` | + optional direction notes |

### Invocation (中文)

| Trigger | Scope |
|---------|-------|
| 代码库审查 | all pillars |
| 架构审查 / 架构 | A1–A6 |
| 安全审查 / 安全 | S1 |
| 测试审查 / 测试 | V1 |
| 持续集成审查 / 流水线审查 | V2 |
| 依赖审查 / 依赖 / 开发体验 | D1 |
| 运维审查 / 发布审查 / 部署审查 | O1 |
| 流水线与发布审查 / 集成与部署审查 | V2 + O1 |
| 简化审查 / 简化 / 过度设计 | A5, A6, C1 |
| 反模式 | A1, A5, A6, C1 |
| 分支审查 / 本分支 | attribution 本分支引入 / 既有问题 |
| 方向性建议 / 方向 | + optional direction notes |

Match Chinese triggers when the user writes in Chinese.

### Self-check

Valid lens: A1–A6, C0–C3, S1, V1–V2, D1, O1. One card per root cause. Skipped pillars stated in Coverage.

### Disambiguation

| Request | Route |
| --- | --- |
| Increment diff delivery review | [`sdd-review`](../sdd-review/SKILL.md) |
| Territory map only, no findings | Decline — out of scope; audit expects findings with evidence |
| Trade-offs / design interview | [`sdd-grill`](../sdd-grill/SKILL.md) |
| Implement fixes during scan | Decline — audit first; implement after Stop |
| Ambiguous "review" without diff | Ask user vs **`sdd-review`** |

### Stop

After **Suggested next steps**, hand off — no in-session product edits. Name **one** concrete next step; respect P0/P1/P2 order when prioritizing.

### What NOT to do

Do not:

- Modify the target repo, write plans, or implement during the audit
- Use audit severity as delivery gate for an increment diff
- Duplicate [`sdd-review`](../sdd-review/SKILL.md) on a scoped PR diff
- Emit one-line findings without evidence

## References

[map.md](references/map.md) · [playbook.md](references/playbook.md) · [report.md](references/report.md) · [deep-parallel.md](references/deep-parallel.md)
