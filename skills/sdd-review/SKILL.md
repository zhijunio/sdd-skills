---
name: sdd-review
description: Use when a scoped diff needs an independent, read-only review before delivery, after implementation, or when the user asks for a review. Classifies code diff vs prose/docs-only; mandatory architecture walk on code diffs only.
---

# sdd-review

## Role

You're a senior software engineer performing a **read-only delivery review** on a defined **increment diff**. You produce a **delivery verdict** with evidence — not implementation, plan updates, or full verification.

Review the **work product**, not session history. Default: post the full review in chat. Write to a file only when the user asks.

## Task

1. **Establish scope** — per [scope.md](references/scope.md): user range, merge-base diff, or task-related uncommitted work; never assume `main`/`master` without evidence; record **Diff kind** (`code` / `prose/docs-only`) in the report
2. **Read the scoped diff** — complete increment, or triage large diffs per scope.md and disclose **Limits**
3. **Read spec/plan when available** — map Acceptance Criteria when a plan exists; disclose missing spec/plan and label **inferred** claims
4. **Review test changes first**, then walk review dimensions per [review-dimensions.md](references/review-dimensions.md):
    - **Core (always):** spec/plan compliance; correctness/regressions; tests; docs/traceability + reference integrity on renames
    - **Mandatory on code diffs:** architecture (structure + DRY/KISS in the diff) — **skip** on prose/docs-only
    - **Conditional when signals apply:** standards, security, performance, dependencies, observability, accessibility, operations — record `*: skip` in **Coverage** when not walked
5. **Present** the review per [finding-format.md](references/finding-format.md) — section order in the **Report template**; **Suggested next steps** last
6. **Verdict** — state whether this increment is blocked; name one next skill in **Suggested next steps** (see below)

Use [lens-map.md](references/lens-map.md) for lens ids on findings. Prefer a fresh agent/subagent when available; optional two-pass on large diffs; default one pass.

## Present

Write the review in the **user's language** (latest user turn when unclear) — do not default to English for report prose. Keep literal: lens ids, skill ids, `file:line`, git literals, delivery groups **🔴 must-fix / 🟡 should-fix / 🟢 suggestion**.

| Group | Meaning |
| --- | --- |
| **🔴 must-fix** | Blocks delivery for this increment — delivery gate |
| **🟡 should-fix** | Fix unless the user accepts risk |
| **🟢 suggestion** | Non-blocking |

Optional impact emoji per [`sdd-audit` report.md](../sdd-audit/references/report.md) — ranks within a group; **not** the delivery gate.

## Guidelines

### Scope and dimensions

- **Increment diff only** — not whole-repo health audit (see Disambiguation)
- **Never skip architecture on code diffs** — empty walk → `architecture: pass` in Coverage
- Pre-existing issues **outside** the scoped diff → **Coverage — Limits** or out-of-scope observations — not must-fix unless the diff reintroduces or worsens them
- Each finding needs **Evidence**; avoid one-line findings without grading

### Disambiguation

| Request | Route |
| --- | --- |
| Codebase / branch health audit without delivery increment | [`sdd-audit`](../sdd-audit/SKILL.md) |
| Territory map only, no delivery diff | Decline — out of scope for delivery review |
| Ambiguous "review" with no diff range | Ask user vs **`sdd-audit`** |
| Full AC evidence tables / ship checklist | [`sdd-verify`](../sdd-verify/SKILL.md) — not here |

### Stop

After **Suggested next steps**, hand off — no in-session product edits or plan updates:

- **`sdd-build`** when 🔴 must-fix findings are unresolved
- **`sdd-verify`** otherwise (fresh verification on this increment)

### What NOT to do

Do not:

- Edit product, test, or plan files while reviewing
- Review staged-only when the increment includes unstaged work the user expects in scope
- Use a path alone without a commit range, PR, or baseline
- Treat whole-repo patterns as must-fix without a scoped diff (note in Limits or route to **`sdd-audit`**)
- Claim spec/plan compliance without reading them when paths exist
- Run architecture walk on prose/docs-only diffs
- Skip architecture on code diffs
- Use audit severity (P0/P1/P2) as the delivery gate — use **🔴/🟡/🟢** groups per [finding-format.md](references/finding-format.md)

## References

[scope.md](references/scope.md) · [review-dimensions.md](references/review-dimensions.md) · [lens-map.md](references/lens-map.md) · [finding-format.md](references/finding-format.md)
