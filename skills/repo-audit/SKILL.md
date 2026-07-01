---
name: repo-audit
description: >
  Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD/spec asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".
---

Two-axis review of the diff between HEAD and a fixed point the user supplies:

- Standards — does the code conform to this repo's documented coding standards?
- Spec — does the code faithfully implement the originating issue / PRD / spec?

Within the **Standards** axis, review across six dimensions: **correctness**, **maintainability**, **tests**, **architecture**, and conditional **security** / **performance**.

Both axes run as parallel sub-agents so they don't pollute each other's context, then this skill aggregates their findings.

## Process

### 1. Pin the fixed point

Whatever the user said is the fixed point — a commit SHA, branch name, tag, main, HEAD~5, etc. If they didn't specify one, ask for it.

Capture the diff command once: git diff <fixed-point>...HEAD (three-dot, so the comparison is against the merge-base). Also note the list of commits via git log <fixed-point>..HEAD --oneline.

Before going further, confirm the fixed point resolves (git rev-parse <fixed-point>) and the diff is non-empty. A bad ref or empty diff should fail here — not inside two parallel sub-agents.

### 2. Identify the spec source

Look for the originating spec, in this order:

- Issue references in the commit messages (#123, Closes #45, GitLab !67, etc.).
- A path the user passed as an argument.
- A PRD/spec file under docs/, specs/ or wiki/ matching the branch name or feature.

If nothing is found, ask the user where the spec is. If they say there isn't one, the Spec sub-agent will skip and report "no spec available".

### 3. Identify the standards sources

Anything in the repo that documents how code should be written, such as CODING_STANDARDS.md or CONTRIBUTING.md.

On top of whatever the repo documents, the Standards axis always carries the six-dimension baseline below — a fixed checklist that applies even when a repo documents nothing. Two rules bind it:

- The repo overrides. A documented repo standard always wins; where it endorses something the baseline would flag, suppress the finding.
- Always a judgement call. Each item is a labelled heuristic ("possible DRY violation"), never a hard violation — and, like any standard here, skip anything tooling already enforces.

Walk the diff against six review dimensions. Always walk **correctness**, **maintainability**, **tests**, and **architecture**. Open **security** and **performance** only when the diff has signals that make them relevant. Functional correctness here means correctness bugs in the code itself (edge cases, error paths, races); conformance to the originating spec is the Spec axis below, not this one.

**Dimension 1 — Correctness.** Does the changed code behave correctly under real inputs and failure modes?

- Intended behavior vs actual implementation on changed paths
- Input boundaries — null/empty, off-by-one, type coercion, unchecked casts
- Error paths — swallowed exceptions, wrong status codes, partial failure without rollback
- Resource lifecycle — leaks, missing close/dispose/finally
- Concurrency & state — races, TOCTOU, shared mutable state, async ordering
- **LSP (Liskov Substitution)** — a subclass must honour the parent's pre/post-conditions; overriding to break them is a correctness bug.
- **FFP (Fail Fast)** — detect a config conflict at startup and throw an explicit exception; don't fail silently at runtime.
- **Defensive Programming** — assert param validity at a public method's entry; don't wait for an NPE mid-execution.

**Dimension 2 — Maintainability.** Is the code easy to read, reason about, and change without scattered edits?

- Prefer honest names and direct code over cleverness: **Mysterious Name**, **Primitive Obsession**
- Remove duplication and accidental complexity: **Duplicated Code**, **Data Clumps**, **Middle Man**
- Avoid over-design for needs the spec does not have yet: **Speculative Generality**, **YAGNI**
- Apply these principles as judgement calls: **KISS**, **DRY**, **SLAP**
- **Prefer Immutability** — prefer `final` fields over mutable state when it reduces incidental state and surprise

**Dimension 3 — Tests.** Do the tests cover the changed behavior cheaply and convincingly?

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

**Dimension 5 — Security (conditional).** Open this dimension when the diff touches untrusted input, auth, secrets, storage, network boundaries, or other obvious attack surfaces.

- Injection — SQL/NoSQL/command/template injection, unsanitised output (XSS)
- Auth & authz — missing auth checks, broken access control, privilege escalation
- Secrets & data exposure — logged secrets, sensitive data in responses/errors, insecure storage
- Unsafe APIs — deserialisation of untrusted data, path traversal, reflection on untrusted input, disabled validation

**Dimension 6 — Performance (conditional).** Open this dimension when the diff touches hot paths, loops, queries, rendering, startup, concurrency, or scale-sensitive code.

- Hot paths — N+1 queries, repeated work in loops, unnecessary allocations, blocking I/O on a request thread
- Complexity — algorithmic cost that will not scale (for example O(n²) over growing inputs), unbounded collections
- Resource cost — missing cache/pool, redundant serialisation, eager load where lazy would do
- Start-up & footprint — expensive init, work moved from startup into a hot path, or new background churn

### 4. Spawn both sub-agents in parallel

Send a single message with two `Agent` tool calls. Use the `general-purpose` subagent for both.

**Standards sub-agent prompt** — include:

- The full diff command and commit list.
- The list of standards-source files you found in step 3, **plus the six-dimension baseline from step 3** pasted in full — the sub-agent has no other access to it.
- The brief: "Report — per file/hunk where relevant — (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline finding you spot: name its dimension (and principle or smell) and quote the hunk. Always walk correctness, maintainability, tests, and architecture. Only open security or performance when the diff has real signals. Distinguish hard violations from judgement calls — documented-standard breaches can be hard, but baseline findings are always judgement calls, and a documented repo standard overrides the baseline. Skip anything tooling enforces. Under 400 words."

**Spec sub-agent prompt** — include:

- The diff command and commit list.
- The path or fetched contents of the spec.
- The brief: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

If the spec is missing, skip the Spec sub-agent and note this in the final report.

### 5. Aggregate

Present the two reports under `## Standards` and `## Spec` headings, verbatim or lightly cleaned. Do **not** merge or rerank findings — the two axes are deliberately separate (see _Why two axes_).

End with a one-line summary: total findings per axis, and the worst issue _within each axis_ (if any). Don't pick a single winner across axes — that's the reranking the separation exists to prevent.

## Why two axes

A change can pass one axis and fail the other:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**

Reporting them separately stops one axis from masking the other.
