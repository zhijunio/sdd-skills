# SDD Skills Domain

Vocabulary for the **sdd-skills** pack — delivery-loop stages and independent review/improve utilities.

## Language

**Spec**:
A durable behavior contract for one change: goal, scope, non-goals, and pass/fail acceptance criteria.
_Avoid_: Plan, ticket, design doc, brainstorm notes

**Requirement**:
A narrative statement of an intended capability or constraint. It orients readers; it is not the verification contract.
_Avoid_: AC, acceptance criterion (those are narrower)

**Acceptance Criterion (AC)**:
A stable, independently pass/fail check (`AC-n`) of observable behavior. The only contract that Plan slices and Build verification bind to.
_Avoid_: Requirement, “done when it feels right”, implementation step

**Plan**:
An ordered set of vertical slices that covers every AC, each with verification. May be a single thin slice; must still be approved before Build for new increments.
_Avoid_: Spec, task list by file/layer, sprint backlog

**Vertical Slice**:
A unit of work that ends in new observable behavior (user or external system) plus a concrete verification command — not a layer-only scaffold.
_Avoid_: Horizontal slice, “add repository then service then controller” with no observable outcome

**Approval**:
An explicit conversational confirmation (e.g. confirm / yes / go / 批准) of the Present artifact. File presence alone is never approval. Disk write follows repo convention or explicit request.
_Avoid_: Implied OK, “spec file exists”, silent proceed

**Approval Present**:
The chat Present for Spec/Plan (full contract Body) and Build (status + close-out evidence). Light chrome: Artifact/Body/risks/Ask for Spec·Plan; fixed Slices · Close-out evidence · Deviations · Ask/Stop for Build. Subject of Approval or Stop — not a quality report. Prose follows the **user's language** (not English by default).
_Avoid_: Report Present, Scope/Coverage/Verdict face on Spec·Plan, summary-only Body for Approval, English-default Present when the user writes in another language

**Report Present**:
The chat Present for Delivery Review and Improve Pass. **Delivery Review** (Matt-shaped): Standards · Spec · Summary · Verdict — Standards body uses **(a)/(b)**; Spec body uses **(a)/(b)/(c)**; every finding carries 🔴/🟡/🟢; axes unmerged; Summary is per-axis one-liners; Verdict is gate only after Summary. Fixed point / sample notes live in Summary (no Scope/Coverage headings). **Improve Pass** keeps Scope · Coverage · dimensions · Top recommendation. Ends in Stop; no Approval of a behavior contract. Prose follows the **user's language** (not English by default).
_Avoid_: Approval Present, Suggested next steps as a required section, Scope/Coverage headings on Delivery Review, merging Standards+Spec into one list, unifying loop Present into this face, English-default Present when the user writes in another language

**Alternative Proof**:
A deterministic, rerunnable check used in Build when there is no reasonable automated-test entry (docs, pure config, mechanical renames). Not a substitute for a red test when behavior code has a testable surface.
_Avoid_: Manual “looks fine”, one-off unverifiable demo

**Review-fix Path**:
A Build entry that uses `sdd-review` listed findings as the temporary scope/plan, skipping a new Spec+Plan for that patch set. New behavior outside those findings is out of scope.
_Avoid_: Free implementation after review, silent scope expansion

**Local Reversible Deviation**:
An implementation-detail change during Build that does not alter AC pass/fail or a slice’s completion/verification definition. Record and continue; do not silently change the contract.
_Avoid_: Quiet AC rewrite, unrecorded slice merge/split

## Delivery gate & health

**Delivery Review**:
A read-only two-axis **quality report** (Standards + Spec) on an **increment diff** since a fixed point (user-supplied, else the repo default branch from `origin/HEAD` / common fallbacks — never hard-coded `main` alone; ask only if unresolved). Scope is committed `fixed-point...HEAD` only. Ends in a Verdict. Owned by `sdd-review`. **Independent** — usable alone, not required to follow Spec/Plan/Build.
_Avoid_: Whole-repo improve scan, guessing `main` when the default is elsewhere, reviewing uncommitted WIP by default, “LGTM” without scope, auto-routing into build/spec

