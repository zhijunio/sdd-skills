---
name: sdd-improve
description: Use when the user wants a read-only codebase audit or health check—correctness, security, architecture debt, tests, or branch exploration—outside the delivery loop. Optional satellite; not delivery review of a scoped diff.
---

# SDD Improve

## Goal

Run a read-only multi-category audit and deliver a **conversation findings report** — prioritized verified findings with evidence — without replacing `sdd-review` or entering implementation.

## When to Use

Use when the user asks for a codebase audit, health check, improve pass, or architecture/debt scan across the repo or current branch.

Skip when the task is **delivery review** of a defined increment diff with spec/plan compliance — use `sdd-review`.

Skip when the user only needs a **territory map** without findings — use `sdd-zoom`.

Skip when goals or trade-offs are still open — use `sdd-grill`.

Skip when the user asks for **direct implementation** — decline and route to **`sdd-spec`**, **`sdd-plan`**, or **`sdd-build`** (or recommend **shadcn/improve** for plan+execute workflows).

This is an **optional satellite**. Not mandatory before `sdd-ship`.

### Disambiguation vs `sdd-review`

| | **improve** | **review** |
| --- | --- | --- |
| Question | What opportunities or problems exist? | Does this increment meet spec/plan? |
| Scope | Whole repo or branch vs merge-base | Increment diff only |
| Criteria | Leverage, categories 1–9 | Approved spec / plan / AC |
| Verdict | Findings table; user selects follow-ups | pass / must-fix / should-fix → ship |
| Timing | Exploratory — health check, onboarding | After build, before ship |
| Branch | Tags `introduced` and `pre-existing` | Only defects introduced or worsened by diff |

Full report structure: [finding-format.md](references/finding-format.md).

## Prerequisites

Read repository guidance, README, and optional `CONTEXT.md`, `docs/adr/`, `docs/sdd/*` when present. Infer scope from **natural language** — users need not type `quick`, `branch`, or slash commands. Read-only commands (`tsc --noEmit`, audit in check mode) are allowed.

## Process

**Profile (optional) → Audit → Verify → Present → Confirm → Stop**

1. **Profile** — when effort or scope is ambiguous: project type, inferred effort (`quick` / `standard` / `deep`), in-scope categories, skip reasons. See [profile-guide.md](references/profile-guide.md).
2. **Audit** — read-only scan of in-scope categories (default **standard**: categories **1–8**). All findings use `file:line` evidence. **Never** use the name Simplify. See [audit-playbook.md](references/audit-playbook.md).
3. **Verify** — re-read cited code; reject false positives; record in **considered and rejected**. When a finding contradicts an existing ADR, **mark the conflict** and recommend ADR or spec follow-up — do not override silently.
4. **Present** — findings table by leverage; category 9 **direction** in a separate section when included.
5. **Confirm** — ask which findings to pursue; dependency order for user selections only.
6. **Stop** — recommend **`using-sdd`** only; default next **`sdd-spec`** (needs AC) or **`sdd-grill`** (trade-offs).

Branch scope: tag findings `introduced` or `pre-existing` in touched files.

## Red Flags

- Treating improve as a ship gate or delivery review substitute.
- Implementing fixes during the audit instead of routing to **`sdd-spec`**, **`sdd-plan`**, or **`sdd-build`**.
- Editing product code, spec, plan, or CONTEXT/ADR.
- Default `plans/` or on-disk reports without explicit user request.
- Inventing findings when none exist.
- Reproducing secret values in findings.

## Verification

Confirm deliverable states inferred effort and scope, lists verified findings with evidence or explicit none-found, and includes considered/rejected when applicable.

## Output

**Conversation findings report** — optional Profile, verified findings table, direction section when category 9 ran, considered and rejected. Default **no** durable file. See [finding-format.md](references/finding-format.md).

Persist `docs/sdd/YYYY-MM-DD-<topic>-improve.md` or file issues only when the user explicitly asks.

## Stop Conditions

Stop after the conversation deliverable and one routing recommendation through **`using-sdd`** only.
