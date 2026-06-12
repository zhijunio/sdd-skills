---
name: sdd-publish
description: Use when a completed SDD increment passed ship and the user explicitly requests remote integration — push, PR, merge, tag, or GitHub release — in a git repo.
---

Optional **post-loop** satellite — remote integration after the six-stage loop. **Present → user confirms →** run mutating git/gh only after explicit per-step approval. Not spec, plan, build, review, or ship.

**When:** after [`sdd-ship`](../sdd-ship/SKILL.md) — user explicitly requests push, PR, merge, tag, release, or integration subset. **Skip:** ship not done or review not passed → [`sdd-review`](../sdd-review/SKILL.md) / [`sdd-ship`](../sdd-ship/SKILL.md) / [`sdd-build`](../sdd-build/SKILL.md); fixing review findings → `sdd-build`; pre-loop isolation → [`sdd-worktree`](../sdd-worktree/SKILL.md); CI triage or PR comment resolution — not this skill.

**Pipeline steps** (user may name a subset; default does **not** chain merge → tag → release):

1. **Gates** — read-only probes (Req §2)
2. **Push** — `git push` (with `-u` on first upstream)
3. **Open PR** — `gh pr create` when `gh` available; else Present copyable command
4. **CI display** — `gh pr checks` / `gh pr view` (display only — no CI babysit)
5. **Merge PR** — `gh pr merge` (separate confirm; CI failed/pending → default stop)
6. **Sync default branch** — after merge, `checkout` + `pull` default branch before tag
7. **Tag** — `git tag -a` + `git push origin <tag>` (version from CHANGELOG)
8. **GitHub Release** — `gh release create` when `gh` available
9. **Optional README pin** — only when repo has recommended-pin paragraph and user confirms

**Evaluation order (fixed):**

1. Gates (Req §2) → **hard stop**
2. User-named step subset (Req §9)
3. Multi-step runs keep pipeline order: push → open PR → CI display → merge → **sync default branch** (after merge, before tag) → tag → release → README pin (skip unnamed steps)
4. Per step: **Present** → confirm (§14) → execute → optional **Stop** (user may continue next session)
5. All requested steps done → **Stop** (integration complete — no default next skill)

**Read-only probe first:** `git rev-parse --is-inside-work-tree`, `git status`, `git branch -vv`, `git remote -v`, `git log -1 --oneline`; when PR context exists and `gh` available → `gh pr view`.

**Hard stops (no mutating git/gh until resolved):**

- **Not a git repo**
- **Dirty working tree** — any uncommitted changes per `git status` (including untracked when status shows dirty) → prompt commit or stash; after stash user must re-`@sdd-publish`
- **On `main` or `master` intending to push new work** — stop; use topic branch + PR (`main` if present, else `master` as production default)
- **No integration intent** — user only asks "can we ship?" without naming steps → **Present** step menu; wait for named subset
- **`sdd-ship` not confirmed** (no ship summary in session and user has not affirmed) **or** increment not passed **`sdd-review`** → hand off `sdd-review` / `sdd-ship` / `sdd-build`
- **Force push, direct push to `main`, or `git config` changes** — refuse

**Push step:** **Present** remote, branch, `git push -u origin <branch>` (or equivalent) → user confirms → execute. Subset "push only" must not auto-run PR/merge/tag/release.

**Open PR step:** **Present** PR title/body (from CHANGELOG `[Unreleased]` or recent commits). `gh` available → `gh pr create` after confirm. No `gh` → **Present** full `gh pr create` command; label **step not executed** — do not claim PR exists.

**CI display step:** when `gh` available and PR exists → **Present** `gh pr checks` summary. Failed or pending → default **do not merge**; suggest fix CI or user **explicitly accepts risk** then re-`@` merge in a new turn.

**Merge step:** **separate confirm** required. **Present** merge method (merge/squash/rebase) and target branch. `gh pr merge` or web-merge path. CI not green and user has not accepted risk → stop.

**Sync default branch step:** when merge ran in this flow → **Present** `git checkout <default>` + `git pull origin <default>` (`<default>` = `main` or `master`) → confirm HEAD is post-merge tip before tag.

**Tag step — version resolution** (stop if still ambiguous):

1. User specifies `vX.Y.Z` in **Present**
2. `CHANGELOG.md` has `## [X.Y.Z]` draft under `[Unreleased]`
3. Suggest semver patch bump from `git describe --tags --abbrev=0` — **Present** for confirm; never silent adopt
4. None of the above → stop; ask user to complete CHANGELOG

**Tag baseline:** after merge in this flow → sync default branch first. Tag-only on topic branch without merge → **Present** explicitly "tag on branch `<branch>` HEAD" and get confirm. Then **Present** `git tag -a vX.Y.Z -m "..."` and `git push origin vX.Y.Z` → confirm → execute.

**CHANGELOG promotion (optional, before tag):** when `[Unreleased]` exists → **Present** promoting to `[vX.Y.Z] - YYYY-MM-DD` (user confirms date) → edit file only after confirm; may share confirm round with tag step.

**GitHub Release step:** `gh` available → **Present** `gh release create vX.Y.Z --notes "..."` (notes from CHANGELOG entry for that version) → confirm → execute. No `gh` → **Present** command only; do not execute.

**README pin (optional):** when `README.md` (or project convention file) has recommended pin / install `@vX.Y.Z` → **Present** whether to replace with new tag → edit only after confirm; skip if absent or user declines.

**No `gh` degradation:** PR, merge, and release steps must not pretend execution — **Present** copyable commands + note local `gh` or web UI required.

**Present:** commands, targets, risks, step menu when needed. User's language — do not default to English. Keep literal: skill ids, git/gh commands, branch names, `vX.Y.Z`.

**Stop:** integration complete — no in-session next-stage work. User may `@` again later for remaining steps.

**Red flags:** mutating git/gh before per-step confirm; skipping gates; auto-chaining merge → tag → release; CI babysit loops; force push; pushing new work from `main`; claiming PR/release created when `gh` unavailable; editing CHANGELOG or README pin without confirm; treating publish as ship gate.

**SDD:** maintainer-authored; explicit `@` only — not superpowers auto-release. Contract: `docs/sdd/2026-06-12-sdd-publish-spec.md`. Experimental optional satellite until consumer spot-check in [CHANGELOG](../../CHANGELOG.md).
