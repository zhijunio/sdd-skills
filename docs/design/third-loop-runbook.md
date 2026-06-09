# 第三次 SDD 闭环 — 运行手册（sdd-architect）

Status: **in progress**（2026-06-09，todo-web）

Last updated: 2026-06-09

Parent: [project-decisions.md](./project-decisions.md) §8

## 目的

在 **独立业务项目** 中验证 **`sdd-architect`** optional satellite 可用，并为 **`v0.2.0`** 提供摩擦证据。通过标准（grill 共识）：

- 先跑 **`sdd-architect`** → 对话交付候选（或 explicit none-found）
- 用户选定候选后，经 **`using-sdd`** 进入 **spec → plan → build → review → ship**（grill 按需）
- **spec / plan 经用户批准**
- 记录 **`sdd-architect` 摩擦**；must-fix 修完再 **`v0.2.0` tag**

本仓 **不** 用 dogfood 代替此次闭环。

---

## 0. 前置（本仓已完成）

- [x] **`sdd-architect`** 合并 `main`（PR #2）
- [x] `using-sdd` / README satellite 路由

---

## 1. 在业务项目中安装

在 **消费者 repo** 根目录追加 satellite：

```bash
npx skills@latest add zhijunio/sdd-skills -s sdd-architect -a cursor -y
```

或重装全量（含 core + satellite）：

```bash
npx skills@latest add zhijunio/sdd-skills -a cursor -a codex -a claude-code -y
```

记录 `skills-lock.json` 与 `sdd-skills` ref（tag 或 commit）。

---

## 2. 闭环步骤

| # | Stage | 产出 / 检查 |
|---|--------|-------------|
| 0 | **`sdd-architect`** | 对话报告：候选字段齐全或 none-found；Stop → `using-sdd` |
| 1 | `using-sdd` | 路由到 spec（或 grill 若 trade-off 仍开放） |
| 2 | `sdd-grill` | 按需；至少 1 决策问答题 |
| 3 | `sdd-spec` | `docs/sdd/YYYY-MM-DD-<topic>-spec.md` + **用户批准** |
| 4 | `sdd-plan` | `docs/sdd/YYYY-MM-DD-<topic>-plan.md` + **用户批准** |
| 5 | `sdd-build` | 按 slice；无 scope 外改动 |
| 6 | `sdd-review` | 固定 Output；pre-existing 非 must-fix |
| 7 | `sdd-ship` | Fresh verification；不自动 push/tag |

---

## 3. 记录摩擦

闭环结束后在本仓新增或更新：

```text
docs/design/third-loop-<project-name>.md
```

摘要写回 [project-decisions.md](./project-decisions.md) 时间线与 §8。

**须单独记录 `sdd-architect` 阶段摩擦**（与 core 阶段分开）。

---

## 4. 闭环后

| 结果 | 动作 |
|------|------|
| 无 must-fix + deepen 证据充分 | 打 **`v0.2.0`** tag；CHANGELOG `[Unreleased]` → release |
| 有 must-fix | 本仓小 PR 修 skill/docs → `check.py` → 再评估 tag |
| deepen 无 credible 候选 | 换 consumer 增量或换项目；**不** 为 tag 硬造 churn |

---

## 模板（复制为 `third-loop-<project>.md`）

见 [third-loop-todo-web.md](./third-loop-todo-web.md) 结构。

---

## 当前状态

| 项 | 状态 |
|----|------|
| 消费者项目 | **todo-web** — [third-loop-todo-web.md](./third-loop-todo-web.md) 🔄 |
| **`v0.2.0` tag** | 待定 |
