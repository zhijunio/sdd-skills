---
name: sdd-improve
description: Use when the user wants a read-only codebase audit or health check—correctness, security, architecture debt, tests, or branch exploration—outside the delivery loop. Optional satellite; not delivery review of a scoped diff.
---

# SDD Improve

## Goal

Run a read-only multi-category audit and deliver a **conversation findings report** — prioritized verified findings with evidence. **Advisor, not implementer:** judge and specify follow-ups; execution belongs in the SDD loop or external **shadcn/improve** — see [handoff.md](references/handoff.md).

## When to Use

Use when the user asks for a codebase audit, health check, improve pass, or architecture/debt scan across the repo or current branch.

Skip when the task is **交付审** (delivery review) of an **increment diff** with spec/plan compliance — use `sdd-review`.

Skip when the user only needs a **territory map** without findings — use `sdd-zoom`.

Skip when goals or trade-offs are still open — use `sdd-grill`.

Skip when the user asks for **direct implementation** — decline; route per [handoff.md](references/handoff.md) (**`sdd-spec`** / **`sdd-build`** or external **shadcn/improve** for `plans/` + `execute`).

This is an **optional satellite**. Not mandatory before `sdd-ship`.

### Disambiguation vs **交付审** `sdd-review`

**机会扫描** (this skill) vs **交付审** — normative table in [using-sdd — Disambiguation](../using-sdd/SKILL.md#disambiguation).

| | **机会扫描** `sdd-improve` | **交付审** `sdd-review` |
| --- | --- | --- |
| Outcome | **Findings report** | **Delivery verdict** (pass / must-fix / should-fix) |
| Scope | Whole repo or branch vs merge-base | Increment diff only |

Report structure: [finding-format.md](references/finding-format.md).

## Prerequisites

Read repository guidance, README, and optional `CONTEXT.md`, `docs/adr/`, `docs/sdd/*` when present. Infer scope from **natural language**. **Read-only audit:** no installs, commits, formatters, or mutating builds on the user's tree — see [audit-playbook.md — Read-only rules](references/audit-playbook.md#read-only-rules).

## Process

**Recon → Profile (optional) → Audit → Verify → Present → Confirm → Stop**

1. **Recon** — always: README/AGENTS, verify command, CI, `HEAD`, working tree, churn hotspots; write **`## Recon`** (类型/验证/CI/HEAD/工作区/活跃区/未审). See [finding-format.md](references/finding-format.md).
2. **Profile** (optional) — when effort or scope is ambiguous; merges into **`## Scope`** only (no Profile heading). See [profile-guide.md](references/profile-guide.md).
3. **Audit** — read-only (default **standard**: categories **1–8**); optional parallel subagents **≤4** / **≤8** (`deep`). **Never** Simplify. See [audit-playbook.md](references/audit-playbook.md).
4. **Verify** — re-read cited code; reject false positives → **considered and rejected**. ADR conflicts: mark and recommend follow-up.
5. **Present** — **`## Recon`**, **`## Scope`**, **`###` findings** (emoji leverage + **Evidence** bullet + Impact/Effort/Confidence/Risk; architecture **Strength**), optional **`## Direction`**, **`## Dependency order`** when ≥2 follow-ups. Not a table. See [finding-format.md](references/finding-format.md).
6. **Confirm** — ask which findings to pursue; restate **dependency order** for selections.
7. **Stop** — one routing recommendation via **`using-sdd`** only (SDD loop vs external improve — [handoff.md](references/handoff.md)); default **`sdd-spec`** or **`sdd-grill`**.

Branch scope: tag findings `introduced` or `pre-existing` in touched files.

## Red Flags

- Treating improve as a ship gate or delivery review substitute.
- Implementing fixes or running **mutating commands** (install, commit, formatters, artifact-writing builds) during the audit.
- Editing product code, spec, plan, or CONTEXT/ADR (except explicit user-requested `docs/sdd/*-improve.md`).
- Default `plans/` or on-disk reports without explicit user request.
- Inventing findings when none exist.
- Reproducing secret values in findings.

## Verification

Confirm deliverable includes **Recon**, **Scope**, findings with **Evidence** bullets, optional **Direction** and **Dependency order**, and considered/rejected when applicable.

## Output

**Conversation findings report** — **`## Recon`**, **`## Scope`**, findings **list** (with **Evidence**), optional **`## Direction`** + **`## Dependency order`**, considered and rejected. Default **no** durable file. See [finding-format.md](references/finding-format.md).

Persist `docs/sdd/YYYY-MM-DD-<topic>-improve.md` or file issues only when the user explicitly asks.

## Stop Conditions

Stop after the conversation deliverable and one routing recommendation through **`using-sdd`** only.
