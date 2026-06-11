# 软件工程方法与思考

Status: **living document**

Last updated: 2026-06-09

Related: [project-decisions.md](./project-decisions.md)（**做了什么**）· [upstream-engineering-rationale.md](./upstream-engineering-rationale.md)（**上游从哪来**）· [context-adr-workflow.md](./context-adr-workflow.md)（可选 CONTEXT/ADR，proposed）

本文件说明 **sdd-skills 背后的工程观**：为何这样组织 SDD、人与 Agent 如何分工、何种质量门禁值得保留。它不是 skill 运行时契约；契约仍以 `skills/*/SKILL.md` 为准。

---

## 1. 我们在解决什么问题

Agent 能写代码，但常出现：

- **意图漂移** — 做着做着偏离用户真正要的 behavior  
- **范围蔓延** — 顺手改无关文件、混入 pre-existing 问题  
- **验证不足** — 「看起来对」就宣称完成  
- **流程过重** — 完整 superpowers 环对一个小 fix 像开工厂  

**sdd-skills 的定位：** 保留 **Spec-Driven Development 的纪律**，去掉 **项目管理器 / 平台锁 / 状态机** 的重量。  
不是替代 TDD、Code Review、CI — 而是给 Agent 一套 **可停止、可审计、可跳过** 的阶段语言。

---

## 2. 核心主张

### 2.1 契约驱动，而非文档驱动

- **Spec** 不是长篇 PRD，而是 **可 pass/fail 的行为契约**（`AC-1`、`AC-2`…）。  
- **Plan** 不是甘特图，而是 **可独立验证的垂直切片**。  
- 文档的价值在于 **能否在 review/ship 时被检验**，而不是页数。

> 思考方式：**先问「怎样算错」，再写实现。**

### 2.2 阶段即边界，而非流水线按钮

每个 skill 是一个 **有 Stop 条件的专业角色**：

- 做完 **一件事** → 输出 → **停** → 用户决定是否进入下一阶段  
- **不** auto-invoke 下一 skill — 避免 Agent 独自跑完「假 SDD」  

这反映一种工程判断：**自动化擅长执行，不擅长替用户承担 scope 与发布责任。**

### 2.3 默认轻量，按需加重

| 默认 | 按需 |
|------|------|
| spec + plan | grill、clarify 文件 |
| Current Context 写本变更事实 | CONTEXT.md（域语言） |
| Constraints 写本变更 trade-off | docs/adr/（跨 feature 决策） |

**YAGNI 应用于流程本身：** 没有重复痛点，就不加 stage、不加持久状态文件。

### 2.4 证据优于断言

- **Review** 只读 — 发现 defect，不「顺手修」  
- **Ship** 复验 — review pass ≠ 可以交付  
- **改 skill / 加 artifact** — 要 **第二次闭环** 等真实用法证据（见 [AGENTS.md](../../AGENTS.md)）  

> 思考方式：**Claim 必须对应 observable evidence。**

### 2.5 平台中立

Skill 是 **纯 Markdown 指令**，不绑定 Cursor hook、Claude 命令或特定 CLI。  
工程方法应 **可移植** — 同一份 skill 拷贝到任意 Agent 环境都能读。

---

## 3. 方法支柱

### 3.1 分离「想清楚 / 写契约 / 拆任务 / 做 / 查 / 交」

```text
grill     → 决策与共识（可选）
spec      → 做什么、验收标准
plan      → 怎么分步验证
build     → TDD 实现
review    → 独立审 diff
ship      → Fresh verification + 交付边界
```

**为何分开：**

| 混合在一起的后果 |
|------------------|
| 想清楚 + 写 AC 同屏 | AC 里藏 implementation steps |
| 实现 + review 同人 | 确认偏误，漏测 |
| review + ship 合并 | 「看过 diff」被当成「跑过测试」 |

这与经典 **Inspection ≠ Testing**、**Design ≠ Construction** 一致，只是粒度适配 Agent 会话。

### 3.2 垂直切片（Vertical Slice）

Plan 强调 **15–60 分钟、端到端可验证** 的 slice，而非层间大 bang：

- 每个 slice 映射至少一个 AC  
- 先 **red-green-refactor**，再下一个 slice  

**思考：** 集成风险越早暴露越好；Agent 尤其容易在「层间 stubs」里假进度。

### 3.3 采访式决策（Grill）

Grill 继承 **grill-me / brainstorming** 的纪律：

- **一次一问** — 避免信息洪水与伪共识  
- **每问带推荐** — Agent 不是空白问卷，而是有立场的 sparring partner  
- **Explore + Challenge** — 既收敛多方案，也压测已有 plan  

**思考：** 架构与产品决策是 **序贯依赖树**；并行抛 10 个结论通常意味着没有真正 decision。

### 3.4 Scope 诚实（Review）

Review 的 merge-base diff + **pre-existing 不得 must-fix** 体现：

- 只对 **本次 increment** 负责  
- 不把「顺手修全库」包装成 deliverable  

**思考：** 可维护性重要，但 **scope creep 是 Agent PR 的第一类风险**；必须语言上区分 delivery blocker vs observation。

### 3.5 契约可修订（Spec Revision）

Build/review 中发现 AC 需改时：

- **原地修订** + Revision log — 一条 spec 一条线  
- 区分 **措辞澄清** vs **AC 变更** — 避免无效 re-approval 或跳过批准  

**思考：** 计划会变，但变更必须 **可追溯、可批准** — 不是 silent mutation。

---

## 4. 知识如何分层

