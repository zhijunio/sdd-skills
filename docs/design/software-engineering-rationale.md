# 本仓怎么想软件工程

Status: **living document**

更新: **2026-06-11**

相关: [upstream-engineering-rationale.md](./upstream-engineering-rationale.md)（思想从哪来）· [SOURCES.md](../../SOURCES.md)（进了哪个 skill）

**谁说了算：** 日常行为看 `skills/*/SKILL.md` 和 `references/**`；上游映射看 SOURCES；本文解释 **为什么这样设计**。发版与 consumer 实证见 [CHANGELOG.md](../../CHANGELOG.md)、[consumer-loops/](./consumer-loops/)。

---

## 1. 要治什么毛病

Agent 能写代码，但常见四类问题：

1. **做着做着跑偏** — 和用户要的 behavior 不是一回事。  
2. **范围偷偷变大** — 顺手改无关文件，把老债也算进本次交付。  
3. **没验证就说完了** — 「看起来对」就当 ship。  
4. **流程太重** — 小改动也走完整 superpowers 长跑，像开工厂。

**sdd-skills 干什么：** 留下「先契约、再切片、再实现、再独立审、再复验」的纪律；去掉项目管理器、平台锁、状态机。不替代 TDD、CI、人工 code review — 给 Agent 一套 **能停、能跳、能审计** 的阶段语言。

---

## 2. 几条硬主张

### 2.1 要的是能验的契约，不是厚文档

- **Spec** 写清「怎样算对、怎样算错」（AC-1、AC-2…），能 pass/fail。  
- **Plan** 是能在几十分钟内跑通验证的 **竖切片**，不是甘特图。  
- 文档厚不厚不重要，重要的是 **review 和 ship 时能不能对照检查**。

### 2.2 一个 skill 干一件事，干完就停

每个 skill 是一个角色：产出一份结果 → **停** → 等人决定要不要下一阶段。

**不** 自动调用下一个 skill。人要在场选 scope、选风险、选要不要发版。自动化适合执行，不适合替人签收。

### 2.3 默认轻，痛了再加

| 多数项目够用 | 痛了再加 |
|--------------|----------|
| spec + plan | grill 多轮对齐 |
| spec 里写本变更事实 | 根目录 CONTEXT（域语言） |
| spec Constraints（本变更取舍） | docs/adr（跨多次交付的架构决定） |

流程也讲 YAGNI：没有重复痛点，不加阶段，不加磁盘上的流程状态文件。

### 2.4 说了就要能证明

- **Review** 只读，不顺手改产品代码。  
- **Ship** 再跑一遍验证 — review 通过 ≠ 可以交付。  
- 改 skill、加产物，最好有 **第二次真实项目闭环** 再写进基线（见 AGENTS.md）。

### 2.5 不绑平台

Skill 就是 Markdown。不依赖某个 IDE 的 hook、某个 CLI 的 slash 命令。拷到别的 Agent 环境也能读。

---

## 3. 方法怎么落地

### 3.1 六段分开干

```text
grill   → 决策还没定？先对齐（可选）
spec    → 这次交付必须满足什么
plan    → 分几步、每步怎么验
build   → 按 TDD 做
review  → 别人视角审这次 diff
ship    → 再验一遍，人点头才发
```

**为什么不能糊在一起：**

- 想清楚和写 AC 一屏写完 → AC 里会偷偷夹实现步骤。  
- 实现的人自己审 → 容易确认偏误。  
- 审完就当能发 → 「看过 diff」不等于「测试跑过」。

### 3.2 竖切片，别层间空转

一片大概 15–60 分钟，端到端能验；至少挂一个 AC；红绿重构后再下一片。Agent 特别爱在「各层先 stub」里假进度，切片是为了早点撞集成问题。

### 3.3 Grill：一次一问

继承 grill-me / brainstorming：**一次只问一个关键问题**，可以带推荐立场。决策是树，不是一次吐十条结论的伪共识。

### 3.4 Review：只对本次增量负责

- 默认看 `merge-base…HEAD` 这类 **本次增量 diff**。  
- diff 外老问题只能当 **观察**，不能当本次 must-fix。  
- 可维护性重要，但 **scope 膨胀是 Agent PR 的头号风险**。

