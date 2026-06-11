# 第四次 SDD 闭环 — 运行手册（sdd-improve）

Status: **Pass** — [todo-web-0.3.0](./todo-web-0.3.0.md) Path A ✅

Last updated: 2026-06-11

Parent: [consumer-loops/README.md](./README.md)

## 目的

在 **独立业务项目** 中验证 **`sdd-improve`** optional satellite，为 semver gate 提供摩擦证据：

- 先跑 **`sdd-improve`** → 对话 **findings report**（`Context → Findings → Coverage → Follow-up`），或 explicit **none found**
- 用户 **Confirm** 选定 follow-up 后，hand off 进入 **spec → plan → build → review → ship**（grill 按需；用户 `@` 阶段技能）
- **spec / plan 经用户批准**
- **无 credible findings** 且摩擦可接受 → 仍可 Pass（须写明 examined 范围）
- 记录 **`sdd-improve` 摩擦**（与 core 阶段分开）

本仓 **不** 用 dogfood 代替 consumer 闭环。

---

## 1. 在业务项目中安装

在 **消费者 repo** 根目录：

```bash
npx skills@latest add zhijunio/sdd-skills -s sdd-improve -a cursor -y
```

需 core loop 时一并安装：

```bash
npx skills@latest add zhijunio/sdd-skills \
  -s sdd-grill -s sdd-spec -s sdd-plan -s sdd-build -s sdd-review -s sdd-ship \
  -s sdd-improve -a cursor -y
```

记录 `skills-lock.json` 与 `sdd-skills` ref（tag 或 commit）。

---

## 2. 闭环步骤

| # | Stage | 产出 / 检查 |
|---|--------|-------------|
| 0 | **`sdd-improve`** | 对话报告：骨架见 [finding-format.md](../../../skills/sdd-improve/references/finding-format.md)；**🔴/🟡/🟢** 为 follow-up 优先级（**非** ship gate）；Stop → 点名 next per [closing-the-loop](../../../skills/sdd-improve/references/closing-the-loop.md) |
| 0b | **Confirm** | 用户选定 follow-up（或 explicit none-actionable）；可问 direction（cat 9） |
| 1 | hand off | **`sdd-spec`**（默认）或 **`sdd-grill`**（trade-off 仍开放） |
| 2 | `sdd-grill` | 按需 |
| 3 | `sdd-spec` | `docs/sdd/YYYY-MM-DD-<topic>-spec.md` + **用户批准** |
| 4 | `sdd-plan` | `docs/sdd/YYYY-MM-DD-<topic>-plan.md` + **用户批准** |
| 5 | `sdd-build` | 按 slice；无 scope 外改动 |
| 6 | `sdd-review` | **交付审** — increment diff only；与 improve **机会扫描** 勿混用 |
| 7 | `sdd-ship` | Fresh verification；consumer 仓执行 |

### Stage 0 建议触发语（consumer 侧）

- 「用 **sdd-improve** 做一次 codebase health check」
- 「**improve** 这个 repo，重点 architecture + tests」
- 「这个分支相对 main 改了什么风险？」（branch scope → `introduced` / `pre-existing` 标签）

**勿** 用本 loop 验证「整仓 delivery review」— 那是 **`sdd-review`** 在 **increment diff** 上的职责。

### Pass 路径（二选一）

| 路径 | 条件 |
|------|------|
| **A — findings → SDD** | ≥1 个用户确认的 follow-up 走完 spec/plan/build/review/ship |
| **B — none-actionable** | improve 报告 explicit none found 或用户不选任何 finding；**Coverage — Examined** 与 **Limits** 可信；摩擦记录完整 |

---

## 3. 记录摩擦

闭环结束后在本仓新增：

```text
docs/design/consumer-loops/<project>-0.3.0.md
```

从下方 **模板** 复制填写。摘要写回 [CHANGELOG.md](../../../CHANGELOG.md) 与本目录 [README](./README.md) gate 表。

**须单独记录 `sdd-improve` 阶段摩擦**，至少覆盖：

- 报告骨架是否齐全
- Disambiguation：是否误用 delivery review
- 只读约束：扫描中是否出现 mutating 命令
- 无 findings 路径是否可信
- 对话 → 闭环记录的人工搬运（by design，是否可接受）

---

## 4. 闭环后（本仓 maintainer）

| 结果 | 动作 |
|------|------|
| Pass + 摩擦可接受 | **`sdd-ship`** slice：`CHANGELOG` 发版节、README pin、`tag` |
| 有 must-fix（skill/docs） | 本仓 PR → `check.py` → 再评估 |
| improve 无 credible 输出 | 换 consumer 增量或加深 scope |
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
- sdd-skills ref: tag or commit
- Consumer branch:
- Consumer delivery commit (if path A):

## Stage log

| Stage | Used | Pass | Notes |
|-------|------|------|-------|
| **sdd-improve** | | | standard / quick / deep；range: whole repo / branch |
| Confirm (user) | | | findings selected / none-actionable |
| hand off | | | |
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
