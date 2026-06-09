# sdd-architect Optional Satellite Skill

## Goal

Consumers can run an optional **`sdd-architect`** satellite that surfaces architecture deepening opportunities in a codebase conversation without entering the core seven-stage delivery loop or replacing `sdd-review`.

## Scope

- Add `skills/sdd-architect/SKILL.md` as an **optional satellite** skill (eighth published skill).
- Update `using-sdd` with satellite routing when the user wants deepening, shallow modules, seam friction, or mud-ball architecture review.
- Update `README.md`, `SOURCES.md`, and `tests/check.py` so the new skill is installable and validated.
- Record the decision in `docs/design/project-decisions.md` and `CHANGELOG.md` `[Unreleased]`.
- Keep the core loop unchanged: `using-sdd → (optional sdd-grill) → sdd-spec → sdd-plan → sdd-build → sdd-review → sdd-ship`.

## Non-goals

- HTML reports, Mermaid diagrams, or OS temp-file deliverables.
- Mandatory subagents, platform hooks, or plugin manifests.
- Required `CONTEXT.md` or `docs/adr/` in consumer repos.
- Inline creation or mutation of CONTEXT, ADR, spec, plan, or product code inside `sdd-architect`.
- Replacing or merging with `sdd-review`, `sdd-grill`, or Matt's full `improve-codebase-architecture` skill.
- A durable on-disk deepen artifact by default (conversation deliverable only).
- **`v0.2.0` tag** in this increment — tag waits for a third consumer loop with deepening evidence.

## Current Context

- Repository ships **seven** core SDD skills at **`v0.1.1`**; platform-neutral Markdown skills under `skills/<name>/`.
- `sdd-review` already covers **Architecture** as a conditional dimension on a **scoped diff**; it does not scan whole-codebase deepening opportunities.
- Grill consensus (2026-06-09) adapted ideas from Matt's `improve-codebase-architecture` as a **lightweight satellite**.
- `CONTEXT/ADR` workflow remains **proposed**; consumer repos may omit domain docs.
- Version gate: new skills merge to `main` first; minor tag only after consumer friction evidence.

## Requirements

1. **`sdd-architect`** must describe when to use and skip the skill, and must stop after a conversation deliverable without auto-invoking the next skill.
2. The skill must use **depth**, **seam**, **shallow module**, and **deletion test** vocabulary in plain language without requiring bundled HTML or external report tools.
3. The skill may read optional consumer `CONTEXT.md` and `docs/adr/` when present; when absent, it must continue from repository code and existing SDD artifacts only.
4. Each reported candidate must include at minimum: affected area, problem, proposed deepening direction, expected leverage or testability benefit, and recommendation strength (`Strong`, `Worth exploring`, or `Speculative`).
5. After delivery, the skill must recommend **`using-sdd`** as the next step; when the chosen candidate needs a behavior contract, the default recommendation inside that routing must be **`sdd-spec`** unless trade-offs remain open.
6. **`using-sdd`** must list `sdd-architect` under optional satellites with triggers such as deepening, architecture debt, shallow modules, or mud-ball concerns, and must not add it to the mandatory core loop table.
7. **`tests/check.py`** must validate the eighth skill directory and frontmatter like existing skills.
8. Documentation must attribute Matt's skill as inspiration in `SOURCES.md` without copying HTML/subagent requirements.

## Acceptance Criteria

- **AC-1:** When a consumer agent loads `skills/sdd-architect/SKILL.md`, the skill identifies itself as an **optional satellite** and does not claim to be a mandatory delivery stage.
- **AC-2:** When `sdd-architect` completes, the deliverable is a **conversation report** with at least one candidate or an explicit none-found statement; no deepen file is required by default.
- **AC-3:** When optional `CONTEXT.md` or `docs/adr/` exist in a consumer repo, the skill instructions require reading them before proposing candidates; when they do not exist, the skill instructions require proceeding without them.
- **AC-4:** When a candidate contradicts an existing ADR, the skill instructions require marking the conflict and recommending ADR or spec follow-up rather than silently overriding the ADR.
- **AC-5:** When `sdd-architect` stops, it recommends **`using-sdd`** only and states that **`sdd-spec`** is the default next stage when the user selects a candidate that needs acceptance criteria.
- **AC-6:** When `using-sdd` routes for mud-ball or deepening intent, it recommends **`sdd-architect`** without invoking it automatically.
- **AC-7:** When `python3 tests/check.py` runs on this repository, it passes with **eight** skills validated.
- **AC-8:** When a reader opens `README.md` and `SOURCES.md`, they can discover `sdd-architect` as an optional installable skill separate from the core seven-stage loop.

## Constraints

- Keep every skill self-contained under `skills/sdd-architect/`; do not add shared cross-skill fragment files.
- Keep `SKILL.md` concise; put grill-derived rationale in `docs/design/project-decisions.md`, not in the skill body.
- Do not bump the public semver tag in this increment.
- Preserve platform neutrality: no `.cursor-plugin`, hooks, or agent manifests.

## Decisions

- **Chosen:** optional satellite **`sdd-architect`**, conversation-only deliverable, optional CONTEXT/ADR read, stop → `using-sdd` with default **`sdd-spec`** path.
- **Rejected:** external-only pointer to Matt's skill (user chose in-repo skill); full HTML/Matt port; core-loop stage; durable deepen files by default; immediate **`v0.2.0`** tag.

## Open Questions

None.

## Revision log

- 2026-06-09: Approved by user.
- 2026-06-09: Skill renamed **`sdd-deepen`** → **`sdd-architect`** (pre-`v0.2.0`).
