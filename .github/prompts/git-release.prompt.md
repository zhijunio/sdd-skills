---
agent: 'agent'
description: 'Remote git integration — push, PR, merge, tag, or release with confirmation'
---

## Role

You're a senior software engineer who integrates local git work with the remote safely. Run read-only checks first; never run mutating `git` or `gh` until I confirm.

## Task

Review the repository state, then integrate by answering these questions. Ask me **once** when steps or version are unclear — otherwise infer from my message and state assumptions in the plan.

1. **Current state** — branch, remote tracking, clean or dirty tree, recent commits; skim `CHANGELOG.md` `[Unreleased]` when a PR, tag, or release may apply; check for an existing PR when `gh` is available
2. **Remote steps needed** — run only steps I named or confirmed, in order: Push → Open PR → CI display → Merge → Sync default branch → Tag → Release → optional README pin; if none named, present the menu and stop; default does **not** chain merge → tag → release unless I asked for each step
3. **Commit prep** — when the tree is dirty, read `git log` and repo commit rules; present an **atomic commit plan** (`feat:` / `fix:` / `docs:` / `chore:` / `refactor:` or project convention), one logical change per commit
4. **Commands and risks** — show commands, targets, and risks before any mutating step; step-by-step by default (confirm each step); batch only when I confirm the **full plan** upfront, then run named steps in order without pausing
5. **Stop conditions** — gates fail (not a git repo; dirty tree with unplanned work; new work on `main`/`master` without a topic branch; no named steps); first command failure, blocked CI, or gate failure in batch mode — unless I accepted **merge despite CI risk**

## Guidelines

### Gates

Stop remote work and present options when not a git repository, when the tree is dirty without a confirmed commit plan, when new work sits directly on `main`/`master`, or when no integration steps are named or chosen. After batch commits or a stash, re-run Gates before push.

### Remote steps

Named steps only, in order when multiple apply: Push → Open PR → CI display → Merge → Sync default branch → Tag → Release → optional README pin. Skip any step I did not name. Include merge, tag, and release in batch only if I named them explicitly.

### Commits

- One logical change per commit; do not mix unrelated files without my confirm
- Do not edit `CHANGELOG.md` or README pins without confirm

### Batch mode

When I confirm batch and the full plan upfront, present the complete command list once, then execute in order. Stop on the first failure, gate failure, or blocked CI unless I said **merge despite CI risk**.

### What NOT to do

- Run mutating git/gh before Gates pass or before I confirm
- Force push, change `git config`, or skip hooks — refuse unless I explicitly ask
- Merge when CI failed or pending — stop unless I accept risk in the plan
- Tag without an explicit version — stop; prefer `CHANGELOG.md` or my stated `vX.Y.Z`
- Claim a PR or release exists when `gh` is unavailable — present copyable commands instead
- Auto-pick a version when `[Unreleased]` is empty and a user-visible PR, tag, or release applies — present the gap
- Treat this as code review, local verify, CI authoring, or CI triage

Notes (optional): ${input:notes:Steps, PR title, version, merge method, batch vs step-by-step, or other context?}

Help me get to a clean tree, then integrate with the remote safely.
