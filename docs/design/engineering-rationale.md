# 工程观与上游对照

Status: **living document**

更新: **2026-06-09**

**谁说了算：** 日常行为看 `skills/*/SKILL.md`；pin 与 skill 映射看 [SOURCES.md](../../SOURCES.md)；本文解释 **本仓怎么想、上游怎么想、我们怎么取舍**。发版与 consumer 实证见 [CHANGELOG.md](../../CHANGELOG.md)、[consumer-loops/](./consumer-loops/)。

---

## 维护提示词

> 给 Agent 或维护者：刷新、扩写或对照上游升级时使用。**先读 skill 与 SOURCES，再改本文。**

```text
任务：维护 docs/design/engineering-rationale.md（本仓工程观 + 四源上游对照）。

事实来源（按优先级）：
1. skills/<name>/SKILL.md 与 references/**
2. SOURCES.md 三个 pin 仓库的 commit + shadcn/improve（未 pin）
3. CHANGELOG.md、consumer-loops/* 已发生的 trial 证据
4. 禁止编造未发生的 consumer 结果或版本 tag

文体：直白中文；对比用表格；一节一事；不用「经调研」「值得注意的是」。

必须保留的结构：
§1 本仓要治的毛病、§1.0 核心原则（六条、形态/交付/治理）
§2 本仓落地（六段环、竖切片、review vs improve、卫星、知识分层）
§3 四源一句话 + 共同点/分歧表
§4 分源对照（每源固定五段：他们说什么 / 假设 / 拿什么 / 扔什么 / 落在哪些 skill）
§5 对照总表（superpowers | agent-skills | matt | shadcn/improve | sdd-skills）
§2.5 可选 CONTEXT/ADR（锚点 `#41-可选-context-与-adr` 保留；在 §2 内）
§6 演化原则与反模式
§7 延伸阅读
文首 §维护提示词（本节，固定不动）

分源对照写作模板（复制到 §4 每一小节）：
- **他们解决什么：**
- **背后假设：**
- **本仓拿什么 →** 对应 skill/文件
- **本仓扔什么：**
- **实现过程要点：** 从上游概念到本仓文件的一次迁移叙述（1 短段）

对比维度（总表必含）：自动化程度 | 主产物 | 审阅/体检拆分 | 域语言文档 | 平台绑定

特殊规则：
- shadcn/improve：不 pin；清单大变时对照 GitHub 更新 §4.4 与 audit-dimensions.md
- 可读性 / code-simplify：上游独立步；本仓并进 architecture（improve cat 5 + review Architecture）
- improve 的 Next stage 可 spec / build / direct edit；见 closing-the-loop.md，不在本文展开流程细节
- 与 skill 冲突时以 skill 为准；改 skill 后再同步本文

