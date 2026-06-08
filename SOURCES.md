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

## Local Skills

### `using-sdd`

Sources:

- `obra/superpowers`: `skills/using-superpowers`
- `addyosmani/agent-skills`: `skills/using-agent-skills`

Local decisions:

- Route one stage without automatic invocation.
- Infer progress from artifacts and diff; do not persist workflow state.

### `sdd-brainstorm`

Sources:

- `mattpocock/skills`: `skills/productivity/grill-me`
- `obra/superpowers`: `skills/brainstorming`
- `addyosmani/agent-skills`: `skills/interview-me`, `skills/idea-refine`

Local decisions:

- Ask one decision at a time and provide a recommendation.
- Make the stage optional and avoid a durable artifact by default.

### `sdd-grill`

Sources:

- `mattpocock/skills`: `skills/productivity/grill-me`
- `addyosmani/agent-skills`: `skills/interview-me`

Local decisions:

- Optional SDD stage; body follows `grill-me` with SDD stop routing only.
- Do not write spec, plan, or code in this skill.

### `sdd-spec`

Sources:

- `obra/superpowers`: `skills/brainstorming`
- `addyosmani/agent-skills`: `skills/spec-driven-development`
- `mattpocock/skills`: `skills/engineering/to-prd`

Local decisions:

- Keep behavior and necessary technical constraints in one concise document.
- Require observable acceptance criteria and explicit user approval.

### `sdd-plan`

Sources:

- `obra/superpowers`: `skills/writing-plans`
- `addyosmani/agent-skills`: `skills/planning-and-task-breakdown`
- `mattpocock/skills`: `skills/engineering/to-issues`

Local decisions:

- Prefer 15-60 minute vertical slices over microtasks.
- Do not maintain a separate traceability matrix or workflow status.

### `sdd-build`

Sources:

- `mattpocock/skills`: `skills/engineering/tdd`
- `obra/superpowers`: `skills/test-driven-development`
- `addyosmani/agent-skills`: `skills/test-driven-development`,
  `skills/incremental-implementation`

Local decisions:

- Keep red-green-refactor and repeatable verification.
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

