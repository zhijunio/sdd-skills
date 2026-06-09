# Repository Guidelines

- Keep the repository platform-neutral. Do not add commands, hooks, agent personas, or platform-specific manifests.
- Keep every skill self-contained under `skills/<name>/`.
- Keep `SKILL.md` concise. The frontmatter description must describe triggering conditions, not summarize the workflow.
- Do not add runtime state files or status fields without evidence from real usage.
- Update `SOURCES.md` when upstream-derived behavior changes.
- Run `python3 tests/check.py` after modifying skills or templates.
- Preserve third-party notices.

## Git commits

- Commit **only when the user asks**; run `git commit` before claiming a commit was made.
- **Atomic commits** — one logical change each; several per PR is fine.
- **Format:** `feat:`, `fix:`, `docs:`, `chore:`, `refactor:` — or project/team convention; ask if unspecified.
- **Body (when allowed):** Chinese — problem/need, approach, optional repro.
- **Safety:** no `git config` changes; no force-push to `main`/`master`; no `--amend` unless the user asks and the commit was not pushed.

## Git workflow

- Use `main`/`master` as integration only — branch for day-to-day work; emergency/baseline sync may push directly.
- Topic branch from updated `main`: `feat/<topic>`, `fix/<topic>`, or `docs/<topic>` (or project naming); commit per **Git commits** above.
- One reviewable theme per PR/MR; extend an open PR instead of many micro-PRs.
- **Release on `main`:** after merge, update `CHANGELOG.md` for user-visible changes; batch release notes, watchlist sync, and tags in one release PR when possible.
