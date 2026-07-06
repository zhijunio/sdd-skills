---
name: sdd-review
description: >
  Review a scoped increment diff before delivery. Use when the user wants a branch, PR, WIP change, or "review since X" checked against repo standards and the originating spec. Not whole-repo health audit.
---

# sdd-review

Two-axis delivery review of an increment diff:

- **Standards** — does the diff conform to this repo's documented standards and baseline quality bar?
- **Spec** — does the diff faithfully implement the originating issue / PRD / spec / plan?

Both axes may run as parallel sub-agents so they do not pollute each other's context. This skill aggregates their findings and gives a delivery verdict. Read-only: no file edits, plan edits, commits, or fixes.

## Process

### 1. Pin the scope

Use the fixed point or range the user supplies: commit SHA, branch, tag, PR, `main`, `HEAD~5`, etc.

If they did not specify one, infer from the current task/spec/plan or current branch merge-base. Ask only when the scope is ambiguous: path-only request, unrelated dirty files, unknown integration branch, multiple topics, or a very large diff.

For a very large diff, triage before deep review: record file count and diffstat, group changed files by subsystem, identify public API / docs / tests / build / migration hotspots, then inspect the highest-risk hunks first. If time or context limits prevent full coverage, say exactly which groups were sampled and which remain unreviewed.

Capture once:

- Diff command: `git diff <fixed-point>...HEAD` when a fixed point exists
- WIP commands when scope includes working tree changes: `git diff` and `git diff --cached`
- WIP file list: `git status --short` so untracked files are not missed
- Commit list: `git log <fixed-point>..HEAD --oneline` when useful
- Diff kind: `code` / `prose/docs-only`; mixed diffs count as `code`

Confirm the scope resolves and has reviewable changes before reviewing. Bad ref or empty committed/staged/unstaged scope fails here, not inside sub-agents.

### 2. Identify the spec source

Look for the originating contract, in this order:

- A spec / plan path the user passed
- Issue or PR references in commit messages
- A PRD/spec file under `docs/`, `specs/`, or `wiki/` matching the branch or feature
- Repository docs that define expected behavior for this increment

If nothing is found, disclose it. Skip the Spec axis only when no local source is discoverable or the user says there is no spec. In that case, do not claim **Spec pass**. For an SDD delivery gate, do not route to `sdd-ship` unless the user explicitly accepts a standards-only review; otherwise route to `sdd-spec` / `sdd-plan`.

### 3. Identify the standards sources

Use repo guidance such as `AGENTS.md`, README, CONTRIBUTING, CODING_STANDARDS, CI docs, and touched-area conventions.

On top of documented standards, carry this baseline:

- **Correctness** — changed code behaves correctly under real inputs, edge cases, failures, state, lifecycle, and concurrency.
- **Maintainability** — names, duplication, KISS, DRY, SLAP, YAGNI, immutability, and avoidable complexity stay reasonable.
- **Tests / verification** — changed behavior has convincing behavior-focused coverage, CI/local verification covers the risk, or there is a deterministic alternative proof.
- **Docs / traceability / compatibility** — spec, plan, CHANGELOG, links, install examples, public APIs, config keys, package names, migration paths, skill lists, and routing tables still match the tree.
- **Architecture** — for code diffs only: boundaries, responsibilities, dependency direction, half migrations, dead code, parallel APIs, and large duplication.
- **Conditionals** — security, performance, dependencies, data/migration/persistence, observability, accessibility, and operations only when the diff has real signals.

Repo standards override the baseline. Baseline findings are judgement calls; documented-standard breaches may be hard violations. Skip style nits already enforced by tooling.

### 4. Review both axes

Prefer two parallel sub-agents when available.

**Standards brief:** inspect the scoped diff against documented standards and the baseline. Quote file/hunk evidence. Classify each finding as **🔴 must-fix**, **🟡 should-fix**, or **🟢 suggestion**.

**Spec brief:** compare the scoped diff to the spec/plan. Report missing/partial requirements, scope creep, and wrong-looking implementations. Quote spec lines when possible. Classify each finding as **🔴 must-fix**, **🟡 should-fix**, or **🟢 suggestion**.

If sub-agents are unavailable, run the two passes sequentially and disclose that in Coverage.

Run only relevant, non-mutating verification commands when they materially reduce uncertainty. Report command outcomes as evidence, not as a substitute for review. Tie each skipped command to the risk it leaves open, especially for integration tests, generated docs, package metadata, and release notes.

### 5. Aggregate

Present `Standards` and `Spec` separately. Do not merge or rerank the axes.

Delivery verdict:

- **blocked** — any unresolved **🔴 must-fix**
- **pass** — no unresolved **🔴 must-fix** and no unaccepted **🟡 should-fix**
- **pass pending risk acceptance** — no **🔴 must-fix**, but **🟡 should-fix** remains for the user to accept or route to `sdd-build`

End with one next route:

- **`sdd-build`** when blocked
- **`sdd-ship`** when pass
- **`sdd-spec`** when the spec/AC must change before judging the diff

## Present

Write the report in the **user's language** when clear from the latest user turn. Localize section headings too. Keep literal: `AC-n`, `file:line`, git refs, skill ids, and **🔴/🟡/🟢** groups.

Optimize for a clear, readable review, not a formal dump. Findings and verdict matter more than the template, but the reader must be able to scan scope, coverage, evidence, and next route quickly.

Required semantic sections. The English labels below name the slots; do not force them as headings when the user is using another language:

- **Scope** — baseline/range, diff kind, spec source, standards sources
- **Coverage** — examined axes/dimensions, large-diff triage if any, commands run/skipped, and limits
- **Standards**
- **Spec**
- **Verdict**
- **Suggested next steps** — always last

For Chinese output, use headings like **范围**, **覆盖**, **标准**, **规格**, **结论**, **建议下一步**.

## Guidelines

### Delivery groups

| Group | Use when |
| --- | --- |
| **🔴 must-fix** | Blocks delivery: correctness, security, spec/AC gap, data loss, non-goal violation |
| **🟡 should-fix** | Fix unless user accepts risk: half migration, changed-path test gap, meaningful duplication |
| **🟢 suggestion** | Non-blocking: docs, small DRY/KISS, readability in the diff |

### Disambiguation

| Request | Route |
| --- | --- |
| Whole-repo / module / area audit | [`sdd-audit`](../sdd-audit/SKILL.md) |
| Fresh health roadmap | [`sdd-audit`](../sdd-audit/SKILL.md) |
| Final AC evidence / delivery verification | [`sdd-ship`](../sdd-ship/SKILL.md) |
| Fix review findings | [`sdd-build`](../sdd-build/SKILL.md) |

### What NOT to do

Do not:

- Edit files while reviewing
- Treat whole-repo patterns as must-fix unless the diff introduced or worsened them
- Use audit P0/P1/P2 as the delivery gate
- Claim spec compliance without reading the spec when it exists
- Pick one winner across Standards and Spec

## Why two axes

A change can pass one axis and fail the other:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks repo conventions → **Spec pass, Standards fail.**

Keeping the axes separate stops one from masking the other.
