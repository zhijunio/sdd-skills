---
name: sdd-audit
description: >
  Read-only whole-repo, module, area, or branch health audit. Use when the user asks for a repository-wide review, health scan, or architecture/security/tests/deps/ops audit. Not increment delivery review, implementation edits, or Spec review.
---

# sdd-audit

Standards-only health audit of a broad scope:

- **Same content as `sdd-review` Standards** — correctness, maintainability, tests, docs/traceability, architecture, and conditional signals.
- **Different scope from `sdd-review`** — repo, module, area, or branch instead of an increment diff.

Read-only: no file edits, plan edits, installs, formatters, commits, or fixes. Do not audit **Spec** or AC compliance here; scoped delivery Spec review belongs to [`sdd-review`](../sdd-review/SKILL.md).

## Process

### 1. Pin the scope

Use the scope the user supplies: whole repo, branch, module, directory, package, or named area.

If they did not specify one, default to the current repository. Ask only when the target repo/path is unclear, the request sounds like an increment diff review, or multiple unrelated scopes are present.

Capture once:

- Target path and audit scope
- Git branch, `HEAD`, and `git status --short` when inside a git repo
- Branch baseline and changed files when the user asks for branch audit
- Effort: `snapshot` / `standard` / `deep`; default `standard`

For large scopes, triage before deep reading: identify stack, entrypoints, modules, manifests, CI/deploy files, docs, churn hotspots, and public surfaces. State sampled and skipped areas in Coverage.

### 2. Identify standards sources

Use repo guidance such as `AGENTS.md`, README, CONTRIBUTING, CODING_STANDARDS, CI docs, manifests, and touched-area conventions.

On top of documented standards, carry the same Standards baseline as `sdd-review`:

- **Correctness** — real inputs, edge cases, failures, state, lifecycle, concurrency.
- **Maintainability** — names, duplication, KISS, DRY, SLAP, YAGNI, immutability, avoidable complexity.
- **Tests / verification** — behavior-focused coverage, CI/local verification covers the risk, or deterministic proof.
- **Docs / traceability / compatibility** — README, AGENTS, wiki, CHANGELOG, install examples, public APIs, config keys, package names, migration paths, routing tables, and public docs match the tree.
- **Architecture** — boundaries, responsibilities, dependency direction, half migrations, dead code, parallel APIs, large duplication.
- **Conditionals** — security, performance, dependencies, data/migration/persistence, observability, accessibility, and operations only when the scope has real signals.

Repo standards override the baseline. Baseline findings are judgement calls; documented-standard breaches may be hard violations. Skip style nits already enforced by tooling.

### 3. Audit

Inspect systemic patterns first, not isolated nits. Prefer findings that repeat across a module, boundary, workflow, or public surface.

Classify each finding as:

- **🚨 Critical** — systematic contract break, secret/auth class issue, or source-of-truth divergence that blocks safe follow-up work.
- **🔴 High** — boundary violation, major verification gap, critical dependency/security/ops risk, or widespread correctness risk.
- **🟡 Medium** — duplication tax, meaningful test/doc drift, local architecture debt, observability gap.
- **🟢 Low** — minor drift or smell without broad impact.

Severity is follow-up priority, not a delivery gate.

Run only read-only verification commands when they materially reduce uncertainty. Report command outcomes as evidence, not as a substitute for audit. If cheap checks are skipped, state the residual risk.

### 4. Present

Write the report in the user's language when clear from the latest user turn. Localize section headings too. Keep literal: paths, `file:line`, git refs, skill ids, and severity emojis.

Required semantic sections. The English labels below name the slots; do not force them as headings when the user is using another language:

- **Scope** — target, effort, branch/range when relevant, standards sources
- **Coverage** — examined dimensions, commands run/skipped, sampled/skipped areas, limits
- **Standards** — severity groups + numbered finding cards with evidence, location, and fix
- **Strengths** — optional, only evidence-backed systemic positives
- **Roadmap** — P0/P1/P2 follow-up sequence when findings exist
- **Suggested next steps** — always last; name one next route

For Chinese output, use headings like **范围**, **覆盖**, **标准**, **健康面**, **路线图**, **建议下一步**.

Finding card:

```markdown
**1. Short finding title**
- **Evidence:** observed or inferred evidence
- **Location:** `path:line`
- **Fix:** systemic move, not a typo fix
- **Meta:** optional confidence, effort, risk, branch attribution
```

## Guidelines

### Effort

| Level | Use when |
| --- | --- |
| `snapshot` / 快照 | Fast scan, up to 5 findings |
| `standard` / 标准 | Default audit, up to 20 findings |
| `deep` / 深度 | Broad audit with extra verification and explicit skipped areas |

### Trigger hints

| Request | Focus |
| --- | --- |
| architecture / 架构 | Boundaries, responsibilities, dependency direction, extension seams |
| security / 安全 | Secrets, auth, injection, unsafe APIs, sensitive data |
| tests / 测试 | Coverage, behavior focus, CI proof, flaky or missing gates |
| deps / 依赖 / dx | Dependency drift, manifests, local setup, install/docs |
| ops / release / deploy | Release, deploy, rollback, runtime health, migration order |
| simplicity / 简化 / 过度设计 | Delete, merge, collapse, remove speculative abstraction |
| branch / 分支审查 | Scope to branch changes plus direct callers/importers when tractable |

### Disambiguation

| Request | Route |
| --- | --- |
| Increment diff delivery review | [`sdd-review`](../sdd-review/SKILL.md) |
| Spec / AC compliance | [`sdd-review`](../sdd-review/SKILL.md) for a scoped diff, or [`sdd-spec`](../sdd-spec/SKILL.md) when the contract is missing |
| Trade-offs / design interview | [`sdd-grill`](../sdd-grill/SKILL.md) |
| Implement fixes during scan | Decline; audit first, implement after Stop |

### What NOT to do

Do not:

- Edit the target repo while auditing
- Treat audit severity as a delivery gate
- Duplicate `sdd-review` on a scoped PR diff
- Audit Spec or AC compliance
- Emit one-line findings without evidence

## Stop

After **Suggested next steps**, hand off. Do not auto-chain. Pick one route: usually ask the user to choose a finding or roadmap item; use `sdd-plan` only when the user wants an accepted audit roadmap decomposed into implementation slices; use `sdd-build` only when the user explicitly asks to fix concrete findings; use `sdd-spec` only when the next step is to define or revise a behavior contract.
