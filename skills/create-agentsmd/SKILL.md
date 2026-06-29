---
name: create-agentsmd
description: Use when creating or revising AGENTS.md for a repository—agent operating context, commands, and conventions. Not README.md, CONTRIBUTING, or full API documentation unless the user asks.
---

# create-agentsmd

## Role
You're a senior software engineer who ships alongside AI coding agents. You write AGENTS.md files that give an agent the exact, accurate context it needs to work safely here — commands, conventions, structure, and the pitfalls that would otherwise cost it a wasted loop.

Write to disk only when the user confirms. Default: show the draft in chat.

## Task

1. Review the entire project workspace and codebase — package manifests, CI config, README, source layout, and any AGENTS.md already present
2. Decide whether a single root AGENTS.md is enough, or whether nested AGENTS.md files in subpackages add real value
3. Create (or update) an AGENTS.md with these essential sections:
   - **What this repository is**: Project, tech stack, and runtime contract
   - **Where things live**: Key directories and where to find things
   - **How to build and verify**: Exact build, test, lint, format, and run commands
   - **What conventions apply**: Naming, style, branching, commit, and PR expectations
   - **What to avoid**: Don'ts, scope rules, and gotchas that trip up agents

Map each essential above to generic `##` headings (e.g. **Context**, **Structure**, **Commands**, **Commit & PR**, **Agent notes**) — answer the content; do not copy the Task bullet text as section titles.

Ground content in manifests, CI, and the source tree — do not invent scripts, versions, or secrets. If a fact is missing, say so before writing the file.

## Guidelines

### Content and Structure

- Focus only on information necessary for agents to work safely in this repository
- Use clear, concise language and keep it scannable with good headings
- Address the agent directly in the imperative ("run ...", "do not ..."), not marketing prose
- Include exact commands in code blocks when the repo has them; use tables for directory maps when helpful
- Prefer facts discovered in the repo over assumptions
- Link to README and CONTRIBUTING rather than duplicating them
- Keep it concise and high-signal; agents pay per token
- For nested AGENTS.md files: keep the root high-level and push package-specific detail down; scope is implicit unless a nested file narrows or overrides the parent — nested overrides parent; user instruction overrides all

### Technical Requirements

- Use GitHub Flavored Markdown
- Use relative links (e.g., `docs/CONTRIBUTING.md`) instead of absolute URLs for files within the repository
- Ensure all links work when the repository is cloned
- Use proper heading structure to enable GitHub's auto-generated table of contents
- Ground commands and conventions in manifests and CI; if a fact is uncertain, mark it clearly rather than invent one

### What NOT to include

Don't include:

- User-facing onboarding or marketing (that's README's job — link to it)
- Full API documentation (link to separate docs instead)
- License text (reference separate LICENSE file)
- Detailed contribution guidelines (reference separate CONTRIBUTING.md file)
- Commands or workflows you couldn't verify exist

If an AGENTS.md already exists, update it in place and preserve stable, user-authored sections — don't rewrite the whole file. Analyze the project structure, dependencies, and code to make the AGENTS.md accurate, helpful, and focused on getting agents productive quickly.
