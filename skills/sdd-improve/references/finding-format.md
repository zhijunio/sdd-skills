# Finding Format

## Conversation findings report

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

## Disambiguation vs `sdd-review`

| Dimension | **improve** | **review** |
| --- | --- | --- |
| Question | Opportunities / problems? | Increment meets spec/plan? |
| Scope | Whole repo or branch | Increment diff only |
| Overlap | correctness, security, performance, tests, arch debt (whole-repo or branch) | Same lenses **only on diff**; plus spec/plan AC gate |
| Not in review | DX (7), direction (9), whole-repo pre-existing | — |
| Not in improve | — | Spec/plan compliance, must-fix ship gate |

Whole-repo or branch health check → **improve**. Defined diff delivery gate → **review**.