**两种「审」，别混：**

| | `sdd-review`（核心环） | `sdd-improve`（卫星） |
|---|------------------------|------------------------|
| 问什么 | 这次改动能发吗 | 全库/分支有啥机会和风险 |
| 看什么 | 仅 increment diff | 全库或 branch |
| 产出 | 交付结论（挡不挡 ship） | 发现列表（先修啥） |
| 🔴🟡🟢 | **挡发货** | **排优先级**，不挡 ship |

配对表见 `using-sdd` Disambiguation。

**diff 分两类（review）：**

- **code diff** — 有源码、测试、CI 脚本等 → **必走架构检查**（结构 + 重复代码/能否写更简单）。  
- **prose/docs-only** — 只有文档、注释 → **跳过架构**，重点查 spec/文档、**链接有没有断**（重命名后 grep 旧路径）。

**架构这一透镜，improve 和 review 都有：** 差别只是范围（全库 vs 本次 diff 引入的问题）。上游单独的「可读性」「code-simplify」步骤，本仓都并进 **architecture**。

**可观测性、无障碍、运维：** 不每次全扫。improve 嵌在性能/架构/体验类里；review 在 diff 碰到日志、UI、部署配置时才走 — skills-only 仓不会空跑一堆用不上的清单。

### 3.5 卫星：zoom 与 improve

| 卫星 | 干什么 | 什么时候 |
|------|--------|----------|
| **sdd-zoom** | 画模块关系地图 | 领域不熟，先要地图再 spec |
| **sdd-improve** | 全库体检报告 | 健康检查、技术债、路线探索 |

做完仍通过 **`using-sdd`** 回核心环。**禁止** 用 improve 代替 review，或当 ship 前置门禁。老 **`sdd-architect`** 已并进 improve 第 5 类后删除。

### 3.6 Spec 可以改，但要留痕

build/review 发现 AC 不对：在 spec **原地改** + Revision log；分清「改措辞」和「改验收标准」；后者要重新批准。

---

## 4. 知识放哪一层

```text
CONTEXT（可选）  → 项目怎么说、域边界
ADR（可选）      → 跨多次交付的架构为什么这样选
Spec / Plan      → 这次做什么、怎么验
```

| 层 | 管多久 | 例子 |
|----|--------|------|
| CONTEXT | 很多个 spec | 「Order」还是「Purchase」 |
| ADR | 很多个 feature | 「为什么用事件溯源」 |
| Spec Constraints | 本变更 | 「本 PR 为什么限流放网关」 |
| AC | 本变更、可测 | 「当 X 则 Y」 |

**别把所有东西塞进 spec。** 重复越多，越该下沉到 CONTEXT/ADR；小项目 **不必** 下沉。本仓库维护者用 AGENTS + SOURCES，**不在** 根目录放 CONTEXT。

### 4.1 可选 CONTEXT 与 ADR

给 **用 SDD 的消费者项目**，不是本仓 maintainer 必填物。L2 技能改动 **还没做**。

**默认仍只要 spec + plan。**

| 产物 | 回答 |
|------|------|
| spec / plan | 这次做什么、怎么验 |
| CONTEXT | 稳定术语、域边界 |
| ADR | 跨 feature 的架构取舍 |

**分工（目标态）：**

- CONTEXT 管 **是什么**，ADR 管 **为什么**，spec Constraints 管 **本变更的取舍**。  
- 纯架构、没有 feature 边界 → grill 可写 ADR 后停；绑 AC 的仍走 spec，用 Related ADRs 链接。  
- grill 可改 CONTEXT 的 Language 段；spec 兜底；其它 core skill 不写 ADR。  
- 有 CONTEXT/ADR 就读相关段；没有就继续，别卡住。

**目录习惯：**

```text
# 单域
CONTEXT.md
docs/adr/

# 多域（不要 CONTEXT-MAP 索引）
docs/context/<domain>/CONTEXT.md
docs/adr/
```

**做到哪了：**

