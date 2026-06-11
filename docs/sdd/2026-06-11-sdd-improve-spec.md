# sdd-improve Optional Satellite Skill

## Goal

Consumers can run an optional **`sdd-improve`** satellite that performs a read-only, multi-category codebase audit and returns a prioritized conversation findings report — without entering the core six-stage delivery loop, writing `plans/` by default, or replacing **`sdd-review`**.

## Scope

- Add `skills/sdd-improve/` with `SKILL.md` and bundled `references/` (`audit-dimensions.md`, `finding-format.md`, `profile-guide.md`, `closing-the-loop.md`).
- Update **`sdd-zoom`**, **`sdd-review`**, **`README.md`**, **`SOURCES.md`**, **`tests/check.py`**, **`CHANGELOG.md`**, and **`docs/design/engineering-rationale.md`** (as needed).
- Keep the core loop unchanged: `(optional sdd-grill) → sdd-spec → sdd-plan → sdd-build → sdd-review → sdd-ship`; user **`@`** stage skills — no central routing doc.
- Record upstream playbook attribution in **`SOURCES.md`** / **`THIRD_PARTY_NOTICES.md`** only — **`sdd-improve` skill text does not reference other improve packages**.

## Non-goals

- A phase, category, or deliverable block named **Simplify** anywhere in **`sdd-improve`**.
- Default on-disk deliverables (`plans/`, architect reports, HTML, Mermaid diagrams, OS temp files).
- **`execute`**, **`reconcile`**, **`plans/`** factories, or isolated worktree dispatch inside **`sdd-improve`** (use **`sdd-spec`** → **`sdd-plan`** → **`sdd-build`** after findings).
- Mandatory subagents, platform hooks, or agent manifests (`.cursor-plugin`, slash commands).
- Required `CONTEXT.md` or `docs/adr/` in consumer repos.
- Inline creation or mutation of CONTEXT, ADR, spec, plan, or product code inside **`sdd-improve`**.
- Replacing **`sdd-grill`** (decision interviews), **`sdd-zoom`** (territory map without findings), or **`sdd-review`** (scoped diff delivery review).
- A public semver tag in this increment — tag waits for consumer friction evidence per repository gate.

## Current Context

- Repository ships **eight** installable skills: six core loop skills plus optional satellites **`sdd-improve`** and **`sdd-zoom`**.
- **`sdd-improve`** is a **standalone** SDD satellite — not coupled to any other vendor or community **improve** skill package.
- Grill consensus (2026-06-11): multi-category read-only audit rigor in an in-repo SDD satellite; **conversation-only** default output; SDD stage handoff only.
- Amendment (2026-06-11): **no Simplify** in audit — over-engineering and duplication are **architecture** (category 5) findings; optional **Profile** step merges into report **`## Scope`** before **Audit**.
- **`sdd-review`** covers delivery dimensions on a **scoped diff** only — see **Disambiguation** vs **`sdd-improve`** (opportunity scan vs ship gate).
- Platform-neutral skills live under `skills/<name>/`; progressive disclosure via bundled `references/` is allowed within the skill directory.

## Requirements

### Skill identity and boundaries

1. **`sdd-improve`** must identify as an **optional satellite**; not a mandatory stage before **`sdd-ship`**.
2. The skill must be **read-only** on consumer source: no edits, no mutating git commands, no installs that change the working tree. Read-only analysis commands (e.g. `tsc --noEmit`, audit in check mode) are allowed.
3. Secret handling: findings reference **`file:line`** and credential type only; never reproduce secret values.
4. When the user asks for direct implementation, the skill must decline and route to **`sdd-spec`**, **`sdd-plan`**, or **`sdd-build`** per **`references/closing-the-loop.md`**.

5. **Default deliverable:** a **conversation findings report** — **`## Recon`**, **`## Scope`** (Profile merges here), findings **list** with **Evidence** bullets (not a table), optional **`## Direction`** and **`## Dependency order`**, considered and rejected. Default **no** on-disk file.

### Disambiguation (normative)

**Canonical names:** **opportunity scan** (`sdd-improve`) vs **delivery review** (`sdd-review`). **`sdd-improve`** / **`sdd-review`** `SKILL.md` **When/Skip** cross-link only — no duplicated pairing table elsewhere. Skill text **English only**.

**Heuristic:** PR / plan / AC / ship / merge / deliver → **`sdd-review`**; health check / audit / architecture debt without delivery context → **`sdd-improve`**.

