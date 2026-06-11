# Profile Guide

Optional **Profile** step before **Audit** when effort or scope is ambiguous. Skip when the user already named focus and depth.

**Report rule:** **Recon** (always) and **Scope** (Profile merges here) are separate sections — never a `## Profile` heading. Recon = territory facts; Scope = effort/range/categories/skips.

## Scope section (report)

```markdown
## Scope

- **Project type:** e.g. skills repo, app, library, monorepo
- **Effort:** quick / standard / deep (inferred)
- **Range:** whole repo / branch vs merge-base
- **Categories:** names or numbers 1–8; 9 only when user asks direction
- **Skipped:** category — project-specific reason
```

On small repos, recommend **standard** before downgrading to **quick**; wait for acceptance.

## Natural language → scope (internal labels)

Users describe intent in natural language. Map to internal labels — users need not type keywords.

| User intent (examples) | Inferred behavior |
| --- | --- |
| 体检、全面看看、audit | **standard**, categories 1–8 |
| 快速扫一眼、时间紧 | **quick** |
| 仔细、深入、deep dive | **deep** |
| 只看架构、泥球、浅模块 | category **5 architecture** primarily |
| 只看安全 / 性能 / … | named category primarily |
| 这个分支、PR 前、改了什么 | **branch** scope |
| 下一步、路线图 | category **9** direction; trade-offs → `sdd-grill` |
| 没说清 | **standard** 1–8; run Profile → fill **Scope** |

## Effort levels

| | quick | standard (default) | deep |
| --- | --- | --- | --- |
| Coverage | Hotspots — churn / criticality | Hotspot-weighted, key packages | Whole repo; monorepo → per-package |
| Subagents | 0–1 | **≤4 concurrent** | **≤8 concurrent** |
| Categories | correctness, security, tests (~HIGH) unless narrowed | **1–8**; **9** only on direction ask | **1–9** unless skipped in Scope |
| Findings | top ~6, HIGH-confidence only | full verified list | full list incl. LOW investigate |

## Skip rules

Name every skipped category in **Scope** with a **project-specific** reason (e.g. no runtime code → skip performance). Do not skip **architecture** (category 5) when user named architecture intent.
