# Consumer loop evidence

Validation runbooks and per-project friction records for **semver gate** releases. Not default SDD artifacts for projects using the skills.

| Loop | Gate / tag | Runbook | Record(s) |
| --- | --- | --- | --- |
| **第一次** | pre-gate（回溯） | [runbook-first.md](./runbook-first.md) | [todo-web-first.md](./todo-web-first.md) |
| **第二次** | **0.1.0** → `v0.1.0` | [runbook-0.1.0.md](./runbook-0.1.0.md) | [todo-web-0.1.0.md](./todo-web-0.1.0.md) |
| **第三次** | **0.2.0** → `v0.2.0` | [runbook-0.2.0.md](./runbook-0.2.0.md) | [todo-web-0.2.0.md](./todo-web-0.2.0.md) |
| — | **0.2.1** | —（maintainer patch：CI + doc sync） | —（无 consumer gate） |
| **第四次** | **0.3.0**（planned）→ `v0.3.0` | [runbook-0.3.0.md](./runbook-0.3.0.md)（trial Pass） | [todo-web-0.3.0.md](./todo-web-0.3.0.md) ✅ |

**第一次** 为 greenfield 回溯建档（无 semver gate）。**第二次起** 用 `runbook-<gate>.md` + `<project>-<gate>.md`；结果写入 [CHANGELOG.md](../../../CHANGELOG.md) 与本目录。

## Release grill 共识（2026-06-11）

Maintainer **`sdd-grill`** on next semver + trial scope:

| 决策 | 结论 | 拒绝的替代 |
| --- | --- | --- |
| **下一 tag** | **`v0.3.0`**（minor） | `v0.2.2` patch — 掩盖 `sdd-architect` 移除 breaking |
| **Gate 对象** | 第四次 loop 只验 **`sdd-improve`** | 把 `sdd-zoom` 补 loop 并入同一 gate — 推迟，见 `v0.2.0` 脚注 |
| **Pass 标准** | 独立业务项目：conversation findings report + 摩擦记录；有 findings 则经 **`using-sdd`** 进 SDD loop，或 explicit none-actionable | 本仓 dogfood 代替 consumer trial |
| **Tag 时机** | trial Pass 后 **`sdd-ship`** slice（README pin、`CHANGELOG` 发版节、tag） | 本 increment 直接打 tag（spec non-goal） |

## Watchlist（living）

| 项 | 状态 | 备注 |
| --- | --- | --- |
| **`sdd-improve`** | trial **Pass** → **`v0.3.0` tag** | [todo-web-0.3.0](./todo-web-0.3.0.md)；待 PR merge + ship |
| **`sdd-zoom`** | shipped `v0.2.0` | gate 未单独覆盖；见 [runbook-0.2.0.md](./runbook-0.2.0.md) 脚注 |
| **CONTEXT/ADR L2** | proposed | [engineering-rationale §2.5](../engineering-rationale.md#41-可选-context-与-adr) |
| **context/adr-template** | watchlist | L3，有证据再做 |
