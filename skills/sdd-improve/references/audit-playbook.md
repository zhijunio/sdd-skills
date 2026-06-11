# Audit Playbook

Condensed read-only checklist per category. Adapted from [shadcn/improve](https://github.com/shadcn/improve) (MIT). **No step named Simplify** — over-engineering and duplication are category 5 findings.

## 1 correctness

- Unchecked errors, swallowed exceptions, wrong defaults
- Async hazards: missing await, race windows, stale closures
- Edge cases on empty, null, boundary inputs

## 2 security

- Auth gaps, missing authorization on mutations
- User input in queries, shell, or path traversal
- Secrets in repo or logs — cite `file:line` and type only; never reproduce values

## 3 performance

- N+1 queries, unbounded loops or fetches
- Hot-path synchronous work, missing indexes or caches

## 4 test coverage

- Missing tests on critical paths; fragile assertions
- Tests that lock implementation detail instead of behavior

## 5 tech-debt & architecture

Absorbs legacy `sdd-architect` signals:

- **Over-engineering** — pass-through layers, abstractions without reuse
- **Duplication** — parallel APIs, repeated 5+ line blocks, copy-paste UI
- **Deletion test** — if deleting a module scatters complexity, it may earn its keep; if complexity vanishes, pass-through noise
- **Depth / seam** — shallow modules, leaky seams between layers
- Strength: `Strong`, `Worth exploring`, `Speculative`

## 6 dependencies & migrations

- Lockfile drift, unpinned risky deps, audit failures
- Half-finished migrations, deprecated API still in use

## 7 experience & tooling

- Local dev friction, missing scripts, slow CI, unclear setup

## 8 docs

- README drift, stale examples, missing docs for public APIs

## 9 direction

Only when user asks roadmap / next steps. Evidence-grounded; 2–4 items max; open trade-offs → `sdd-grill`.

## Branch scope

When scope is branch vs merge-base, tag each finding `introduced` or `pre-existing` in touched files.
