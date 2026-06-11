# 工程观与上游对照

Status: **living** · 更新: **2026-06-11**

**谁说了算：** 日常行为以 `skills/*/SKILL.md` 为准；上游 pin 与 skill 映射见 [SOURCES.md](../../SOURCES.md)；本文说明 **本仓怎么想、上游怎么想、我们怎么取舍**。发版与试跑摘要见 [CHANGELOG.md](../../CHANGELOG.md)；维护操作见 [AGENTS.md](../../AGENTS.md)。

**维护者：** 先改 skill 与 SOURCES，再同步本文。禁止编造未发生的 consumer 结果或版本 tag。若本文与 skill 冲突，以 skill 为准。

---

## 1. 要治什么毛病

Agent 能写代码，但常见四类问题：

1. **做着做着跑偏** — 实现出来的行为和用户要的不是一回事。
2. **范围偷偷变大** — 顺手改无关文件，增量边界模糊。
3. **没验证就说完了** — 「看起来对」就当可以 ship。
4. **流程太重** — 小改动也走完整 superpowers 长跑，停不下来。

**sdd-skills 干什么：** 留下「先契约、再切片、再实现、再独立审、再复验」的纪律；去掉项目管理器、平台锁、状态机。不替代 TDD、CI、人工 review，而是给 Agent **能停、能跳、能审计** 的阶段语言。

### 1.0 核心原则