验收：文内本地链接无断链；不新增第二份 rationale 文件。
```

---

## 1. 要治什么毛病

Agent 能写代码，但常见四类问题：

1. **做着做着跑偏** — 和用户要的 behavior 不是一回事。
2. **范围偷偷变大** — 顺手改无关文件。
3. **没验证就说完了** — 「看起来对」就当 ship。
4. **流程太重** — 小改动也走完整 superpowers 长跑。

**sdd-skills 干什么：** 留下「先契约、再切片、再实现、再独立审、再复验」的纪律；去掉项目管理器、平台锁、状态机。不替代 TDD、CI、人工 review — 给 Agent **能停、能跳、能审计** 的阶段语言。

### 1.0 核心原则

六条分三层：**形态**（仓库是什么）、**交付**（消费者怎么出货）、**治理**（维护者怎么演进）。

#### 形态

| # | 原则 | 本仓落地 |
| --- | --- | --- |
| 1 | **轻量中立** | 短 `SKILL.md`；默认 spec+plan；纯 Markdown — 无 hook/slash/manifest、无强制卫星 |
| 2 | **显式阶段** | 可只装 `@sdd-spec`；用户 `@` 点名（artifact 前置见 README Skills 表）；产出 → **停** → hand off — 不自动链式、不同会话做下一阶段 |

#### 交付

| # | 原则 | 本仓落地 |
| --- | --- | --- |
| 3 | **可验切片** | Spec 写 AC；Plan 竖切片 15–60 分钟（非甘特图）；grill/zoom/improve 需要时再加 |
| 4 | **测试与证明** | `sdd-build` 先红测试；`sdd-review` 只读有据；`sdd-ship` 重跑验证、读全输出 — 无证据不断言完成 |

#### 治理

| # | 原则 | 本仓落地 |
| --- | --- | --- |
| 5 | **借鉴不重造** | pin 上游 @ SOURCES；verbatim @ pin + 最小 SDD 尾；融合取用、不镜像整库 catalog |
| 6 | **拒绝空转** | 无 consumer 证据不加核心阶段/状态字段；skill 变更靠 consumer 闭环，不用本仓 dogfood |

| 毛病（§1） | 主要靠 |
| --- | --- |
| 做着跑偏 | **可验切片**（spec AC） |
| 范围偷偷变大 | **可验切片** + **显式阶段**（停就停） |
| 没验证就说完了 | **测试与证明** |
| 流程太重 | **轻量中立** + **显式阶段** |

---

## 2. 本仓怎么落地

### 2.1 核心环

```text
grill（可选）→ spec → plan → build → review → ship
```

| 段 | 角色 |
| --- | --- |
| grill | 决策未定，一次一问 |
| spec | 本次必须满足什么（AC 可 pass/fail） |
| plan | 竖切片，15–60 分钟能验一片 |
| build | TDD；要求 approved spec+plan（review 修 fix 除外） |
| review | 只读；仅 **increment diff**；给交付结论 |
| ship | 再验一遍；不静默 push |

### 2.2 两种「审」

| | `sdd-review`（核心） | `sdd-improve`（卫星） |
| --- | --- | --- |
| 问什么 | 这次改动能发吗 | 全库/分支有啥机会 |
| 范围 | increment diff | whole repo / branch |
| 产出 | 交付结论 | findings 报告 |
| 🔴🟡🟢 | **挡 ship** | **排 follow-up**，不挡 ship |

配对：各 skill **When/Skip** 互指（improve ↔ review）；维度文件：`audit-dimensions.md` / `review-dimensions.md`。

**review diff 分类：** code diff → 必走 Architecture；prose/docs-only → 跳过 Architecture，查链接与 spec 对齐。

### 2.3 卫星

| 卫星 | 干什么 |
| --- | --- |
| `sdd-zoom` | 领土地图，无 findings |
| `sdd-improve` | 机会扫描；follow-up 可走 SDD 技能或 **direct edit**（见 `closing-the-loop.md`） |

**禁止：** improve 代替 review；improve 当 ship 门禁。

### 2.4 知识分层

```text
CONTEXT（可选）→ 域语言
ADR（可选）    → 跨 feature 架构为什么
Spec / Plan    → 这次做什么、怎么验
```

本仓维护者用 AGENTS + SOURCES，**不在** 根目录放 CONTEXT。

<a id="41-可选-context-与-adr"></a>

### 2.5 可选 CONTEXT 与 ADR

给 **消费者项目**，非本仓必填。默认仍 **spec + plan**。

| 层级 | 状态 |
| --- | --- |
| L0 spec+plan | ✅ |
| L1 模板 Decisions / Related ADRs | ✅ |
| L1+ README/spec 注释 CONTEXT 路径 | ✅ |
| L2 多 skill 统一读 CONTEXT/ADR | ❌ 等有证据 |
| L3 context/adr 模板 | ❌ |

**何时 L2：** 多篇 spec 重复术语、命名漂移、纯架构变更过多、第二次闭环证明 Constraints 扛不住 — **多条同时成立**。

目录：单域 `CONTEXT.md` + `docs/adr/`；多域 `docs/context/<domain>/CONTEXT.md`（不要 CONTEXT-MAP）。

---

## 3. 上游四源概览

Pin 快照: **2026-06-08**（[SOURCES.md](../../SOURCES.md)）。**shadcn/improve** 未 pin（MIT）。

| 来源 | 一句话 |
| --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | SDD **全自动长跑**：spec→plan→子 agent 实现，TDD/YAGNI/DRY |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | **分阶段生产技能**，slash 表达「先 spec 再写码」 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | **小技能可拼装**；grill；CONTEXT/ADR；架构深化词汇 |
| [shadcn/improve](https://github.com/shadcn/improve) | **只读体检** 按类清单；顾问角色；不替用户改代码 |

**共同点：** 先对齐再写码 · 测试作反馈 · skill 可复用 · 做/查分离 · 健康度单独看。

**分歧（摘要）：**

| | superpowers | agent-skills | matt | shadcn/improve |
| --- | --- | --- | --- | --- |
| 自动化 | 高 | 中 | 低 | 中 |
| 平台 | 插件重 | 多 IDE | 较轻 | 独立产品向 |
| 域语言 | 无 | 无 | CONTEXT+ADR | 无 |

---

## 4. 分源对照：上游 → 本仓

### 4.1 superpowers

- **他们解决什么：** Agent 别一上来改文件；spec→批准→TDD 计划→子 agent 长跑。
- **假设：** 用户愿走完整环；接受 worktree、自动触发。
- **拿什么：** 竖切片、TDD、review 只读、ship 再验、grill 式决策前置。
- **扔什么：** 自动链下一 skill、强制 worktree、session hook、plan 工厂。
- **落在：** 六核心环 + 二卫星（八技能）；无子 agent 编排。

### 4.2 agent-skills

- **他们解决什么：** spec/plan/build/review/ship 各阶段一致门禁；`/review` + `/code-simplify`。
- **拿什么：** 主环阶段；`code-review-and-quality` 五轴 → 本仓两维度文件。
- **怎么改五轴：** 可读性 + simplify **并进 architecture**；交付门禁 **只在 sdd-review**。
- **扔什么：** slash 体系、大 catalog、独立 `/test` 阶段。
- **落在：** `review-dimensions.md`、`audit-dimensions.md`；验证在 build+ship。

### 4.3 mattpocock/skills

- **他们解决什么：** 小技能组合；grill-me；CONTEXT/ADR；improve-codebase-architecture；zoom-out。
- **拿什么：** grill 一问一答；架构词汇 → **sdd-improve** cat 5；zoom → **sdd-zoom**。
- **扔什么：** issue 状态机进 core；grill 边聊边改满仓库文档（本仓 CONTEXT/ADR **可选**）；diagnose 不进 core。
- **落在：** `sdd-grill`、`sdd-improve`、`sdd-zoom`。

### 4.4 shadcn/improve

- **他们解决什么：** 分类只读体检；发现列表；扫描期不改仓库。
- **拿什么：** `audit-dimensions.md` 多类清单骨架；只读规则；标准 1–8 类。
- **扔什么：** 完整产品壳；独立 **Simplify** 步；体检当 ship 门禁。
- **落在：** `sdd-improve` + `references/`；归因在 THIRD_PARTY_NOTICES，不 pin commit。

---

## 5. 对照总表

```text
              superpowers   agent-skills    matt          shadcn/improve   sdd-skills
