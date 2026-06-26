# Vet checklist (before Present)

Run after draft, before **Present**. Fail any item → revise draft or note exception in **Omitted sections**.

## Recon recorded

- [ ] **Shape** chosen (app/library · collection · monorepo · docs-only)
- [ ] **README depth** chosen (**thin** vs **full** — [readme-outline.md § README depth](readme-outline.md#readme-depth))
- [ ] **Doc locale** noted (from existing README / wiki / CHANGELOG / conventions)
- [ ] **Doc hubs** listed (see [Hub map](#hub-map) below)
- [ ] **Badges** — included which shields (or skipped + why) — [badges.md](badges.md)
- [ ] **Optional README sections** — Prerequisites, Getting Help, JavaDoc sub-list, TOC: included or skipped + why

## Hub map (required in Present)

| Hub | Path | Canonical for | New README / AGENTS |
| --- | --- | --- | --- |
| User / product | e.g. `wiki/Home.md` | Features, quick start, starter matrix | Link only — no copied bullets or XML |
| Conventions | e.g. `docs/rose-conventions.md` | Module rules, Style, Testing tables | AGENTS link; no duplicated § |
| Design | e.g. `docs/design/` | Architecture essays | Link only |
| *(none)* | — | — | Draft carries full onboarding |

## Dedup

- [ ] No install block in README **and** AGENTS
- [ ] No item/package table in both README and AGENTS
- [ ] No Features / quick-start paragraph copied from an existing hub
- [ ] No **metadata / coordinates table** (Group ID, BOM, license row, Java matrix) copied from hub when hub already has it — pitch + badges suffice
- [ ] **README depth** matches hubs — **full** at root only when no user hub owns onboarding (or nested scope); **thin** when hub exists
- [ ] **Style** / **Testing** in AGENTS are links only when a long conventions doc exists (> ~80 lines or has its own test/build §)
- [ ] **Commit & PR** canonical in one place (default AGENTS)

## Evidence

- [ ] Every command appears in CI, `package.json` scripts, Makefile, or existing docs — else **`TBD — confirm with user`**
- [ ] Commit message style matches recent `git log` on target repo
- [ ] No invented paths, scripts, or secret values
- [ ] **Badges:** each URL uses recon **ORG/REPO/workflow/registry** — no guessed versions; no SNAPSHOT version badge unless user asked — [badges.md](badges.md)

## Length & headings

- [ ] AGENTS root draft ~200–400 words (monorepo index may exceed)
- [ ] Section titles match [readme-outline.md](readme-outline.md) / [codex-init-outline.md](codex-init-outline.md) — generic headings, repo facts in bullets
- [ ] **README authoring** — [readme-authoring.md](readme-authoring.md): in-repo **relative** links; no LICENSE full text; no API/troubleshooting essays; &lt; ~500 KiB

## Nested scope

- [ ] Nested `AGENTS.md` scoped to subtree only; links root README