```text
         ┌─────────────────────────────────────┐
         │  CONTEXT（可选）— 怎么说、域边界      │
         └─────────────────────────────────────┘
                           │
         ┌─────────────────────────────────────┐
         │  ADR（可选）— 跨 feature 为什么这样选 │
         └─────────────────────────────────────┘
                           │
         ┌─────────────────────────────────────┐
         │  Spec — 这次交付必须真的什么          │
         │  Plan — 这次怎么分步证明              │
         └─────────────────────────────────────┘
```

| 层 | 时间尺度 | 典型问题 |
|----|----------|----------|
| CONTEXT | 跨 many specs | 「Order 还是 Purchase？」 |
| ADR | 跨 many features | 「为何 event-sourced？」 |
| Spec Decisions / Constraints | 本变更 | 「本 PR 为何选 gateway rate limit？」 |
| AC | 本变更、可测 | 「When X then Y」 |

**原则：** 不要把所有知识塞进 spec — **重复越多，越该下沉到 CONTEXT/ADR**；默认项目 **不必** 下沉。

详见 [context-adr-workflow.md](./context-adr-workflow.md)。

---

## 5. 人与 Agent 的分工假设

| 人 | Agent |
|----|-------|
| 批准 spec / plan | 起草 spec / plan |
| 选择下一 stage | 推荐下一 stage（不自动执行） |
| Explicit push / PR / release | 运行验证、呈现 evidence |
| 接受 should-fix 风险 | 区分 must-fix / should-fix |
| 在 grill 中做 value judgment | Explore 方案、Challenge 假设 |

**隐含前提：** 用户 **在场**；SDD skills 不是无人值守 CI pipeline。  
若未来要无人值守，需要 **另外** 的状态与门禁 — 那已超出本仓库 non-goals。

---

## 6. 与常见做法的关系

| 做法 | sdd-skills 的态度 |
|------|-------------------|
| **完整 superpowers 环**（worktree、subagent、自动链） | 吸收 TDD/review/plan 思想；**丢弃** 重基础设施 |
| **仅 README + 口头约定** | 不够 — Agent 需要 **触发条件清晰的 skill** |
| **Jira 驱动** | 不内置 — plan slice 可对 issue，但不强制 |
| **Big Design Up Front** | 反对 — grill/spec 要 **小、可批准、可修订** |
| **No spec 直接写** | 小 reversible fix 可跳过 grill；**meaningful change 仍要 spec** |
| **matt CONTEXT + grill-with-docs** | 可选借鉴；见 [context-adr-workflow.md](./context-adr-workflow.md) |

**融合而非镜像：** 上游工程观见 [upstream-engineering-rationale.md](./upstream-engineering-rationale.md)；映射与 Local decisions 见 [SOURCES.md](../../SOURCES.md)。

---

## 7. 演化哲学

1. **先跑通闭环，再定版本** — 0.1.0 前需要第二次真实 spec→ship。  
2. **先减 skill 数量，再加能力深度** — 8→7（brainstorm∪grill）是 **减熵**。  
3. **单项目经验不反向污染基线** — 不为某一 repo 的特例改 platform-neutral skill。  
4. **设计文档与 skill 分离** — `docs/design/` 存 **为什么**；`SKILL.md` 存 **怎么做**（简洁）。  
5. **Atomic commits + 中文 body** — 维护者决策同样要 **可读、可追溯**。

---

## 8. 反模式（本方法明确反对）

| 反模式 | 为何有害 |
|--------|----------|
| 文件存在 = 用户批准 | 假进度 |
| 每个 trade-off 一篇 ADR | 文档通胀 |
| Review 中改产品代码 | 失去独立视角 |
| Ship 静默 push | 用户失去交付控制 |
| 持久 workflow status.json | 状态机 + 平台绑定 |
| 为「看起来专业」加第 N 个 skill | sprawl，无 evidence |
| spec 里写 file-by-file 实现 | 混淆 spec 与 plan |
| Agent 一次输出整棵决策树 | 伪共识（grill 反模式） |

---

## 9. 如何用这套思考

**如果你是维护者：**

- 新想法先问：**补的是 SDD 环哪一段断档？有重复痛点吗？**  
- 能通过扩展现有 skill / 模板解决吗？  
- 上游变了 — 更新 SOURCES pin + Local decisions，而非 silent drift  

**如果你是用 SDD 的项目：**

- 小改动：**spec → plan → build** 可能够，grill 可跳过  
- 术语乱：**再考虑 CONTEXT**  
- 架构决策跨 feature：**再考虑 ADR**  
- 永远：**AC 必须可 pass/fail**  

**如果你是 Agent：**

- 读 skill 的 **When to Use** 与 **Stop Conditions**，不要 invent 阶段  
- 推荐下一 skill 时 **只推荐一个**，不链式 invoke  

---

## 10. 进一步阅读

- [project-decisions.md](./project-decisions.md) — 决策与时间线  
- [upstream-engineering-rationale.md](./upstream-engineering-rationale.md) — 三上游工程观  
- [context-adr-workflow.md](./context-adr-workflow.md) — 可选 CONTEXT/ADR（proposed）  
- [docs/design/README.md](./README.md) — 阅读顺序  
- [README.md — Design](../../README.md#design)  
- [SOURCES.md — Why seven skills](../../SOURCES.md#why-seven-skills) — core loop；optional satellites **`sdd-improve`** / **`sdd-zoom`** 见 [README Skills](../../README.md#skills) 与 [consumer-loops/](./consumer-loops/)
