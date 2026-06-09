# Repository Guidelines

- Keep the repository platform-neutral. Do not add commands, hooks, agent personas, or platform-specific manifests.
- Keep every skill self-contained under `skills/<name>/`.
- Keep `SKILL.md` concise. The frontmatter description must describe triggering conditions, not summarize the workflow.
- Do not add runtime state files or status fields without evidence from real usage.
- Update `SOURCES.md` when upstream-derived behavior changes.
- Run `python3 tests/check.py` after modifying skills or templates.
- Preserve third-party notices.

## Git commits

- **When:** commit only when the user explicitly asks.
- **Scope:** atomic commits — one logical change per commit; several commits per PR is fine.
- **Format:** follow this repository's commit convention (see **This repository** below, project rules, or team docs). If unspecified, ask before committing.
- **Message (when the project allows a body):** Chinese — problem or need, approach, and optional repro path.
- **Safety:** do not change `git config`; no force-push to `main`/`master`; no `--amend` unless the user explicitly requests it and the commit was not pushed.
- **Do not claim a commit** was made without actually running `git commit`.

## Git workflow

- **Integration branch:** treat `main` or `master` as integration only — do not commit or push day-to-day work there directly.
- **Branch:** create a topic branch from an updated integration branch; use this project's branch naming (team docs or **This repository** below).
- **Commit on the branch** (see **Git commits** above).
- **Batch before opening a PR/MR:** one reviewable theme per PR — accumulate related changes on the branch or extend an open PR instead of opening many micro-PRs.
- **Verify before PR:** run this project's required checks or tests (CI, linters, scripts — see **This repository** when present).
- **Merge via PR/MR** into the integration branch after review (or self-review with a recorded diff when solo).
- **Releases:** tag on the integration branch only after merge and project release checks, when the project uses tags.

Direct pushes to the integration branch are for one-time baseline sync or emergencies only.

## This repository

Maintainer workflow for **sdd-skills** (platform-neutral **skills** do not prescribe Git hosting elsewhere).

- **Commit prefixes:** `feat:`, `fix:`, `docs:`, `chore:`, `refactor:` — matching branch prefixes `feat/`, `fix/`, `docs/`.
- **Branches:** `feat/<topic>`, `fix/<topic>`, or `docs/<topic>` from updated `main`.
- **Before PR:** run `python3 tests/check.py` (CI runs the same check on GitHub Actions for PRs to `main`).
- **Releases on `main`:** after merge, use `sdd-ship` checks (`CHANGELOG`, `check.py`); include release notes, watchlist sync, and tag follow-ups in the **same release PR** when possible.

