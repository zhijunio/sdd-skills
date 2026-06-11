# 第一次 SDD 闭环 — 运行手册（回溯建档）

Status: **complete**（2026-06-08，todo-web；**回溯**补录 — 当时无 consumer-loops 目录）

Last updated: 2026-06-11

Parent: [consumer-loops/README.md](./README.md)

## 目的

在 **独立业务项目**（greenfield）中首次用 **六核心 SDD 环**交付可用软件，验证 skills 在真实 Spring Boot 项目上的可行性。

> **与 semver gate 的关系：** 第一次闭环 **早于** `v0.1.0` tag 与 `runbook-0.1.0` 制度化；证据见 [todo-web-first.md](./todo-web-first.md)。**第二次**闭环才对应 gate **`0.1.0`** → [runbook-0.1.0.md](./runbook-0.1.0.md)。

本仓当时 **未** 要求 consumer-loops 记录；本文档为 **事后归档**，摩擦表可能不完整。

---

## 0. 前置（回顾）

- [x] `sdd-skills` 核心技能可安装
- [x] todo-web 空仓库就绪
- [x] 无 maintainer 自动 verify gate（`v0.2.1` 曾加 `tests/check.py` + CI；后移除 — 验收靠 consumer loop runbook）

---

## 1. 在业务项目中安装

（回溯 — 与当时实践一致，非现行唯一路径）

```bash
npx skills@latest add zhijunio/sdd-skills -a cursor -a codex -a claude-code -y
```

或按 slice 逐步安装 core skills。consumer 是否提交 `.agents/` 由项目自定（第二次 loop 摩擦 F3 后写入 [runbook-0.1.0](./runbook-0.1.0.md) §1）。

---

## 2. 闭环步骤

| # | Stage | 产出 / 检查（todo-web 实例） |
|---|--------|-------------------------------|
| 1 | `sdd-spec` | `docs/sdd/2026-06-08-todo-web-spec.md` + 用户批准 |
| 2 | `sdd-plan` | `docs/sdd/2026-06-08-todo-web-plan.md`（多 slice）+ 用户批准 |
| 3 | `sdd-build` | 按 plan slice 1→4 实现（`e1fcce9`…`960ef75`） |
| 4 | `sdd-review` | 增量 review（无正式 consumer 摩擦表） |
| 5 | `sdd-ship` | 测试 + 手测响应式（plan 声明 manual） |

**注：** greenfield 首交付常 **spec/plan 先行**；`sdd-grill` 在需要时出现。

---

## 3. 记录摩擦

当时 **无** `<project>-first.md` 模板。回溯记录：[todo-web-first.md](./todo-web-first.md)。

---

## 4. 闭环后

| 结果 | 动作（回顾） |
|------|----------------|
| 应用可运行、测试绿 | 继续在同一 consumer 上做 **第二次** 增量（删除确认 → `v0.1.0` gate） |
| — | **未** 因第一次单独打 sdd-skills tag |

---

## 当前状态

| 项 | 状态 |
|----|------|
| 消费者项目 | **todo-web** — [todo-web-first.md](./todo-web-first.md) ✅（回溯） |
| sdd-skills tag | 无独立 gate；能力沉淀进后续 **`v0.1.0`** |
| 下一 loop | [runbook-0.1.0.md](./runbook-0.1.0.md)（第二次） |
