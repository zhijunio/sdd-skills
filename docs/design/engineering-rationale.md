# 工程观与上游对照

Status: **living** · 更新: **2026-06-11**

**谁说了算：** 日常行为以 `skills/*/SKILL.md` 为准；上游 pin 与 skill 映射见 [SOURCES.md](../../SOURCES.md)；本文说明 **本仓怎么想、上游怎么想、我们怎么取舍**。发版与试跑摘要见 [CHANGELOG.md](../../CHANGELOG.md)；维护操作见 [AGENTS.md](../../AGENTS.md)。

**维护者：** 先改 skill 与 SOURCES，再同步本文。禁止编造未发生的 consumer 结果或版本 tag。若本文与 skill 冲突，以 skill 为准。刷新本文时：直白中文、一节一事、对比用列表；不新增第二份 rationale 文件。

---

## 1. 要治什么毛病

Agent 能写代码，但常见四类问题：

1. **做着做着跑偏** — 实现出来的行为和用户要的不是一回事；没有可判定的 AC，就只能靠「感觉对了」。
2. **范围偷偷变大** — 顺手改无关文件，增量边界模糊；review 时说不清「这次到底改了什么」。
3. **没验证就说完了** — 测试没跑、输出没读，就宣布可以 merge 或 ship。
4. **流程太重** — 小改动也走完整 superpowers 长跑；用户无法在某个阶段停下来换思路。

**sdd-skills 干什么：** 留下「先契约、再切片、再实现、再独立审、再复验」的纪律；去掉项目管理器、平台锁、状态机。不替代 TDD、CI、人工 review，而是给 Agent **能停、能跳、能审计** 的阶段语言。

毛病与原则的对应关系：

- 做着跑偏 → **可验切片**（spec 写 AC）
- 范围变大 → **可验切片** + **显式阶段**（Stop 就停，不自动链下一阶段）
- 没验证就说完 → **测试与证明**（build / review / ship 分工）
- 流程太重 → **轻量中立** + **显式阶段**（只装需要的 skill，`@` 点名）

### 1.0 核心原则

