# Profile Guide

Optional **Profile** step before **Audit** when effort or scope is ambiguous. Skip when the user already named focus and depth.

**Report rule:** **Recon** (always) and **Scope** (Profile merges here) are separate sections — never a `## Profile` heading. Recon = territory facts + **Not audited** (skips/limits); Scope = effort / range / **in-scope categories only**.

## Scope section (report)

```markdown
## Scope

- **Project type:** e.g. skills repo, app, library, monorepo
- **Effort:** quick / standard / deep (inferred)
- **Range:** whole repo / branch vs merge-base
- **Categories:** in-scope names or numbers 1–8; 9 only when user asks direction
```

On small repos, recommend **standard** before downgrading to **quick**; wait for acceptance.

## Natural language → scope (internal labels)

Users describe intent in natural language (any locale). Map to internal labels — users need not type keywords.

| User intent (examples) | Inferred behavior |
| --- | --- |
| health check, full audit, codebase review | **standard**, categories 1–8 |
| quick pass, time-constrained | **quick** |
| deep dive, exhaustive | **deep** |
| architecture only, mud-ball, shallow modules | category **5 architecture** primarily |
| security / performance / … only | named category primarily |
| this branch, before PR, what changed | **branch** scope |
| roadmap, next steps, direction | category **9** direction; trade-offs → `sdd-grill` |
| unclear | **standard** 1–8; run Profile → fill **Scope** |

Effort levels (quick / standard / deep): normative table in [SKILL.md — Process](../SKILL.md#process).

## Skip rules

Name every skipped category or audit limit in **Recon — Not audited** with a **project-specific** reason (e.g. no runtime code → skip performance). Do not skip **architecture** (category 5) when user named architecture intent.
