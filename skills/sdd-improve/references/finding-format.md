# Finding Format

## Conversation findings report

**机会扫描** outcome — not a **交付审** delivery verdict.

```markdown
# SDD Improve

## Scope

Effort (quick / standard / deep), categories in scope, whole repo or branch range.

## Profile

Optional — omit when user already set scope.

## Findings

| # | Category | Location | Finding | Leverage | Tag |
| --- | --- | --- | --- | --- | --- |
| 1 | tech-debt & architecture | path:line | … | high | introduced |

Order by leverage (impact ÷ effort × confidence). Category 9 **direction** goes in a separate section below (2–4 items). When a finding **contradicts an ADR**, note the ADR path and recommend ADR or spec follow-up.

## Considered and rejected

Brief list of candidates dropped during **Verify**.

## Suggested next stage

One skill via **using-sdd** — default **sdd-spec** when selected finding needs AC; **sdd-grill** when trade-offs remain open.
```

## Verify rules

- Re-read every cited location before presenting.
- Downgrade, correct, or reject false positives.
- No credible findings → explicit **none found** with what was examined.

## Disambiguation vs **交付审** `sdd-review`

Normative pair: **机会扫描** vs **交付审** — full table in [using-sdd — Disambiguation](../../using-sdd/SKILL.md#disambiguation).

| | **机会扫描** `sdd-improve` | **交付审** `sdd-review` |
| --- | --- | --- |
| Question | Opportunities / problems? | Increment meets spec/plan and ship? |
| Scope | Whole repo or branch vs merge-base | Increment diff only |
| Outcome | **Findings report** | **Delivery verdict** |
| Overlap | correctness, security, performance, tests, arch debt | Same lenses **on diff only**; plus AC gate |
| Not in 交付审 | DX (7), direction (9), branch pre-existing tags | — |
| Not in 机会扫描 | — | Spec/plan AC mapping, Simplify pass, ship gate |
