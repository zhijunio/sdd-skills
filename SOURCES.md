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
- Require an explicit diff range; spec and plan are optional.
- Never assume `main` is the integration branch.
- Default scope is merge-base diff only; pre-existing issues outside scope are not `must-fix`.
- Core dimensions: spec/plan, correctness, tests, docs/traceability.
- Conditional dimensions: architecture, security, performance, readability/change size.
- Process tests-first; optional two-pass review for large plans.
- Output includes strengths, dimension coverage, verdict, and residual gaps; full verification stays in `sdd-ship`.
- Output uses fixed headings: Scope → Strengths → Findings (must-fix / should-fix / suggestion) → Dimension Coverage → Assumptions & Gaps → Verdict.

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

