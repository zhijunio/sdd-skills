# Repository Guidelines

- Keep the repository platform-neutral. Do not add commands, hooks, agent personas, or platform-specific manifests.
- Keep every skill self-contained under `skills/<name>/`.
- Keep `SKILL.md` concise. The frontmatter description must describe triggering conditions, not summarize the workflow.
- Do not add runtime state files or status fields without evidence from real usage.
- Update `SOURCES.md` when upstream-derived behavior changes.
- Run `python3 tests/check.py` after modifying skills or templates.
- Preserve third-party notices.
- Use atomic commits with Conventional Commits prefix (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`). Commit body and description in Chinese.

