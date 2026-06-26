---
agent: 'agent'
description: 'Remote git integration — push, PR, merge, tag, or release with confirmation'
---

I need to integrate local git work with the remote. Run read-only checks first; no mutating `git` or `gh` until I confirm.

Integration steps: ${input:steps:Which steps? (e.g., push, open PR, merge, tag, release — or a subset)}
Notes (optional): ${input:notes:PR title, version, merge method, or other context?}
Execution: ${input:mode:Step-by-step (default) or batch? If batch, list the full sequence — e.g. prepare commits → push → open PR → CI → merge if green}

## Workflow

1. **Orient (read-only)** — `git status`, branch, remote, recent commits; skim `CHANGELOG.md` `[Unreleased]` when PR/tag/release may apply; check existing PR if `gh` is available
2. **Gates** — stop remote work if: not a git repo; dirty tree; new work on `main`/`master`; no named steps (present the menu first)
3. **Prepare commits (if dirty)** — read `git log` and repo commit rules; present an **atomic commit plan** (`feat:` / `fix:` / `docs:` / `chore:` / `refactor:` or project convention); one logical change per commit; confirm each `git commit` unless batch covers the full commit plan
4. **Remote steps (named only, in order)** — skip unnamed; default does **not** chain merge → tag → release:
    - Push → Open PR → CI display → Merge → Sync default branch → Tag → Release → optional README pin
5. **Present → confirm → execute** — show exact commands, targets, and risks

## Batch mode

When I choose **batch** and confirm the **full plan** upfront:

* Present the complete command list once, then run steps in order without pausing between them
* Stop on the first failure, gate failure, or blocked CI (unless I said **merge despite CI risk**)
* Include merge, tag, and release in batch only if I named them explicitly
* After batch commits or stash, re-run Gates before push

Default when mode is unclear: **step-by-step** — one mutating step per confirmation.

## Hard stops

* Force push, `git config` changes, or skip hooks — refuse unless I explicitly ask
* Merge when CI failed/pending — stop unless I accept risk in the plan
* Tag without explicit version — stop; prefer `CHANGELOG.md` or my stated `vX.Y.Z`
* No `gh` — present copyable commands; do not claim a PR or release exists
* Empty `[Unreleased]` with user-visible PR/tag/release — present the gap; do not auto-pick silently

## Do not

* Run mutating git/gh before Gates pass or before I confirm (plan confirm for batch; per-step confirm for step-by-step)
* Mix unrelated files in one commit without my confirm
* Edit `CHANGELOG.md` or README pins without confirm
* Treat this as code review, local verify, or CI triage

Help me get to a clean tree, then integrate with the remote safely.
