# Upstream Sources

Snapshot date: 2026-06-12（upstream pin commits 未变；十 skill 含 maintainer-authored **`sdd-worktree`**、**`sdd-publish`**）

## Repositories

- `mattpocock/skills`
  - Branch: `main`
  - Commit: `be55a7970319ede7965edbb02b5e41cba1ca82c9`
- `obra/superpowers`
  - Branch: `main`
  - Commit: `6fd4507659784c351abbd2bc264c7162cfd386dc`
- `addyosmani/agent-skills`
  - Branch: `main`
  - Commit: `c076972e2626fe2acc30b00a6c7240d4c5fb786a`
- [zhijunio/zhijunio-skills `codebase-audit`](https://github.com/zhijunio/zhijunio-skills/tree/main/codebase-audit) — **third-party, not pinned**
  - License: MIT ([THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md))
  - Adapted: MECE playbooks in `skills/sdd-audit/references/` (`map.md`, `playbook.md`, `report.md`, `deep-parallel.md`)
  - Refresh: diff upstream when pillar checklists change materially; no automatic pin
- [shadcn/improve](https://github.com/shadcn/improve) — **superseded** for `sdd-audit` body by `codebase-audit` import (see **`THIRD_PARTY_NOTICES.md`**)

## Why six core skills

Principles (six): [README — Core principles](../../README.md#core-principles) — shape / delivery / governance.

This repository ships a **minimal SDD stage set**, not a mirror of the upstream catalogs.

- **Six core skills cover the delivery loop:** (optional) clarify → spec → plan → build → review → verify. User **`@`** the stage skill directly.
- **Upstream ideas are fused, not copied:** each local skill lists sources in the sections below and records what was deliberately left out (no auto worktree orchestration, no auto-chaining, no state files).
- **Optional clarify stays optional:** `sdd-grill` covers decision interviews before spec or plan; the required artifacts remain spec and plan only.
- **No skill sprawl before evidence:** new core stages need repeated real-project gaps, not parity with upstream skill counts.
- **Optional satellites stay outside the core loop:** `sdd-worktree` (pre-loop git isolation), `sdd-publish` (post-loop remote integration), `sdd-audit` (codebase audit), and `sdd-zoom` (territory map) are published separately; they do not change the six-stage delivery loop.

For stage choice, see [README.md](../../README.md#skills) skills table. **Output locale:** skill instructions English; deliverables follow user's language — **Present** hard rule in every skill `SKILL.md`; improve report in `report.md` **Report locale**; review in `finding-format.md` **Report locale**.

Sources and methodology: [design docs](./README.md) ([engineering-rationale](./engineering-rationale.md)).

## Local Skills

### `sdd-grill`

Sources (pin `be55a797`):

- `mattpocock/skills`: `skills/productivity/grill-me` — one Q/turn + recommendation; decision-tree walk; explore codebase first

Local decisions:

- **`SKILL.md`** — upstream body verbatim @ pin; minimal SDD tail (Skip, **Present**, Stop, Red flags).
- **Thrown:** `obra/superpowers` `skills/brainstorming` (territory/explore → **`sdd-zoom`** or user `@`); `addyosmani/agent-skills` `skills/interview-me`, `skills/idea-refine` (intent clarify — not fused into grill); Superpowers `docs/superpowers/specs/`, auto **writing-plans**, idea-refine `docs/ideas/`, implementation in-session.
- **Present:** `Decisions:` / `Rejected:` / `Boundaries:` / `Open:` — user's language. **Stop:** hand off; default **`sdd-spec`**; **`sdd-plan`** when approved spec exists and subject is plan/slices.

### `sdd-spec`

Sources:

- `obra/superpowers`: `skills/brainstorming`
- `addyosmani/agent-skills`: `skills/spec-driven-development`
- `mattpocock/skills`: `skills/engineering/to-prd`

Local decisions:

- **`SKILL.md`** — upstream opening @ pin; **Present** + [spec-template.md](../../skills/sdd-spec/spec-template.md).
- `docs/sdd/*-spec.md`; in-place revision + **Revision log**; user approval before **`sdd-plan`**.

### `sdd-audit`

Sources:

- [zhijunio/zhijunio-skills `codebase-audit`](https://github.com/zhijunio/zhijunio-skills/tree/main/codebase-audit) — MECE pillars, `map.md`, `playbook.md`, `report.md`, `deep-parallel.md` (bundled under `references/`; sync on intentional upstream changes)
- Prior pins: [shadcn/improve](https://github.com/shadcn/improve), `addyosmani/agent-skills`, `mattpocock/skills` — superseded for checklist body by `codebase-audit` import (see **`THIRD_PARTY_NOTICES.md`**)

Local decisions:

- Optional **satellite** — not a mandatory core stage before `sdd-verify`.
- **`SKILL.md`** — `codebase-audit` body @ sync + minimal **SDD** tail (When/Skip vs `sdd-review`, **Stop**, handoff).
- **`references/`** — `map.md`, `playbook.md`, `report.md`, `deep-parallel.md` synced from upstream; SDD handoff table in **`SKILL.md` Stop**.
- **Present:** report per `report.md` (same section order as upstream). **Suggested next steps** (last) names one route per **`SKILL.md` Stop** handoff table. Severity 🚨🔴🟡🟢 = follow-up priority — **not** `sdd-review` delivery gate.
- Disambiguation vs **`sdd-review`**: **codebase audit** vs **delivery review** — **When/Skip** cross-links only.
- **Stop:** user **`@`** next skill — no auto-chain.

### `sdd-zoom`

Sources (pin `be55a797`):

- `mattpocock/skills`: `skills/engineering/zoom-out` — up one abstraction layer; modules + callers; domain glossary vocabulary

Local decisions:

- **`SKILL.md`** — **zoom-out** body verbatim @ pin; minimal SDD tail (Skip, Diagram, **Present**, Stop, Red flags).
- **Present:** `Territory` / `Map` / `Glossary & Gaps` / `Suggested next`; diagram when ≥3 units. **Stop:** hand off — no in-session next-stage work.
- Orientation only — no refactor findings (**`sdd-audit`**) or delivery review (**`sdd-review`**); no default on-disk map. Optional CONTEXT/ADR when present — infer from code/README when absent.

### `sdd-plan`

Sources:

- `obra/superpowers`: `skills/writing-plans`
- `addyosmani/agent-skills`: `skills/planning-and-task-breakdown`
- `mattpocock/skills`: `skills/engineering/to-issues`

Local decisions:

- **`SKILL.md`** — upstream opening @ pin; **Present** + **15–60 min vertical slices**; [plan-template.md](../../skills/sdd-plan/plan-template.md); user approval before **`sdd-build`**.

### `sdd-build`

Sources:

- `mattpocock/skills`: `skills/engineering/tdd`
- `obra/superpowers`: `skills/test-driven-development`
- `addyosmani/agent-skills`: `skills/test-driven-development`,
  `skills/incremental-implementation`

Local decisions:

- **`SKILL.md`** — superpowers TDD iron law + matt vertical-slice anti-pattern @ pin; **Present** for narration and plan appendices.
- Escalation to **`sdd-spec`** / **`sdd-plan`**; **Stop** → **`sdd-review`**; no worktrees or per-slice commits required.

### `sdd-review`

Sources:

- `obra/superpowers`: `skills/requesting-code-review`,
  `skills/verification-before-completion`
- `addyosmani/agent-skills`: `skills/code-review-and-quality`
- `mattpocock/skills`: review-first engineering practices across the repository

Local decisions:

- Keep review strictly read-only.
- Default scope is merge-base diff plus task-related uncommitted work; never assume `main`.
- Pre-existing issues outside the scoped diff are out-of-scope observations, not delivery blockers.
- Require explicit diff range; a repository path alone is insufficient.
- **`SKILL.md`** — code-review-quality + requesting-code-review @ pin; **Present** + scope in [scope.md](../../skills/sdd-review/references/scope.md); dimensions in `review-dimensions.md`; report in `finding-format.md` (delivery gate).
- Delivery verdict → **`sdd-build`** or **`sdd-verify`**; full verification in **`sdd-verify`**.

### `sdd-worktree`

Sources:

- **Maintainer-authored** — no upstream pin; fused idea from explicit user `@` git isolation, distinct from superpowers auto-worktree orchestration (thrown per engineering-rationale §3.2).

Local decisions:

- **`SKILL.md`** — evaluation order, Present → confirm → mutating git, weak-isolation branch fallback, conflict stop rules; contract `docs/sdd/2026-06-12-sdd-worktree-spec.md`.
- **Thrown:** superpowers session worktree chains, Git hooks, worktree lifecycle cleanup, delivery-gate usage.
- **Present:** user's language. **Stop:** default **`sdd-spec`**; **`sdd-grill`** when intent still vague after slug-default topic only.
- **When/Skip** cross-links with **`sdd-spec`** and **`sdd-grill`** only.

### `sdd-publish`

Sources:

- **Maintainer-authored** — no upstream pin; post-loop integration satellite (standalone `@` OK; does not require `@sdd-verify`); distinct from superpowers auto-release orchestration (thrown per engineering-rationale §3.2).
- Cursor user rule `creating-pull-requests` may coexist — rule covers `gh` format; this skill covers SDD gates and Present/Stop.

Local decisions:

- **`SKILL.md`** — evaluation order, per-step Present → confirm → mutating git/gh, pipeline subset, no-`gh` degradation, merge后 sync default branch before tag; contract `docs/sdd/2026-06-12-sdd-publish-spec.md`.
- **Thrown:** superpowers auto-release chains, CI babysit loops, force push, platform DevOps bundles.
- **Present:** user's language. **Stop:** integration complete — no default next skill.
- **When/Skip** cross-links with **`sdd-verify`** only.

### `sdd-verify`

Sources:

- `obra/superpowers`: `skills/verification-before-completion`,
  `skills/finishing-a-development-branch`
- `addyosmani/agent-skills`: `skills/shipping-and-launch`,
  `skills/git-workflow-and-versioning`

Local decisions:

- **`SKILL.md`** — verification-before-completion iron law @ pin; **Present** verify summary; finishing-branch remote steps → hand off **`sdd-publish`** (explicit user actions only).
- Fresh evidence; CHANGELOG per repo convention only; no push/deploy in-session — separate request → hand off **`sdd-publish`**.

## Updating

Compare each recorded commit with the current upstream branch. Review only
behavior relevant to the mapped local skill, decide manually whether to absorb
it, then update the skill, [SOURCES.md](SOURCES.md) snapshot, spot-check in a consumer repo when material, and commit together.

