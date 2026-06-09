# Repository Guidelines

- Keep the repository platform-neutral. Do not add commands, hooks, agent personas, or platform-specific manifests.
- Keep every skill self-contained under `skills/<name>/`.
- Keep `SKILL.md` concise. The frontmatter description must describe triggering conditions, not summarize the workflow.
- Do not add runtime state files or status fields without evidence from real usage.
- Update `SOURCES.md` when upstream-derived behavior changes.
- Run `python3 tests/check.py` after modifying skills or templates.
- Preserve third-party notices.
- Use atomic commits with Conventional Commits prefix (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`). Commit body and description in Chinese.

## Git workflow (maintainers)

**Do not commit directly to `main`.** This repo treats `main` as the integration branch only.

1. Branch from updated `main`: `feat/<topic>`, `fix/<topic>`, or `docs/<topic>`.
2. Commit on the branch; run `python3 tests/check.py` before opening a PR (CI runs the same check on GitHub Actions for PRs to `main`).
3. Open a PR into `main`; merge after review (or self-review with a recorded diff when solo).
4. Tag releases on `main` only after merge and `sdd-ship` checks (`CHANGELOG`, `check.py`).

Direct pushes to `main` are for one-time baseline sync or emergencies only—not day-to-day skill or doc edits.

Platform-neutral **skills** do not prescribe Git hosting; this section applies to **this repository's maintainer workflow** only.