| 层级 | 内容 | 状态 |
|------|------|------|
| L0 | spec + plan | ✅ |
| L1 | 模板里 Decisions、Related ADRs | ✅ |
| L1+ | README/spec 注释 CONTEXT 路径 | ✅ |
| L2 | 多 skill 统一读 CONTEXT/ADR | ❌ 等有证据 |
| L3 | context/adr 模板文件 | ❌ |

**何时做 L2：** 多篇 spec 重复术语、多人/agent 命名漂移、纯架构变更太多、第二次闭环证明 Constraints 扛不住跨 feature 决策 — **要多条同时成立**。

**故意不做：** 新增 sdd-adr / sdd-context skill；CONTEXT/ADR 变必填；每个小取舍一篇 ADR。

---

## 5. 人和 Agent 怎么分工

| 人 | Agent |
|----|-------|
| 批 spec / plan | 起草 |
| 选下一阶段 | 只推荐一个，不自动执行 |
| 决定 push / PR / 发版 | 跑测试、摆证据 |
| 接受 should-fix 风险 | 标清 must-fix / should-fix |
| grill 里做价值判断 | 出方案、挑刺 |

默认 **人在场**。这套 skill 不是无人值守流水线。

---

## 6. 和别的方法比

| 做法 | 本仓态度 |
|------|----------|
| superpowers 全套（worktree、子 agent 自动链） | 学纪律，扔基础设施 |
| 只有 README 约定 | 不够，要可触发的 skill |
| Jira 驱动一切 | 不内置 |
| 一上来巨型设计 | 反对；spec 要小、可批 |
| 不改 spec 直接写 | 极小 reversible 改动可以；有意义的变更仍要 spec |
| matt 式 grill 边聊边改满仓库文档 | 可选 CONTEXT/ADR，见 §4.1 |

思想来源: [upstream-engineering-rationale.md](./upstream-engineering-rationale.md)（含 [shadcn/improve](https://github.com/shadcn/improve)）。

---

## 7. 演化原则

1. 先跑通真实 spec→ship，再谈版本号。  
2. core 保持七个阶段；体检/地图用 **卫星**，不把 core 撑胖。  
3. 不为某一个下游项目的特例改平台中立 skill。  
4. **怎么做** 在 skill；**为什么** 在本文；历史在 git / CHANGELOG，不维护第二份 skill 镜像文档。  
5. 成对文件对称命名（`audit-dimensions` / `review-dimensions`），各 skill 自包含。

---

## 8. 明确反对的做法

| 反模式 | 为什么不行 |
|--------|------------|
| 文件在磁盘上 = 用户已批准 | 假进度 |
| 每个取舍一篇 ADR | 文档通胀 |
| review 里改产品代码 | 失去独立视角 |
| ship 静默 push | 人失去交付控制 |
| workflow status.json | 状态机 + 平台绑定 |
| 为显得专业多加 core skill | 没证据就膨胀 |
| 用 improve 挡发版 | 混淆体检和交付审 |
| 以为 improve 和 review 的 🔴 是一回事 | 一个排期，一个挡发货 |
| spec 里写逐文件实现步骤 | 那是 plan 的事 |
| grill 一次扔整棵决策树 | 伪共识 |

---

## 9. 怎么用这套想法

**维护者：** 新想法先问「补的是环上哪一段？有人重复痛过吗？」能扩展现有 skill 就别加新的。上游变了就更新 SOURCES 和 rationale，别 silent drift。

**用 SDD 的项目：** 小活可 spec→plan→build；术语乱了再加 CONTEXT；决策跨 feature 再加 ADR；AC 永远要能 pass/fail。

**Agent：** 读 When to Use 和 Stop Conditions；推荐下一阶段 **只推荐一个**；别发明仓库里没有的阶段。

---

## 10. 延伸阅读

- [upstream-engineering-rationale.md](./upstream-engineering-rationale.md) — superpowers、agent-skills、matt、[shadcn/improve](https://github.com/shadcn/improve)  
- [SOURCES.md](../../SOURCES.md)  
- [using-sdd Disambiguation](../../skills/using-sdd/SKILL.md#disambiguation)  
- [docs/design/README.md](./README.md)  
- [consumer-loops/](./consumer-loops/)
