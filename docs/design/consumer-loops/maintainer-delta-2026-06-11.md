# Maintainer delta — satellite SKILL tails (post–0.3.0 Pass)

Date: 2026-06-11  
Status: **shipped** with **`v0.3.0`** — prose-only satellite refactor; fourth consumer loop evidence unchanged in substance

Parent: [consumer-loops/README.md](./README.md)

## Context

[todo-web-0.3.0.md](./todo-web-0.3.0.md) **Pass** used `sdd-improve` on `main` before these maintainer commits:

- `sdd-grill` — grill-me single source + minimal SDD tail
- `sdd-zoom` — zoom-out single source + minimal SDD tail
- `sdd-improve` — one-line Process + minimal tail; `finding-format.md` minimal skeleton
- Removed `tests/check.py` and GitHub Actions `check` — maintainer verify via this directory + README

## Delta vs loop evidence

| Area | Loop-time shape | Current `skills/` | Consumer impact |
| --- | --- | --- | --- |
| `sdd-improve` workflow | 7-step list in `SKILL.md` | One-line **Process** + compressed `references/` | Required report **content** unchanged; optional layout shorter — [finding-format.md](../../../skills/sdd-improve/references/finding-format.md) |
| `sdd-grill` / `sdd-zoom` | Longer SDD sections | Upstream body + short tail | Routing unchanged; Stop/hand-off clearer |
| Maintainer verify | `tests/check.py` (withdrawn) | Consumer loop + README checklist | Installers unaffected |

## Acceptance (`v0.3.0` tag)

1. **References** for `sdd-improve` / `sdd-review` intact — no category or severity semantic change.
2. **When/Skip** cross-links between improve ↔ review ↔ zoom ↔ grill preserved.
3. **No** restoration of `tests/check.py` — gate remains consumer-loop driven per [README — Maintainer verification](../../../README.md#maintainer-verification).
4. Optional: fifth loop or spot consumer re-install after tag if satellite friction appears in the wild.

## Friction

| ID | Area | Severity | Note |
| --- | --- | --- | --- |
| M1 | evidence | nice | 0.3.0 Pass predates tail compression — covered by this delta doc |
| M2 | verify | nice | No in-repo automated gate — intentional; README checklist added |
