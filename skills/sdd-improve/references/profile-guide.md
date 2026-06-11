# Profile Guide

Optional before **Audit** when effort or scope is ambiguous. Skip when user named focus and depth.

**Report:** Profile merges into **Context → Scope** — no `## Profile`. Recon = facts + **Not audited**; Scope = effort / range / in-scope categories. [finding-format.md](finding-format.md).

## Scope fields

**Project type** · **Effort:** quick / standard / deep · **Range:** whole repo / branch vs merge-base · **Categories:** 1–8 (9 on direction ask).

Small repos: recommend **standard** before **quick**; wait for acceptance.

## Natural language → scope

Map user intent to internal labels — no keywords required.

| Intent (examples) | Behavior |
| --- | --- |
| health check, full audit | **standard**, 1–8 |
| quick pass, time-boxed | **quick** |
| deep dive, exhaustive | **deep** |
| architecture, mud-ball, shallow modules | category **5** primarily |
| security / performance / … only | named category |
| this branch, before PR | **branch** scope |
| roadmap, next steps | **9**; trade-offs → `sdd-grill` |
| unclear | **standard** 1–8; run Profile |

## Effort levels

| | quick | standard (default) | deep |
| --- | --- | --- | --- |
| Coverage | Hotspots | Hotspot-weighted | Whole repo; monorepo → per-package |
| Subagents | 0–1 | **≤4** | **≤8** |
| Categories | correctness, security, tests (~HIGH) unless narrowed | **1–8**; **9** on direction ask | **1–9** unless in Recon **Not audited** |
| Findings | top ~6, HIGH only | full verified list | full incl. LOW |

## Skip rules

Every skip → **Recon — Not audited** with a **project-specific** reason. Do not skip **architecture** (5) when user named architecture intent.
