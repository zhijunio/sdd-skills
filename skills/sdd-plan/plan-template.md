# <Title> Implementation Plan

<!--
  Plan writing guide:
  - Each slice must be independently testable and deliver observable behavior.
  - Prefer vertical slices (thin end-to-end functionality) over horizontal layers.
  - Target 15–60 minutes per slice. If a slice is larger, split it.
  - Every acceptance criterion from the spec must be covered by at least one slice.
  - "Done" is set to true only after the verification command passes.
-->

**Spec:** `<relative path to approved spec file>`

## Slice 1: <Observable behavior — what the user or system can do after this slice>

<!--
  Goal: what this slice accomplishes in one sentence.
  Acceptance: which AC(s) this slice covers (e.g., AC-1, AC-2).
  Depends on: prior slice numbers, or "None" if this is the first slice.
  Test or proof: the failing test to write first, or alternative proof for
    non-testable changes (e.g., "curl POST /endpoint returns 200 with JSON body").
  Implementation outline: files to create/modify, key functions, data changes.
    Keep it high-level — not line-by-line code.
  Verification: the exact command to run (e.g., "mvn test -Dtest=PasswordResetTest").
  Done: false (set to true after verification passes).
-->

- Goal:
- Acceptance: AC-1
- Depends on: None
- Test or proof:
- Implementation outline:
- Verification:
- Done: false

## Slice 2: <Observable behavior>

<!-- Repeat the same structure for each slice. Example: -->

- Goal:
- Acceptance: AC-2, AC-3
- Depends on: Slice 1
- Test or proof:
- Implementation outline:
- Verification:
- Done: false

<!--
  Material deviations during build:
  - If a slice boundary changes, record the new boundary and return to sdd-plan.
  - If an acceptance criterion changes, record it and return to sdd-spec.
  - Keep a running log of verified slices at the bottom of this file during build.
-->
