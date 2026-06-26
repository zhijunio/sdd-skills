# Docs split

How to divide **README.md**, **AGENTS.md**, and optional **CONTRIBUTING.md** in any git repo. [agents.md](https://agents.md/) — agent ops; README — human onboarding.

## Files

| File | Audience | Role |
| --- | --- | --- |
| **README.md** | Humans | Pitch, install, usage, **one canonical item table** (if the repo has one) |
| **AGENTS.md** | Agents & maintainers | Commands, paths, conventions, merge checklist |
| **CLAUDE.md** | Claude Code | **Pointer only** to `AGENTS.md` — no duplicate body |
| **CONTRIBUTING.md** | Human contributors | **Optional** — see [When to add](#when-to-add-contributing) |
| **docs/** | Maintainers | Design rationale — not default contributor how-to |

## Division

| Content | README | AGENTS | CONTRIBUTING |
| --- | --- | --- | --- |
| Pitch & long principles | · | link | — |
| Badges (CI, license, version) | ○ | — | — |
| Install / quick start | · (or link hub) | link or — | — |
| Prerequisites (JDK, runtime, wrapper) | ○ | — | — |
| Item table / workflow diagrams | · | — | — |
| Documentation hub links + JavaDoc / release notes | ○ table + sub-lists | link | — |
| Getting Help (issues, discussions) | ○ links | — | ○ |
| Table of contents | ○ long README only | — | — |
| Directory map | ○ brief | · | — |
| Commands (build/test/lint) | ○ pointer | · | link AGENTS |
| How to change key repo files | — | · under **Maintainer** | — |
| Merge checklist | ○ link | · | — |
| Commit / PR | ○ one line | · canonical | ○ human tone |
| Cursor `.mdc` bodies | — | link | — |
| Design essays | link | link | — |
| Code of conduct | — | — | link CoC file |

**Commit/PR:** one canonical copy — default **AGENTS**; CONTRIBUTING links there unless team chooses otherwise.

## CLAUDE.md

Default stub (generate on request):

```markdown
# Claude Code

Repository agent instructions: AGENTS.md (link at repo root).

Do not duplicate content here — edit AGENTS.md only.
```

Large existing `CLAUDE.md` body → converge to pointer; merge unique ops into AGENTS. Same policy for other tool stubs (`GEMINI.md`, …) when present.

## When to add CONTRIBUTING

| Situation | Action |
| --- | --- |
| Small / maintainer-led | Skip — README → AGENTS |
| Open community, CoC, issue templates | Add CONTRIBUTING; AGENTS keeps commands |
| User asks | Draft per readme **Contributing** row |

Do not auto-create CoC unless user asks.

## Dedup (before Present)

1. No duplicated paragraphs across README / AGENTS / CONTRIBUTING — use links.
2. Item tables and install blocks — **README only** unless user moves them.
3. `.cursor/rules/` — AGENTS links; does not copy rule text.

## Existing doc hubs (recon first)

Before drafting, locate **canonical** docs already maintained in the target repo:

| Hub | Typical paths | README role |
| --- | --- | --- |
| User / product docs | `wiki/`, `docs/`, `website/`, `mkdocs.yml` / `docusaurus.config.*`, published GitHub Wiki | **Thin entry** — pitch + **Documentation** links; do **not** copy Features, install blocks, starter matrices, or **metadata tables** from the hub |
| Maintainer / conventions | `docs/*conventions*`, `CONTRIBUTING.md`, `docs/development.md` | README **Contributing** one line → hub; AGENTS **Maintainer** / **Style** / **Testing** → link, do not paste tables |
| Design | `docs/design/`, `adr/` | Link only |

If a hub already covers onboarding, root README adds only: title, **badges** (when recon supports — [badges.md](badges.md)), **Packages** / item table (if missing from hub), **Documentation** hub links (table or bullets), license, changelog link, and pointers.

When recon finds a **wiki publish workflow** (e.g. `.github/workflows/publish-wiki.yml`), one line in **Documentation** may note sync to GitHub Wiki — cite the workflow trigger from recon.

**Documentation** may add optional sub-sections (links only, no pasted API docs):

| Sub-section | When |
| --- | --- |
| **JavaDoc** / API index | Recon finds `javadoc.io`, docs.rs, typedoc, Sphinx hosted API, or per-module published API URLs |
| **Release notes** | `release-notes.md` or GitHub Releases is user-facing changelog — link; keep maintainer `CHANGELOG.md` as separate row if both exist |

**Published libraries:** README **Development** may state that consumers need not build from source when registry artifacts exist; clone/build commands belong in **AGENTS** only.

## Doc locale

Draft language follows **target repo** evidence (existing README, wiki, CHANGELOG, conventions) — not the user's chat language alone. Mixed repos: match the file being written (e.g. English README + link to Chinese conventions is OK when recon shows that split). **Label** cross-locale links in link text (e.g. `Implementation rules (中文)`) so readers know before they click.
