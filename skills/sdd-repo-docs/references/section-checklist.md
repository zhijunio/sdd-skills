# AGENTS checklist by repo shape

Pick **one shape** during recon of the **target repo**. **·** = include when applicable; **○** = optional; **—** = skip unless user asks.

README headings: [readme-outline.md](readme-outline.md) (**shape** + **thin/full depth**). File split: [docs-split.md](docs-split.md).

## README depth

| Depth | README | AGENTS |
| --- | --- | --- |
| **Full** (canonical) | [Full library / platform](readme-outline.md#full-library--platform-canonical-readme) — Introduction through License; **Building from Source** → minimal + link AGENTS | **Commands** canonical; README does not duplicate full build matrix |
| **Thin** (hub owns onboarding) | Badges, pitch, Packages, Documentation links — see monorepo / hub rules | Unchanged |

| Section | app / library | collection | monorepo package | docs-only |
| --- | --- | --- | --- | --- |
| Context | · | · | · | · |
| Structure | · | · | · | ○ |
| Commands | · | ○ | · | — |
| Style | · | ○ | · | — |
| Testing | · | — | · | — |
| Commit & PR | · | · | · | ○ |
| Maintainer | ○ | · | ○ | ○ |
| Security | ○ | ○ | ○ | ○ |
| Agent notes | ○ | ○ | ○ | — |
| Related | · | · | · | · |

## app / library

README: optional [badges](badges.md); **full** depth → [full library outline](readme-outline.md#full-library--platform-canonical-readme); **thin** → install/usage links only; AGENTS: **Commands**, **Style**, **Testing** when recon shows them.

## collection

README: optional [badges](badges.md); **one item table**; AGENTS: **Commands** (if any) and **Maintainer**. Do not duplicate install or hub-owned onboarding.

## monorepo (root)

When **`wiki/` or consumer docs** exist: README = title + **badges** (optional) + **Packages** table (if hub lacks reactor map) + **Documentation** links — not Features/Install copied from hub. AGENTS = **Commands** + **Commit & PR** + **Maintainer**; **Style**/**Testing** link to conventions when present.

Snippet shapes: [examples/outline-snippets.md](examples/outline-snippets.md).

## monorepo nested AGENTS

- File in package directory; scope commands to that package.
- Link root README; do not restate monorepo narrative.
- Nearest AGENTS wins ([agents.md](https://agents.md/) convention).

## Long conventions doc present

When recon finds a single maintainer doc (e.g. `docs/*conventions*`, `CONTRIBUTING.md` > ~80 lines):

- **AGENTS:** **Commands** + **Structure** + **Commit & PR** + short **Maintainer** (merge checklist bullets only).
- **Style** / **Testing:** one line + link — do not duplicate tables or § from the conventions doc.
- **Commit & PR:** brief bullets in the **AGENTS file language** are OK when the conventions doc is another locale — add `conventions §N` pointer; do not paste or translate the full §.
- **Context:** link README **and** the primary user hub (e.g. `wiki/Home.md`) when root README is thin.

## docs-only

- Omit Commands / Style / Testing unless a check script exists.
- **Maintainer** — link integrity, doc PR review.
- Doc diff ship check → hand off **`sdd-review`**.
