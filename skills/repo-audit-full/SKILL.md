---
name: repo-audit-full
description: Use when the user wants a read-only audit of the current whole repository or asks for a repository-wide review. Not an increment delivery review.
---

Two-axis review of the current project as checked out in the repository:

- Standards — does the code conform to this repo's documented coding standards?
- Spec — does the code faithfully implement the originating issue / PRD / spec?

Within the **Standards** axis, review across six dimensions for the whole scope: **correctness**, **maintainability**, **tests**, **architecture**, and conditional **security** / **performance**.

Both axes run as parallel sub-agents so they don't pollute each other's context, then this skill aggregates their findings.

## Process

### 1. Pin the project

The target is the current whole repository checkout. If the user explicitly wants a narrower area, ask them to name it before proceeding.

Capture the review target once. For a repo-wide audit, inspect the current project state directly, not a diff, commit range, or fixed-point comparison by default.

Before going further, confirm the repository resolves and has content. An empty repository or missing path should fail here — not inside two parallel sub-agents.

### 2. Identify the spec source

Look for the originating spec or behavior contract, in this order:

- A path the user passed as an argument.
- Docs under `docs/`, `specs/`, or `wiki/` that describe the current project behavior.
- Other repository docs that define the expected behavior for the area under review.

If nothing is found, the Spec sub-agent will skip and report "no spec available". Do not block the whole audit on missing external specs.

### 3. Identify the standards sources

Anything in the repo that documents how code should be written, such as CODING_STANDARDS.md or CONTRIBUTING.md.

On top of whatever the repo documents, the Standards axis always carries the repo-wide baseline below — a fixed checklist that applies even when a repo documents nothing. Two rules bind it:

- The repo overrides. A documented repo standard always wins; where it endorses something the baseline would flag, suppress the finding.
- Always a judgement call. Each item is a labelled heuristic, never a hard violation — and, like any standard here, skip anything tooling already enforces.

Walk the scope against six review dimensions. Always walk **correctness**, **maintainability**, **tests**, and **architecture**. Open **security** and **performance** only when the scope has signals that make them relevant. Functional correctness here means correctness bugs in the code itself (edge cases, error paths, races); conformance to the originating spec is the Spec axis below, not this one.

**Dimension 1 — Correctness.** Does the repo behave correctly under real inputs and failure modes?

- Intended behavior vs actual implementation on inspected paths
- Input boundaries — null/empty, off-by-one, type coercion, unchecked casts
- Error paths — swallowed exceptions, wrong status codes, partial failure without rollback
- Resource lifecycle — leaks, missing close/dispose/finally
- Concurrency & state — races, TOCTOU, shared mutable state, async ordering
- **LSP (Liskov Substitution)** — a subclass must honour the parent's pre/post-conditions; overriding to break them is a correctness bug.
- **FFP (Fail Fast)** — detect a config conflict early and throw an explicit exception; don't fail silently at runtime.
- **Defensive Programming** — assert param validity at a public entry; don't wait for an NPE mid-execution.

**Dimension 2 — Maintainability.** Is the code easy to read, reason about, and change without scattered edits?

- Prefer honest names and direct code over cleverness: **Mysterious Name**, **Primitive Obsession**
- Remove duplication and accidental complexity: **Duplicated Code**, **Data Clumps**, **Middle Man**
- Avoid over-design for needs the spec does not have yet: **Speculative Generality**, **YAGNI**
- Apply these principles as judgement calls: **KISS**, **DRY**, **SLAP**
- **Prefer Immutability** — prefer `final` fields over mutable state when it reduces incidental state and surprise

**Dimension 3 — Tests.** Do the tests cover the changed or risky behavior cheaply and convincingly?

- Coverage of changed paths — error paths and boundaries, not only the happy path
- Seams — dependencies injectable or replaceable without reaching into internals
- **Test Behavior, not implementation** — assert outputs/results, not internal call order or mock minutiae

**Dimension 4 — Architecture.** Do module boundaries, responsibilities, and dependency directions stay coherent?