自动化        高            中              低            中               低（人选阶段）
主产物        长计划+子agent 分阶段命令      issues/PRD    发现报告         spec+plan
域语言        无            无              CONTEXT+ADR   无               可选 §2.5
审阅/体检     子agent       /review+simplify improve-arch 全库 audit      review+improve
平台绑定      重            重              较轻          产品向           纯 Markdown
```

**合成一句：**

> superpowers **阶段纪律** + agent-skills **生命周期与审阅轴** + matt **采访与架构词汇** + shadcn/improve **分类体检清单** − **自动编排、平台锁、独立 Simplify**。

---

## 6. 演化原则与反模式

**演化：** 先真实 spec→ship 再谈版本；core 保持 **六阶段环**；卫星不撑胖 core；**怎么做** 在 skill，**为什么** 在本文；成对命名（`audit-dimensions` / `review-dimensions`）。

| 反模式 | 为什么不行 |
| --- | --- |
| 磁盘文件 = 已批准 | 假进度 |
| review 里改产品代码 | 失去独立视角 |
| improve 挡 ship | 混淆体检与交付审 |
| 两技能 🔴 语义混用 | 一个排期一个挡发货 |
| workflow status.json | 状态机 + 平台绑定 |
| 每个取舍一篇 ADR | 文档通胀 |

---

## 7. 延伸阅读

- [SOURCES.md](../../SOURCES.md) · [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md)
- [sdd-improve](../../skills/sdd-improve/SKILL.md) / [sdd-review](../../skills/sdd-review/SKILL.md) — When/Skip
- [consumer-loops/](./consumer-loops/) · [docs/design/README.md](./README.md)
