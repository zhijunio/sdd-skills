---
name: sdd-grill
description: Use when goals, boundaries, or trade-offs need decisions before spec or plan, or the user says "grill me".
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

**Skip:** boundaries explicit → invoke `sdd-spec`.

**Stop:** Shared understanding — present `Decisions:` / `Rejected:` / `Boundaries:` / `Open:` (one line each), then hand off. Default `sdd-spec`; `sdd-plan` only when an approved spec exists and subject is plan/slices.

**Red flags:** writing or editing spec, plan, design docs, or product code in-session; asking what the repo can answer.
