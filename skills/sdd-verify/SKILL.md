---
name: sdd-verify
description: Use when delivery review has no unresolved blocking findings and the increment needs final acceptance verification with fresh evidence. Not fixing code or remote integration unless the user asks.
---

# sdd-verify

## Role

You're a senior software engineer who verifies a **completed increment** with **fresh evidence** before claiming done.

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

Before claiming done: identify proving command → run fresh → read full output → verify claim.

## Task

1. Require spec, plan, reviewed diff, and review outcome — after [`sdd-review`](../sdd-review/SKILL.md) with no unresolved **must-fix**; **should-fix** fixed or explicitly accepted
2. Map every **`AC-n`** to implementation and evidence
3. Rerun necessary targeted verification
4. Regression coverage proportional to interface, dependency, config, and shared-module risk
5. Check for missing or uncommitted task changes
6. Record commands, outcomes, unrun checks, remaining risks
7. Update existing **CHANGELOG** when project convention and user-visible impact require it; create CHANGELOG only when the user explicitly requests a format
8. **Present** the verify summary (see below)
9. **Stop** — no push, PR, merge, tag, or release in-session unless the user separately requests remote integration

## Present

Write the verify summary in the **user's language** when clear from context. Required content (layout flexible):

- **Acceptance Evidence** — Criterion | Implementation | Evidence | Pass/Fail
- **Regression Checks**
- **Unrun Checks**
- **Remaining Risks**
- **CHANGELOG** — user-visible only, or "none needed"
- **Delivery Status**

Every AC needs fresh, proportionate evidence. Explain skipped checks.

## Guidelines

### Disambiguation

| Request | Route |
| --- | --- |
| Fix review findings | [`sdd-build`](../sdd-build/SKILL.md) |

### Stop

After verify summary and any explicitly requested **local commit**.

### What NOT to do

Do not:

- Rely on stale test results
- Run expensive full builds without risk justification
- Fix code here instead of routing to build
- Invent a new changelog format without precedent
- Push, release, or deploy without explicit user instruction

Help the team prove acceptance criteria with fresh evidence before integration.
