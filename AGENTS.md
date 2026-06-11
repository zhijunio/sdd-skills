# Repository Guidelines

**Core principles (six, three layers):** shape — minimal & neutral · explicit stages; delivery — verifiable slices · test and prove; governance — borrow don't rebuild · no empty ceremony. See [README — Core principles](README.md#core-principles) and [engineering-rationale §1.0](docs/design/engineering-rationale.md#10-核心原则).

- Keep the repository platform-neutral. Do not add commands, hooks, agent personas, or platform-specific manifests.
- Keep every skill self-contained under `skills/<name>/`.
- Keep `SKILL.md` concise. The frontmatter description must describe triggering conditions, not summarize the workflow.
- Skills with upstream pins: keep borrowed prose verbatim @ pin (see `SOURCES.md`); minimal **SDD:** tail for routing/throws. No fixed section template — short like upstream.
- No central routing doc — user **`@`** stage skills. At **Stop**, hand off to next stage skill; no in-session next-stage work.
- Do not add runtime state files or status fields without evidence from real usage.
- Update `SOURCES.md` when upstream-derived behavior changes.
- Preserve third-party notices.