- Change shape signals: **Feature Envy**, **Repeated Switches**, **Shotgun Surgery**, **Divergent Change**, **Message Chains**, **Refused Bequest**
- **SRP** — one class or module should not own unrelated jobs
- **OCP** — repeated type switches or condition cascades often want an extension seam instead
- **ISP** — interfaces should not force callers or implementers to carry methods they do not need
- **DIP** — depend on interfaces or stable seams, not concrete implementations
- **LoD (Law of Demeter)** — avoid reaching through long object chains (`a.b().c().d()`)
- **CRP (Composition over Inheritance)** — prefer delegation/composition to inheritance when reuse is the real goal
- **Least Exposure** — widen visibility only as far as the callers actually require

#### Repo-wide dimensions

**Dependencies.** Does the repo keep dependency choice, versioning, and scope under control?

- Duplicate or conflicting versions, unnecessary transitive pull-ins, stale test deps, and module-to-module drift
- Public starter or BOM surfaces stay aligned with the actual dependency graph

**Verification / CI.** Do the build, test, and release gates prove the repo state the docs claim?

- CI and local commands match the repo docs
- Coverage, matrix jobs, and integration checks cover the repo's public surface
- Generated or published artifacts are verified rather than assumed

**Docs / Traceability.** Do user-facing docs match the code and release state?

- README, AGENTS, wiki, CHANGELOG, and design docs stay in sync with code and module naming
- Public APIs, configuration prefixes, and package boundaries are discoverable

**Compatibility / API.** Does the repo preserve public contracts and migration paths?

- Semver, deprecations, artifact names, package paths, and configuration keys remain coherent
- Backward-compatibility risks are called out when public entrypoints change

**Dimension 5 — Security (conditional).** Open this dimension when the scope touches untrusted input, auth, secrets, storage, network boundaries, or other obvious attack surfaces.

- Injection — SQL/NoSQL/command/template injection, unsanitised output (XSS)
- Auth & authz — missing auth checks, broken access control, privilege escalation
- Secrets & data exposure — logged secrets, sensitive data in responses/errors, insecure storage
- Unsafe APIs — deserialisation of untrusted data, path traversal, reflection on untrusted input, disabled validation

**Dimension 6 — Performance (conditional).** Open this dimension when the scope touches hot paths, loops, queries, rendering, startup, concurrency, or scale-sensitive code.

- Hot paths — N+1 queries, repeated work in loops, unnecessary allocations, blocking I/O on a request thread
- Complexity — algorithmic cost that will not scale, unbounded collections
- Resource cost — missing cache/pool, redundant serialisation, eager load where lazy would do
- Start-up & footprint — expensive init, work moved from startup into a hot path, or new background churn

### 4. Spawn both sub-agents in parallel

Send a single message with two `Agent` tool calls. Use the `general-purpose` subagent for both.

**Standards sub-agent prompt** — include:

- The current project target the user supplied.
- The list of standards-source files you found in step 3, **plus the repo-wide baseline from step 3** pasted in full — the sub-agent has no other access to it.
- The brief: "Report — per file/hunk where relevant — (a) every place the scope violates a documented standard: cite the standard (file + the rule); and (b) any baseline finding you spot: name its dimension (and principle or smell) and quote the hunk. Always walk correctness, maintainability, tests, and architecture. Only open security or performance when the scope has real signals. Distinguish hard violations from judgement calls — documented-standard breaches can be hard, but baseline findings are always judgement calls, and a documented repo standard overrides the baseline. Skip anything tooling enforces. Under 400 words."

**Spec sub-agent prompt** — include:

- The current project target the user supplied.
- The path or fetched contents of the spec.
- The brief: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the scope that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

If the spec is missing, skip the Spec sub-agent and note this in the final report.

### 5. Aggregate

Present the two reports under `## Standards` and `## Spec` headings, verbatim or lightly cleaned. Do **not** merge or rerank findings — the two axes are deliberately separate (see _Why two axes_).

End with a one-line summary: total findings per axis, and the worst issue _within each axis_ (if any). Don't pick a single winner across axes — that's the reranking the separation exists to prevent.

## Why two axes

A change can pass one axis and fail the other:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**

Reporting them separately stops one axis from masking the other.
