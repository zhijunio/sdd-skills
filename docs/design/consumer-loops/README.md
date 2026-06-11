# Consumer loop evidence

Validation runbooks and per-project friction records for **semver gate** releases. Not default SDD artifacts for projects using the skills.

| Loop | Gate / tag | Runbook | Record(s) |
| --- | --- | --- | --- |
| **第一次** | pre-gate（回溯） | [runbook-first.md](./runbook-first.md) | [todo-web-first.md](./todo-web-first.md) |
| **第二次** | **0.1.0** → `v0.1.0` | [runbook-0.1.0.md](./runbook-0.1.0.md) | [todo-web-0.1.0.md](./todo-web-0.1.0.md) |
| **第三次** | **0.2.0** → `v0.2.0` | [runbook-0.2.0.md](./runbook-0.2.0.md) | [todo-web-0.2.0.md](./todo-web-0.2.0.md) |
| — | **0.2.1** | —（maintainer patch） | — |
| **第四次** | **0.3.0** | [runbook-0.3.0.md](./runbook-0.3.0.md) | [todo-web-0.3.0.md](./todo-web-0.3.0.md) ✅ |

**Maintainer delta** (prose-only satellite tail refactor after 0.3.0 Pass): [maintainer-delta-2026-06-11.md](./maintainer-delta-2026-06-11.md).

**第一次** 为 greenfield 回溯建档（无 semver gate）。**第二次起** 用 `runbook-<gate>.md` + `<project>-<gate>.md`；结果写入 [CHANGELOG.md](../../../CHANGELOG.md) 与本目录。本仓 **不** 使用 `tests/check.py` — 见 [README — Maintainer verification](../../../README.md#maintainer-verification)。

## Watchlist

| 项 | 状态 | 备注 |
| --- | --- | --- |
| **CONTEXT/ADR L2** | proposed | [engineering-rationale §2.5](../engineering-rationale.md#41-可选-context-与-adr) |
| **context/adr-template** | watchlist | L3，有证据再做 |
