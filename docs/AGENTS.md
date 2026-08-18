# AGENTS.md

## Core Principles

- Choose the simplest implementation that fully satisfies the current requirements. Avoid unnecessary abstraction, configuration, indirection, or speculative extensibility.

- Make the smallest necessary change that fixes the root cause. Do not refactor unrelated modules or change strategy semantics unless explicitly requested.

- Grow the system in layers. Start from the smallest working end-to-end version and add new capabilities incrementally. Never replace a working system with unfinished complexity.

- Reuse existing project components before creating new ones. Prefer extending proven modules over introducing parallel implementations.

- Prefer well-maintained libraries when they reduce overall complexity or improve reliability. Do not reimplement common functionality without a clear benefit.

- Keep components modular with clearly defined responsibilities. Avoid unnecessary coupling between strategy logic, execution, accounting, replay, and infrastructure.

- Design for long-term maintainability once a feature or strategy has been validated. Do not over-engineer speculative ideas before evidence exists.

---

## Strategy Development

- Validate hypotheses with historical replay before introducing forward-only logic whenever historical validation is possible.

- Every trading strategy must progress through Replay → Shadow → Canary → Live. Do not skip validation stages.

- Base design decisions on measurable evidence rather than intuition. Optimize only after demonstrating that an edge exists.

- Treat every strategy as an independent contract. Do not silently alter frozen behavior without explicit authorization.

---

## Existing Systems

- Do not break running Shadow or Live systems for unrelated work.

- Preserve compatibility only when required by active production or validation workflows. Otherwise, remove obsolete code instead of accumulating compatibility layers.

- Reuse existing infrastructure whenever possible, including replay engines, accounting, execution, wallet management, order book handling, logging, monitoring, and daemon frameworks.

---

## Engineering Standards

- Prefer deterministic behavior to hidden automation.

- Fail loudly when assumptions are violated. Do not silently ignore errors or fall back to unexpected behavior.

- Keep configuration minimal. Introduce new configuration only when behavior genuinely needs to vary.

- Remove dead code instead of leaving unused paths behind.

- Write code that is easy to inspect, replay, test, and reason about.

- Keep implementation consistent with existing project architecture unless an architectural change is explicitly requested.

---

## Scope Discipline

- Implement only the requested scope.

- Do not introduce unrelated optimizations, redesigns, migrations, or feature expansions.

- Non-blocking findings outside the requested scope may be noted separately but must not be merged into the current task.

- Consider a task complete once its agreed acceptance criteria are satisfied. Treat subsequent improvements as separate work items.