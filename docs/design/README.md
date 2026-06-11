# Design Documents

Decision and methodology records for the **sdd-skills repository**. These are **not** default SDD artifacts for projects using the skills.

Runtime contracts: `skills/<name>/SKILL.md` and [SOURCES.md](../../SOURCES.md).

## Reading order

| Order | Document | When to read |
| --- | --- | --- |
| 1 | [software-engineering-rationale.md](./software-engineering-rationale.md) | 本仓工程观（直白中文；含可选 CONTEXT/ADR §4.1） |
| 2 | [upstream-engineering-rationale.md](./upstream-engineering-rationale.md) | 上游与 [shadcn/improve](https://github.com/shadcn/improve) 怎么取舍 |
| — | [consumer-loops/](./consumer-loops/) | Semver gate validation runbooks and per-project evidence |

## Index

| Document | Scope | Status |
| --- | --- | --- |
| [software-engineering-rationale.md](./software-engineering-rationale.md) | Principles, thinking, anti-patterns, CONTEXT/ADR north star | living |
| [upstream-engineering-rationale.md](./upstream-engineering-rationale.md) | Upstream repos at pinned commits in SOURCES | living |
| [consumer-loops/](./consumer-loops/) | Gate runbooks + per-project friction records | see [index](./consumer-loops/README.md) |

Maintainer Git workflow: [AGENTS.md](../../AGENTS.md). Release history: [CHANGELOG.md](../../CHANGELOG.md).
