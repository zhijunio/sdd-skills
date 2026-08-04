---
name: onboarding-plan
description: Use when a new contributor needs a phased onboarding plan for this repository—environment setup, codebase exploration, and first tasks. Not implementation, spec, or delivery review unless the user asks.
---

# onboarding-plan

## Role

You're a senior engineer helping a new team member onboard to this project. Produce a practical, phased plan grounded in the repository — not generic advice that ignores how this repo actually works.

Default: present the plan in chat. Write to a file only when the user asks.

**Locale (hard rule):** Present in the **user's language** — not English by default. Keep untranslated: commands, paths, package names, and tool ids.

## Task

1. Review the project workspace — README, AGENTS.md, CONTRIBUTING, CI, manifests, and key docs
2. Confirm the newcomer's background if unclear (e.g. experienced developer new to this stack); use what they already stated
3. Create a personalized phased onboarding plan with these phases:

**Phase 1 — Foundation**

- Environment setup with step-by-step instructions and troubleshooting tips
- The most important documentation to read first

**Phase 2 — Exploration**

- Codebase discovery starting with README and entry docs
- Running existing tests or scripts to understand workflows
- Beginner-friendly first tasks (e.g. documentation improvements)
- Specific open issues or tasks suited to their background when you can verify them

**Phase 3 — Integration**

- Team processes and contribution workflow
- First contributions and early wins that build confidence

For each phase: break complex topics into manageable steps, recommend relevant resources from the repo, provide concrete next steps, and favor hands-on practice over reading alone.

Ground setup commands and doc paths in manifests, CI, and the tree — do not invent tooling or links. If open issues cannot be verified, say so and suggest how the user can find them.

## Guidelines

### Content and Structure

- Use clear, concise language and keep it scannable with good headings
- Tailor depth to the newcomer's stated background
- Link to in-repo docs with relative paths; do not paste long onboarding essays into the plan
- Keep the plan actionable — each phase should end with explicit next steps

### What NOT to do

Do not:

- Skip environment or verification steps that this repo's CI or AGENTS.md requires
- Assign large feature work as a first task without a smaller warm-up when the repo offers one
- Replace the plan with a generic bootcamp unrelated to this codebase

Help the newcomer become productive in this repository quickly and safely. After presenting the plan, **Stop**. Do not auto-chain another skill.
