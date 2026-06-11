# Upstream Sources

Snapshot date: 2026-06-11（upstream pin commits 未变；八 skill **Present** locale 硬约束；**`sdd-improve`** / **`sdd-review`** references 压短）

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
- [shadcn/improve](https://github.com/shadcn/improve) — **third-party, not pinned**
  - License: MIT ([THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md))
  - Adapted: condensed audit checklist in `skills/sdd-improve/references/audit-dimensions.md`
  - Refresh: diff upstream when audit categories change materially; no automatic pin

## Why six core skills

Principles (six): [README — Core principles](README.md#core-principles) — shape / delivery / governance.

This repository ships a **minimal SDD stage set**, not a mirror of the upstream catalogs.

- **Six core skills cover the delivery loop:** (optional) clarify → spec → plan → build → review → ship. User **`@`** the stage skill directly.
- **Upstream ideas are fused, not copied:** each local skill lists sources in the sections below and records what was deliberately left out (no worktrees, no auto-chaining, no state files).
- **Optional clarify stays optional:** `sdd-grill` covers decision interviews before spec or plan; the required artifacts remain spec and plan only.
- **No skill sprawl before evidence:** new core stages need repeated real-project gaps, not parity with upstream skill counts.
- **Optional satellites stay outside the core loop:** `sdd-improve` (codebase audit) and `sdd-zoom` (territory map) are published separately; they do not change the six-stage delivery loop.

For stage choice, see [README.md](README.md#skills) skills table. **Output locale:** skill instructions English; deliverables follow user's language — **Present** hard rule in every skill `SKILL.md`; improve/review details in `finding-format.md` **Report locale**.

Sources and methodology: [docs/design/](docs/design/) ([index](docs/design/README.md)).

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

- **`SKILL.md`** — upstream opening @ pin; **Present** + [spec-template.md](skills/sdd-spec/spec-template.md).
- `docs/sdd/*-spec.md`; in-place revision + **Revision log**; user approval before **`sdd-plan`**.

### `sdd-improve`

Sources:

- [shadcn/improve](https://github.com/shadcn/improve) — audit playbook condensed in `references/audit-dimensions.md` (see **`THIRD_PARTY_NOTICES.md`**)
- Community audit playbooks — same file; pairs with **`sdd-review`** `review-dimensions.md`
- `addyosmani/agent-skills`: `skills/code-review-and-quality` — five-axis checklist summarized into categories 1–6 and 8 of `references/audit-dimensions.md`; merge verdict, spec compliance, and change-sizing gates deliberately left in **`sdd-review`**
- `mattpocock/skills`: `skills/improve-codebase-architecture` (category 5: depth, seam, deletion-test vocabulary)

Local decisions:

- Optional **satellite** — not a mandatory core stage before `sdd-ship`.
- **`SKILL.md`** — one-line **Process** + **Present** + minimal tail; report **content** in `finding-format.md` (follow-up priority, not ship gate); effort in [profile-guide.md](skills/sdd-improve/references/profile-guide.md); checklists in `audit-dimensions.md`. **Read-only** on user tree.
- Natural-language scope inference; **standard** default = categories 1–8.
- **Readability** absorbed into category 5 (**architecture**), not a separate category or Simplify step.
- Disambiguation vs **`sdd-review`**: **opportunity scan** vs **delivery review** — **When/Skip** cross-links only; outcomes **findings report** vs **delivery verdict**.
- Read optional consumer `CONTEXT.md` and `docs/adr/` when present; do not require or inline-write them.
- **Stop:** name next per [closing-the-loop.md](skills/sdd-improve/references/closing-the-loop.md); Common routes in **`SKILL.md`**; hand off — **direct edit** or load named stage skill.

### `sdd-zoom`

Sources (pin `be55a797`):

- `mattpocock/skills`: `skills/engineering/zoom-out` — up one abstraction layer; modules + callers; domain glossary vocabulary

Local decisions:

- **`SKILL.md`** — **zoom-out** body verbatim @ pin; minimal SDD tail (Skip, Diagram, **Present**, Stop, Red flags).
- **Present:** `Territory` / `Map` / `Glossary & Gaps` / `Suggested next`; diagram when ≥3 units. **Stop:** hand off — no in-session next-stage work.
- Orientation only — no refactor findings (**`sdd-improve`**) or delivery review (**`sdd-review`**); no default on-disk map. Optional CONTEXT/ADR when present — infer from code/README when absent.

### `sdd-plan`

Sources:

- `obra/superpowers`: `skills/writing-plans`
- `addyosmani/agent-skills`: `skills/planning-and-task-breakdown`
- `mattpocock/skills`: `skills/engineering/to-issues`

Local decisions:

- **`SKILL.md`** — upstream opening @ pin; **Present** + **15–60 min vertical slices**; [plan-template.md](skills/sdd-plan/plan-template.md); user approval before **`sdd-build`**.

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
- **`SKILL.md`** — code-review-quality + requesting-code-review @ pin; **Present** + scope in [scope.md](skills/sdd-review/references/scope.md); dimensions in `review-dimensions.md`; report in `finding-format.md` (delivery gate).
- Delivery verdict → **`sdd-build`** or **`sdd-ship`**; full verification in **`sdd-ship`**.

### `sdd-ship`

Sources:

- `obra/superpowers`: `skills/verification-before-completion`,
  `skills/finishing-a-development-branch`
- `addyosmani/agent-skills`: `skills/shipping-and-launch`,
  `skills/git-workflow-and-versioning`

Local decisions:

- **`SKILL.md`** — verification-before-completion iron law @ pin; **Present** ship summary; finishing-branch options as explicit user actions.
- Fresh evidence; CHANGELOG per repo convention only; no push/deploy unless requested.

## Updating

Compare each recorded commit with the current upstream branch. Review only
behavior relevant to the mapped local skill, decide manually whether to absorb
it, then update the skill, [SOURCES.md](SOURCES.md) snapshot, spot-check in a consumer repo when material, and commit together.

