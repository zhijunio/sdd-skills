# Upstream Sources

Snapshot date: 2026-06-12（upstream pin commits 未变；maintainer-authored satellites 含 **`sdd-worktree`**、**`sdd-publish`**、meta **`sdd-readme`** / **`sdd-agents`** / **`sdd-explain`** / **`sdd-zoom`** / **`sdd-grill`** / **`sdd-onboard`**）

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
- Maintainer-authored MECE playbooks in `skills/sdd-audit/references/` (`map.md`, `playbook.md`, `report.md`, `deep-parallel.md`)
- [shadcn/improve](https://github.com/shadcn/improve) — **third-party, not pinned**
  - License: MIT ([THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md))
  - Historical audit checklist influence; **`sdd-audit`** body uses bundled MECE playbooks under `references/`

## Why six core skills

Principles (six): [engineering-rationale §1.0](./engineering-rationale.md#10-核心原则) — shape / delivery / governance.

This repository ships a **minimal SDD stage set**, not a mirror of the upstream catalogs.

- **Six core skills cover the delivery loop:** (optional) clarify → spec → plan → build → review → verify. User **`@`** the stage skill directly.
- **Upstream ideas are fused, not copied:** each local skill lists sources in the sections below and records what was deliberately left out (no auto worktree orchestration, no auto-chaining, no state files).
- **Optional clarify stays optional:** `sdd-grill` can stress-test plans and trade-offs before spec or plan; the required delivery artifacts remain spec and plan only.
- **No skill sprawl before evidence:** new core stages need repeated real-project gaps, not parity with upstream skill counts.
- **Optional satellites stay outside the core loop:** utility **`sdd-worktree`** (git isolation), **`sdd-publish`** (remote integration), **`sdd-audit`** (codebase audit), and meta skills `sdd-readme` / `sdd-agents` / `sdd-explain` / `sdd-ci` / `sdd-zoom` / `sdd-grill` / `sdd-onboard` are published separately; they do not change the six-stage delivery loop.

For stage choice, see [engineering-rationale §2](./engineering-rationale.md#2-本仓定位与边界) and each skill `SKILL.md`. **Output locale:** skill instructions English; deliverables follow user's language — **Present** hard rule in every skill `SKILL.md`; improve report in `report.md` **Report locale**; review in `finding-format.md` **Report locale**.

Sources and methodology: [design docs](./README.md) ([engineering-rationale](./engineering-rationale.md)).

## Skill and prompt pairs

Several skills share **basically the same content** as a [`.github/prompts/*.prompt.md`](../../.github/prompts/) file — one entry point for **`@` skills**, one for Cursor GitHub prompts.

| Rule | Detail |
| --- | --- |
| **Independent** | `SKILL.md` and the prompt file do **not** link to each other — no "Skill entry" or "GitHub prompt entry" lines |
| **Content parity** | Role, task flow, and guidelines stay aligned; when behavior changes, update **both** in the same change |
| **Mapping only in maintainer docs** | Pairing table lives here and in [ONBOARDING.md](../ONBOARDING.md) — not in runtime artifacts |

Prompt-only `${input:...}` placeholders stay in the prompt; the skill uses plain defaults (e.g. default platform, default triggers).

## Local Skills

### `sdd-grill`

Sources:

- [`.github/prompts/grill-me.prompt.md`](../../.github/prompts/grill-me.prompt.md) — content aligned with skill (not verbatim); no cross-links
- `mattpocock/skills`: `skills/productivity/grill-me` @ pin `be55a797` (superseded by local prompt for structure)
- Historical thrown: `obra/superpowers` `skills/brainstorming` (territory/explore → **`sdd-zoom`** or user `@`); `addyosmani/agent-skills` `skills/interview-me`, `skills/idea-refine` (not fused into grill)

Local decisions:

- Optional **meta satellite** — plan/design decision interview in chat; not delivery loop.
- **`SKILL.md`** only — no bundled `references/`; default chat; write disk on user confirm.
- **Present (summary):** `Decisions` → `Rejected` → `Boundaries` → `Open`. One question per turn during interview.

### `sdd-spec`

Sources:

- `obra/superpowers`: `skills/brainstorming`
- `addyosmani/agent-skills`: `skills/spec-driven-development`
- `mattpocock/skills`: `skills/engineering/to-prd`

Local decisions:

- **`SKILL.md`** — body restructured (Role / Task / Guidelines); **Present** + [spec-template.md](../../skills/sdd-spec/references/spec-template.md).
- `docs/sdd/*-spec.md`; in-place revision + **Revision log**; user approval before **`sdd-plan`**.

### `sdd-audit`

Sources:

- Maintainer-authored — MECE pillars in `references/map.md`, `playbook.md`, `report.md`, `deep-parallel.md`
- Prior pins: [shadcn/improve](https://github.com/shadcn/improve), `addyosmani/agent-skills`, `mattpocock/skills` — historical audit checklist influence only (see **`THIRD_PARTY_NOTICES.md`**)

Local decisions:

- Optional **utility satellite** — MECE codebase/branch health audit; not delivery loop.
- **`SKILL.md`** — body restructured (Role / Task / Guidelines); workflow in skill; details in **`references/`**.
- **`references/`** — `map.md`, `playbook.md`, `report.md`, `deep-parallel.md`; report per `report.md`. Severity 🚨🔴🟡🟢 = follow-up priority — **not** `sdd-review` delivery gate.
- Disambiguation vs **`sdd-review`**: codebase audit vs delivery review.
- **Thrown:** full SDD handoff table (spec/plan/build routing) — not fused into skill body; **Suggested next steps** in report only.

### `sdd-readme`

Sources:

- [`.github/prompts/create-readme.prompt.md`](../../.github/prompts/create-readme.prompt.md) — content aligned with skill (not verbatim); no cross-links

Local decisions:

- Optional **meta satellite** — README.md authoring for any git repo; not delivery loop.
- **`SKILL.md`** only — no bundled `references/`; default chat draft; write disk on user confirm.

### `sdd-agents`

Sources:

- [`.github/prompts/create-agents-md.prompt.md`](../../.github/prompts/create-agents-md.prompt.md) — content aligned with skill (not verbatim); no cross-links
- [agents.md](https://agents.md/) — generic `##` heading convention (Context, Structure, Commands, …)

Local decisions:

- Optional **meta satellite** — AGENTS.md authoring for any git repo; not delivery loop.
- **`SKILL.md`** only — no bundled `references/`; default chat draft; write disk on user confirm.

### `sdd-explain`

Sources:

- [`.github/prompts/explain-code.prompt.md`](../../.github/prompts/explain-code.prompt.md) — content aligned with skill (not verbatim); no cross-links

Local decisions:

- Optional **meta satellite** — code explanation in chat; not delivery loop; no default file write.

### `sdd-onboard`

Sources:

- [`.github/prompts/onboarding-plan.prompt.md`](../../.github/prompts/onboarding-plan.prompt.md) — content aligned with skill (not verbatim); no cross-links

Local decisions:

- Optional **meta satellite** — phased contributor onboarding in chat; not delivery loop.
- **`SKILL.md`** only — no bundled `references/`; default chat; write disk on user confirm.

### `sdd-ci`

Sources:

- [`.github/prompts/create-ci.prompt.md`](../../.github/prompts/create-ci.prompt.md) — content aligned with skill (not verbatim); no cross-links

Local decisions:

- Optional **meta satellite** — CI pipeline authoring for any git repo; not delivery loop; no triage of failing CI.
- **`SKILL.md`** only — no bundled `references/`; default chat draft; write workflow files on user confirm.
- **Stack conventions** subsection — Maven / Gradle / Node / Python / Go; apply only when detected; universal CI rules stay separate.

### `sdd-zoom`

Sources:

- [`.github/prompts/zoom-codebase.prompt.md`](../../.github/prompts/zoom-codebase.prompt.md) — content aligned with skill (not verbatim); no cross-links
- Historical: `mattpocock/skills` `skills/engineering/zoom-out` @ pin `be55a797` (superseded by local prompt)

Local decisions:

- Optional **meta satellite** — codebase territory map in chat; not delivery loop.
- **`SKILL.md`** only — no bundled `references/`; default chat; write disk on user confirm.
- **Present:** `Territory` → `Map` → `Diagram` → `Glossary & gaps` → `Suggested next`; diagram when ≥3 units. Orientation only — not code review, audit, or implementation.

### `sdd-plan`

Sources:

- `obra/superpowers`: `skills/writing-plans`
- `addyosmani/agent-skills`: `skills/planning-and-task-breakdown`
- `mattpocock/skills`: `skills/engineering/to-issues`

Local decisions:

- **`SKILL.md`** — body restructured (Role / Task / Guidelines); **15–60 min vertical slices**; [plan-template.md](../../skills/sdd-plan/references/plan-template.md); user approval before **`sdd-build`**.

### `sdd-build`

Sources:

- `mattpocock/skills`: `skills/engineering/tdd`
- `obra/superpowers`: `skills/test-driven-development`
- `addyosmani/agent-skills`: `skills/test-driven-development`,
  `skills/incremental-implementation`

Local decisions:

- **`SKILL.md`** — body restructured (Role / Task / Guidelines); TDD iron law; vertical-slice loop; escalation → **`sdd-spec`** / **`sdd-plan`**; **Stop** → **`sdd-review`**.

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
- **`SKILL.md`** — body restructured (Role / Task / Guidelines); scope in [scope.md](../../skills/sdd-review/references/scope.md); dimensions in `review-dimensions.md`; report in `finding-format.md` (delivery gate).
- Delivery verdict → **`sdd-build`** or **`sdd-verify`**; full verification in **`sdd-verify`**.

### `sdd-worktree`

Sources:

- **Maintainer-authored** — no upstream pin; fused idea from explicit user `@` git isolation, distinct from superpowers auto-worktree orchestration (thrown per engineering-rationale §3.2).

Local decisions:

- Optional **utility satellite** — git isolation (worktree or topic branch); not delivery loop.
- **`SKILL.md`** — body restructured (Role / Task / Guidelines); Present → confirm → mutating git; weak-isolation branch fallback; conflict stop rules.
- **Thrown:** superpowers session worktree chains, SDD handoff to **`sdd-spec`** / **`sdd-grill`**, contract `docs/sdd/2026-06-12-sdd-worktree-spec.md`.

### `sdd-publish`

Sources:

- [`.github/prompts/publish-changes.prompt.md`](../../.github/prompts/publish-changes.prompt.md) — content aligned with skill (not verbatim); no cross-links
- Historical: maintainer `docs/sdd/2026-06-12-sdd-publish-spec.md` (SDD contract — superseded by prompt + skill for agent use)
- Cursor user rule `creating-pull-requests` may coexist — rule covers `gh` format; skill covers gates and Present/confirm flow.

Local decisions:

- Optional **utility satellite** — remote git integration in any repo; not delivery loop.
- **`SKILL.md`** only — no bundled `references/`; Prepare commits, step-by-step / batch, pipeline subset, no-`gh` degradation, sync default branch before tag.
- **Thrown:** superpowers auto-release chains, CI babysit loops, force push; SDD handoff to **`sdd-verify`** (not fused into skill body).

### `sdd-verify`

Sources:

- `obra/superpowers`: `skills/verification-before-completion`,
  `skills/finishing-a-development-branch`
- `addyosmani/agent-skills`: `skills/shipping-and-launch`,
  `skills/git-workflow-and-versioning`

Local decisions:

- **`SKILL.md`** — body restructured (Role / Task / Guidelines); verification-before-completion iron law; **Present** verify summary; remote integration → **`sdd-publish`** on separate user request.

## Updating

Compare each recorded commit with the current upstream branch. Review only
behavior relevant to the mapped local skill, decide manually whether to absorb
it, then update the skill, [SOURCES.md](SOURCES.md) snapshot, try in conversation or maintainer self-trial when material, and commit together.

