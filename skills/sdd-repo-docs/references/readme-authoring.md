# README authoring principles

Draft quality rules for **any** target repo. Section order: [readme-outline.md](readme-outline.md) (**shape** + **thin/full depth**). File split: [docs-split.md](docs-split.md).

Adapted from [microsphere-java `create-readme.prompt.md`](https://github.com/microsphere-projects/microsphere-java/blob/main/.github/prompts/create-readme.prompt.md) — principles only; this skill adds recon, hub dedup, and AGENTS split.

## Five questions (draft mental model)

Every README should answer — map to [full library / platform](readme-outline.md#full-library--platform-canonical-readme) or the shape table when **thin**:

| Question | Typical sections |
| --- | --- |
| **What** does it do? | Title, pitch, **Introduction** (full) |
| **Why** is it useful? | **Features** (full) or one-line pitch (thin) |
| **How** to get started? | **Getting Started** / **Install** + minimal usage — **link hub** when thin |
| **Where** to get help? | **Documentation**, **Getting Help** |
| **Who** maintains it? | **Contributing**, **Maintainers** → **AGENTS.md** for checklist detail |

Skip questions already owned by a doc hub — link instead of rewriting.

## Markdown

- **GitHub Flavored Markdown** by default on GitHub-hosted repos.
- **Relative links** for paths inside the repo (`docs/guide.md`, `wiki/Home.md`, `LICENSE`) so links work when cloned — not `https://github.com/ORG/REPO/blob/main/...` for in-repo files.
- External URLs OK for registry, CI, Discussions, third-party docs.
- **`##` / `###` hierarchy** — GitHub may auto-generate a sidebar TOC; manual **Table of contents** only when ~8+ sections and navigation still hard ([readme-outline.md § Length](readme-outline.md#length)).

## Length

- Keep README scannable: headings, tables, short bullets.
- GitHub truncates display around **500 KiB** — do not paste large generated docs or license full text.

## Include when depth allows

- Minimal **copy-paste** install / dependency snippets (evidence from manifests).
- **Usage examples** — small, runnable; long tutorials → user guide / wiki / **Documentation** links.
- **Badges** when recon supports — [badges.md](badges.md).

## Do not include in README

| Avoid | Instead |
| --- | --- |
| Full **API reference** | **Documentation** → JavaDoc / typedoc / `docs/api/` |
| Long **troubleshooting** | Wiki or dedicated doc |
| **LICENSE** full text | `## License` → link `LICENSE` |
| Detailed **contribution** essay | One line → `CONTRIBUTING.md`, conventions, or **AGENTS.md** |
| **Command matrices** for maintainers | **AGENTS.md** **Commands** |
| Hub-owned **Features / quick start** | **Documentation** link — [docs-split.md § Existing doc hubs](docs-split.md#existing-doc-hubs-recon-first) |

## Accuracy

Content from **recon** (tree, manifests, CI, existing docs) — never invent scripts, versions, or secrets. Missing facts → **`TBD — confirm with user`** in **Present**, not in the committed draft unless user confirms write.
