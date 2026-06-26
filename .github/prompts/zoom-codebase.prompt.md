---
agent: 'agent'
description: 'Map unfamiliar code: modules, callers, and domain vocabulary'
---

I'm new to this part of the codebase and need a high-level map before diving into changes.

Focus area: ${input:scope:What module, feature, or path should the map center on? (e.g., auth/, checkout flow, src/api/)}
Goal (optional): ${input:goal:What do you want to do next? (e.g., fix a bug, add a feature, review a PR)}

Please provide in this order:

* **Territory** — what this area is for, boundaries, and how it fits the wider project
* **Map** — relevant modules, packages, or layers and who calls whom (dependencies and call direction)
* **Diagram** — when three or more units interact, add a Mermaid flowchart/graph or ASCII sketch showing relationships
* **Glossary & gaps** — domain terms used in code and docs; note ambiguous or missing definitions
* **Suggested next** — one concrete next step (e.g., read specific files, trace one entry point, run a test)

Explain relationships in plain language; keep module paths, artifact names, and project terms literal. Use the project's existing naming and vocabulary. Prefer roles and relationships over a raw directory tree.

Do **not** treat this as a code review, security audit, or refactor report — stay at the map-and-orient layer. Do not write specs, plans, or product code in this session.
