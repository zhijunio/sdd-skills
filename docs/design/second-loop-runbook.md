# 第二次 SDD 闭环 — 运行手册

Status: **complete**（2026-06-09，todo-web）

Last updated: 2026-06-09

Parent: [project-decisions.md](./project-decisions.md) §8

## 目的

在 **独立业务项目** 中验证 7 技能交付环可用，为 **0.1.0** 提供证据。通过标准（grill 共识）：

- 跑满 **grill → spec → plan → build → review → ship**
- **spec / plan 经用户批准**
- 记录摩擦；**must-fix 修完再 tag**

本仓 **不** 用 dogfood 代替此次闭环（skill 库缺真实 feature diff）。

---

## 0. 前置（本仓已完成）

- [x] README Installation（`5926403`）
- [x] push `origin/main` — 远程 **7 skills**（无 `sdd-brainstorm`）

---

## 1. 在业务项目中安装

在 **消费者 repo** 根目录：

```bash
npx skills@latest add zhijunio/sdd-skills -a cursor -a codex -a claude-code -y
```

或最小集：

```bash
npx skills@latest add zhijunio/sdd-skills -s using-sdd -s sdd-grill -s sdd-spec -s sdd-plan -s sdd-build -s sdd-review -s sdd-ship -y
```

确认本地 agent 读到的是合并后的 **`sdd-grill`**（非旧版 `sdd-brainstorm`）。

**Consumer git：** `.agents/` 与 `skills-lock.json` 为安装器产物；是否提交由业务项目决定（本闭环未纳入 `8770a82`）。

---

## 2. 闭环步骤

| # | Stage | 产出 / 检查 |
|---|--------|-------------|
| 1 | `using-sdd` | 路由合理，只推荐一个 next skill |
| 2 | `sdd-grill` | 至少 1 个决策问答题；Explore 或 Challenge |
| 3 | `sdd-spec` | `docs/sdd/YYYY-MM-DD-<topic>-spec.md` + **用户批准** |
| 4 | `sdd-plan` | `docs/sdd/YYYY-MM-DD-<topic>-plan.md` + **用户批准** |
| 5 | `sdd-build` | 按 slice TDD；无 scope 外改动 |
| 6 | `sdd-review` | 固定 Output；pre-existing 非 must-fix |
| 7 | `sdd-ship` | Fresh verification；不自动 push |

---

## 3. 记录摩擦

闭环结束后在本仓新增：

```text
docs/design/second-loop-<project-name>.md
```

从下方 **模板** 复制填写。摘要写回 [project-decisions.md](./project-decisions.md) 时间线与 §8。

---

## 4. 闭环后

| 结果 | 动作 |
|------|------|
| 无 must-fix | 打 **0.1.0** tag；README 可写推荐 install 版本 |
| 有 must-fix | 本仓小 PR 修 skill/docs → `check.py` → 再评估 tag |
| 重复 CONTEXT/ADR 痛点 | 评估 [context-adr-workflow.md](./context-adr-workflow.md) L2 |

---

## 模板（复制为 `second-loop-<project>.md`）

```markdown
# Second loop: <project-name>

Date:
Consumer repo:
Increment (one sentence):

## Environment

- Agent(s):
- skills install scope: project / global
- sdd-skills ref: commit or tag

## Stage log

| Stage | Used | Pass | Notes |
|-------|------|------|-------|
| using-sdd | | | |
| sdd-grill | | | |
| sdd-spec | | | |
| sdd-plan | | | |
| sdd-build | | | |
| sdd-review | | | |
| sdd-ship | | | |

## Friction

| ID | Stage | Severity (must/should/nice) | Description | Fix in sdd-skills? |
|----|-------|----------------------------|-------------|-------------------|

## Verdict

- [ ] Pass (full loop + approved spec/plan)
- [ ] Blocked — reason:

## Follow-ups

- 
```

---

## 当前状态

| 项 | 状态 |
|----|------|
| 消费者项目 | **todo-web** — [second-loop-todo-web.md](./second-loop-todo-web.md) ✅ |
| `second-loop-*.md` | [second-loop-todo-web.md](./second-loop-todo-web.md) |
| 0.1.0 tag | **`v0.1.0`**（2026-06-09） |