六条原则分三层。英文速查表见 [README — Core principles](../../README.md#core-principles)。

#### 形态（仓库是什么）

- **轻量中立** — `SKILL.md` 保持简短；消费者默认只需 spec + plan 两份文档；本仓只发 Markdown skill，不加 hook、slash 命令、manifest，也不强制安装卫星 skill。
- **显式阶段** — 用户每次 `@` 一个 stage skill；该阶段产出后 **Stop**，再 hand off 下一阶段；不自动链式执行，也不在同一会话里偷偷做下一阶段的工作。

#### 交付（消费者怎么出货）

- **可验切片** — spec 写清可 pass/fail 的 AC；plan 拆成 15–60 分钟能验完的竖切片，而不是甘特图；grill、zoom、improve 仅在需要时加装。
- **测试与证明** — `sdd-build` 先写失败测试；`sdd-review` 只读且有证据；`sdd-ship` 重跑验证并读全输出，无证据不断言完成。

#### 治理（维护者怎么演进）

- **借鉴不重造** — 上游 prose 在 pin commit 处 verbatim 借用，再加最小 SDD 尾；融合取用，不镜像整库 skill catalog。映射见 SOURCES。
- **拒绝空转** — 没有 consumer 证据就不加 core 阶段或运行时状态字段；对本仓 skill 的**实质**变更，在 consumer 项目里 spot-check（重装 pin、跑一轮增量），而不是 maintainer dogfood 假验收。

---

## 2. 本仓怎么落地

### 2.1 八技能与主路径

核心交付环（六段）：

```text
grill（可选澄清）→ spec → plan → build → review → ship
```

可选卫星（二颗）：

- **`sdd-zoom`** — 领土地图：模块、调用方、域词汇；不给 refactor findings。
- **`sdd-improve`** — 机会扫描：全库或分支只读体检，产出 findings 报告。

技能指令用 **English**；交给用户的交付物（spec、plan、review 报告、grill 决策摘要等）跟 **用户语言** — 每个 skill 的 **Present** 步骤有硬约束，不默认英文。

各段职责简述：

- **grill** — 决策未定时一次一问；可 hand off 到 spec，或在已有 approved spec 时 hand off 到 plan。
- **spec** — 本次必须满足什么；AC 可判定 pass/fail。
- **plan** — 竖切片与验证命令；需用户批准后再 build。
- **build** — TDD 按片实现；review 列出的 fix 除外，需 approved spec + plan。
- **review** — 只读；仅 **increment diff**；给**交付结论**。
- **ship** — 再验一遍；不静默 push/发版。

### 2.2 两种「审」：review 与 improve

二者共用 🔴🟡🟢 标签，**语义不同**，不可混用。

**`sdd-review`（核心环 · 交付审）**

- 问的是：**这一次增量**能不能发？
- 范围：**increment diff**（用户指定范围；不默认 `main`）。
- 产出：**delivery verdict** — 挡不挡本次 ship。
- 🔴 must-fix：**挡本次增量**的 correctness、security、spec/AC 缺口等。
- code diff 必走 Architecture；纯 prose/docs-only diff 可 `architecture: skip`，改查链接与 spec 对齐。
- 清单：`review-dimensions.md`；报告：`finding-format.md`。

**`sdd-improve`（卫星 · 机会扫描）**

- 问的是：全库或分支里**有哪些跟进机会**？
- 范围：whole repo 或 branch vs merge-base。
- 产出：**findings 报告** + next-stage 路由建议；不是 ship 门禁。
- 🔴🟡🟢：只排 **follow-up 优先级**，不挡 `sdd-ship`。
- follow-up 可走 SDD 技能链，也可 **direct edit**（见 `closing-the-loop.md`）。
- 清单：`audit-dimensions.md`；报告：`finding-format.md`。

**配对规则：** 仅在各 skill **When/Skip** 互链；别处不重复 pairing 表。用户只说「review」却没有 diff 时，必须问清是 delivery review 还是 opportunity scan。

**禁止：** improve 代替 review；improve 当 ship 门禁。

### 2.3 知识分层（消费者项目）

```text
CONTEXT（可选）  → 稳定域语言、术语表
ADR（可选）      → 跨 feature、跨增量的架构取舍
Spec / Plan      → 这一次改什么、怎么验
```

- 默认工作流仍只需 **spec + plan**；CONTEXT/ADR 是加分项，不是本 skill 包的必填物。
- 单域可用根目录 `CONTEXT.md`；多域用 `docs/context/<domain>/CONTEXT.md`（不用 CONTEXT-MAP）。ADR 放 `docs/adr/`。
- 何时值得上 L2（多 skill 统一读 CONTEXT）：多篇 spec 重复术语、命名漂移、纯架构变更过多等 — **需多条证据同时成立**，见 consumer 试跑，不在本文写死门槛。

本仓是 skill 维护项目：用 [AGENTS.md](../../AGENTS.md) + SOURCES，**不在** 根目录放 CONTEXT。

<a id="41-可选-context-与-adr"></a>

目录与模板约定见 [README — Minimal artifacts](../../README.md#minimal-artifacts)。

---

## 3. 上游四源与本仓合成

Pin 快照：**2026-06-08**（[SOURCES.md](../../SOURCES.md)）。**shadcn/improve** 未 pin commit，清单大变时人工对照 GitHub 更新 `audit-dimensions.md`。

### 3.1 各源在解决什么

- **obra/superpowers** — 让 Agent 别一上来改文件：spec → 批准 → TDD 计划 → 子 agent 长跑；强调 YAGNI/DRY。
- **addyosmani/agent-skills** — 用分阶段 skill（spec、plan、build、review…）和 slash 命令表达「先契约再写码」；`code-review-and-quality` 提供五轴审阅清单。
- **mattpocock/skills** — 小技能可拼装；`grill-me` 决策采访；`zoom-out` 地图；`improve-codebase-architecture` 架构词汇；CONTEXT/ADR 实践。
- **shadcn/improve** — 分类只读体检 playbook；顾问角色；扫描期不改用户仓库。

共同点：先对齐再写码、测试作反馈、做/查分离、健康度可单独看。

### 3.2 本仓从各源拿什么、扔什么

**superpowers**

- 拿：六段环纪律、竖切片、TDD、review 只读、ship 再验。
- 扔：自动链下一 skill、worktree 编排、session hook、plan 工厂。

**agent-skills**

- 拿：主环阶段划分；五轴审阅清单 → 拆成 `review-dimensions.md` 与 `audit-dimensions.md`。
- 改：可读性与 simplify **并进 architecture**（improve 第 5 类 + review Architecture）；交付门禁**只在** `sdd-review`。
- 扔：slash 体系、大 catalog、独立 `/test` 阶段。

**mattpocock/skills**

- 拿：`grill-me` → `sdd-grill`；`zoom-out` → `sdd-zoom`；架构词汇 → improve 第 5 类。
- 扔：issue 状态机进 core；grill 边聊边写满仓库文档（本仓 CONTEXT 对消费者可选）；diagnose 不进 core。

**shadcn/improve**

- 拿：`audit-dimensions.md` 多类清单骨架与只读规则；标准扫描覆盖 1–8 类。
- 扔：完整产品壳、独立 **Simplify** 步骤、体检当 ship 门禁。归因见 THIRD_PARTY_NOTICES。

### 3.3 对照摘要（本仓站位）

- **自动化程度** — 低于 superpowers：用户每次 `@` 阶段，不自动编排子 agent。
- **主产物** — spec + plan 两份默认契约；不是长计划工厂或 issues 流水线。
- **审阅 / 体检** — `sdd-review`（diff 交付审）+ `sdd-improve`（全库机会扫描）拆分清楚。
- **域语言文档** — 借鉴 matt 的 CONTEXT/ADR 思路，但对消费者**可选**（§2.3）。
- **平台绑定** — 纯 Markdown skill；无插件 manifest、无 status.json。

合成一句：superpowers 的**阶段纪律** + agent-skills 的**生命周期与审阅轴** + matt 的**采访与架构词汇** + shadcn/improve 的**分类体检清单**，减去**自动编排、平台锁、独立 Simplify**。

---

## 4. 反模式

- **磁盘上有 spec/plan 文件 = 已批准** — 文件存在不代表用户点头；批准发生在 Present 之后。
- **review 会话里改产品代码** — 失去独立审阅视角；修 fix 应 hand off `sdd-build`。
- **用 improve 挡 ship** — 体检报告排期，不是本次增量的发货门禁。
- **两技能 🔴 语义混用** — improve 的 🔴 是 follow-up 优先级；review 的 🔴 才挡本次 ship。
- **workflow status.json 或中心路由表** — 状态机 + 平台绑定，违背轻量中立。

**演化原则：** core 保持六段环；卫星不撑胖 core；**怎么做** 写在 skill，**为什么** 写在本文明；成对命名（`audit-dimensions` / `review-dimensions`）。

---

## 5. 延伸阅读

- [SOURCES.md](../../SOURCES.md) · [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md) · [AGENTS.md](../../AGENTS.md)
- [sdd-improve](../../skills/sdd-improve/SKILL.md) / [sdd-review](../../skills/sdd-review/SKILL.md) — When/Skip
- [docs/design/README.md](./README.md)
