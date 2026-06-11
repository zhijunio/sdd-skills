# sdd-improve Optional Satellite Skill

## Goal

Consumers can run an optional **`sdd-improve`** satellite that performs a read-only, multi-category codebase audit and returns a prioritized conversation findings report — replacing **`sdd-architect`** — without entering the core seven-stage delivery loop, writing `plans/` by default, or replacing **`sdd-review`**.

## Scope

- Add `skills/sdd-improve/` with `SKILL.md` and bundled `references/` (`audit-playbook.md`, `finding-format.md`, `profile-guide.md`).
- Add **`sdd-improve`** alongside **`sdd-architect`** during build; **remove** `skills/sdd-architect/` only after the **user explicitly confirms** migration (breaking rename).
- Update **`using-sdd`**, **`sdd-zoom`**, **`sdd-review`**, **`README.md`**, **`SOURCES.md`**, **`tests/check.py`**, **`CHANGELOG.md`**, and **`docs/design/project-decisions.md`**.
- Keep the core loop unchanged: `using-sdd → (optional sdd-grill) → sdd-spec → sdd-plan → sdd-build → sdd-review → sdd-ship`.
- Attribute **[shadcn/improve](https://github.com/shadcn/improve)** (MIT) and Matt `improve-codebase-architecture` as upstream inspiration in **`SOURCES.md`**.

## Non-goals

- A phase, category, or deliverable block named **Simplify** anywhere in **`sdd-improve`**.
- Default on-disk deliverables (`plans/`, architect reports, HTML, Mermaid diagrams, OS temp files).
- **`execute`**, **`reconcile`**, or isolated worktree dispatch inside **`sdd-improve`** (use **`sdd-build`** after spec/plan, or install **shadcn/improve** separately for plan+execute loops).
- Mandatory subagents, platform hooks, or agent manifests (`.cursor-plugin`, slash commands).
- Required `CONTEXT.md` or `docs/adr/` in consumer repos.
- Inline creation or mutation of CONTEXT, ADR, spec, plan, or product code inside **`sdd-improve`**.
- Replacing **`sdd-grill`** (decision interviews), **`sdd-zoom`** (territory map without findings), or **`sdd-review`** (scoped diff delivery review).
- A public semver tag in this increment — tag waits for consumer friction evidence per repository gate.

## Current Context

- Repository ships **nine** installable skills at **`v0.2.1`**: seven core loop skills plus optional satellites **`sdd-zoom`** and **`sdd-architect`**.
- **`sdd-architect`** (2026-06-09) is a lightweight architecture opportunity scan; conversation-only deliverable; Matt `improve-codebase-architecture` adapted.
- **[shadcn/improve](https://github.com/shadcn/improve)** provides a fuller read-only audit (nine categories, recon, vet, effort levels, `plans/` + `execute`) as a separate single-skill package.
- Grill consensus (2026-06-11): fuse more **improve** rigor into an in-repo SDD satellite while keeping **conversation-only** default output and SDD routing.
- Amendment (2026-06-11): **no Simplify** in audit — over-engineering and duplication are **findings** under **tech-debt & architecture**; optional **Profile** sets effort and scope before **Audit**.
- **`sdd-review`** covers delivery dimensions on a **scoped diff** only — see **Disambiguation** vs **`sdd-improve`** (opportunity scan vs ship gate).
- Platform-neutral skills live under `skills/<name>/`; progressive disclosure via bundled `references/` is allowed within the skill directory.

## Requirements

### Skill identity and boundaries

1. **`sdd-improve`** must identify as an **optional satellite**; not a mandatory stage before **`sdd-ship`**.
2. The skill must be **read-only** on consumer source: no edits, no mutating git commands, no installs that change the working tree. Read-only analysis commands (e.g. `tsc --noEmit`, audit in check mode) are allowed.
3. Secret handling: findings reference **`file:line`** and credential type only; never reproduce secret values.
4. When the user asks for direct implementation, the skill must decline and route to **`sdd-spec`**, **`sdd-plan`**, or **`sdd-build`** (or recommend **shadcn/improve** for plan+execute workflows).

5. **Default deliverable:** a **conversation findings report** — optional Profile, verified findings table, direction section when category 9 ran, considered and rejected. Default **no** on-disk file (same delivery style as **`sdd-architect`**, different content and verdict).

### Disambiguation (normative)

**vs `sdd-review` (delivery review)**

| | **`sdd-improve`** | **`sdd-review`** |
| --- | --- | --- |
| Question | What opportunities or problems exist? | Does **this increment** meet spec/plan and ship? |
| Scope | **Whole repo** or **branch** vs merge-base (+ context in touched areas) | **Current increment diff only** |
| Criteria | Leverage, categories 1–9 | Approved **spec / plan / AC** |
| Verdict | Findings table; user **selects** follow-ups | **pass** / **must-fix** / **should-fix** → **`sdd-ship`** |
| Timing | Exploratory — onboarding, health check, before/without a defined increment | After **`sdd-build`**, before ship |
| Branch | Tags **`introduced`** and **`pre-existing`** in touched files | Judges only defects **introduced or worsened by this diff** |

When the user says **「review」** without a **defined diff** and spec/plan context, **`using-sdd`** must ask: delivery review (**`sdd-review`**) vs codebase health check (**`sdd-improve`**). Do not route ambiguous 「review」to **`sdd-improve`** silently.

**vs `sdd-architect`**

- **`sdd-improve`** supersedes **`sdd-architect`**: category 5 retains architect vocabulary; adds categories 1–4 and 6–8; **conversation findings report** replaces architect **candidates** list.

**vs `sdd-zoom`**

- **`sdd-zoom`**: territory map, no refactor findings. **`sdd-improve`**: findings with evidence — route map-only requests to **`sdd-zoom`**.

### Workflow (improve-derived, SDD-stopped)

**Phase order:** **`Profile` (optional) → `Audit` → `Verify` → `Present` → `Confirm` → `Stop`**

(`Verify` = re-read cited code and drop false positives before findings enter the table — shadcn/improve calls this "vet".)

6. **`Profile` (optional, before Audit):** When effort level is unset or scope is ambiguous, read repository guidance, README, config roots, directory layout, build/test/lint commands, optional `CONTEXT.md` / `docs/adr/`, existing `docs/sdd/*` artifacts, and useful git signal. Output a short **Profile** in the conversation (not required on every run when the user already named effort and focus):
   - project type and size (e.g. skills-only repo, app, library, monorepo)
   - effective **effort level** — infer from natural language (`quick` / `standard` / `deep` internal labels); recommend on small repos and wait for acceptance before downgrading
   - **in-scope categories** and per-category depth (deep / light / skip) with explicit reasons for skips
   - architecture-only intent from natural language (deepen, mud-ball, shallow modules, seams) → scan **category 5** primarily

7. **`Audit` (read-only scan):** Scan **in-scope categories** inferred from the user's request and Profile. All findings use **`file:line`** evidence. **Do not use the name Simplify** for any step, category, or block.

   **Categories (nine total):**

   | # | Category | Notes |
   | --- | --- | --- |
   | 1 | correctness | Bugs, error handling, async hazards |
   | 2 | security | Evidence-based; no secret values |
   | 3 | performance | Algorithmic and architectural wins |
   | 4 | test coverage | Gaps, fragile tests, missing baselines |
   | 5 | **tech-debt & architecture** | **Over-engineering, duplication,** shallow modules, pass-through layers, leaky seams, **deletion test**, depth/seam vocabulary, recommendation strength (`Strong`, `Worth exploring`, `Speculative`) — absorbs legacy **`sdd-architect`** |
   | 6 | dependencies & migrations | Lockfiles, audits, migration drift |
   | 7 | experience & tooling | Local dev friction, scripts, CI ergonomics |
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

9. **Effort levels (internal labels):** **quick**, **standard** (default), **deep** — per the depth table in Constraints.
10. Parallel read-only subagents are **optional** when the host agent supports them; otherwise scan in-scope categories in priority order.
11. **`Verify`:** Re-read cited code for every finding before presenting; downgrade, correct, or reject false positives. Record rejections in **considered and rejected**.
12. **`Present`:** Verified findings table ordered by leverage (impact ÷ effort, weighted by confidence). **Direction** (category 9) appears in a **separate section** after the table (2–4 items max).
13. **`Confirm`:** Ask which findings to pursue. State **dependency ordering** only for **user-selected** findings.
14. **`Stop`:** Recommend **`using-sdd`** only. Default next: **`sdd-spec`** (selected finding needs AC); **`sdd-grill`** (open trade-offs).

### Bundled references

15. `references/profile-guide.md` — optional Profile format, effort recommendations, skip rules, and **natural-language intent → scope** mapping. **No Simplify naming.**
16. `references/audit-playbook.md` — condensed per-category checklist; category 5 includes over-engineering and duplication checks; MIT attribution for **shadcn/improve**.
17. `references/finding-format.md` — table columns and **Verify** rules.
18. **`SKILL.md`** — concise **Disambiguation** vs **`sdd-review`** (per normative table above); ≤90 lines total.

### Repository integration

19. **`using-sdd`** routes **only `sdd-improve`** for audit / improve / health-check / whole-repo or branch exploration. Ambiguous **「review」** without a defined diff → **ask** (see Disambiguation). **`sdd-architect`** not in routing matrix during migration.
20. **`sdd-review`** must include matching **Disambiguation** vs **`sdd-improve`**: delivery gate on increment diff only; whole-repo or branch health check → **`sdd-improve`**. **`sdd-zoom`** → **`sdd-improve`** for refactor findings.
21. **`tests/check.py`** validates **`sdd-improve`**; **`sdd-architect`** may coexist until user confirms removal.
22. **`README.md`** lists **`sdd-improve`**; **`sdd-architect`** deprecated until user-confirmed removal.

### Optional durable artifact (explicit user request only)

23. Persist only when asked: `docs/sdd/YYYY-MM-DD-<topic>-improve.md`.
24. **`--issues`:** `gh issue create` only on explicit user request.

## Acceptance Criteria

- **AC-1:** **`sdd-improve`** identifies as an **optional satellite**; not a mandatory delivery stage.
- **AC-2:** Deliverable is a **conversation findings report**: optional **Profile** + verified findings table + **considered and rejected** when applicable. **No Simplify** block or label.
- **AC-3:** No credible findings → explicit **none found** with evidence; no invented churn.
- **AC-4:** When `CONTEXT.md` / `docs/adr/` exist, read during Profile or Audit setup; proceed without them when absent.
- **AC-5:** ADR conflicts marked; recommend ADR or spec follow-up.
- **AC-6:** Stop recommends **`using-sdd`** only; **`sdd-spec`** or **`sdd-grill`** as default next stages.
- **AC-7:** When the user's message implies **branch** scope, findings tag **`introduced`** vs **`pre-existing`**.
- **AC-8:** Deliverable states inferred effort and scope (e.g. quick / standard / deep; categories in scope) — whether from natural language or Profile.
- **AC-16:** Instructions require inferring scope from **natural language**; users are not required to use keyword or slash-command syntax.
- **AC-9:** **`using-sdd`** routes audit/improve/health-check to **`sdd-improve`** only.
- **AC-10:** `python3 tests/check.py` passes after **`sdd-improve`** published (`sdd-architect` may coexist).
- **AC-11:** **`README.md`** and **`SOURCES.md`** document **`sdd-improve`**, **shadcn/improve**, and pending architect rename.
- **AC-12:** No default `plans/` or on-disk report.
- **AC-13:** Skipped categories named in Profile with project-specific reasons.
- **AC-14:** After **user confirms**, **`sdd-architect`** removed; `check.py` still passes.
- **AC-15:** Category 5 findings may cite over-engineering or duplication with **`file:line`** evidence and architect vocabulary where applicable.
- **AC-17:** **`SKILL.md`** includes normative **Disambiguation** vs **`sdd-review`** (question, scope, criteria, verdict, timing, branch tags).
- **AC-18:** **`using-sdd`** asks when the user says review/审查 without a defined diff — delivery **`sdd-review`** vs health-check **`sdd-improve`**.

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

| | `quick` | `standard` (default) | `deep` |
| --- | --- | --- | --- |
| Coverage | Hotspots — highest churn / criticality | Hotspot-weighted, key packages | Whole repo |
| Subagents | 0–1 when supported | ≤4 when supported | ≤8 when supported |
| Categories | correctness, security, tests (~6, HIGH) unless Profile narrows | **1–8** unless Profile skips; **9** only when user asks direction/roadmap | **1–9** incl. LOW investigate unless Profile skips |
| Report | Profile (if any) + state omissions | Profile (if any) + state omissions | Profile (if any) + state omissions |

### SDD skill boundaries

| Skill | Boundary |
| --- | --- |
| **`sdd-zoom`** | Map only — no findings |
| **`sdd-improve`** | Conversation **findings** report; whole repo or **branch** opportunity scan |
| **`sdd-grill`** | Decisions — not audit |
| **`sdd-review`** | **Increment diff** delivery gate — pass / must-fix vs spec·plan |
| **shadcn/improve** | External `plans/` + `execute` |

### Platform and packaging

- Self-contained under `skills/sdd-improve/`; **`SKILL.md`** ≤90 lines; details in `references/`.
- Platform-neutral; third-party notices for adapted **shadcn/improve** content.

## Decisions

- **Chosen:** **Conversation findings report**; **Disambiguation** vs **`sdd-review`** (opportunity scan vs delivery gate); natural-language inference; no Simplify; **standard = 1–8**; whole repo **or** branch scope; user-confirmed architect removal.
- **Rejected:** Using **`sdd-improve`** as ship gate; silent routing of ambiguous 「review」; Simplify naming; **sdd-architect** in routing; full **shadcn/improve** execute port.

## Related ADRs

None.

## Open Questions

None.

## Revision log

- 2026-06-11: Drafted; approved; amended (Verify, architect removal gate).
- 2026-06-11: Amended — **remove all Simplify**; optional **Profile**; over-engineering/duplication in **category 5**; **standard default categories 1–8**; `profile-guide.md`; AC-15.
- 2026-06-11: Amended — category 7 renamed **DX** → **experience & tooling**.
- 2026-06-11: Amended — **natural-language scope inference**; keywords internal only; v1/later table; AC-16.
- 2026-06-11: Amended — **Disambiguation** vs **`sdd-review`**; conversation findings report; AC-17/AC-18; **`using-sdd`** ask on ambiguous review.
- 2026-06-11: Plan approved; Slice 1–3 implemented (`skills/sdd-improve/`; routing; docs). Slice 4 awaits user-confirmed architect removal.
- 2026-06-11: Slice 4 — **`skills/sdd-architect/`** removed (AC-14); user-confirmed migration.
