---
name: create-readme
description: Use when creating or revising README.md for a project—comprehensive human onboarding for developers. Not AGENTS.md, CONTRIBUTING, or full API documentation unless the user asks.
---

# create-readme

## Role
You're a senior software engineer with extensive experience in open source projects. You create appealing, informative, and easy-to-read README files.

Stack-agnostic: apply to any language, build system, or monorepo layout. Do not assume a particular ecosystem. This skill is for **human** onboarding — not agent operating contracts ([`create-agentsmd`](../create-agentsmd/SKILL.md)).

## Task

1. Review the project workspace and codebase — manifests, CI config, LICENSE, source layout, and any existing README.md
2. Classify the project shape: library, CLI, app, service, docs-only, skill pack, or mixed. Weight setup, usage, config, deploy, API links, and contribution notes accordingly.
3. Create or update a focused README.md with these essential sections (omit any that do not apply to the shape):
   - **What the project does**: Clear project title and description
   - **Why the project is useful**: Key features and benefits
   - **How users can get started**: Installation/setup instructions with usage examples
   - **Where users can get help**: Support resources and documentation links
   - **Who maintains and contributes**: Maintainer information and contribution guidelines

Ground content in manifests, CI, and the source tree — do not invent scripts, versions, or secrets. If a fact is missing, say so before writing the file.

## Present

**Locale (hard rule):** Write the README draft and any chat Present in the **user's language** for this conversation. Do **not** default to English because this skill’s instructions are English. Keep untranslated: command literals, paths, URLs, badge shields, package names.

**Flow:** Show the full draft in chat first. Write to disk **only** after the user confirms. After write (or if they decline): **Stop** — do not auto-chain into AGENTS.md or other skills.

## Guidelines

### Content and Structure

- Focus only on information necessary for developers to get started using and contributing to the project
- Prefer project-shape-specific sections over a fixed template; omit sections that do not apply
- Use clear, concise language and keep it scannable with good headings
- Include relevant code examples and usage snippets
- Badges under the H1: one per line, no blank lines between them (renders as one row); blank line before the body. Infer from CI, LICENSE, manifests, and wired integrations; skip unpublished or unwired services
- Keep content under 500 KiB; GitHub truncates larger README files
- Product “why / features” copy is appropriate here (unlike AGENTS.md) — keep it accurate, not marketing fluff

### Revising an existing README (P3)

- You **may** rearrange sections to match the project shape (library vs app vs service, etc.).
- **Preserve** verified facts and distinctive user-authored voice/branding unless wrong or obsolete.
- Do not replace a solid human README with a generic template face.

### Inventories

- For exhaustive package/module/workspace lists, point at the manifest of record — do not hand-copy a full inventory that will rot.
- Short “key modules / packages” examples are fine if labeled as examples and consistent with the manifest.

### Setup and verify commands

- State **primary** getting-started commands (what a new contributor should run first).
- When the repo supports scoped verify (package filters, workspace targets, etc.), document **also OK** alternatives — do not imply a single path is the only legal one without evidence.
- Every command, badge, version, and external service link must be evidenced in the repo or clearly marked uncertain.

### Architecture and deploy claims

- Architecture diagrams and “how it is deployed” statements need support from the tree, README-already-agreed facts, or ops docs in-repo.
- If evidence is weak, downgrade to a short factual summary or omit — do not invent microservices, clouds, or pipelines.
- Simplified dependency / topology diagrams are allowed when labeled as **illustrative** (not a deployment contract).

### External URLs and ops entrypoints

- Product/env/CI URLs may be kept when carried forward from an existing README or in-repo ops docs.
- Mark them as **from existing docs / ops convention** when the clone itself does not re-verify them (no live check required).

### Cross-link AGENTS.md

- If `AGENTS.md` exists (or will), link it from the README for agent operating rules; keep human onboarding here, agent contracts there.

### Technical Requirements

- Use GitHub Flavored Markdown
- Use relative links (e.g., `docs/CONTRIBUTING.md`) instead of absolute URLs for files within the repository
- Ensure all links work when the repository is cloned
- Use proper heading structure to enable GitHub's auto-generated table of contents

### What NOT to include

Don't include:

- Detailed API documentation (link to separate docs instead)
- Extensive troubleshooting guides (use wikis or separate documentation)
- License text (reference separate LICENSE file)
- Detailed contribution guidelines (reference separate CONTRIBUTING.md file)
- Unverified commands, badges, versions, or service links
- Agent-only operating rules that belong in AGENTS.md (link to AGENTS.md if present)
- Stack-specific assumptions not evidenced in this repo

Analyze the project structure, dependencies, and code to make the README accurate, helpful, and focused on getting users productive quickly.
