# 工程观与上游对照

Status: **living** · 更新: **2026-06-11**

**谁说了算：** 行为 → `skills/*/SKILL.md`；pin 映射 → [SOURCES.md](../../SOURCES.md)；本文 → **为什么这样取舍**。发版记录 → [CHANGELOG.md](../../CHANGELOG.md)。维护细则 → [AGENTS.md](../../AGENTS.md)。

**维护者：** 先改 skill/SOURCES，再同步本文。禁止编造未发生的 consumer 结果或 tag。与 skill 冲突以 skill 为准。

---

## 1. 要治什么毛病

Agent 常见四类问题：做着跑偏 · 范围变大 · 没验证就说完 · 流程太重。

**sdd-skills：** 留下「契约 → 切片 → 实现 → 独立审 → 复验」；去掉项目管理器、平台锁、状态机。不替代 TDD/CI/人工 review — 给 Agent **能停、能跳、能审计** 的阶段语言。

### 1.0 核心原则

六条分三层 — 英文速查见 [README](../../README.md#core-principles)。

| 层 | 原则 | 落地 |
| --- | --- | --- |
| 形态 | 轻量中立 | 短 `SKILL.md`；默认 spec+plan；纯 Markdown |
| 形态 | 显式阶段 | 用户 `@` 点名；**Stop** → hand off；不自动链式 |
| 交付 | 可验切片 | AC；plan 竖切片 15–60 分钟 |
| 交付 | 测试与证明 | build 先红；review 只读有据；ship 重跑验证 |
| 治理 | 借鉴不重造 | pin @ SOURCES；verbatim + 最小 SDD 尾 |
| 治理 | 拒绝空转 | 无 consumer 证据不加 core 阶段；变更靠 consumer spot-check |

---

## 2. 本仓怎么落地

### 2.1 八技能

```text
grill（可选）→ spec → plan → build → review → ship
卫星：zoom（地图）· improve（体检）
```

指令 **English**；交付物跟用户语言 — 各 skill **Present** 硬约束。

### 2.2 review vs improve

| | `sdd-review` | `sdd-improve` |
| --- | --- | --- |
| 问什么 | 这次 diff 能发吗 | 全库/分支有啥机会 |
| 范围 | increment diff | whole repo / branch |
| 🔴🟡🟢 | **挡 ship** | **排 follow-up** |

配对：skill **When/Skip** 互指；清单：`review-dimensions.md` / `audit-dimensions.md`。code diff 必走 Architecture；prose/docs-only 跳过。

### 2.3 知识分层（消费者项目，可选）

```text
CONTEXT（可选）→ 域语言 · ADR（可选）→ 跨 feature 为什么 · Spec/Plan → 本次做什么
```

本仓维护者用 AGENTS + SOURCES，根目录不放 CONTEXT。

<a id="41-可选-context-与-adr"></a>

**CONTEXT/ADR：** 默认仍 spec+plan。L2（多 skill 统一读 CONTEXT）需 consumer 证据；目录见 README Minimal Artifacts。

---

## 3. 上游四源

Pin: [SOURCES.md](../../SOURCES.md)（2026-06-08）。**shadcn/improve** 未 pin。

| 来源 | 一句话 |
| --- | --- |
| superpowers | SDD 全自动长跑 + TDD |
| agent-skills | 分阶段技能 + 五轴审阅 |
| mattpocock/skills | 小技能拼装；grill；CONTEXT/ADR 词汇 |
| shadcn/improve | 分类只读体检 |

**本仓合成：** 阶段纪律 + 审阅轴 + 采访/架构词汇 + 体检清单 − **自动编排、平台锁、独立 Simplify**（可读性并进 architecture）。

| 维度 | superpowers | agent-skills | matt | shadcn/improve | **sdd-skills** |
| --- | --- | --- | --- | --- | --- |
| 自动化 | 高 | 中 | 低 | 中 | 低（人选阶段） |
| 主产物 | 长计划+子 agent | 分阶段命令 | issues/PRD | 发现报告 | spec+plan |
| 审阅/体检 | 子 agent | /review | improve-arch | 全库 audit | review+improve |
| 平台 | 重 | 重 | 较轻 | 产品向 | 纯 Markdown |

**分源取舍（摘要）：**

- **superpowers** → 六环 + TDD + review/ship 再验；扔 worktree、自动链、hook。
- **agent-skills** → 五轴清单拆成两维度文件；扔 slash catalog、独立 simplify 步。
- **matt** → grill/zoom/improve 卫星；扔 issue 状态机进 core、会话内写满 CONTEXT。
- **shadcn/improve** → `audit-dimensions.md` 骨架；扔产品壳、体检当 ship 门禁。

---

## 4. 反模式

| 反模式 | 为什么不行 |
| --- | --- |
| 磁盘文件 = 已批准 | 假进度 |
| review 里改代码 | 失去独立视角 |
| improve 挡 ship | 混淆体检与交付审 |
| 两技能 🔴 语义混用 | 一个排期一个挡发货 |
| workflow status.json | 状态机 + 平台绑定 |

**演化：** core 保持六环；卫星不撑胖 core；**怎么做** 在 skill，**为什么** 在本文。

---

## 5. 延伸阅读

- [SOURCES.md](../../SOURCES.md) · [AGENTS.md](../../AGENTS.md)
- [sdd-improve](../../skills/sdd-improve/SKILL.md) / [sdd-review](../../skills/sdd-review/SKILL.md) — When/Skip
- [docs/design/README.md](./README.md)