When the user says **"review"** without **increment diff** and delivery context, agent must ask: **`sdd-review`** vs **`sdd-improve`**. Do not pick silently.

**vs `sdd-zoom`**

- **`sdd-zoom`**: territory map, no refactor findings. **`sdd-improve`**: findings with evidence — route map-only requests to **`sdd-zoom`**.

### Workflow (improve-derived, SDD-stopped)

**Phase order:** **`Recon` → `Profile` (optional) → `Audit` → `Verify` → `Present` → `Confirm` → `Stop`**

(`Verify` = re-read cited code and drop false positives before findings are presented.)

6. **`Profile` (optional, before Audit):** When effort level is unset or scope is ambiguous, read repository guidance, README, config roots, directory layout, build/test/lint commands, optional `CONTEXT.md` / `docs/adr/`, existing `docs/sdd/*` artifacts, and useful git signal. Write results into report **`## Scope`** only — **no separate `## Profile` heading** (not required when the user already named effort and focus):
   - project type and size (e.g. skills-only repo, app, library, monorepo)
   - effective **effort level** — infer from natural language (`quick` / `standard` / `deep` internal labels); recommend on small repos and wait for acceptance before downgrading
   - **in-scope categories** and per-category depth (deep / light); skip reasons go in **`## Recon` — Not audited** at Present, not Scope
   - architecture-only intent from natural language (deepen, mud-ball, shallow modules, seams) → scan **architecture** (category 5) primarily

7. **`Audit` (read-only scan):** Scan **in-scope categories** inferred from the user's request and Profile. All findings use **`file:line`** evidence. **Do not use the name Simplify** for any step, category, or block.

   **Categories (nine total):**

   | # | Category | Notes |
   | --- | --- | --- |
   | 1 | correctness | Bugs, error handling, async hazards |
   | 2 | security | Evidence-based; no secret values |
   | 3 | performance | Algorithmic and architectural wins |
   | 4 | test coverage | Gaps, fragile tests, missing baselines |
   | 5 | **architecture** | **Over-engineering, duplication,** shallow modules, pass-through layers, leaky seams, **deletion test**, depth/seam vocabulary, recommendation strength (`Strong`, `Worth exploring`, `Speculative`) |
   | 6 | dependencies & migrations | Lockfiles, audits, migration drift |
   | 7 | **experience** | Local dev friction, scripts, CI ergonomics |
   | 8 | docs | Drift, missing docs, stale README |
   | 9 | direction | Features / where to take the project — evidence-grounded only |

   **Default when unspecified:** categories **1–8** (**standard** effort). Include **direction** (category 9) only when the user asks for roadmap / next-steps / where to take the project.

8. **Natural-language scope inference (required):** Infer effort, categories, and branch scope from the user's message. **Do not require** keywords, slash commands, or `focus` / `quick` / `branch` / `next` syntax from the user. Internal labels below are **agent shorthand** for SKILL authors only.

   | User intent (examples) | Inferred behavior |
   | --- | --- |
   | 体检、全面看看、audit | **standard**, categories 1–8 |
   | 快速扫一眼、时间紧 | **quick** (see effort table) |
   | 仔细、深入、deep dive | **deep** |
   | 只看架构、deepen、泥球、浅模块 | category **5** primarily |
   | 只看安全 / 性能 / … | named category primarily |
   | 这个分支、PR 前、改了什么 | **branch** scope; tag `introduced` / `pre-existing` |
   | 下一步做什么、路线图、direction | include category **9**; trade-offs → **`sdd-grill`** |
   | 没说清 | **standard** 1–8; optional **Profile** |

9. **Effort levels (internal labels):** **quick**, **standard** (default), **deep** — normative table in [profile-guide.md](../../skills/sdd-improve/references/profile-guide.md).
10. Parallel read-only subagents are **optional** when the host agent supports them; otherwise scan in-scope categories in priority order.
11. **`Verify`:** Re-read cited code for every finding before presenting; downgrade, correct, or reject false positives. Record rejections in **considered and rejected**.
12. **`Present`:** **`## Recon`** (Type/Verification/CI/HEAD/Working tree/Hotspots/Not audited); **`## Scope`**; **`## Findings`** as **`### 🔴/🟡/🟢` severity** list blocks (**not a table**): **Evidence** + Impact/Effort/Confidence/Risk emoji grading; **architecture** adds **Strength**. **`## Direction`** when category 9; **`## Dependency order`** when ≥2 follow-ups.
13. **`Confirm`:** Ask which findings to pursue. State **dependency ordering** only for **user-selected** findings.
14. **`Stop`:** Name next per **closing-the-loop**; hand off (default **`sdd-spec`** when AC needed; **`sdd-grill`** when trade-offs open).

