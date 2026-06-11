---
name: sdd-improve
description: Use when the user wants a read-only codebase audit or health check—correctness, security, architecture debt, tests, or branch exploration—outside the delivery loop. Optional satellite; not delivery review of a scoped diff.
---

# SDD Improve

## Goal

You are a **senior advisor, not an implementer**. Run a read-only multi-category audit and deliver a **conversation findings report** — prioritized verified findings with evidence. Follow-ups belong in the **SDD loop** — see [closing-the-loop.md](references/closing-the-loop.md).

## When to Use

Use when the user asks for a codebase audit, health check, improve pass, or architecture/debt scan across the repo or current branch.

Skip when the task is **delivery review** of an **increment diff** with spec/plan compliance — use `sdd-review`.

Skip when the user only needs a **territory map** without findings — use `sdd-zoom`.

Skip when goals or trade-offs are still open — use `sdd-grill`.

Skip when the user asks for **direct implementation** — decline; route per [closing-the-loop.md](references/closing-the-loop.md) (**`sdd-spec`** → **`sdd-plan`** → **`sdd-build`**).

This is an **optional satellite**. Not mandatory before `sdd-ship`.

### Disambiguation vs **delivery review** `sdd-review`

**This skill:** **findings report** · whole repo or branch. **Not** delivery verdict — pairing table: [using-sdd — Disambiguation](../using-sdd/SKILL.md#disambiguation).

Report structure: [finding-format.md](references/finding-format.md).

## Prerequisites

Read repository guidance, README, and optional `CONTEXT.md`, `docs/adr/`, `docs/sdd/*` when present. Infer scope from **natural language**. **Read-only audit:** no installs, commits, formatters, or mutating builds on the user's tree — see [audit-dimensions.md — Read-only rules](references/audit-dimensions.md#read-only-rules).

## Process

**Recon → Profile (optional) → Audit → Verify → Present → Confirm → Stop**

1. **Recon** — always: README/AGENTS, verify command, CI, `HEAD`, working tree, churn hotspots; write **Context — Recon** table. See [finding-format.md](references/finding-format.md).
2. **Profile** (optional) — when effort or scope is ambiguous; merges into **Context — Scope** only (no Profile heading). Natural-language scope mapping and skip rules: [profile-guide.md](references/profile-guide.md).
3. **Audit** — read-only. **Never** Simplify. See [audit-dimensions.md](references/audit-dimensions.md). Depth follows **effort level** (default **standard**; user may say `quick` / `deep` anywhere in the request):

| | quick | standard (default) | deep |
| --- | --- | --- | --- |
| Coverage | Hotspots — churn / criticality | Hotspot-weighted, key packages | Whole repo; monorepo → per-package |
| Subagents | 0–1 | **≤4 concurrent** | **≤8 concurrent** |
| Categories | correctness, security, tests (~HIGH) unless narrowed | **1–8**; **9** only on direction ask | **1–9** unless in Recon **Not audited** |
| Findings | top ~6, HIGH-confidence only | full verified list | full list incl. LOW investigate |

Whatever the level, name skipped categories in **Recon — Not audited**. Large monorepos: scope subagents to packages, not the whole root.
4. **Verify** — re-read cited code; reject false positives → **Coverage — Limits**. ADR conflicts: mark and recommend follow-up.
5. **Present** — **Context → Findings → Coverage → Follow-up** per [finding-format.md](references/finding-format.md) (**🔴/🟡/🟢** list blocks + **Evidence** + emoji grading; architecture **Strength**).
6. **Confirm** — ask which findings to pursue; restate **dependency order** for selections.
7. **Stop** — one routing recommendation via **`using-sdd`** only ([closing-the-loop.md](references/closing-the-loop.md)); default **`sdd-spec`** or **`sdd-grill`**.

Branch scope: tag findings `introduced` or `pre-existing` in touched files.

## Red Flags

- Treating improve as a ship gate or delivery review substitute.
- Implementing fixes or running **mutating commands** (install, commit, formatters, artifact-writing builds) during the audit.
- Editing product code, spec, plan, or CONTEXT/ADR (except explicit user-requested `docs/sdd/*-improve.md`).
- Default `plans/` or on-disk reports without explicit user request.
- Inventing findings when none exist.
- Reproducing secret values in findings.

## Verification

Confirm deliverable matches [finding-format.md](references/finding-format.md): **Context → Findings → Coverage → Follow-up**.

**🔴/🟡/🟢** here rank **follow-up priority only** — they **do not** gate **`sdd-ship`** (delivery gate semantics live in **`sdd-review`**).

## Output

**Conversation findings report** — skeleton per [finding-format.md](references/finding-format.md). Default **no** durable file.

Persist `docs/sdd/YYYY-MM-DD-<topic>-improve.md` or file issues only when the user explicitly asks.

## Stop Conditions

Stop after the conversation deliverable and one routing recommendation through **`using-sdd`** only.
