# Handoff — advisor role and closing the loop

**机会扫描** ends at judgment and evidence — not implementation. This file routes follow-ups without porting **shadcn/improve** `plans/` / `execute` / `reconcile` into **`sdd-improve`**.

## Advisor, not implementer

- **This skill:** understand, vet, prioritize, present findings — like improve's senior advisor phase.
- **Not this skill:** edit product code, write default `plans/`, dispatch worktree executors, or merge/push. During the scan: **no mutating commands** on the user's tree — [audit-playbook — Read-only rules](audit-playbook.md#read-only-rules) (same spirit as improve Hard Rules #2).

**Strong / weak split in SDD terms:**

| Role | SDD skills | improve (external) |
| --- | --- | --- |
| Judge + specify | **`sdd-improve`**, **`sdd-grill`**, **`sdd-spec`**, **`sdd-plan`** | Audit + write **`plans/`** |
| Execute | **`sdd-build`** (test-first on approved plan) | **`execute <plan>`** (executor subagent) |
| Review verdict | **`sdd-review`** (increment diff) | Advisor review after execute |
| Ship evidence | **`sdd-ship`** | User merge; advisor never pushes |

## After **Confirm** — route via **`using-sdd`**

| User intent | Next |
| --- | --- |
| Selected finding needs **acceptance criteria** or behavior contract | **`sdd-spec`** → **`sdd-plan`** → **`sdd-build`** |
| Trade-offs or direction still open | **`sdd-grill`** |
| Increment already built; check diff vs spec/plan | **`sdd-review`** → **`sdd-build`** (fixes) → **`sdd-ship`** |
| **Self-contained handoff** for a weaker model with **zero SDD context** | Install **[shadcn/improve](https://github.com/shadcn/improve)** — audit finding → **`plans/`** → optional **`execute`** / **`reconcile`** |
| User asks to **implement during the scan** | Decline; pick a row above |

Respect **Dependency order** from the report when multiple findings are selected.

## Closing the loop (SDD vs improve)

**SDD loop** (default for this repo's consumers):

```text
sdd-improve → sdd-spec → sdd-plan → sdd-build → sdd-review → sdd-ship
```

**Reconcile equivalents** — no `plans/README.md` in SDD by default:

| User says | Route |
| --- | --- |
| 「上次体检选的 #3 做完了吗」 | If spec/plan exists → **`sdd-review`** / **`sdd-ship`** on the increment; else re-run **`sdd-improve`** or check **`docs/sdd/*`** if user asked to persist |
| 「plan 002  blocked / 漂移了」 | **`improve reconcile`** if using external improve; in SDD → refresh **`docs/sdd/*-plan.md`** or **`sdd-plan`** / **`sdd-build`** |
| 「对一下 watchlist / tag」 | **`sdd-ship`** + maintainer docs (`CHANGELOG`, `project-decisions` §8) |

Full **execute / reconcile / `--issues`** semantics: [shadcn/improve `closing-the-loop`](https://github.com/shadcn/improve/blob/main/skills/improve/references/closing-the-loop.md) — link out; do not duplicate here.

## Optional durable artifact

Only when the user explicitly asks: `docs/sdd/YYYY-MM-DD-<topic>-improve.md` — findings summary for later reconcile, not a substitute for spec/plan.
