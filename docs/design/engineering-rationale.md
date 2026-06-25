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
- 没验证就说完 → **测试与证明**（build / review / verify 分工）
- 流程太重 → **轻量中立** + **显式阶段**（只装需要的 skill，`@` 点名）

### 1.0 核心原则

六条原则分三层。英文速查表见 [README — Core principles](../../README.md#core-principles)。

#### 形态（仓库是什么）

- **轻量中立** — `SKILL.md` 保持简短，细节进 `references/`；消费者默认只需 spec + plan；本仓只发 Markdown skill，不加 hook、slash、manifest，也不强制卫星。目的是让消费者按项目体量「选配」，而不是背一整套平台仪式。
- **显式阶段** — 用户每次 `@` 一个 stage skill；产出后 **Stop**，再 hand off；不自动链式、不同会话偷偷做下一阶段。目的是让「现在处于哪一步」对用户可见、可打断。

#### 交付（消费者怎么出货）

- **可验切片** — spec 写清可 pass/fail 的 AC；plan 拆 15–60 分钟竖切片；grill / zoom / improve 按需加装。目的是每个增量都有可演示、可命令验证的完成定义。
- **测试与证明** — build 先红测试；review 只读且有证据；verify 重跑验证、读全输出。目的是「完成」一词必须有可追溯证据，而不是会话里的口头确认。

#### 治理（维护者怎么演进）

- **借鉴不重造** — 上游 @ pin 处 verbatim + 最小 SDD 尾；融合取用，不镜像 catalog。目的是借成熟纪律，但不维护第二套 superpowers 克隆仓。
- **拒绝空转** — 无 consumer 证据不加 core 阶段或状态字段；实质变更在 consumer 项目 spot-check。目的是版本与 skill 文本的演进跟真实摩擦挂钩，而不是 maintainer 自嗨 dogfood。

---

## 2. 本仓怎么落地

### 2.1 八技能与主路径

核心交付环（六段）：

```text
grill（可选澄清）→ spec → plan → build → review → verify
```

可选卫星（四颗：一颗 pre-loop、一颗 post-loop）：

- **`sdd-worktree`** — 开工前 git 隔离（worktree 或 topic 分支）；用户显式 `@`，非 superpowers 自动编排；**不挡** verify。
- **`sdd-publish`** — 远程集成（push / PR / merge / tag / release）；分步 Present + 确认；用户显式 `@`、可单独入口；**不依赖** `@sdd-verify`；**不挡** verify 验收本身。
- **`sdd-zoom`** — 领土地图：模块、调用方、域词汇；**不给** refactor findings，也不给 delivery verdict。
- **`sdd-audit`** — 机会扫描：全库或分支只读体检；产出 findings 与 next-stage 建议，**不挡** verify。

技能指令用 **English**；交给用户的交付物跟 **用户语言** — 各 skill **Present** 硬约束（不默认英文）。字面保留：`AC-n`、skill id、category lens、`file:line`、git 字面量、🔴🟡🟢。

各段职责与典型 hand-off：

- **grill** — 目标、边界、权衡未定时，一次一问、带推荐答案；可探索代码再提问。Stop 后默认 **`sdd-spec`**；已有 approved spec 且议题是 plan/切片时 → **`sdd-plan`**。
- **spec** — 行为契约与 AC；用户批准前不 build。澄清性修订可只记 Revision log；AC 变更需再批准。
- **plan** — 把 AC 映射到竖切片与验证命令；用户批准前不实现。
- **build** — TDD 按片推进；仅实现 approved plan（或 review 点名 fix）。全片完成 → **`sdd-review`**，不跳 verify。
- **review** — 只读审 **increment diff**；有 🔴 则 → **`sdd-build`** 修；通过 → **`sdd-verify`**。
- **verify** — 按 AC 复验；更新 CHANGELOG（若项目惯例需要）；不默认 push/PR/发版；用户另行要求集成 → **`sdd-publish`**。

**何时用卫星（启发式，非强制）：**

- 新需求勿在 `main` 上直接开干 → 可先 **`sdd-worktree`**，再 spec / grill。
- 陌生代码、术语乱 → 先 **`sdd-zoom`**，再 spec / grill。
- 全库健康、分支上线前摸底、架构债盘点 → **`sdd-audit`**（不是「review 这个 PR」）。
- 用户要 push/PR/merge/tag/release → **`sdd-publish`**（常见在 verify 之后，但非前置条件；不是 verify 内默认执行）。
- 权衡仍开放 → **`sdd-grill`**，不要靠 improve 替代表决。

### 2.2 两种「审」：review 与 audit

二者共用 🔴🟡🟢 标签，**语义不同**，不可混用。

**`sdd-review`（核心环 · 交付审）**

- 问的是：**这一次增量**能不能发？
- 范围：**increment diff** — PR、commit range、`merge-base...HEAD`、或用户指定的 staged/unstaged 任务变更；**不默认** `main`。
- 产出：**delivery verdict** — 挡不挡本次 verify。
- 🔴 must-fix：挡本次增量的 correctness、security、spec/AC 缺口、Non-goal 违反等。
- **Diff kind：** 含可执行逻辑或测试 → **code diff**，必走 Architecture（结构 + diff 内 DRY/KISS）；纯 Markdown/文档/注释 → **prose/docs-only**，`architecture: skip`，重点查 spec 对齐与**引用完整性**（改名后链接、install 示例是否仍对）。
- 清单：`review-dimensions.md`；报告：`finding-format.md`。

**`sdd-audit`（卫星 · codebase audit）**

- 问的是：全库或分支里**有哪些值得跟进的发现**？
- 范围：whole repo，或 branch vs merge-base（finding 可标 `introduced` / `pre-existing`）。
- 产出：**Codebase Audit** 报告（与上游 `codebase-audit` 同结构）；handoff 写在报告末 **Suggested next steps**，路由见 **`sdd-audit` `SKILL.md` Stop**。
- 🚨🔴🟡🟢：只排 **follow-up 优先级** — **不挡** `sdd-verify`。
- 六柱 A/C/S/V/D/O；清单 `map.md` / `playbook.md`；报告 `report.md`（与上游同步）。

**配对与歧义处理：**

- 配对只写在各 skill **When/Skip** 互链；README 有一张速查表，本文不重复第三份 pairing 表。
- 用户说「review」但没有 increment diff、也没有「这次 PR/提交」语境 → **必须问清**：delivery review 还是 codebase audit。
- 用户说「体检 / 健康检查 / 架构债」且无 delivery 语境 → 仅 **`sdd-audit`**。

**禁止：** `sdd-audit` 代替 review；`sdd-audit` 当 verify 门禁；review 会话里改产品代码。

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

目录约定见 [README — Minimal artifacts](../../README.md#minimal-artifacts)：单域 `CONTEXT.md`；多域 `docs/context/<domain>/CONTEXT.md`；ADR `docs/adr/0001-short-title.md`。

---

## 3. 上游四源与本仓合成

本仓不是四源的「合集镜像」，而是按 §1.0 **融合取用**：每个本地 skill 只借与阶段纪律相关的部分，并显式记录**扔掉了什么**。细节映射以 [SOURCES.md](../../SOURCES.md) 为准；本节讲**为什么这样拆**。

**Pin 快照：**

- `mattpocock/skills` @ `be55a797`
- `obra/superpowers` @ `6fd450765`
- `addyosmani/agent-skills` @ `c076972e`
- [zhijunio/zhijunio-skills `codebase-audit`](https://github.com/zhijunio/zhijunio-skills/tree/main/codebase-audit) — **未 pin**；MIT；pillar 大变时人工 diff 后更新 `map.md` / `playbook.md` / `report.md` 与本节
- [shadcn/improve](https://github.com/shadcn/improve) — **superseded** for `sdd-audit` checklist body

四源共同点：先对齐再写码、测试作反馈、skill 可复用、**做与查分离**、健康度可单独审视。

---

### 3.1 各源在解决什么问题

#### obra/superpowers

- **解决什么：** 让 Agent 别一上来改文件——先 spec、用户批准、再 TDD 计划、再实现；review 与 ship 强调证据。
- **典型形态：** 长计划、`writing-plans` 路径、子 agent 按片跑、verification-before-completion 铁律。
- **背后假设：** 用户愿走完整 SDD 环；接受 worktree、session 结束自动触发下一 skill。
- **与本仓：** 借阶段顺序与 TDD/review/ship 纪律；不借自动编排与运行时。

#### addyosmani/agent-skills

- **解决什么：** 用可组合 skill 覆盖生命周期，slash 降低「现在该干嘛」的摩擦。
- **典型形态：** `code-review-and-quality` 五轴；`/review` 与 `/code-simplify`；shipping、git-workflow 等。
- **背后假设：** IDE/CLI 入口切换阶段；catalog 可大，按项目选配。
- **与本仓：** 借阶段划分与审阅轴；不借 slash 与整库 mirror。

#### mattpocock/skills

- **解决什么：** 小技能拼装——grill 采访、zoom 地图、TDD 竖切片、to-prd / to-issues。
- **典型形态：** `grill-me` 一次一问；`zoom-out` 模块+调用方；`improve-codebase-architecture` 谈深度与接缝；CONTEXT/ADR。
- **背后假设：** 用户维护 issues/PRD 式产物；采访与地图是 spec 的前置输入。
- **与本仓：** 借 grill/zoom 单源正文与架构词汇；diagnose、issue 状态机不进 core。

#### shadcn/improve

- **解决什么：** 按类**只读**体检，列有证据的发现；顾问扫描期不改仓。
- **典型形态：** 多类 checklist；effort profile；follow-up 路由；上游另有 simplify 命名（本仓**不采用**该步名）。
- **背后假设：** 体检与交付审分离；用户看完 findings 再决定 spec/build 或直接改。
- **与本仓：** 借分类清单与只读规则；不借产品壳、execute 工厂、verify 门禁。

---

### 3.2 本仓从各源拿什么、扔什么、落在哪

维护模板：**解决什么 → 假设 → 拿什么 → 扔什么 → 落在哪些 skill/文件**。

#### superpowers → 六段环纪律

**拿什么**

- spec 批准门、plan 竖切片、TDD → `sdd-spec` / `sdd-plan` / `sdd-build`
- requesting-code-review、verification-before-completion → `sdd-review` / `sdd-verify`
- brainstorming「先想清楚」→ 部分进 `sdd-spec`；领土探索交给 `sdd-zoom`，不塞进 spec

**扔什么**

- 自动链下一 skill、session hook — 违背显式阶段
- worktree / 子 agent — 平台绑定与编排复杂度
- `docs/superpowers/plans/` 默认路径 — 本仓用 `docs/sdd/*-plan.md`
- 计划即执行脚本 — plan 给人读，不是 runtime

#### agent-skills → 生命周期轴与审阅清单

**拿什么**

- spec-driven-development、planning-and-task-breakdown → `sdd-spec` / `sdd-plan` @ pin
- code-review-quality 五轴 → `review-dimensions.md`（diff 审）；全库 MECE 审计 → `sdd-audit` `map.md` / `playbook.md`
- shipping-and-launch（本地验收纪律）→ `sdd-verify`；git-workflow / 远程集成 → **`sdd-publish`**

**改什么**

- 可读性 + simplify **并进 architecture** — 避免独立「简化」步与 delivery 门禁混淆
- merge 裁决、spec 合规 **只在** `sdd-review`
- Nit/FYI → 🟢 suggestion

**扔什么**

- slash 与巨大 catalog — 用户 `@` skill 即可
- 独立 `/test` 阶段 — 测试在 build + verify

#### mattpocock/skills → 采访、地图、架构词汇

**拿什么**

- `grill-me` verbatim → `sdd-grill`；`zoom-out` verbatim → `sdd-zoom`
- `to-prd`、spec 开场 → `sdd-spec`；`to-issues` → `sdd-plan` 竖切片
- `tdd` → `sdd-build`；架构词汇 → `sdd-audit` 第 5 类

**扔什么**

- issue 状态机进 core — 默认只要 spec+plan
- grill 会话内写满 CONTEXT — 消费者 CONTEXT 可选（§2.3）
- `diagnose` 专 skill — 不扩 core

#### zhijunio-skills `codebase-audit` → MECE 全库体检

**拿什么**

- 六柱 lens + effort 变体 → `map.md`、`playbook.md`、`report.md`、`deep-parallel.md`
- 只读规则 → playbook § Recon + SKILL Hard rules
- SDD 路由 → **`sdd-audit` `SKILL.md` Stop**（upstream 无此节）

**扔什么**

- 体检挡 verify — improve 的严重度只排 follow-up
- `plans/` 工厂、executor — 跟进走 SDD 或 direct edit

#### shadcn/improve（已 superseded）

**历史：** 分类清单骨架曾进 `audit-dimensions.md`；现由 `codebase-audit` 取代。归因在 SOURCES / THIRD_PARTY_NOTICES。

---

### 3.3 十技能与四源映射（速查）

- **`sdd-worktree`** — 维护者自研；superpowers 自动 worktree **扔掉**；显式 `@` 轻量隔离
- **`sdd-publish`** — 维护者自研；superpowers 自动发版 **扔掉**；显式 `@` 分步集成
- **`sdd-grill`** — matt `grill-me`（主）；superpowers brainstorming thrown，不融合进正文
- **`sdd-spec`** — agent-skills spec-driven + matt `to-prd` + superpowers brainstorming 开场
- **`sdd-plan`** — superpowers `writing-plans` 精神 + agent-skills planning + matt `to-issues`
- **`sdd-build`** — superpowers + matt TDD @ pin；agent-skills incremental-implementation
- **`sdd-review`** — superpowers requesting-code-review + agent-skills code-review-quality @ pin
- **`sdd-verify`** — superpowers verification-before-completion + agent-skills shipping（本地验收）；远程集成 → **`sdd-publish`**
- **`sdd-zoom`** — matt `zoom-out` @ pin（单源）
- **`sdd-audit`** — zhijunio `codebase-audit` MECE playbooks + SDD handoff in **`SKILL.md` Stop**

---

### 3.4 五维对照：本仓站在哪

- **自动化程度** — superpowers 高、agent-skills 中、matt 低、improve 中；**本仓低**（用户 `@`，无子 agent）
- **主产物** — 上游各异；**本仓**默认 spec+plan，其余多为会话报告
- **审阅 vs 体检** — agent-skills `/review`+simplify、improve 全库 audit；**本仓**拆成 `sdd-review` + `sdd-audit`，simplify 语义并进 architecture
- **域语言** — matt 主推 CONTEXT/ADR；**本仓**对消费者可选 L0–L3（§2.3）
- **平台绑定** — 上游多插件/slash；**本仓**纯 Markdown，无 manifest、`status.json`、`using-sdd`

**合成一句：**

> superpowers **阶段纪律与证据链** + agent-skills **生命周期与审阅轴** + matt **采访、地图与架构词汇** + zhijunio **codebase-audit MECE 体检**，减去 **自动编排、平台锁、独立 Simplify、体检当 verify 门禁**。

上游升级时：只 diff 相关 commit 片段 → 更新 `SKILL.md` / `references/`、`SOURCES.md` → material 变更后 consumer spot-check → 再改本节。

---

## 4. 反模式

- **磁盘上有 spec/plan = 已批准** — 文件存在 ≠ 用户点头；批准在 **Present** 之后。
- **review 里改产品代码** — 失去独立视角；fix → hand off **`sdd-build`**。
- **improve 挡 verify** — `sdd-audit` 体检排期 ≠ 本次增量门禁。
- **两技能 🔴 混用** — `sdd-audit` 的 🚨/🔴 排 follow-up；review 的 🔴 才挡 verify。
- **中心 routing doc 或 `using-sdd`** — 用户应直接 `@` stage skill；routing 增加空转。
- **workflow status.json** — 状态机 + 平台绑定。
- **每个小取舍一篇 ADR** — 文档通胀；ADR 留给跨增量、跨 feature 决策。

**演化原则：** core 保持六段环；卫星不撑胖 core；**怎么做** 在 skill，**为什么** 在本文；`sdd-review` 用 `review-dimensions.md` + `finding-format.md`；`sdd-audit` 用 `map.md` / `playbook.md` / `report.md`（delivery gate 语义不同）。

---

## 5. 延伸阅读

- [SOURCES.md](../../SOURCES.md) · [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md) · [AGENTS.md](../../AGENTS.md)
- [README — Skills](../../README.md#skills) · [Maintainer verification](../../README.md#maintainer-verification)
- [sdd-audit](../../skills/sdd-audit/SKILL.md) / [sdd-review](../../skills/sdd-review/SKILL.md) — When/Skip
- [docs/design/README.md](./README.md)

