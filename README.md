# SDD Skills

[![CI](https://github.com/zhijunio/sdd-skills/actions/workflows/check.yml/badge.svg)](https://github.com/zhijunio/sdd-skills/actions/workflows/check.yml)
[![License](https://img.shields.io/github/license/zhijunio/sdd-skills)](LICENSE)

**Eleven** platform-neutral agent skills in one repo: a **five-stage SDD delivery loop** (plus optional `sdd-audit`) and **five independent utility skills** that are not part of that loop. No state machine, project manager, or Git workflow framework — SDD stages you **`@`** one at a time.

## Why use these skills

- **Explicit stages** — one skill output → **Stop** → hand off; no auto-chaining
- **Verifiable slices** — spec AC, plan as vertical slices, test-first build, evidence-backed review and verify
- **SDD optional** — `sdd-audit` (codebase health) only when you need it; use an upstream design-interview skill for plan/design clarification
- **Review/audit split** — `sdd-review` gates increment diffs; `sdd-audit` reviews repo / module / area / branch health
- **Independent utilities** — README, AGENTS.md, explain, onboarding, over-engineering audit — install separately; no SDD coupling
- **Platform-neutral** — Markdown skills only; works with Cursor, Codex, Claude Code, and other agents via the [skills CLI](https://github.com/vercel-labs/skills)

Six principles (shape / delivery / governance): explicit stages, verifiable slices, test and prove, borrow don't rebuild — embodied in skill `SKILL.md` files and [AGENTS.md](AGENTS.md).

## Getting started

Install from this repository:

```bash
npx skills@latest add zhijunio/sdd-skills
```

Non-interactive (multiple agents):

```bash
npx skills@latest add zhijunio/sdd-skills -a cursor -a codex -a claude-code -y
```

SDD core loop only:

```bash
npx skills@latest add zhijunio/sdd-skills \
  -s sdd-spec -s sdd-plan -s sdd-build -s sdd-review -s sdd-ship \
  -a cursor -y
```

Minimal path (spec + plan):

```bash
npx skills@latest add zhijunio/sdd-skills -s sdd-spec -s sdd-plan -y
```

Independent skills only (examples):

```bash
npx skills@latest add zhijunio/sdd-skills -s ponytail-audit -a cursor -y
npx skills@latest add zhijunio/sdd-skills -s create-readme -s create-agentsmd -y
```

SDD optional audit:

```bash
npx skills@latest add zhijunio/sdd-skills -s sdd-audit -a cursor -y
```

**Stable pin** (`v0.3.1` — eight skills, pre-rename ids):

```bash
npx skills@latest add zhijunio/sdd-skills@v0.3.1 -a cursor -a codex -a claude-code -y
```

| Scope | Flag | Where skills land |
| --- | --- | --- |
| Project (default) | — | `./.agents/skills/` |
| Global | `-g` | Cursor: `~/.cursor/skills/` · Codex: `~/.codex/skills/` · Claude Code: `~/.claude/skills/` |

List without installing: `npx skills@latest add zhijunio/sdd-skills --list`

**Manual install:** copy `skills/<name>/` into your agent's skills directory (include bundled `references/` where present).

> **Breaking on current `main` (unreleased):** `sdd-verify` → `sdd-ship`; `repo-audit` → `sdd-review`; `repo-audit-full` → `sdd-audit`; `sdd-improve` → `sdd-audit`; `sdd-explain` → `explain-code`; `sdd-onboard` → `onboarding-plan`; `sdd-readme` / `sdd-agents` → `create-readme` / `create-agentsmd`; **`sdd-grill`**, **`git-release`**, **`sdd-worktree`**, and **`sdd-zoom` removed**. Use an upstream design-interview skill for plan/design clarification. Update `@` references after upgrading from `v0.3.1`.

## SDD workflow

```mermaid
flowchart TD
  subgraph audit["Optional audit"]
    A[sdd-audit]
  end

  S[sdd-spec] -->|user approval| P[sdd-plan]
  P -->|user approval| B[sdd-build]
  B --> R[sdd-review]
  R -->|must-fix| B
  R -->|pass| V[sdd-ship]

  A --> S
```

## Skills

Skill instructions are written in English.

### SDD delivery loop

| Skill | Use when |
| --- | --- |
| `sdd-spec` | A behavior contract and acceptance criteria are needed |
| `sdd-plan` | An approved spec needs testable vertical slices |
| `sdd-build` | An approved plan is ready for test-first implementation |
| `sdd-review` | An increment diff needs a delivery verdict |
| `sdd-ship` | Verify and ship a reviewed increment — from evidence through merged PR |

### SDD optional

| Skill | Use when |
| --- | --- |
| `sdd-audit` | Whole-repo / module / area / branch health audit using the same `Standards` dimensions as `sdd-review` — not a delivery gate and not a Spec review |

Use an upstream design-interview skill when goals, boundaries, or trade-offs need interview before spec or plan.

**Review vs audit:** `sdd-review` gates **this increment**; `sdd-audit` audits the **repo / module / area / branch** for follow-ups.

### Independent (not SDD)

Bundled in this repo for convenience; **no SDD loop coupling** — `@` only when you need the task.

| Skill | Use when |
| --- | --- |
| `create-readme` | Human-facing README.md for a project |
| `create-agentsmd` | AGENTS.md for agent operating context |
| `explain-code` | Explain code in chat |
| `onboarding-plan` | Phased contributor onboarding plan |
| `ponytail-audit` | Whole-repo over-engineering audit |

Paired prompt files under [`docs/prompts/`](docs/prompts/) — independent files, content aligned with skills below (no cross-links between skill and prompt).

| Skill | Paired prompt |
| --- | --- |
| `create-readme` | `create-readme.prompt.md` |
| `create-agentsmd` | `create-agentsmd.prompt.md` |
| `explain-code` | `explain-code.prompt.md` |
| `onboarding-plan` | `onboarding-plan.prompt.md` |

`ponytail-audit` has no paired prompt.

**Prompt-only** (no skill):

| Prompt | Prefer skill when |
| --- | --- |
| `review-code.prompt.md` | Increment delivery gate → `sdd-review` |
| `document-api.prompt.md` | Behavior contract / AC → `sdd-spec` |
| `generate-unit-tests.prompt.md` | Test-first on approved plan → `sdd-build` |
| `git-release.prompt.md` | Push & PR lifecycle → `sdd-ship` |

### Consumer artifacts

Default documents in **your** project:

```text
docs/sdd/YYYY-MM-DD-<topic>-spec.md
docs/sdd/YYYY-MM-DD-<topic>-plan.md
```

Optional: `docs/adr/`, `CONTEXT.md` for stable domain language in consumer projects.

## Documentation

| Topic | Link |
| --- | --- |
| Agent operating guide | [AGENTS.md](AGENTS.md) |
| Contributor onboarding | [`onboarding-plan`](skills/onboarding-plan/SKILL.md) skill · [prompt](docs/prompts/onboarding-plan.prompt.md) |
| Release history | [CHANGELOG.md](CHANGELOG.md) |

## Contributing

Maintainers: read [AGENTS.md](AGENTS.md). Open PRs to `main`; CI job **`validate`** must pass (eleven skills, `sdd-ship` present, retired ids absent). User-visible changes → [CHANGELOG.md](CHANGELOG.md) `[Unreleased]`.

## Sources

Ideas from [mattpocock/skills](https://github.com/mattpocock/skills), [obra/superpowers](https://github.com/obra/superpowers), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), and [shadcn/improve](https://github.com/shadcn/improve) (audit influence for **`sdd-audit`**).

## License

MIT — see [LICENSE](LICENSE).
