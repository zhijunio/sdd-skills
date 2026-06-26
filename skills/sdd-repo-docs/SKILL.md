---
name: sdd-repo-docs
description: Use when creating or revising root README.md and/or AGENTS.md (or nested AGENTS) for any git repo—not other repo instruction files, Cursor .mdc rules, or CONTRIBUTING unless the user asks. Optional satellite; not delivery review or codebase audit.
---

# sdd-repo-docs

**Role:** Read-only **README.md** and **AGENTS.md** author for **any** git repository — human onboarding plus agent/maintainer operating guide.

**Produces (chat only by default):** scope note, dedup table, README and/or AGENTS draft (or section patches), optional `CLAUDE.md` stub, optional write when user confirms.

**Does not produce:** other instruction files in the target repo (skills, rules, specs), CHANGELOG, `.cursor/rules/*.mdc`, or `CONTRIBUTING.md` unless user explicitly asks.

**Present:** Write deliverables in the **target repo's doc language** (from recon: existing README/wiki/CHANGELOG/conventions). When unclear, use the **user's latest turn** — do not default to English. Keep literal: paths, git commands, env var **names**, ids from recon.

## Hard rules

1. **Evidence first** — commands and layout from manifests, CI, tree, existing docs; **`TBD — confirm with user`** when absent. Never invent scripts or secrets.
2. **One truth** — no duplicate item tables, install blocks, or hub-owned prose across README, AGENTS, and existing doc hubs; link per [docs-split.md](references/docs-split.md).
3. **Concise headings** — **full** README depth → [full library / platform](references/readme-outline.md#full-library--platform-canonical-readme) titles; otherwise shape tables in [readme-outline.md](references/readme-outline.md) + [codex-init-outline.md](references/codex-init-outline.md). Draft from **target repo recon**, not bundled examples.
4. **AGENTS length** — target **200–400 words** at repo root unless monorepo index.
5. **AGENTS title** — `# Repository Guidelines` at root (or scoped nested title; localized when **Present** is not English).
6. **CLAUDE.md** — pointer to AGENTS only unless user overrides.
7. **Default read-only** — write disk only after explicit user confirmation.

## Workflow

1. **Recon** — target repo only: tree, manifests, CI, **`git remote`** (for badges), recent `git log`; map **doc hubs**, **doc locale**, and **README depth** (thin vs full — [readme-outline.md § README depth](references/readme-outline.md#readme-depth)); record root vs nested path and files user wants.
2. **Shape** — [readme-outline.md](references/readme-outline.md) (**shape** + **thin/full depth**) + [section-checklist.md](references/section-checklist.md).
3. **Hub map** — table: each existing hub → what stays canonical → what README/AGENTS may add (required in **Present**).
4. **Dedup** — [docs-split.md](references/docs-split.md); thin README when user hub exists.
5. **Draft** — README per [readme-outline.md](references/readme-outline.md) + [readme-authoring.md](references/readme-authoring.md); optional badges per [badges.md](references/badges.md); AGENTS per [codex-init-outline.md](references/codex-init-outline.md); omit inapplicable sections.
6. **Vet** — [vet-checklist.md](references/vet-checklist.md).
7. **Present** — output shape below; **`Suggested next steps` last**.

## Output shape

`Scope` → `Executive summary` (shape + **thin/full depth**) → **`Hub map`** → `Draft` → `README vs AGENTS` → `Omitted sections` (include **badges** when skipped) → **`Suggested next steps` last**

## SDD

Optional **satellite** — not core loop; not mandatory before verify.

**When/Skip:** Single-file typo → edit directly. Cursor glob rules → **`create-rule`** / `.cursor/rules/*.mdc`. Heavy scaffold/validate → [netresearch/agent-rules-skill](https://github.com/netresearch/agent-rules-skill). Increment diff → [`sdd-review`](../sdd-review/SKILL.md). Repo doc health → [`sdd-audit`](../sdd-audit/SKILL.md).

**Stop:** After **Present**; user **`@`** next skill or confirms disk write. Do not auto-chain.

| Intent | Route |
| --- | --- |
| User confirms write | Apply draft(s); **`sdd-review`** on prose diff if shipping |
| CONTRIBUTING / CoC | Draft only when user asked |
| Scoped Cursor rules | **`create-rule`** / `.mdc` |
| Monorepo AGENTS scaffold | **agent-rules** (external) |

## References

[readme-outline.md](references/readme-outline.md) · [readme-authoring.md](references/readme-authoring.md) · [badges.md](references/badges.md) · [docs-split.md](references/docs-split.md) · [codex-init-outline.md](references/codex-init-outline.md) · [section-checklist.md](references/section-checklist.md) · [vet-checklist.md](references/vet-checklist.md) · [examples/outline-snippets.md](references/examples/outline-snippets.md)

**Provenance:** AGENTS sections from Codex `init` + [agents.md](https://agents.md/); README outline maintainer-authored.
