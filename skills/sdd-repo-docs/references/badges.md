# README badges

Optional **shields** under the `# Title`, **before** the one-line pitch. **AGENTS.md** never includes badges.

## When to include

| Evidence in recon | Include? |
| --- | --- |
| `.github/workflows/*.yml` with CI on `main` / PR | **CI badge** for primary workflow |
| GitLab CI (`.gitlab-ci.yml`) on default branch | GitLab pipeline badge ○ — use project path from remote |
| `LICENSE` file | **License badge** (GitHub or SPDX shields) |
| Published version on registry (Maven Central, npm, PyPI, crates.io, RubyGems, …) | **Registry version badge** — only if index/API confirms release; never SNAPSHOT |
| CI uploads coverage (Codecov, Coveralls, …) and project exists on service | **Coverage badge** — note may show *unknown* until first upload |
| Third-party doc index (DeepWiki, Zread, …) already linked in README or docs | That service's badge ○ — link to the same URL; do not add without an existing project entry |
| `renovate.json` / Renovate bot active | Renovate badge ○ |
| Existing README already uses badges | Preserve style; update broken links |
| None of the above | **Skip** — do not add decorative badges |

Never badge **SNAPSHOT** / unreleased versions unless user explicitly asks.

## Placement

```markdown
# Project Name

[![CI](https://github.com/ORG/REPO/actions/workflows/WORKFLOW.yml/badge.svg)](https://github.com/ORG/REPO/actions/workflows/WORKFLOW.yml)
[![License](https://img.shields.io/github/license/ORG/REPO)](LICENSE)

One-line project purpose…
```

- One row of badges; wrap long rows to two lines max (~5 badges).
- Each badge **links** to the resource it represents (Actions, LICENSE, registry page, issues).
- Use **ORG/REPO** (or GitLab `group/project`) from `git remote` — do not guess. Non-GitHub hosts: CI/registry badge only when recon confirms URL pattern; otherwise skip.

## Common patterns (adapt from recon)

| Kind | Template (replace ORG, REPO, WORKFLOW) |
| --- | --- |
| GitHub Actions | `https://github.com/ORG/REPO/actions/workflows/WORKFLOW.yml/badge.svg` |
| License | `https://img.shields.io/github/license/ORG/REPO` → link `LICENSE` |
| Maven Central | `https://img.shields.io/maven-central/v/GROUP/ARTIFACT` — verify artifact exists |
| npm | `https://img.shields.io/npm/v/PACKAGE` |
| PyPI | `https://img.shields.io/pypi/v/PACKAGE` |
| crates.io | `https://img.shields.io/crates/v/CRATE` |
| Static stack label | `https://img.shields.io/badge/STACK-VERSION-color?logo=…` — only when version pinned in manifest |
| Codecov | `https://codecov.io/gh/ORG/REPO/branch/main/graph/badge.svg` → app.codecov.io |
| DeepWiki (example) | `https://deepwiki.com/badge.svg` → project page on that service |
| Issues | `https://img.shields.io/github/issues/ORG/REPO` ○ |

## Dedup

- License appears in badge **and** `## License` section — OK.
- Do not duplicate CI/version in a metadata table **and** badges unless the table adds facts badges lack (e.g. Java matrix). When hub owns the metadata table, **omit** it from thin README.

## Hub repos

When README is **thin** (wiki hub owns Features/Install), badges on root README are still OK — they summarize repo health at a glance.