### Bundled references

15. `references/profile-guide.md` — optional Profile format, skip rules, **natural-language intent → scope** mapping, and effort table. **No Simplify naming.**
16. `references/audit-dimensions.md` — condensed per-category checklist (pairs with **`sdd-review`** `review-dimensions.md`); category 5 includes over-engineering and duplication checks; upstream attribution in repo **`THIRD_PARTY_NOTICES.md`** only.
17. `references/finding-format.md` — **🔴/🟡/🟢** severity semantics + **Verify** rules; required report **content** (layout flexible per skill); **Report locale** — skill instructions English, report prose follows user language.
18. `references/closing-the-loop.md` — advisor role; SDD follow-through (layout mirrors improve `closing-the-loop.md`); **no cross-reference** to other improve skill packages.
19. **`SKILL.md`** — concise **When/Skip** vs **`sdd-review`** (peer link only; no duplicated table); ≤90 lines total.

### Repository integration

20. Audit / health-check intent → **`sdd-improve`** only. Ambiguous **"review"** without increment diff → **ask** (see Disambiguation).
21. **`sdd-review`** (**delivery review**) includes matching **Disambiguation** vs **`sdd-improve`**: increment diff only; whole-repo or branch **opportunity scan** → **`sdd-improve`**. **`sdd-zoom`** → **`sdd-improve`** for refactor findings.
22. **`tests/check.py`** validates **`sdd-improve`** (eight skills discovered; six core + two satellites).
23. **`README.md`** lists **`sdd-improve`** and install examples.

### Optional durable artifact (explicit user request only)

24. Persist only when asked: `docs/sdd/YYYY-MM-DD-<topic>-improve.md`.
25. **`--issues`:** `gh issue create` only on explicit user request.

## Acceptance Criteria

- **AC-1:** **`sdd-improve`** identifies as an **optional satellite**; not a mandatory delivery stage.
- **AC-2:** Deliverable is a **conversation findings report**: **`## Recon`** + **`## Scope`** + findings **list** with **Evidence** bullets (not a table) + optional **Direction** / **Dependency order** + **considered and rejected** when applicable. **No Simplify** block or label.
- **AC-3:** No credible findings → explicit **none found** with evidence; no invented churn.
- **AC-4:** When `CONTEXT.md` / `docs/adr/` exist, read during Profile or Audit setup; proceed without them when absent.
- **AC-5:** ADR conflicts marked; recommend ADR or spec follow-up.
- **AC-6:** Stop names next per closing-the-loop; hand off; default **`sdd-spec`** or **`sdd-grill`**.
- **AC-7:** When the user's message implies **branch** scope, findings tag **`introduced`** vs **`pre-existing`**.
- **AC-8:** Deliverable **`## Scope`** states inferred effort and range (e.g. quick / standard / deep; categories in scope) — whether from natural language or Profile step.
- **AC-16:** Instructions require inferring scope from **natural language**; users are not required to use keyword or slash-command syntax.
- **AC-9:** Audit / health-check user intent maps to **`sdd-improve`** only.
- **AC-10:** `python3 tests/check.py` passes with **`sdd-improve`** published (eight skills).
- **AC-11:** **`README.md`** and **`SOURCES.md`** document **`sdd-improve`**.
- **AC-12:** No default `plans/` or on-disk report.
- **AC-13:** Skipped categories and audit limits named in **`## Recon` — Not audited** with project-specific reasons — not in **`## Scope`**.
- **AC-15:** Category 5 findings may cite over-engineering or duplication with **`file:line`** evidence and depth/seam vocabulary where applicable.
- **AC-17:** **`SKILL.md`** links **When/Skip** vs **`sdd-review`** peer-to-peer only (no duplicated pairing table in skill bodies).
- **AC-18:** Agent asks when user says "review" without increment diff — **`sdd-review`** vs **`sdd-improve`**.

## Constraints

### Scope inference (natural language)

Users describe intent in **natural language**. Agents map intent to internal effort/scope labels — users need not type `quick`, `branch`, `next`, or `focus`.

