# AGENTS.md outline

Borrowed from Codex **`init`** + [agents.md](https://agents.md/). Default section scaffold for **any** git repo; **omit** what recon shows irrelevant — list omissions in **Present**.

README scaffold: [readme-outline.md](readme-outline.md). File split: [docs-split.md](docs-split.md).

## Requirements

- Title: **`# Repository Guidelines`** (root) or scoped title for nested files.
- **200–400 words** at repo root unless monorepo index; short bullets, repo-specific paths and commands.
- Evidence from manifests, CI, existing docs — never invent scripts or secret values.
- Headings stay **generic** — no repo-specific product names in section titles (put paths and file names in bullets).

## Sections

Use these **`##` headings** when applicable:

| Heading | Content |
| --- | --- |
| **Context** | One paragraph: what the repo is; link README for onboarding; link **primary user hub** when README is thin |
| **Structure** | Source, tests, config, assets — directory map |
| **Commands** | Build, test, lint, dev server — one line each with cwd |
| **Style** | Formatting, naming, lint — how to run check-only; **link only** if conventions doc owns this |
| **Testing** | Framework, layout, how to run; omit if no tests; **link only** if conventions doc owns this |
| **Commit & PR** | Message style from recent `git log`; PR expectations |
| **Maintainer** | Merge/release checklist; from recon: rules for editing key files (bullets, not a custom heading) |
| **Related** | README, CONTRIBUTING, rules, external docs |
| **Security** *(optional)* | Secrets policy, env var names, unsafe ops |
| **Architecture** *(optional)* | Link ADR / design docs — no essay |
| **Agent notes** *(optional)* | Handoff, read-only paths, tool-specific rules |

Required rows by repo shape: [section-checklist.md](section-checklist.md).

## Adaptation

Add headings when recon shows need. Never paste README install or marketing blocks wholesale.
