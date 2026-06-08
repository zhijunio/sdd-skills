---
name: sdd-ship
description: Use when review has no unresolved blocking findings and a completed SDD increment needs final acceptance verification and delivery readiness checks.
---

# SDD Ship

## Goal

Provide fresh evidence that the reviewed increment is ready for delivery.

## When to Use

Use after `sdd-review` has no unresolved `must-fix` findings and any `should-fix` finding is fixed or explicitly accepted.

Do not use to fix review findings.

## Prerequisites

Require the approved spec file, plan, reviewed diff, and review outcome.

## Process

1. Map every acceptance criterion to implementation and evidence.
2. Rerun the necessary targeted verification.
3. Expand regression coverage according to interface, dependency, configuration, and shared-module risk.
4. Check for missing or uncommitted task changes.
5. Record commands, outcomes, unrun checks, and remaining risks.
6. Update an existing CHANGELOG when project convention and user-visible impact require it.
7. Create a CHANGELOG only when the user explicitly requests a format.

## Red Flags

- Reusing stale test results.
- Running an expensive full build without risk justification.
- Fixing code instead of returning to `sdd-build`.
- Introducing a changelog tool or format without project precedent.
- Pushing, releasing, or deploying without explicit instruction.

## Verification

Every acceptance criterion must have fresh, proportionate evidence. Explain any skipped check.

## Output

Provide a ship summary with acceptance results, commands, outcomes, unrun checks, and remaining risks. Record only user-visible changes in CHANGELOG.

## Stop Conditions

Stop after the ship summary and any explicitly requested local commit. Do not push, open a PR, publish, or deploy unless separately requested.
