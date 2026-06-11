---
name: sdd-ship
description: Use when review has no unresolved blocking findings and a completed SDD increment needs final acceptance verification and delivery readiness checks.
---

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

Before claiming done: identify proving command → run fresh → read full output → verify claim.

**When:** after `sdd-review` — no unresolved must-fix; should-fix fixed or explicitly accepted. **Not for:** fixing review findings (→ `sdd-build`).

Require spec, plan, reviewed diff, and review outcome.

**Process:**

1. Map every `AC-n` to implementation and evidence.
2. Rerun necessary targeted verification.
3. Regression coverage proportional to interface, dependency, config, and shared-module risk.
4. Check for missing or uncommitted task changes.
5. Record commands, outcomes, unrun checks, remaining risks.
6. Update existing CHANGELOG when project convention and user-visible impact require it.
7. Create CHANGELOG only when user explicitly requests a format.

**Red flags:** stale test results; expensive full build without risk justification; fixing code here instead of `sdd-build`; new changelog tool/format without precedent; push/release/deploy without explicit instruction.

Every AC needs fresh, proportionate evidence. Explain skipped checks.

**Present:** Write the ship summary in the **user's language** (latest user turn when unclear) — do not default to English. Required content (layout flexible): Acceptance Evidence (Criterion | Implementation | Evidence | Pass/Fail); Regression Checks; Unrun Checks; Remaining Risks; CHANGELOG (user-visible only, or "none needed"); Delivery Status. Record CHANGELOG user-visible changes only.

**SDD:** Stop after ship summary and any explicitly requested local commit. No push, PR, publish, or deploy unless separately requested.
