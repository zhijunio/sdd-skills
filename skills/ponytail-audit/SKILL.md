---
name: ponytail-audit
description: >
  Whole-repo (or named-scope) audit for over-engineering only: ranked cuts to delete,
  simplify, or replace with stdlib/native. Use for "audit for over-engineering",
  "what can I delete", "find bloat", "ponytail-audit". One-shot report; does not apply fixes.
  Not a full Standards health scan or increment quality report.
---

# ponytail-audit

Independent **over-engineering** audit — ranked cuts, no fixes. Keep the report lean.

## Process

### 1. Scope

- If the user named a module, path, or package — scan that first.
- Else prefer recent churn (`git log --oneline` hotspots), then widen if needed.
- Default when still unclear: whole repo (excluding vendored/generated noise when obvious).

### 2. Hunt (tags)

- `delete:` dead code, unused flexibility, speculative feature. Replacement: nothing.
- `stdlib:` hand-rolled thing the standard library ships. Name the function.
- `native:` dependency or code doing what the platform already does. Name the feature.
- `yagni:` abstraction with one implementation, config nobody sets, layer with one caller.
- `shrink:` same logic, fewer lines. Show the shorter form.

Focus: deps the stdlib/platform already ships, single-implementation interfaces, one-product factories, pass-through wrappers, single-export files, dead flags/config, hand-rolled stdlib.

### 3. Present

**Locale (hard rule):** Present in the **user's language** — not English by default. Keep untranslated: cut-tags (`delete:` / …), paths, `net:` numbers.

One line per finding, **biggest cut first**:

`<tag> <what to cut>. <replacement>. [path]`

Then:

- `net: -<N> lines, -<M> deps possible.`
- **Top cut:** one sentence — which finding to tackle first and why.

Nothing to cut: `Lean already.`

**Stop.** Optionally ask which cut to explore; do not apply fixes or auto-chain other skills.

## Disambiguation

| Request | Route |
| --- | --- |
| Over-engineering / bloat / what to delete | **This skill** |
| Broad Standards health / architecture+tests+docs candidates | [`sdd-improve`](../sdd-improve/SKILL.md) |
| Increment diff / PR / since X quality report | [`sdd-review`](../sdd-review/SKILL.md) |

## Boundaries

- **In scope:** over-engineering and complexity only.
- **Out of scope:** correctness bugs, security, performance, Spec/AC compliance — point the user at `sdd-review` or `sdd-improve` as appropriate; do not expand this report.
- Read-only: list findings, apply nothing.
