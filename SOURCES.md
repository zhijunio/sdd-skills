# Upstream Sources

Snapshot date: 2026-06-08

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

## Why seven skills

This repository ships a **minimal SDD stage set**, not a mirror of the upstream catalogs.

- **Seven skills cover the delivery loop:** route → (optional) clarify → spec → plan → build → review → ship.
- **Upstream ideas are fused, not copied:** each local skill lists sources in the sections below and records what was deliberately left out (no worktrees, no auto-chaining, no state files).
- **Optional clarify stays optional:** `sdd-grill` covers explore-and-challenge before spec or plan; the required artifacts remain spec and plan only.
- **No skill sprawl before evidence:** new core stages need repeated real-project gaps, not parity with upstream skill counts.
- **Optional satellites stay outside the core loop:** `sdd-architect` is published separately for architecture deepening; it does not change the seven-stage delivery loop.

For routing, see [README.md](README.md#quick-routing) and [skills/using-sdd/SKILL.md](skills/using-sdd/SKILL.md#routing-examples).

Sources and methodology: [docs/design/](docs/design/) ([index](docs/design/README.md)).

## Local Skills

### `using-sdd`

Sources:

- `obra/superpowers`: `skills/using-superpowers`
- `addyosmani/agent-skills`: `skills/using-agent-skills`

Local decisions:

- Route one stage without automatic invocation.
- Infer progress from artifacts and diff; do not persist workflow state.
- May briefly announce the routing check and recommended skill; still do not invoke it automatically.
- List **`sdd-architect`** under optional satellites; route deepening intent there without auto-invocation.

### `sdd-grill`

Sources:

- `mattpocock/skills`: `skills/productivity/grill-me`
- `obra/superpowers`: `skills/brainstorming`
- `addyosmani/agent-skills`: `skills/interview-me`, `skills/idea-refine`

Local decisions:

- Merged pre-spec explore and plan stress-test into one optional stage.
- Ask one decision at a time with a recommendation; explore compares approaches, challenge grills what is on the table.
- Optional SDD stage but works standalone; no disk artifact required by default.
- Do not write spec, plan, or code in this skill.
- Stop conditions recommend `sdd-spec` or `sdd-plan` contextually; do not invoke them automatically.

### `sdd-spec`

Sources:

- `obra/superpowers`: `skills/brainstorming`
- `addyosmani/agent-skills`: `skills/spec-driven-development`
- `mattpocock/skills`: `skills/engineering/to-prd`

Local decisions:

- Keep behavior and necessary technical constraints in one concise document.
- Require observable acceptance criteria and explicit user approval.
- Revise approved specs in place with a Revision log; distinguish clarification-only edits from AC changes.
- Optional template sections: Decisions (this change), Related ADRs (links only); optional consumer `docs/adr/` per README.
- Self-review checklist before user approval (adapted from sibling [sdd-lite](https://github.com/zhijunio/sdd-lite) written-artifact gate; kept inline, no shared fragment file).

### `sdd-architect`

Sources:

- `mattpocock/skills`: `skills/improve-codebase-architecture` (depth, seam, deletion-test vocabulary; grilling after candidate selection)

Local decisions:

- Optional **satellite** — not a mandatory core stage before `sdd-ship`.
- Conversation deliverable only; no HTML reports, subagents, or default on-disk deepen file.
- Read optional consumer `CONTEXT.md` and `docs/adr/` when present; do not require or inline-write them.
- Stop → recommend **`using-sdd`** only; default next stage after candidate selection is **`sdd-spec`** when acceptance criteria are needed.
- **`v0.2.0` tag** waits for a third consumer loop with deepening friction evidence.

### `sdd-plan`

Sources:

- `obra/superpowers`: `skills/writing-plans`
- `addyosmani/agent-skills`: `skills/planning-and-task-breakdown`
- `mattpocock/skills`: `skills/engineering/to-issues`

Local decisions:

- Prefer 15-60 minute vertical slices over microtasks.
- Do not maintain a separate traceability matrix or workflow status.
- Optional **Risks / Dependencies** section in the plan template when build order or verification is affected.
- Self-review checklist before user approval (adapted from sibling sdd-lite; inline in skill, not a cross-skill file).

### `sdd-build`

Sources:

- `mattpocock/skills`: `skills/engineering/tdd`
- `obra/superpowers`: `skills/test-driven-development`
- `addyosmani/agent-skills`: `skills/test-driven-development`,
  `skills/incremental-implementation`

Local decisions:

- Keep red-green-refactor and repeatable verification.
- Match consumer repository conventions from guidance and surrounding code when present; when guidance is silent, follow spec/plan and touched-code patterns only.
- Red for intended behavior; slice idempotency; review-fix scope boundary; no premature ship claims (adapted from sdd-lite TDD discipline; no per-green commit requirement).
- Do not require worktrees, subagents, or per-slice commits.

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
- Core and conditional review dimensions; fixed output headings including Dimension Coverage and Verdict.
- Plan **Acceptance** mapping (`met` / `partial` / `missing` / `unclear`); large-diff triage and **Limits** disclosure (adapted from sdd-lite / agent-skills axes; no bundled templates or review subagents).
- Full verification stays in `sdd-ship`.

### `sdd-ship`

Sources:

- `obra/superpowers`: `skills/verification-before-completion`,
  `skills/finishing-a-development-branch`
- `addyosmani/agent-skills`: `skills/shipping-and-launch`,
  `skills/git-workflow-and-versioning`

Local decisions:

- Require fresh, risk-proportionate evidence.
- Keep commit, push, PR, release, and deployment as explicit user actions.
- Allow CHANGELOG updates only when repository convention requires them.

## Updating

Compare each recorded commit with the current upstream branch. Review only
behavior relevant to the mapped local skill, decide manually whether to absorb
it, then update the skill, checks, and commit snapshot together.

