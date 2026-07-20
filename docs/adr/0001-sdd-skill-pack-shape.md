# SDD skill pack shape: three-stage loop + independent review/improve

This pack is Markdown skills for Spec-Driven Development without owning a PM, state machine, or Git workflow. We keep a **three-stage delivery loop** (`sdd-spec` → `sdd-plan` → `sdd-build` → Stop) that the user `@`s one stage at a time, plus two **independent** skills (`sdd-review`, `sdd-improve`) that share Standards baselines but do not require Spec/Plan/Build. Goal: less rework via verifiable contracts, not more ceremony.

**Status:** accepted

## Considered options

| Option | Why not (or why) |
| --- | --- |
| Full loop ending in ship/verify/git | Rejected — contradicts “not a Git framework”; AC evidence lives in build close-out + review Spec axis |
| Fold review into build | Rejected — loses independent read-only quality report |
| Matt-only smells for Standards | Extended — four dimensions (Correctness · Structure+smells · Verification · Traceability) for review/improve |
| `sdd-audit` as health scan | Replaced by `sdd-improve` — hotspot-first candidates, Markdown only, no HTML |
| Auto-chain stages | Rejected — explicit Stop; user `@`s the next skill |

## Consequences

- Runtime truth is each `skills/*/SKILL.md`; this ADR records *why* the pack is shaped this way.
- `sdd-review` / `sdd-improve` must not hard-route to spec/plan/build.
- Shared Standards live under `skills/sdd-review/references/*-baseline.md`.
- Consumer docs stay `docs/sdd/*-spec.md` / `*-plan.md` by convention (optional).