**Standards Axis**:
Whether the scoped change meets documented repo standards and the shared **four-dimension** baseline: **Correctness**, **Structure** (includes Fowler smells), **Verification**, **Traceability**. Present as Matt **(a) Documented standards & baseline dimensions** / **(b) Baseline smells**, each finding tagged with a Delivery Group emoji and a dimension label (smells usually Structure). Non-smell Correctness/Verification/Traceability gaps belong in **(a)** citing `standards-baseline.md` when no repo doc applies. Documented standards may be hard; baseline/smells are judgement calls unless they also break a standard or AC. Signal-gated risks (security, concurrency, data/migration, performance) sit under Correctness.
_Avoid_: Spec compliance, product roadmap, a separate Maintainability/Architecture/Conditionals checklist beside Structure, dimension-first Present that drops Matt (a)/(b), double-filing the same issue on both axes

**Spec Axis**:
Whether the scoped change faithfully implements the originating Spec/Plan/AC (and related issue/PRD when that is the contract). Present as Matt **(a) Missing / partial** · **(b) Scope creep** · **(c) Looks implemented but wrong**, each finding tagged with a Delivery Group emoji. Prefer Spec **(a)** only when the contract itself is incomplete/partial; repo test-norm gaps without an AC stay on Standards **(a)·Verification**.
_Avoid_: Style-only review, whole-repo opportunity scan, merging Spec buckets into Standards, inventing Spec findings for pure Standards issues

**Delivery Group**:
Review finding severity on a Delivery Review: 🔴 must-fix (blocks), 🟡 should-fix (fix or explicit risk acceptance), 🟢 suggestion (non-blocking).
_Avoid_: Improve Priority Critical/High/Medium/Low, P0/P1/P2 roadmap phases

**Verdict**:
The delivery-gate outcome of a Delivery Review: **blocked**, **pass**, or **pass pending risk acceptance**. Computed after both axes are presented; must not merge or rewrite axis findings. Full **pass** (or pass after explicit 🟡 acceptance) ends the report — Stop. Git/PR/merge are outside this pack.
_Avoid_: Improve Priority, informal thumbs-up, auto-routing into other skills, a single “overall finding” list that blends Standards and Spec

**Standards-only Review**:
A Delivery Review that skips the Spec axis because no originating contract was found. May still report Standards findings; must not claim Spec pass.
_Avoid_: Claiming the change “matches Spec” with no Spec

**Health Audit** / **Improve Pass**:
A read-only Standards assessment of a **broad scope** (repo, module, area, or branch) for follow-up **candidates** — hotspot-first, four dimensions matching Delivery Review Standards, no Spec axis, Markdown only (no HTML). Owned by `sdd-improve`. **Independent of the delivery loop** (not a Spec/Plan/Build stage). Not a delivery gate.
_Avoid_: Delivery Review, merge blocker, Spec pass/fail, HTML architecture reports, requiring Spec/Plan first

**Audit Severity** / **Improve Priority**:
Follow-up priority on an Improve Pass: 🚨 Critical / 🔴 High / 🟡 Medium / 🟢 Low. Not interchangeable with Delivery Groups; never used alone to block merge.
_Avoid_: must-fix / should-fix / suggestion

**Roadmap Phase**:
Audit scheduling labels **P0 / P1 / P2** for systemic follow-ups. Independent of Audit Severity emoji; text-only.
_Avoid_: Delivery Verdict, must-fix

**Close-out Verification**:
Proportionate fresh evidence after Build slices finish (full suite when practical, else targeted regression). Recorded on the plan; useful to a later Delivery Review Spec axis when the user runs one. Not a separate SDD stage.
_Avoid_: Dedicated verify/ship skill, stale logs as proof, “shipped” meaning merged

**Review Freshness**:
A prior Delivery Review may be reused across sessions for the **same increment scope**. If HEAD or the worktree has **material drift** since that review, re-run Delivery Review before treating the gate as current.
_Avoid_: “We reviewed last week” with no scope check
