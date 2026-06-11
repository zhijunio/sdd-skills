# First loop: todo-web（回溯）

Date: 2026-06-08
Consumer repo: `zhijunio/todo-web`
Increment (one sentence): Greenfield — 从零交付可持久化的 Todo Web（spec 多 slice 至响应式 UI）

> **Archival:** 补录于 2026-06-11。当时无 consumer-loops 目录；摩擦表为回顾性摘要。

## Environment

- Agent(s): Cursor
- skills install scope: project（`.agents/skills/`，后纳入 git 由 consumer 决定）
- sdd-skills ref: project install（后 pin **`v0.1.0`**）
- Consumer delivery range: `e1fcce9`（spec/plan）… `960ef75`（UI + README）
- SDD artifacts: `docs/sdd/2026-06-08-todo-web-spec.md`、`docs/sdd/2026-06-08-todo-web-plan.md`

## Stage log

| Stage | Used | Pass | Notes |
|-------|------|------|-------|
| hand off | skip | yes | greenfield 以 spec/plan 驱动为主 |
| sdd-grill | skip | — | 首交付边界在 spec 已写明 |
| sdd-spec | yes | yes | `2026-06-08-todo-web-spec.md` |
| sdd-plan | yes | yes | 4 slices（create → edit → toggle/delete → responsive） |
| sdd-build | yes | yes | `8be82bb` … `960ef75` |
| sdd-review | yes | yes | 无正式模板摩擦记录 |
| sdd-ship | yes | yes | `./mvnw test`；AC 响应式手测（plan 声明） |

## Delivery commits（摘要）

| Commit | Summary |
|--------|---------|
| `e1fcce9` | 确定 Todo Web 规格与实施计划 |
| `8be82bb` | 实现 Todo 新增与文件持久化 |
| `6887695` | 实现 Todo 标题编辑与异常反馈 |
| `c920c16` | 实现 Todo 状态切换与删除 |
| `960ef75` | 完善响应式界面与运行文档 |

## Friction（回顾性）

| ID | Stage | Severity | Description | Fix in sdd-skills? |
|----|-------|----------|-------------|-------------------|
| H1 | process | should | 第一次无 consumer-loops 记录约定，摩擦未结构化留存 | yes — 第二次起 `runbook-0.1.0` + 模板 |
| H2 | sdd-plan | nice | 多 slice 跨多次 commit，spec/plan 与代码 commit 边界松散 | no — 绿field 常见 |
| H3 | skills | nice | 试验期 skill 名（`sdd-brainstorm`）与现 `sdd-grill` 不一致 | yes — 已合并更名 |

## Verdict

- [x] Pass（回溯认定 — 应用可用、测试通过、spec/plan 已批准并落地）
- [ ] Blocked — reason:

## Follow-ups

- [x] **第二次 loop** — [todo-web-0.1.0.md](./todo-web-0.1.0.md)（删除确认 → **`v0.1.0`** gate）
- [x] consumer-loops 制度化 — `v0.2.0` 迁至 `docs/design/consumer-loops/`
