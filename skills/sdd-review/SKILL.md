---
name: sdd-review
description: Use when a scoped diff needs an independent, read-only review before delivery, after implementation, or when the user asks for a review. Classifies code diff vs prose/docs-only; mandatory architecture walk on code diffs only.
---

Read-only reviewer — not implementer. Multi-axis review on a defined **increment diff**; **delivery verdict** with evidence. No edits to product, test, or plan files.

**Core principle:** Review early, review often — on the **work product**, not session history.

**When:** before delivery, after implementation, or user asks for review. Can run with diff only — missing spec/plan reduces traceability; disclose. **Skip:** codebase audit without delivery increment → [`sdd-audit`](../sdd-audit/SKILL.md). **Delivery review** — increment diff only. Ambiguous "review" without diff → ask vs [`sdd-audit`](../sdd-audit/SKILL.md).

**Scope:** [scope.md](references/scope.md). **Dimensions:** [review-dimensions.md](references/review-dimensions.md). **Lenses:** [lens-map.md](references/lens-map.md). **Report:** [finding-format.md](references/finding-format.md).

**Dimensions (scoped diff only):**

- **Core (always):** spec/plan compliance; correctness/regressions; tests; docs/traceability + reference integrity on renames.
- **Mandatory on code diffs:** architecture (structure + DRY/KISS in diff). **Skip** on prose/docs-only.
- **Conditional when signals apply:** standards, security, performance, dependencies, observability, accessibility, operations — skip with `*: skip` in Coverage. **Never skip architecture on code diffs.**

**Process:**

1. **Context — Scope** per finding-format — include **Diff kind** (`code` / `prose/docs-only`).
2. Read complete scoped diff — or triage large diffs per scope.md; disclose **Limits**.
3. Read spec/plan when available; map AC when plan exists.
4. Review test changes first.
5. Walk core; architecture on code diffs; applicable conditionals. `architecture: pass` or `architecture: skip` in Coverage.
6. **Present** Context → Findings → Coverage → Follow-up.

**Present:** User's language. Literals: lens ids, skill ids, `file:line`, git literals, delivery **🔴/🟡/🟢** groups. Optional impact emoji per `sdd-audit/references/report.md`. [finding-format.md](references/finding-format.md).

Fresh agent/subagent when available; else reread baseline. Optional two-pass on large plans; default one pass.

**Red flags:** editing while reviewing; staged-only when increment includes unstaged; assuming `main`/`master`; whole repo without range; path-only scope; pre-existing outside diff as must-fix; compliance claims without spec; full verification or plan updates here; code diff without architecture walk; architecture on prose-only; one-line findings without Evidence/grading.

**Verdict:** 🔴 must-fix blocks **this increment** (delivery gate). 🟡 should-fix unless user accepts risk. 🟢 suggestion — non-blocking.

**SDD:** read-only; fresh verification → `sdd-ship`. Layout flexible. Default no durable file; do not update plan. Stop → invoke `sdd-build` if blocking findings; else invoke `sdd-ship`.