| Internal label | Inferred when user… |
| --- | --- |
| **standard** | wants a codebase health check / audit (default) |
| **quick** | wants a fast, shallow pass |
| **deep** | wants exhaustive coverage |
| **single category** | names one concern (architecture, security, …) |
| **branch** | asks about this branch / PR / recent changes |
| **direction** | asks roadmap / next steps / where to take the project |

Persist / GitHub issues: only when the user **explicitly** asks to save or file issues.

### v1 vs later (implementation)

| **v1 (this increment)** | **Later** |
| --- | --- |
| Natural-language → **standard** (1–8) | Finer **quick** / **deep** tuning |
| Natural-language → **architecture** (category 5) | Full single-category matrix |
| Optional **Profile** | **`--issues`** automation |
| | **branch** tagging polish |

### Effort levels (internal: `quick` / `standard` / `deep`)

Normative table: **`skills/sdd-improve/SKILL.md` — Process** step 3 (Audit). Summary for spec readers:

| | `quick` | `standard` (default) | `deep` |
| --- | --- | --- | --- |
| Categories | correctness, security, tests (~HIGH) unless narrowed | **1–8**; **9** on direction ask | **1–9** unless in Recon **Not audited** |
| Findings | top ~6, HIGH-confidence | full verified list | full incl. LOW investigate |

### SDD skill boundaries

| Skill | Boundary |
| --- | --- |
| **`sdd-zoom`** | Map only — no findings |
| **`sdd-improve`** | Conversation **findings** report; whole repo or **branch** opportunity scan |
| **`sdd-grill`** | Decisions — not audit |
| **`sdd-review`** | **Increment diff** delivery gate — pass / must-fix vs spec·plan |

### Platform and packaging

- Self-contained under `skills/sdd-improve/`; **`SKILL.md`** ≤90 lines; details in `references/`.
- Platform-neutral; third-party notices for adapted playbook content in **`THIRD_PARTY_NOTICES.md`** — not cited in skill text.

## Decisions

- **Chosen:** **Conversation findings report**; **Disambiguation** vs **`sdd-review`** (opportunity scan vs delivery gate); natural-language inference; no Simplify; **standard = 1–8**; whole repo **or** branch scope.
- **Rejected:** Using **`sdd-improve`** as ship gate; silent pick on ambiguous 「review」; Simplify naming; central routing doc; **`plans/`** / **`execute`** inside **`sdd-improve`**; cross-reference to other improve packages.

## Related ADRs

None.

## Open Questions

None.

## Revision log

- 2026-06-11: Drafted; approved; amended (Verify).
- 2026-06-11: Amended — **remove all Simplify**; optional **Profile**; over-engineering/duplication in **category 5**; **standard default categories 1–8**; `profile-guide.md`; AC-15.
- 2026-06-11: Amended — category 7 renamed **DX** → **experience & tooling**.
- 2026-06-11: Amended — **natural-language scope inference**; keywords internal only; v1/later table; AC-16.
- 2026-06-11: Amended — **Disambiguation** vs **`sdd-review`**; conversation findings report; AC-17/AC-18; ask on ambiguous review.
- 2026-06-11: Plan approved; implemented (`skills/sdd-improve/`; docs).
- 2026-06-11: Unified **机会扫描** / **交付审** naming; heuristic in skill **When/Skip**; outcomes **findings report** / **delivery verdict**.
- 2026-06-11: Report — **Scope** only (Profile merges in); findings **list** not table; categories **architecture** (5), **experience** (7).
- 2026-06-11: `references/closing-the-loop.md` — advisor role; SDD follow-through (mirrors improve file layout; no `execute`/`plans/` port).
- 2026-06-11: `audit-dimensions` — read-only rules (no mutating commands); parallel subagent caps ≤4/≤8 (improve effort table).
- 2026-06-11: **Scope** — in-scope categories only; skips in **Recon — Not audited** (remove Scope **Skipped**).
- 2026-06-11: **Standalone satellite** — `closing-the-loop.md` routes **SDD loop** only.
- 2026-06-11: Skill text **English only**; **opportunity scan** / **delivery review**; Recon **Not audited** (no Scope Skipped).
- 2026-06-11: **Output locale** — each skill **Output**; reports in `finding-format.md` **Report locale** (improve + review). No central routing doc.
- 2026-06-11: Report **content** over shared layout — improve/review need not share markdown skeleton; example blocks optional.
- 2026-06-11: Findings **🔴/🟡/🟢** severity; shared list-block format with **`sdd-review`**; effort table in **`SKILL.md` Process**; **`sdd-review`** drops **Strengths** section.
