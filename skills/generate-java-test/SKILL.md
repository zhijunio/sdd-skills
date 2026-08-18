---
name: generate-java-test
description: Use when the user wants Java unit or integration tests for a class, package, module, or project.
---

# java-test

## When

Use this skill to generate or improve Java tests for a specified production scope. Ask for the scope when it is missing; do not silently choose a subset.

Determine the mode:

- `unit`: isolate the target with mocks, fakes, controlled fixtures, or proxies.
- `integration`: exercise existing framework wiring and real boundaries.
- `both`: classify every class and generate unit tests, integration tests, or both as its behavior requires; when both are needed, finish the unit coverage before adding distinct boundary cases.

If the mode is missing, default to `both`. For every target class, classify the required test surface from its dependencies and boundary: generate a unit test for isolated behavior, an integration test for framework or external-boundary behavior, and both when the class has meaningful behavior in both categories. Do not ask the user to choose between the two unless the repository's test infrastructure is genuinely unclear.

Choose `unit` for deterministic class behavior such as properties, enums, validation, conditions, activation decisions, container metadata, exception messages, and configuration branches using mocks or controlled fixtures. Choose `integration` for real boundaries such as Spring Boot auto-configuration, context loading, bean conditions, `@ServiceConnection`, container lifecycle, real JDBC/Redis connectivity, IdP config mounting, health checks, and cross-component event wiring. Do not use Docker or a full application context to duplicate behavior already proven by unit tests, and do not use mocks to claim real framework or external-service wiring.

## Skip

Use another skill when the request is test-first implementation under an approved SDD plan. If the requested scope has no Java production behavior, report the mismatch and stop; do not turn this skill into a generic repository audit. Do not modify production code, build files, wrappers, configuration, unrelated tests, or unrelated worktree changes unless explicitly asked.

## Recon

Before editing:

1. Read `AGENTS.md`, `CONTRIBUTING.md`, and `CONTEXT.md` when present.
2. Inventory the requested production scope, existing tests, test layout, build commands, coverage configuration, and CI conventions.
3. Read each target class and its direct production dependencies.
4. For integration mode, or when a class is classified as requiring integration coverage, read existing fixtures, framework test setup, integration configuration, and `*IT` conventions.
5. Identify every target class with executable behavior. Record interfaces, abstract-only types, and other non-coverable types separately.
6. Classify each target class before writing tests:
   - **Unit** — its behavior can be proven with isolated inputs and replaceable dependencies; prefer `FooTest`.
   - **Integration** — correctness depends on framework wiring, serialization, validation, persistence, messaging, or another real boundary; use the repository's integration suffix, typically `FooIT`.
   - **Both** — isolated business behavior and distinct boundary behavior both matter; create both files without duplicating scenarios.

The classification is per class, not per package or project. Record the classification and evidence in the final report.

Use the repository's existing framework and conventions. Use JUnit 5 only when the repository does not clearly establish another JUnit version. Never invent a framework, command, fixture, container, or external service.

## Build the tests

Work one class at a time:

1. Apply the class's classification: create or update `FooTest`, `FooIT`, or both. For `both`, keep unit tests focused on isolated behavior and integration tests focused on distinct wiring or boundary behavior.
2. Cover each meaningful public behavior: normal inputs, validation and boundaries, expected failures, state changes, and relevant dependency interactions.
3. Keep tests deterministic, isolated, order-independent, and focused on one behavior. Prefer AAA, descriptive names, direct assertions, realistic data, and existing fixtures/utilities.
4. Test public behavior by default. Do not add integration tests merely to repeat unit scenarios, and do not replace boundary tests with mocks.
5. Run the focused test command and, when coverage tooling exists, inspect the class coverage before moving to the next target.

## Red gate

Use the repository's existing coverage tooling and policy without changing their scope. When coverage tooling is configured, generate the narrowest useful report and enforce explicit thresholds at their configured class, package, module, or aggregate scope. Do not promote an aggregate threshold to a per-class gate. When no coverage tool is configured, do not add one: report coverage as `not measured` and use focused test results plus explicit behavior cases as evidence.

When a 100% JaCoCo gate is explicitly in force for the target classes, completion requires:

- focused tests pass for every processed target;
- every measurable target class reaches 100% line, instruction, and applicable branch coverage;
- multi-class scopes also report aggregate coverage without substituting it for per-class results;
- the configured integration-test phase passes whenever any target class is classified as `integration` or `both`;
- after all classes pass, the narrowest aggregate command for the requested scope passes.

If a deterministic reachable path is uncovered, inspect the report, add a focused test, and repeat. If a configured threshold cannot be met, report the exact class, file/line, path, and reason; the scope remains incomplete. Never lower an explicit project/user threshold or imply completion with missing evidence.

Abstract-only interfaces and types with no executable production bytecode are outside the measurable denominator, but list them explicitly as non-coverable. Do not change production code to create coverage points.

A scheduler-dependent concurrency branch may be accepted only when deterministic tests prove observable thread-safety behavior and JaCoCo cannot force the interleaving. Record the class, file/line, raw missed counter, test evidence, and reason. This is the only coverage exception.

Private-method reflection is allowed only when a reachable path has independent behavioral value, public APIs cannot reach it, and changing production code solely for testability would be worse. Document the exact class/method and rationale in the test and report; never use reflection only to inflate coverage.

## Test shape

- One dedicated `FooTest`, `FooIT`, or both according to the per-class classification.
- One test method per behavior where practical.
- Simple setup and direct assertions; comments only for non-obvious setup.
- Unit tests stay fast and isolated; integration tests use repository-approved managed fixtures.
- Reuse existing helpers before introducing new abstractions.
- Avoid uncontrolled timing, network, filesystem, or clock behavior unless the target requires it and the test controls it.

## Present

**Locale (hard rule):** Present in the **user's language** — not English by default. Keep untranslated: Java identifiers, commands, paths, coverage counters, and `file:line`.

Report all of the following:

- requested scope, effective mode, every processed production class, and each class's unit/integration/both classification with evidence;
- created or updated test files;
- focused, aggregate, and integration-phase commands and results;
- line, instruction, and applicable branch coverage per target when the configured tooling provides it, plus aggregate coverage for multi-class scopes; otherwise state `not measured`;
- non-coverable or skipped types, uncovered paths, reflective tests, scheduler exceptions, and unrelated blockers with exact file/line references;
- production-code optimization opportunities discovered during the work, separately from test results, without applying them.

The scope is complete when focused and aggregate tests pass, every applicable existing coverage gate is satisfied, and any allowed scheduler exception is documented. The absence of coverage tooling alone does not make the scope incomplete.

After presenting the report, **Stop**. Do not auto-chain another skill.
