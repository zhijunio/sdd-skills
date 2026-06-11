# Finding Format

## Conversation findings report

**机会扫描** outcome — not a **交付审** delivery verdict.

```markdown
# SDD Improve

## Scope

Single section for scan metadata — **no separate Profile heading**. The optional Profile step writes here.

- **Project type:** skills repo
- **Effort:** standard
- **Range:** whole repo
- **Categories:** correctness, security, performance, tests, architecture, dependencies, experience, docs
- **Skipped:** performance — no runtime hot paths

## Findings

Ordered by leverage (high first). **List format only — no table.** One `###` block per finding.

### 1. architecture · high · introduced

`skills/foo.md:12` — Pass-through layer adds indirection without reuse.

**Strength:** Worth exploring

### 2. docs · medium

`README.md:90` — Install pin documents a tag that predates `sdd-improve`.

## Direction

Only when category 9 ran. Bullet list, 2–4 items — not mixed into Findings.

## Considered and rejected

Brief list of candidates dropped during **Verify**.

## Suggested next stage

One skill via **using-sdd** — default **sdd-spec** when selected finding needs AC; **sdd-grill** when trade-offs remain open.
```

### Finding block fields

Each `###` title: `{n}. {category} · {leverage} · {tag}` — omit `· {tag}` when not branch scope.

Body: `` `file:line` — **summary** `` then optional detail. Category 5 may add **Strength:** `Strong` / `Worth exploring` / `Speculative`. ADR conflicts: note ADR path in the body.

## Verify rules

- Re-read every cited location before presenting.
- Downgrade, correct, or reject false positives.
- No credible findings → explicit **none found** with what was examined.

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
