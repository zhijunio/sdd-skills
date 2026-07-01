---
name: sdd-ship
description: Use when delivery review has no unresolved blocking findings and the increment needs final verification, push, PR, merge, tag, or release. Not fixing code or local verification in isolation unless the user asks.
---

# sdd-ship

## Role

You're a senior software engineer who verifies a **completed increment** with **fresh evidence** and then **ships it** end to end — from clean commit through merged PR.

```
FROM ISSUE TO MERGED PR — AI SITS IN EVERY STEP OF THE LOOP
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

This skill has two phases:

- **Verify** — quality gate (evidence, regression, CHANGELOG)
- **Ship** — delivery (commit, push, PR, merge, tag, release)

## Gates (both phases)

### Entry gates

- Spec, plan, reviewed diff, and review outcome after [`sdd-review`](../sdd-review/SKILL.md) — no unresolved **must-fix**; **should-fix** fixed or explicitly accepted
- Not a git repo — hard stop
- New work on `main`/`master` — use topic branch + PR

### Phase separation

| If user says… | Route |
|---|---|
| "ship it" / "release" / no explicit scope | Full pipeline: Verify → Ship |
| "is it ready?" / "verify" / "check" | Verify phase only, then stop |
| "push" / "open PR" | Ship phase only (skip verify — present the risk) |
| "fix this" | [`sdd-build`](../sdd-build/SKILL.md) |

## Task

### Verify phase

1. **Map** every **`AC-n`** to implementation and evidence
2. **Rerun** necessary targeted verification (fresh)
3. **Regression** coverage proportional to interface, dependency, config, and shared-module risk
4. **Check** for missing or uncommitted task changes
5. **Record** commands, outcomes, unrun checks, remaining risks
6. **Update** existing **CHANGELOG** when project convention and user-visible impact require it; create CHANGELOG only when the user explicitly requests a format
7. **Present** the verify summary (see Present)
8. **Ask**: "Continue to Ship phase?" — if yes, proceed to Ship phase; if no, stop here

### Ship phase

1. **Orient (read-only)** — `git rev-parse --is-inside-work-tree`, `git status`, `git branch -vv`, `git remote -v`, `git log -1 --oneline`; skim `CHANGELOG.md` `[Unreleased]` when PR/tag/release may apply; when `gh` is available, check existing PR context
2. **Confirm steps** — user names a subset (push, open PR, merge, tag, release, …); if vague (e.g. "can we ship?"), present the full step menu and wait
3. **Gates** — hard stop before remote mutation if gates fail (see Guidelines)
4. **Prepare commits (if dirty tree)** — read `git log` and repo commit rules (`AGENTS.md`, `CONTRIBUTING.md` when present); present an **atomic commit plan** (`feat:` / `fix:` / `docs:` / `chore:` / `refactor:` or project convention); one logical change per commit; confirm each `git commit` unless batch covers the full plan; re-run **Gates** when clean
5. **Run named remote steps** in pipeline order (skip unnamed; default does **not** chain merge → tag → release):

    - **Gates** (re-check) → **Push** → **Open PR** → **CI display** → **Merge** → **Sync default branch** → **Tag** → **GitHub Release** → **Optional README pin**

6. **Present → confirm → execute** — step-by-step (default) or batch when the user confirms the full plan upfront (see Guidelines)
7. **Stop** when requested steps complete — user may continue remaining steps in a later session

## Present

Write the verify summary in the **user's language** when clear from context. Required content (layout flexible):

- **Acceptance Evidence** — Criterion | Implementation | Evidence | Pass/Fail
- **Regression Checks**
- **Unrun Checks**
- **Remaining Risks**
- **CHANGELOG** — user-visible only, or "none needed"
- **Delivery Status** — "Ready for Ship" or "Gaps found"

Every AC needs fresh, proportionate evidence. Explain skipped checks.

## Guidelines

### Execution modes (Ship phase)

| Mode | Behavior |
|---|---|
| **Step-by-step** (default) | One mutating step per explicit user confirmation |
| **Batch** | User confirms the **full plan** upfront → present the complete command list once → run in order; stop on first failure, gate failure, or blocked CI (unless user said **merge despite CI risk**); merge/tag/release only if named in the plan |

After batch commits or stash, re-run **Gates** before push.

### Hard stops (Ship phase)

- Dirty working tree without commit/stash plan
- Force push, direct push to `main`, or `git config` changes — refuse
- No named integration steps — present menu; wait

### CHANGELOG gaps (before tag/release)

When `[Unreleased]` is empty and user-visible PR/tag/release is likely → present the gap; wait for explicit choice:

1. **Continue** — commit-based PR body and/or defer tag/release
2. **Patch `[Unreleased]` now** — present draft bullets; user confirms local edit (file only)
3. **Defer tag/release** — push/PR may still proceed if already confirmed

### Pipeline step notes

See [references/pipeline-notes.md](references/pipeline-notes.md).

### Disambiguation

| Request | Route |
|---|---|
| Fix review findings | [`sdd-build`](../sdd-build/SKILL.md) |
| Fresh codebase audit | [`sdd-audit`](../sdd-audit/SKILL.md) |

### Stop

After verify summary, ship delivery, and any explicitly requested **local commit**. Do not auto-chain beyond what the user confirmed.

### What NOT to do

Do not:

- Rely on stale test results
- Run expensive full builds without risk justification
- Fix code here instead of routing to build
- Invent a new changelog format without precedent
- Babysit or fix CI in this session
- Push new work from `main`/`master`
- Amend, rebase, or skip hooks unless the user explicitly asks
- Mix unrelated changes in one commit without confirm
- Tag/release with empty `[Unreleased]` when user-visible impact exists without presenting the gap
