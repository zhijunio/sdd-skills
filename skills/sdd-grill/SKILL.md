---
name: sdd-grill
description: Use when a software change has unclear goals, boundaries, or trade-offs before specification, when the user wants to stress-test a plan or design, or mentions "grill me". Works within SDD or standalone.
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

Resolve blocking decisions before writing or revising spec or plan. Subject may be file, pasted summary, or conversation — disk artifact not required. SDD or standalone. **Skip** when boundaries explicit → `sdd-spec`.

Read repository guidance; explore code/docs before asking user.

**Explore** (directions still open — brainstorming / idea-refine): check project state; one question at a time; 2–3 approaches with trade-offs; lead with recommendation; converge on direction + boundaries; record rejected approaches.

**Interview** (vague intent — interview-me): `Q:` + `GUESS:` per turn; stop at ~95% confidence you could write observable AC without guessing.

**Challenge** (plan/design on table — grill-me): interview every aspect until shared understanding; resolve dependent decisions one-by-one.

Both phases may appear in one session — explore first when open, challenge when stable enough to stress-test.

**Red flags:** asking what repo can answer; implementation detail before goal stable; mandatory before every spec/plan; writing/editing spec, plan, design docs, or product code.

**Output:** recommended direction, rationale, rejected alternatives, boundaries, shared understanding, remaining spec/plan questions. Optional `docs/sdd/YYYY-MM-DD-<topic>-clarify.md` only when complex decisions must survive conversation. Throw upstream design-doc / `docs/ideas/` paths.

**SDD:** User's language; layout flexible. Stop after shared understanding — name one next skill (`sdd-spec` or `sdd-plan`); **hand off** — invoke it on continuation, no in-session spec/plan work.
