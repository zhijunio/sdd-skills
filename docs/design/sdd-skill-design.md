# SDD Skill Design Draft

## Positioning

- Used to turn an unclear request into a testable specification, then into an executable plan, then into implementation and review.
- The goal is not more ceremony. The goal is less rework.
- Best for new features, cross-module changes, and behavior that can drift easily.

## Use / Don't Use

- Use when the request needs a durable behavior contract before code.
- Use when multiple files or modules may change together.
- Use when later review should compare implementation against a clear spec.
- Do not use for pure brainstorming.
- Do not use for trivial one-line fixes.
- Do not use for tasks that are already fully specified and only need a direct edit.

## Trigger Conditions

- The user says “write the spec first”, “make a plan first”, “use SDD”, or “don’t implement yet”.
- The request has unclear boundaries, multiple modules, or a high risk of behavior drift.
- The work would benefit from a durable contract that later steps can follow.

## Core Principles

- Contract before code.
- Specs must be verifiable.
- Every step needs clear input, output, and stop conditions.
- Keep specs stable and plans short-lived.
- Prefer the smallest correct change over broad abstraction.

## Recommended Structure

- `sdd-spec` - write the behavior contract.
- `sdd-plan` - split the contract into vertical, testable slices.
- `sdd-build` - implement the plan with tests alongside the code.
- `sdd-review` - review the change independently, read-only, with no file writes.
- `sdd-ship` - confirm completion and prepare delivery.
- `sdd-audit` - inspect an existing repository holistically, not an increment.

## Stage Contracts

### `sdd-spec`

- Input: a problem statement, constraints, and any known context.
- Output: a behavior contract with scope, non-goals, acceptance criteria, and edge cases.
- Stop when the behavior can be verified without guessing intent.

### `sdd-plan`

- Input: an approved spec.
- Output: a small set of vertical slices with clear verification points.
- Stop when each slice can be delivered and checked independently.

### `sdd-build`

- Input: an approved plan.
- Output: code changes and tests that satisfy the plan.
- Stop when the implementation matches the spec and the tests pass.

### `sdd-review`

- Input: the current implementation plus the approved spec and repo standards.
- Output: two independent findings sets - `Spec` and `Standards`.
- No file writes.
- No spec rewrite.
- No implementation changes.
- Stop after reporting both axes independently.
- If no spec exists, skip the `Spec` axis and report `Standards` only.

### `sdd-ship`

- Input: a reviewed change with no blocking findings.
- Output: final verification and delivery notes.
- Stop when the change is ready to hand off or publish.

### `sdd-audit`

- Input: the current repository state.
- Output: a repo-level health review, not an increment review.
- Stop when the repo-level findings are collected.

## Main Flow

### 1. Understand the goal

- Confirm what problem needs solving before proposing a solution.
- Output: goal, scope, non-goals, success criteria.

### 2. Write the spec

- Describe behavior in user language, not implementation language.
- Include:
  - trigger conditions
  - inputs
  - expected behavior
  - edge cases and failures
  - acceptance checks
- The spec should be testable, not just readable.

### 3. Split the plan

- Each step should be independently finishable and verifiable.
- Prefer vertical slices over file-by-file division.
- Every step should answer: how do we know this part is done?
- If a step cannot be verified, it is too vague.

### 4. Implement and verify

- Keep tests and behavior in sync.
- Use the smallest change that works.
- If the plan breaks down, return to the spec instead of forcing the code.
- Do not expand scope while implementing unless the spec changes first.

### 5. Review and deliver

- Review in two axes:
  - `Spec` - does the implementation match the approved contract?
  - `Standards` - does the implementation follow repo conventions and quality expectations?
- Each axis should cover:
  - correctness
  - maintainability
  - tests
  - architecture
  - security and performance only when there is signal
- Before delivery, be able to answer:
  - what changed
  - why it changed
  - how it was verified
  - what risk remains
- Review is read-only. It does not write files, notes, or artifacts.

## Output Template

- `Spec`
- `Plan`
- `Implementation notes`
- `Verification`
- `Open questions`

## Minimal End-to-End Example

- User request: “Add a retry button to failed uploads.”
- `sdd-spec`: define when the retry appears, what it retries, and what success/failure look like.
- `sdd-plan`: split into UI, network retry path, and test coverage.
- `sdd-build`: implement the smallest slice first, then add tests for failure and success.
- `sdd-review`: check the change against the spec and against repo standards in parallel.
- `sdd-ship`: confirm the change is verified and ready to hand off.

## Failure Modes

- Jumping into implementation before the spec exists.
- Writing a spec that is only background context, not a contract.
- Making the plan too coarse to execute independently.
- Expanding scope at every step.
- Treating review as a rubber stamp instead of an independent check.
- Using abstraction to solve problems that have not happened yet.
- Making review produce files instead of findings.

## Skill Boundaries

- Keep the main skill lean.
- Put examples, templates, and checklists in `references/`.
- Split by stage if the workflow grows.
- Do not turn the skill into a generic developer assistant.
- Do not fold unrelated repo-audit behavior into the delivery loop.

## What To Put In SKILL.md

- The trigger conditions.
- The stage boundaries.
- The stage contracts.
- The stop conditions.
- The minimal example.

## What To Put In References

- Spec template.
- Plan template.
- Review checklist.
- Example prompts.
- Any longer per-stage guidance.
