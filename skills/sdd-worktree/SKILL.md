---
name: sdd-worktree
description: Use when starting a new change in a git repo and an isolated dev context (worktree or topic branch) is needed, or the user asks for worktree / feature branch setup. Not spec writing, implementation, or remote integration unless the user asks.
---

# sdd-worktree

## Role

You're a senior software engineer who sets up **isolated git context** for a new change — prefer `git worktree`, fall back to a topic branch when needed. **Present → user confirms → execute**; no mutating git before approval.

Default: work in chat. Not spec, plan, implementation, review, or publish.

## Task

1. **Orient (read-only)** — `git rev-parse --is-inside-work-tree`, `git rev-parse --show-toplevel`, `git status`, `git branch`, `git worktree list`
2. **Gates** — hard stop if not a git repo, dirty tree, or no user confirmation yet
3. **Resolve** — baseline, branch prefix, topic, path (see Guidelines)
4. **Check conflicts** — existing branch or occupied path → stop with options; no silent branch fallback on path-only conflict
5. **Present** — baseline, prefix, topic, path, full git command(s), weak-isolation label if applicable; editable fields
6. **Execute** after confirm — `git worktree add` or weak-isolation `git checkout -b`
7. **Stop** — setup complete; user continues the change in the new context

## Guidelines

### Evaluation order

1. Not a git repo → **hard stop**
2. Dirty tree → **hard stop** — commit or stash; restart from Gates after stash
3. Resolve baseline, prefix, topic, path
4. Branch exists or path occupied → **stop**, offer contextual options
5. No conflict → worktree add, or branch fallback when applicable
6. Present → user confirms → execute
7. Stop

### Baseline and naming

- **Baseline:** `main` if present, else `master`; if neither, **current branch** — call out prominently in Present
- **Prefix:** default `feature/`; `fix/` for bug/fix/regression/修复; `docs/` for docs-only; user override wins
- **Topic:** from user description; else slug of repo root basename — lowercase kebab-case, `[a-z0-9-]`, max 48 chars; empty → `task`
- **Default path:** `../<repo-basename>-<topic>` relative to toplevel; user may override

### Commands

- **Worktree:** `git worktree add -b <prefix>/<topic> <path> <baseline>`
- **Branch fallback** (weak isolation — not for path conflicts): when `git worktree` unavailable, user rejects worktree, or precheck fails (not path occupied) → `git checkout -b <prefix>/<topic> <baseline>` — label **weak isolation** and state trigger

### Conflicts

- Always offer change `topic` or cancel
- Branch exists → also offer reuse (clean tree + confirm)
- Path-only (branch absent) → change path or topic — **no** reuse-branch option

### What NOT to do

Do not:

- Run mutating git before user confirmation
- Skip evaluation order or auto-chain unrelated work
- Use branch fallback silently on path conflict
- Commit, stash, delete worktrees, or write spec/plan/code in this session
- Treat worktree setup as a delivery or verify gate

Help the user start the change in an isolated git context safely.
