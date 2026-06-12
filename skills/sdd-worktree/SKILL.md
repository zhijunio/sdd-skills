---
name: sdd-worktree
description: Use when starting a new change in a git repo and an isolated dev context (worktree or topic branch) is needed before spec or implementation, or the user asks for worktree / feature branch setup.
---

Optional pre-loop satellite — isolate git context before the six-stage loop. **Present → user confirms →** run mutating git only after explicit approval. Not spec, plan, build, review, or ship.

**When:** new increment in a consumer git repo; user wants worktree or `feature/` / `fix/` / `docs/` branch before coding on `main`. **Skip:** spec/plan authoring → [`sdd-spec`](../sdd-spec/SKILL.md); open trade-offs only → [`sdd-grill`](../sdd-grill/SKILL.md); already on an isolated branch/worktree with clean tree and clear next stage.

**Evaluation order (fixed):**

1. Not a git repo (Req §2) → **hard stop**
2. Dirty working tree (uncommitted changes) → **hard stop** — commit or stash; after stash user must re-`@sdd-worktree`
3. Resolve baseline (§5–§6), prefix (§7), `topic` (§8–§9), path (§12)
4. Branch `<prefix>/<topic>` exists or worktree path occupied → **stop**, contextual options (§10) — **no** branch fallback for path-only conflict
5. No conflict: if branch fallback applies (§3) → `git checkout -b` (**weak isolation** — same directory); else → `git worktree add`
6. **Present** editable prefix, topic, path; highlight non-standard baseline in same round if no `main`/`master` (§6)
7. User confirms (确认 / yes / go / equivalent) → execute mutating commands
8. **Stop** → hand off per rules below

**Read-only probe first:** `git rev-parse --is-inside-work-tree`, `git rev-parse --show-toplevel`, `git status`, `git branch`, `git worktree list`.

**Hard stops:**

- **Not a git repo** — do not run `git branch` or `git worktree`; ask user to retry inside the target repo.
- **Dirty tree** — no new branch/worktree; prompt commit or stash; do not auto-retry after stash in the same turn.
- **No user confirmation** — read-only git only; no `git worktree add`, no `git checkout -b`.

**Baseline:** `main` if present, else `master` if present (prefer `main` when both exist). If neither exists, use **current branch** as baseline — call this out prominently in **Present** and include in the same confirmation round.

**Prefix:** default `feature/`; `fix/` when description mentions bug / fix / regression / 修复; `docs/` when clearly docs-only (README/CHANGELOG/comments, no behavior change). User override in **Present** wins.

**Topic:** extract from user description; else slug of repo root basename (`git rev-parse --show-toplevel`). Slug: lowercase kebab-case, `[a-z0-9-]`, max 48 chars, collapse `-`, trim edges; invalid → `-`; empty → `task`. Path uses **raw** root basename; topic segment is slugged.

**Default path:** `../<repo-basename>-<topic>` relative to toplevel. User may override with path relative to toplevel or absolute path before confirm.

**Worktree command:** `git worktree add -b <prefix>/<topic> <path> <baseline>`

**Branch fallback (§3 only — not for path conflicts):** use when any of: `git worktree` subcommand unavailable; user explicitly rejects worktree this turn; worktree precheck fails (permissions, illegal path — **not** path already occupied). Command: `git checkout -b <prefix>/<topic> <baseline>` — label **weak isolation** in **Present** and state which trigger applied.

**Conflicts (§10):** always offer change `topic` or cancel. If branch exists: also offer reuse (clean tree + user confirms). If path-only (branch absent): offer change path or `topic` — **no** reuse-branch option.

**Present:** baseline, prefix, topic, path, full git command(s), weak-isolation label if applicable, editable fields. User's language — do not default to English. Keep literal: skill ids, git commands, branch names.

**Stop:** hand off — no in-session next-stage work.

- Default **`sdd-spec`** when user gave recognizable intent (topic sentence or fix/docs keywords) or changed topic from slug default in **Present**.
- **`sdd-grill`** when user gave no recognizable intent, topic stayed slug default, and user only replied 确认 without changing topic (e.g.「开个 worktree」only).

**Red flags:** mutating git before confirm; skipping evaluation order; auto-chaining next skill; path conflict → silent branch fallback; treating worktree as ship gate; spec/plan/code in-session; cleaning dirty tree or deleting worktrees for the user.

**SDD:** maintainer-authored; explicit `@` only — not superpowers auto-worktree. Contract: `docs/sdd/2026-06-12-sdd-worktree-spec.md`.
