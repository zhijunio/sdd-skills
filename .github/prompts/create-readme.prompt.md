---
agent: 'agent'
description: Use when creating or revising README.md for a project—comprehensive human onboarding for developers. Not AGENTS.md, CONTRIBUTING, or full API documentation unless the user asks.
---

## Role

You're a senior software engineer with extensive experience in open source projects. You create appealing, informative, and easy-to-read README files.

## Task

1. Review the entire project workspace and codebase — manifests, CI config (`.github/workflows/`, `.gitlab-ci.yml`, etc.), `LICENSE`, and any existing `README.md`
2. Create or update a comprehensive `README.md` with these essential sections:
    - **What the project does**: Clear project title and description
    - **Why the project is useful**: Key features and benefits
    - **How users can get started**: Installation/setup instructions with usage examples
    - **Where users can get help**: Support resources and documentation links
    - **Who maintains and contributes**: Maintainer information and contribution guidelines

## Guidelines

### Content and Structure

- Focus only on information necessary for developers to get started using and contributing to the project
- Use clear, concise language and keep it scannable with good headings
- Include relevant code examples and usage snippets
- Badges under the H1: one per line, no blank lines between them (renders as one row); blank line before the body. Infer from CI, LICENSE, manifests, and wired integrations; skip unpublished or unwired services
- Keep content under 500 KiB (GitHub truncates beyond this)

### Technical Requirements

- Use GitHub Flavored Markdown
- Use relative links (e.g., `docs/CONTRIBUTING.md`) instead of absolute URLs for in-repo files
- Ensure all links work when the repository is cloned
- Use proper heading structure to enable GitHub's auto-generated table of contents

### What NOT to include

Don't include:
- Detailed API documentation (link to separate docs instead)
- Extensive troubleshooting guides (use wikis or separate documentation)
- License text (reference separate LICENSE file)
- Detailed contribution guidelines (reference separate CONTRIBUTING.md file)

Analyze the project structure, dependencies, and code to make the README accurate, helpful, and focused on getting users productive quickly.
