# 第四次 SDD 闭环 — 运行手册（sdd-improve）

Status: **draft**（待 `main` 合并 **`sdd-improve`** 增量后启动 consumer trial）

Last updated: 2026-06-11

Parent: [consumer-loops/README.md](./README.md)

## 目的

在 **独立业务项目** 中验证 **`sdd-improve`** optional satellite 可用，并为 **`v0.3.0`** 提供摩擦证据。通过标准（[Release grill 共识](./README.md#release-grill-共识2026-06-11)）：

- 先跑 **`sdd-improve`** → 对话 **findings report**（`Context → Findings → Coverage → Follow-up`），或 explicit **none found**（AC-3）
- 用户 **Confirm** 选定 follow-up 后，经 **`using-sdd`** 进入 **spec → plan → build → review → ship**（grill 按需）
- **spec / plan 经用户批准**
- **无 credible findings** 且摩擦可接受 → 仍可 Pass（须写明 examined 范围，不得硬造 churn）
- 记录 **`sdd-improve` 摩擦**（与 core 阶段分开）；must-fix 修完本仓 skill/docs 后再 **`v0.3.0` tag**

> **v0.3.0 发布范围：** tag gate **仅 `sdd-improve`**（接替已移除的 **`sdd-architect`**）。**`sdd-zoom`** 不纳入本 loop — 见 [watchlist](./README.md#watchlistliving) 与 [runbook-0.2.0](./runbook-0.2.0.md) 脚注。

本仓 **不** 用 dogfood 代替此次闭环。

---

## 0. 前置（本仓）

- [ ] **`sdd-improve`** 合并 `main`（含 **`sdd-architect`** 移除、`audit-dimensions.md`、`using-sdd` Disambiguation）
- [x] `runbook-0.3.0.md` 起草
- [ ] `python3 tests/check.py` 在 `main` 通过

---

## 1. 在业务项目中安装

在 **消费者 repo** 根目录。tag **`v0.3.0`** 发布前，从 **`main`** 装 satellite（或 pin 合并 commit）：

```bash
npx skills@latest add zhijunio/sdd-skills -s sdd-improve -a cursor -y
```

需 core loop 时一并安装：

```bash
npx skills@latest add zhijunio/sdd-skills \
  -s using-sdd -s sdd-grill -s sdd-spec -s sdd-plan -s sdd-build -s sdd-review -s sdd-ship \
  -s sdd-improve -a cursor -y
```

**迁移：** 若曾装 **`sdd-architect`** 或 **`sdd-deepen`**，删除旧目录后重装 **`-s sdd-improve`**。

记录 `skills-lock.json` 与 `sdd-skills` ref（commit；`v0.3.0` 前勿假设 tag 含 improve）。

---

## 2. 闭环步骤

| # | Stage | 产出 / 检查 |
|---|--------|-------------|
| 0 | **`sdd-improve`** | 对话报告：骨架见 [finding-format.md](../../../skills/sdd-improve/references/finding-format.md)；**🔴/🟡/🟢** 为 follow-up 优先级（**非** ship gate）；Stop → **`using-sdd`** only |
| 0b | **Confirm** | 用户选定 follow-up（或 explicit none-actionable）；可问 direction（cat 9） |
| 1 | `using-sdd` | 路由到 **`sdd-spec`**（默认）或 **`sdd-grill`**（trade-off 仍开放） |
| 2 | `sdd-grill` | 按需 |
| 3 | `sdd-spec` | `docs/sdd/YYYY-MM-DD-<topic>-spec.md` + **用户批准** |
| 4 | `sdd-plan` | `docs/sdd/YYYY-MM-DD-<topic>-plan.md` + **用户批准** |
| 5 | `sdd-build` | 按 slice；无 scope 外改动 |
| 6 | `sdd-review` | **交付审** — increment diff only；与 improve **机会扫描** 勿混用 |
| 7 | `sdd-ship` | Fresh verification；**本仓** tag 由 maintainer 在 trial Pass 后执行 |

### Stage 0 建议触发语（consumer 侧）

任选其一，覆盖 **standard**（categories 1–8）即可：

- 「用 **sdd-improve** 做一次 codebase health check」
- 「**improve** 这个 repo，重点 architecture + tests」
- 「这个分支相对 main 改了什么风险？」（branch scope → `introduced` / `pre-existing` 标签）

**勿** 用本 loop 验证「整仓 delivery review」— 那是 **`sdd-review`** 在 **increment diff** 上的职责。

### Pass 路径（二选一）

| 路径 | 条件 |
|------|------|
| **A — findings → SDD** | ≥1 个用户确认的 follow-up 走完 spec/plan/build/review/ship（或 review pass + ship 在 consumer 仓） |
| **B — none-actionable** | improve 报告 explicit none found 或用户不选任何 finding；**Coverage — Examined** 与 **Limits** 可信；摩擦记录完整 |

---

## 3. 记录摩擦

闭环结束后在本仓新增：

```text
docs/design/consumer-loops/<project>-0.3.0.md
```

从下方 **模板** 复制填写。摘要写回 [CHANGELOG.md](../../../CHANGELOG.md) `[Unreleased]` 与本目录 [README](./README.md) gate 表。

**须单独记录 `sdd-improve` 阶段摩擦**（与 core 阶段分开），至少覆盖：

- 报告骨架是否齐全（Recon / Scope / Findings / Coverage / Follow-up）
- Disambiguation：是否误用 delivery review
- 只读约束：扫描中是否出现 mutating 命令
- 无 findings 路径是否可信（AC-3）
- 对话 → 闭环记录的人工搬运（by design，是否可接受）

---

## 4. 闭环后（本仓 maintainer）

| 结果 | 动作 |
|------|------|
| Pass + 摩擦可接受 | **`sdd-ship`** slice：`CHANGELOG` 发版节、README pin `@v0.3.0`、打 tag |
| 有 must-fix（skill/docs） | 本仓小 PR → `check.py` → 再跑 consumer 或补记录 → 再评估 tag |
| improve 无 credible 输出 | 换 consumer 增量、换项目或加深 scope；**不** 为 tag 硬造 churn |
| 仅 nice friction | 记入 `<project>-0.3.0.md`；不阻塞 tag |

---

## 模板（复制为 `<project>-0.3.0.md`）

```markdown
# Fourth loop: <project-name> (sdd-improve)

Date:
Consumer repo:
Increment (one sentence):

## Environment

- Agent(s):
- skills install scope: project / global
- sdd-skills ref: commit (pre-v0.3.0) or tag
- Consumer branch:
- Consumer delivery commit (if path A):
- Prior loops: [todo-web-0.2.0.md](./todo-web-0.2.0.md)（可选）

## Stage log

| Stage | Used | Pass | Notes |
|-------|------|------|-------|
| **sdd-improve** | | | standard / quick / deep；range: whole repo / branch |
| Confirm (user) | | | findings selected / none-actionable |
| using-sdd | | | |
| sdd-grill | | | |
| sdd-spec | | | |
| sdd-plan | | | |
| sdd-build | | | |
| sdd-review | | | increment diff only |
| sdd-ship | | | consumer 仓 only |

## sdd-improve deliverable (summary)

**Pass path:** A (findings → SDD) / B (none-actionable)

### Context (abbrev.)

- Effort:
- Range:
- Categories audited:
- Not audited:

### Findings (count)

| Group | Count | Top item (one line) |
|-------|-------|---------------------|
| 🔴 must-fix | | |
| 🟡 should-fix | | |
| 🟢 suggestion | | |

**User selected for follow-up:** #… / none

### Coverage

- Examined:
- Limits / rejected:

## Friction (sdd-improve)

| ID | Severity (must/should/nice) | Description | Fix in sdd-skills? |
|----|----------------------------|-------------|-------------------|
| I1 | | | |

## Friction (core loop)

| ID | Stage | Severity | Description | Fix in sdd-skills? |
|----|-------|----------|-------------|-------------------|

## Verdict

- [ ] Pass (path A or B per runbook-0.3.0)
- [ ] Blocked — reason:

## Follow-ups

-
```

---

## 推荐 consumer 场景（非强制）

延续 [todo-web](./todo-web-0.2.0.md) 时可选：

- **whole repo** — 测试/架构接缝是否还有 improve 信号（对比 0.2.0 已做 test fixtures）
- **branch scope** — 某 feature 分支的 `introduced` vs `pre-existing` 标签是否好用

也可用 **新项目** 或 **无 SDD 历史的存量仓**，以验证「无 CONTEXT/ADR 仍可 improve」（AC-4）。

---

## 当前状态

| 项 | 状态 |
|----|------|
| Runbook | **draft**（本文件） |
| 消费者项目 | 待定 — `<project>-0.3.0.md` |
| **`v0.3.0` tag** | 待 trial Pass |
| 前置 PR | 待 **`sdd-improve`** 合并 `main` |