六条原则分三层。英文速查表见 [README — Core principles](../../README.md#core-principles)。

#### 形态（仓库是什么）

- **轻量中立** — `SKILL.md` 保持简短，细节进 `references/`；消费者默认只需 spec + plan；本仓只发 Markdown skill，不加 hook、slash、manifest，也不强制卫星。目的是让消费者按项目体量「选配」，而不是背一整套平台仪式。
- **显式阶段** — 用户每次 `@` 一个 stage skill；产出后 **Stop**，再 hand off；不自动链式、不同会话偷偷做下一阶段。目的是让「现在处于哪一步」对用户可见、可打断。

#### 交付（消费者怎么出货）

- **可验切片** — spec 写清可 pass/fail 的 AC；plan 拆 15–60 分钟竖切片；grill / zoom / improve 按需加装。目的是每个增量都有可演示、可命令验证的完成定义。
- **测试与证明** — build 先红测试；review 只读且有证据；ship 重跑验证、读全输出。目的是「完成」一词必须有可追溯证据，而不是会话里的口头确认。

#### 治理（维护者怎么演进）

- **借鉴不重造** — 上游 @ pin 处 verbatim + 最小 SDD 尾；融合取用，不镜像 catalog。目的是借成熟纪律，但不维护第二套 superpowers 克隆仓。
- **拒绝空转** — 无 consumer 证据不加 core 阶段或状态字段；实质变更在 consumer 项目 spot-check。目的是版本与 skill 文本的演进跟真实摩擦挂钩，而不是 maintainer 自嗨 dogfood。

---

## 2. 本仓怎么落地

### 2.1 八技能与主路径

核心交付环（六段）：

```text
grill（可选澄清）→ spec → plan → build → review → ship
```

可选卫星（二颗）：

- **`sdd-zoom`** — 领土地图：模块、调用方、域词汇；**不给** refactor findings，也不给 delivery verdict。
- **`sdd-improve`** — 机会扫描：全库或分支只读体检；产出 findings 与 next-stage 建议，**不挡** ship。

技能指令用 **English**；交给用户的交付物跟 **用户语言** — 各 skill **Present** 硬约束（不默认英文）。字面保留：`AC-n`、skill id、category lens、`file:line`、git 字面量、🔴🟡🟢。

各段职责与典型 hand-off：

- **grill** — 目标、边界、权衡未定时，一次一问、带推荐答案；可探索代码再提问。Stop 后默认 **`sdd-spec`**；已有 approved spec 且议题是 plan/切片时 → **`sdd-plan`**。
- **spec** — 行为契约与 AC；用户批准前不 build。澄清性修订可只记 Revision log；AC 变更需再批准。
- **plan** — 把 AC 映射到竖切片与验证命令；用户批准前不实现。
- **build** — TDD 按片推进；仅实现 approved plan（或 review 点名 fix）。全片完成 → **`sdd-review`**，不跳 ship。
- **review** — 只读审 **increment diff**；有 🔴 则 → **`sdd-build`** 修；通过 → **`sdd-ship`**。
- **ship** — 按 AC 复验；更新 CHANGELOG（若项目惯例需要）；不默认 push/PR/发版。

**何时用卫星（启发式，非强制）：**

- 陌生代码、术语乱 → 先 **`sdd-zoom`**，再 spec / grill。
- 全库健康、分支上线前摸底、架构债盘点 → **`sdd-improve`**（不是「review 这个 PR」）。
- 权衡仍开放 → **`sdd-grill`**，不要靠 improve 替代表决。

### 2.2 两种「审」：review 与 improve

二者共用 🔴🟡🟢 标签，**语义不同**，不可混用。

**`sdd-review`（核心环 · 交付审）**

- 问的是：**这一次增量**能不能发？
- 范围：**increment diff** — PR、commit range、`merge-base...HEAD`、或用户指定的 staged/unstaged 任务变更；**不默认** `main`。
- 产出：**delivery verdict** — 挡不挡本次 ship。
- 🔴 must-fix：挡本次增量的 correctness、security、spec/AC 缺口、Non-goal 违反等。
- **Diff kind：** 含可执行逻辑或测试 → **code diff**，必走 Architecture（结构 + diff 内 DRY/KISS）；纯 Markdown/文档/注释 → **prose/docs-only**，`architecture: skip`，重点查 spec 对齐与**引用完整性**（改名后链接、install 示例是否仍对）。
- 清单：`review-dimensions.md`；报告：`finding-format.md`。

**`sdd-improve`（卫星 · 机会扫描）**

- 问的是：全库或分支里**有哪些值得跟进的发现**？
- 范围：whole repo，或 branch vs merge-base（finding 可标 `introduced` / `pre-existing`）。
- 产出：**findings 报告** + **Next stage** 路由；经 **Confirm** 后 hand off，不是当场改产品代码。
- 🔴🟡🟢：只排 **follow-up 优先级**（例如缺验证基线、HIGH 把握的安全项），**不挡** `sdd-ship`。
- 标准扫描默认覆盖类别 1–8；用户问 roadmap 时才走 category 9 direction。
- 清单：`audit-dimensions.md`；报告：`finding-format.md`；路由：`closing-the-loop.md`。

**配对与歧义处理：**

- 配对只写在各 skill **When/Skip** 互链；README 有一张速查表，本文不重复第三份 pairing 表。
- 用户说「review」但没有 increment diff、也没有「这次 PR/提交」语境 → **必须问清**：delivery review 还是 opportunity scan。
- 用户说「体检 / 健康检查 / 架构债」且无 delivery 语境 → 仅 **`sdd-improve`**。

**禁止：** improve 代替 review；improve 当 ship 门禁；review 会话里改产品代码。

### 2.3 知识分层（消费者项目）

```text
CONTEXT（可选）  → 稳定域语言、术语表
ADR（可选）      → 跨 feature、跨增量的架构取舍与理由
Spec / Plan      → 这一次改什么、怎么验（增量事实）
```

- **Spec 的 Current Context** 记本次增量事实；稳定术语应引用 CONTEXT，不要在每篇 spec 里复制一整本 glossary。
- 默认工作流仍只需 **spec + plan**；CONTEXT/ADR 是加分项。

**成熟度阶梯（本 skill 包视角）：**

- **L0** — 仅 spec + plan（默认，已足够多数增量）。
- **L1** — spec 模板含 **Related ADRs** / grill 的 **Decisions**；README 或 spec 注释里写明 CONTEXT 路径（若存在）。
- **L2** — 多个 skill 会话稳定读取同一份 CONTEXT/ADR（需在项目里约定路径，而不是靠 Agent 猜）。
- **L3** — 提供 context/adr 脚手架模板 — **等有 consumer 证据再做**，不预先塞进本仓。

**何时考虑升到 L2（多条同时成立时再动）：**

- 连续多篇 spec 大段重复同一术语定义；
- 同名概念在不同模块写法漂移，review 频繁标「spec 与代码用语不一致」；
- 增量以纯架构/边界调整为主，Constraints 节越来越长却无处沉淀；
- 第二次以上 consumer 试跑证明「只靠 spec/plan 扛不住跨增量约束」。

本仓是 skill 维护项目：用 [AGENTS.md](../../AGENTS.md) + SOURCES，**不在** 根目录放 CONTEXT。

<a id="41-可选-context-与-adr"></a>

目录约定见 [README — Minimal artifacts](../../README.md#minimal-artifacts)：单域 `CONTEXT.md`；多域 `docs/context/<domain>/CONTEXT.md`；ADR `docs/adr/0001-short-title.md`。

---

## 3. 上游四源与本仓合成

Pin 快照：**2026-06-08**（[SOURCES.md](../../SOURCES.md)）。**shadcn/improve** 未 pin commit；审计类别若大变，对照 GitHub 更新 `audit-dimensions.md` 与 §3.2 叙述。

### 3.1 各源在解决什么

- **obra/superpowers** — Agent 别一上来改文件：spec → 用户批准 → TDD 计划 → 子 agent 实现长跑。假设用户愿意走完整环并接受 worktree、自动触发。
- **addyosmani/agent-skills** — 用分阶段 skill 与 slash 表达生命周期；`code-review-and-quality` 把审阅拆成多轴清单。假设 IDE 集成与命令入口。
- **mattpocock/skills** — 小技能拼装；grill 决策树；zoom 地图；架构深化词汇；CONTEXT/ADR 作为长期知识。假设用户愿意维护 issues/PRD 式产物。
- **shadcn/improve** — 按类只读体检、列发现、顾问不改仓。假设体检与实现分离，但不替代 delivery gate。

共同点：先对齐再写码、测试作反馈、skill 可复用、做/查分离、健康度可单独审视。

### 3.2 本仓从各源拿什么、扔什么

**superpowers**

- 拿：六段环纪律、竖切片、TDD、review 只读、ship 再验、grill 式决策前置。
- 扔：自动链下一 skill、worktree 编排、session hook、plan 工厂、子 agent 编排。

**agent-skills**

- 拿：主环阶段；五轴清单 → `review-dimensions.md` + `audit-dimensions.md`。
- 改：可读性 / simplify **并进 architecture**；交付门禁**只在** `sdd-review`。
- 扔：slash catalog、独立 `/test` 阶段、Nit/FYI 标签进 delivery gate（映射为 🟢 suggestion）。

**mattpocock/skills**

- 拿：`grill-me` → `sdd-grill`；`zoom-out` → `sdd-zoom`；架构词汇 → improve 第 5 类。
- 扔：issue 状态机进 core；grill 会话内写满仓库文档；diagnose 不进 core。

**shadcn/improve**

- 拿：`audit-dimensions.md` 清单骨架、只读规则、标准 1–8 类；closing-the-loop 式路由思想 → SDD hand-off。
- 扔：产品壳、独立 **Simplify** 步、体检当 ship 门禁、`execute` / `plans/` 工厂。归因见 THIRD_PARTY_NOTICES。

### 3.3 对照摘要（本仓站位）

- **自动化程度** — 低于 superpowers：用户 `@` 阶段，不自动编排子 agent。
- **主产物** — spec + plan 两份默认契约；不是长计划工厂或 issues 流水线。
- **审阅 / 体检** — `sdd-review`（diff 交付审）与 `sdd-improve`（全库机会扫描）职责拆分。
- **域语言文档** — 借鉴 matt，对消费者**可选**（§2.3 阶梯）。
- **平台绑定** — 纯 Markdown；无 manifest、无 `status.json`、无中心 routing skill。

合成：superpowers **阶段纪律** + agent-skills **生命周期与审阅轴** + matt **采访与架构词汇** + shadcn/improve **分类体检清单**，减去 **自动编排、平台锁、独立 Simplify**。

---

## 4. 反模式

- **磁盘上有 spec/plan = 已批准** — 文件存在 ≠ 用户点头；批准在 **Present** 之后。
- **review 里改产品代码** — 失去独立视角；fix → hand off **`sdd-build`**。
- **improve 挡 ship** — 体检排期 ≠ 本次增量门禁。
- **两技能 🔴 混用** — improve 的 🔴 排 follow-up；review 的 🔴 才挡 ship。
- **中心 routing doc 或 `using-sdd`** — 用户应直接 `@` stage skill；routing 增加空转。
- **workflow status.json** — 状态机 + 平台绑定。
- **每个小取舍一篇 ADR** — 文档通胀；ADR 留给跨增量、跨 feature 决策。

**演化原则：** core 保持六段环；卫星不撑胖 core；**怎么做** 在 skill，**为什么** 在本文；成对文件（`audit-dimensions` / `review-dimensions`，`finding-format` 语义同步）。

---

## 5. 延伸阅读

- [SOURCES.md](../../SOURCES.md) · [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md) · [AGENTS.md](../../AGENTS.md)
- [README — Skills](../../README.md#skills) · [Maintainer verification](../../README.md#maintainer-verification)
- [sdd-improve](../../skills/sdd-improve/SKILL.md) / [sdd-review](../../skills/sdd-review/SKILL.md) — When/Skip
- [docs/design/README.md](./README.md)
