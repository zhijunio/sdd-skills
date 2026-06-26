# Maintainer SDD archives

Historical **spec** and **plan** documents for increments landed in this repository. They record decisions at merge time — **not** current runtime contracts. Archive prose may reference removed paths (e.g. `docs/design/`, retired skill ids) — ignore for current behavior.

**Live contracts:** `skills/<name>/SKILL.md` · [README.md](../../README.md) · [AGENTS.md](../../AGENTS.md)

| File | Topic | Note |
| --- | --- | --- |
| [2026-06-11-sdd-improve-spec.md](./2026-06-11-sdd-improve-spec.md) | `sdd-audit` (formerly improve) | Pre-rename ids in prose |
| [2026-06-11-sdd-improve-plan.md](./2026-06-11-sdd-improve-plan.md) | same | |
| [2026-06-12-sdd-worktree-spec.md](./2026-06-12-sdd-worktree-spec.md) | `git-context` (formerly sdd-worktree) | Independent skill; no SDD handoff |
| [2026-06-12-sdd-worktree-plan.md](./2026-06-12-sdd-worktree-plan.md) | same | |
| [2026-06-12-sdd-publish-spec.md](./2026-06-12-sdd-publish-spec.md) | `git-release` (formerly sdd-publish) | Independent skill; no SDD handoff |
| [2026-06-12-sdd-publish-plan.md](./2026-06-12-sdd-publish-plan.md) | same | |

Consumer projects use their own `docs/sdd/*-spec.md` and `*-plan.md` by convention — unrelated to this folder.
