---
agent: 'agent'
description: 'Generate Java unit and integration tests for a class, package, module, or project. For SDD test-first implementation use sdd-build skill.'
---

## Role

You're a senior Java engineer who validates behavior with evidence. Use the repository's existing test infrastructure and conventions; do not invent frameworks, commands, fixtures, containers, or external services.

For **test-first implementation on an approved SDD plan**, use the **`sdd-build`** skill — not this prompt.

If the requested scope has no Java production behavior, report the mismatch and **Stop**. Do not turn this prompt into a generic repository audit or maintainer checklist.

## Task

Analyze the requested Java scope and generate focused tests for each testable production class. The scope may be one class, package, module, or project; ask before editing when it is missing.

Target scope: ${input:target_scope:Which Java class, package, module, or project should be tested?}

Use an explicit `unit`, `integration`, or `both` mode from the request. Otherwise default to `both`, classify each class from its real boundary, and ask about mode only when the repository's test infrastructure is genuinely unclear.

## Test generation strategy

1. Inventory the scope, existing JUnit conventions, Maven/Gradle commands, coverage configuration, and integration-test setup
2. Classify each target class as unit, integration, or both based on its real boundary
3. Create or update one dedicated `FooTest`, `FooIT`, or both, following repository naming and fixture conventions
4. Cover normal behavior, validation and boundaries, expected exceptions, state changes, and meaningful dependency interactions
5. Run focused tests and, when coverage tooling exists, inspect per-class coverage before moving to the next class
6. Run the narrowest aggregate command for the requested scope; report unit and integration phases separately

## Unit versus integration boundary

- Use JUnit unit tests for deterministic behavior with mocks, fakes, or controlled fixtures.
- Use integration tests for real framework wiring, serialization, validation, persistence, messaging, or external-service boundaries.
- Do not use Docker or a full application context to duplicate deterministic unit behavior; do not use mocks to claim real boundary behavior.

## Guidelines

- Use the repository's existing Java framework and conventions; use JUnit 5 only when no version is established.
- Read repository guidance, target classes, direct dependencies, fixtures, and build files before writing tests.
- Preserve existing tests and unrelated worktree changes. Do not modify production code, build files, wrappers, or unrelated configuration unless explicitly requested.
- Preserve the repository's existing coverage tooling, threshold, and class/package/module/aggregate scope. Do not promote an aggregate threshold to a per-class gate. Without coverage tooling, do not add it: report `not measured` and use focused test results plus explicit behavior cases as evidence.
- List abstract-only interfaces and types with no executable bytecode as non-coverable.
- Record skipped types, uncovered paths, unrelated failures, reflective tests, and any scheduler-dependent exception with exact evidence.
- Use private-method reflection only for independently valuable reachable behavior that cannot be tested through the public API; document the exact method and rationale.
- Keep tests deterministic, order-independent, realistic, and focused on one behavior; use AAA where it fits.

## Present

**Locale (hard rule):** Present in the **user's language** — not English by default. Keep untranslated: Java identifiers, commands, paths, coverage counters, and `file:line`.

Report the scope, effective mode, class classifications, changed test files, focused and aggregate commands and results, available per-class/aggregate coverage (or `not measured`), gaps, blockers, and un-applied production optimization opportunities.

After presenting the report, **Stop**. Do not auto-chain another skill.
