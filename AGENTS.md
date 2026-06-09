# Repository Guidelines

- Keep the repository platform-neutral. Do not add commands, hooks, agent personas, or platform-specific manifests.
- Keep every skill self-contained under `skills/<name>/`.
- Keep `SKILL.md` concise. The frontmatter description must describe triggering conditions, not summarize the workflow.
- Do not add runtime state files or status fields without evidence from real usage.
- Update `SOURCES.md` when upstream-derived behavior changes.
- Run `python3 tests/check.py` after modifying skills or templates.
- Preserve third-party notices.
- **Maintainers:** `feat:`/`fix:`/`docs:`/`chore:`/`refactor:` commits; `feat/`/`fix/`/`docs/<topic>` branches from `main`; run `check.py` before PR; release on `main` via `sdd-ship` (`CHANGELOG`, `check.py`), batch release notes/watchlist/tags in one PR when possible.

## Git commits

- Commit **only when the user asks**; run `git commit` before claiming a commit was made.
- **Atomic commits** — one logical change each; several per PR is fine.
- **Format:** follow project rules or team docs; ask if unspecified.
- **Body (when allowed):** Chinese — problem/need, approach, optional repro.
- **Safety:** no `git config` changes; no force-push to `main`/`master`; no `--amend` unless the user asks and the commit was not pushed.

## Git workflow

- Use `main`/`master` as integration only — branch for day-to-day work; emergency/baseline sync may push directly.
- Topic branch from updated integration branch; commit per **Git commits** above.
- One reviewable theme per PR/MR; extend an open PR instead of many micro-PRs.
- Run project checks before PR; merge via PR/MR; tag after merge when the project uses releases.
