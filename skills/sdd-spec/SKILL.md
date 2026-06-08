---
name: sdd-spec
description: Use when a software change needs a durable behavior contract, scope, acceptance criteria, and necessary technical constraints before implementation planning.
---

# SDD Spec

## Goal

Write a concise specification that defines what must be true without prescribing file-by-file implementation.

## When to Use

Use for a new project, feature, bug fix, migration, or meaningful behavior change whose intent is sufficiently clear.

Do not use to explore unresolved design directions or to write implementation tasks.

## Prerequisites

Read repository guidance, relevant code and docs, and any brainstorm outcome. Ask only for decisions that cannot be discovered locally.

Repository domain docs may inform scope and constraints; they are **not** a substitute for this skill's output.

## Process

1. Start from [spec-template.md](spec-template.md).
2. Define the goal, scope, and non-goals.
3. Record only repository facts that constrain the change.
4. Write requirements and necessary compatibility, migration, security, or interface constraints when relevant.
5. Give each observable acceptance criterion a stable identifier such as `AC-1`.
6. Remove irrelevant template sections.
7. Present the written specification for user approval.

## Red Flags

- Treating a repository domain doc as the spec without writing `docs/sdd/...-spec.md`.
- Hiding implementation steps inside acceptance criteria.
- Copying the brainstorm transcript.
- Leaving open questions that block planning.
- Treating file existence as user approval.

## Verification

Check that every criterion has a clear pass/fail result and that no requirement depends on an undefined term.

## Output

Write `docs/sdd/YYYY-MM-DD-<topic>-spec.md`.

## Stop Conditions

Stop after the user approves the specification. Recommend `sdd-plan`.
