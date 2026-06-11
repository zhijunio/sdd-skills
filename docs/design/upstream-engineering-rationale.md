# 上游从哪来、本仓怎么取舍

Status: **living document**（重大范式变化时修订）

Pin 快照: **2026-06-08**（见 [SOURCES.md](../../SOURCES.md) 三个 Git 仓库的 commit）

本仓解读更新: **2026-06-11**（**sdd-improve** 卫星、审阅维度配对、架构吸收可读性与简化检查）

[SOURCES.md](../../SOURCES.md) 记的是「哪个上游想法进了哪个 skill」。本文记的是「上游想解决什么问题、我们为什么只拿一部分」。

Pin 住的三个仓库 **不等于** 它们 GitHub 上今天的 `main`。 [shadcn/improve](https://github.com/shadcn/improve) 另列第四节，许可证见 [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md)，本仓未 pin commit。

相关: [software-engineering-rationale.md](./software-engineering-rationale.md)（本仓怎么想）· [SOURCES.md](../../SOURCES.md)（映射与 Local decisions）

---

## 1. 为什么要写这份文档

读 skill 之前，先知道思想从哪来，才分得清：

- 哪些是 **该学的纪律**（先写 spec、测试当证据、审阅只读）
- 哪些是 **该扔的包袱**（自动串下一阶段、绑死某个 IDE、强制 worktree）

上游升级时，对照本文判断：是吸收思想，还是噪音。

---

## 2. 四个来源，各一句话

| 来源 | 快照 / 许可 | 一句话 |
|------|-------------|--------|
| [obra/superpowers](https://github.com/obra/superpowers) | `6fd45076…` | 把 SDD 做成 **全自动长跑**：spec→plan→子 agent 实现，强调 TDD、YAGNI、DRY |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | `c076972e…` | **生产级** 分阶段技能目录，用 slash 命令表达「先 spec 再写码」 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `be55a797…` | **小技能可拼装**；采访式对齐；CONTEXT/ADR；引用经典工程书 |
| [shadcn/improve](https://github.com/shadcn/improve) | MIT；未 pin | **只读代码库体检**：按类目录清单找问题，顾问角色，不替用户改代码 |

---

## 3. 上游共同点与分歧

**共同点：**

1. **先对齐再写码** — 减少 Agent 和用户各说各话。  
2. **测试是反馈** — 不能光靠「看起来对」。  
3. **Skill 是可复用流程** — 不是一次性长 prompt。  
4. **做和查要分开** — 实现的人不宜独自宣布「审过了」。  
5. **代码健康要单独看** — 本仓拆成 **交付审阅**（`sdd-review`）和 **机会扫描**（`sdd-improve`），见下文各节。

**分歧：**

| | superpowers | agent-skills | matt | shadcn/improve |
|---|-------------|--------------|------|----------------|
| 自动化 | 高：自动触发、子 agent 长跑 | 中：命令 + 部分自动触发 | 低：人选技能 | 中：体检流程，不绑 SDD 环 |
| 平台 | 插件生态重 | 多 IDE 安装文档 | skills.sh，较轻 | 独立 improve 产品向 |
| 域语言文档 | 无 | 无 | CONTEXT + ADR | 无 |
| 本仓关系 | core 环纪律来源 | 生命周期与五轴审阅 | grill、架构词汇 | **audit 类清单** 摘要 |

---

## 4. obra/superpowers — 全自动方法论

**他们在说什么：** Agent 别一上来就改文件。先弄清要什么 → 写出人能读的 spec → 人批准 → 写出初级工程师也能跟的计划（真 TDD、真 YAGNI）→ 子 agent 长跑实现。

**背后假设：** 用户愿意走完整环；能接受 worktree、子 agent、自动触发。

**我们拿什么：**

- 垂直切片计划、TDD、审阅只读、交付前再验一遍  
- 实现前先用 grill 把决策问清楚  

**我们扔什么：**

- 自动链式调用下一 skill  
- 强制 worktree、专用 plan 目录、session hook  

---

## 5. addyosmani/agent-skills — 分阶段生产技能

**他们在说什么：** 让 Agent 像资深工程师一样，在 spec、plan、build、review、ship 各阶段有一致门禁。

**概念上的阶段：** `/spec` 先契约 → `/plan` 小任务 → `/build` 一次一片 → `/test` 测试即证据 → `/review` 改健康度 → `/code-simplify` 求清晰 → `/ship` 敢发版。

**我们拿什么：**

- spec→plan→build→review→ship 主环  
- `code-review-and-quality` 的五条检查线：正确性、安全、性能、架构、可读性 — 压缩进本仓两个维度文件：  
  - **`sdd-improve`** `audit-dimensions.md`（全库/分支，类 1–9）  
  - **`sdd-review`** `review-dimensions.md`（只看本次 diff）  

**我们怎么改五轴：**

- **可读性** 和 **`/code-simplify`** 不再单独成步，并入 **架构（architecture）**：既看结构，也看重复代码和能否写更简单。  
- **交付门禁**（验收项对照、diff 类型、能否发货）只放在 **`sdd-review`**。

**相对上游「一个 /review」的拆分：**

| 上游在干什么 | 本仓 |
|--------------|------|
| 审这次改动能不能合 | **`sdd-review`** — 只看 increment diff，给交付结论 |
| 扫全库机会和风险 | **`sdd-improve`** — 体检报告，不挡发版 |

**我们扔什么：** slash 命令体系、大 catalog 自动挂载、各 IDE 安装手册、独立 `/test` 阶段（验证主要在 build + ship）。

---

## 6. mattpocock/skills — 小技能与域语言

**他们在说什么：** 技能要小、可改、可组合；反对把流程框架做成「拿走控制权」的 GSD/BMAD 式重物。

**四个典型失败与药方：**

| 问题 | 药方 |
|------|------|
| Agent 没做对你要的 | **grill-me**：一次一问，逼出真需求 |
| 术语乱、废话多 | **CONTEXT.md**：项目怎么说一件事 |
| 代码跑不起来 | **TDD**、**diagnose** |
| 架构成泥球 | **improve-codebase-architecture**：深模块、接缝、删了模块复杂度去哪 |

**CONTEXT + ADR：** matt 的 grill-with-docs 会在采访里直接改 CONTEXT 和 ADR。本仓 **不** 照抄：消费者可选 CONTEXT/ADR，见 [software-engineering-rationale §4.1](./software-engineering-rationale.md#41-可选-context-与-adr)。

**我们拿什么：**

- grill 一问一答、tdd、spec/plan 精神  
- **improve-codebase-architecture** → 卫星 **`sdd-improve`** 第 5 类（结构洞察、Strength 分级）；原 **`sdd-architect`** 已删  
- **zoom-out** 实践 → 卫星 **`sdd-zoom`**（只画地图，不给重构结论）  

**我们扔什么：** issue 状态机、triage、diagnose 进 core 环；不把 improve 和 review 合成一个审阅 skill。

---

## 7. shadcn/improve — 代码库体检清单

仓库: [https://github.com/shadcn/improve](https://github.com/shadcn/improve)  
许可: MIT（[THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md)）

**他们在说什么：** 给 Agent 一套 **只读体检** 流程 — 按类别（正确性、安全、测试、架构、依赖、体验、文档等）在代码库里找可证据化的问题，输出 **发现列表**，由人决定要不要做。角色是 **顾问**，扫描期间 **不改** 用户仓库。

**和本仓其它来源怎么拼：**

| 来源 | 进到 `sdd-improve` 的什么 |
|------|---------------------------|
| **shadcn/improve** | `audit-dimensions.md` 的 **多类清单骨架**（社区 audit playbook 摘要） |
| **agent-skills** `code-review-and-quality` | 同类里的正确性、安全、性能、架构轴 |
| **matt** `improve-codebase-architecture` | 第 5 类里的 deletion test、seam、Strength |

**我们拿什么：**

- 分类走查、只读规则、发现要带 `file:line` 证据  
- 标准档走类 1–8；用户问路线才走第 9 类 direction  

**我们扔什么 / 怎么改：**

- 不镜像 shadcn 的完整产品壳（安装、触发、执行器）  
- 不单独叫 **Simplify** 一步 — 和 agent-skills 一样，并进 **architecture**  
- 体检 **不** 当 delivery review，**不** 当 ship 门禁 — 那是 **`sdd-review`**  
- 摘要写在 `audit-dimensions.md`，**不** pin 上游 commit；大改版时对照 GitHub  diff 选择性更新  

---

## 8. 对照总表

```text
              superpowers    agent-skills      matt           shadcn/improve    sdd-skills
自动化        高             中                低             中（体检）        低（人选阶段）
主产物        长计划+子agent  分阶段命令        issues/PRD     发现报告          spec+plan
域语言        无             无                CONTEXT+ADR    无                可选（§4.1）
审阅/体检     子agent review /review+simplify  improve-arch   全库audit         review+improve卫星
平台绑定      重             重                较轻           独立产品向        纯 Markdown
```

**合成一句话：**

> superpowers 的 **阶段纪律** + agent-skills 的 **生命周期与审阅轴** + matt 的 **采访与架构词汇** + shadcn/improve 的 **分类体检清单** − **自动编排、平台锁、独立 Simplify 步骤**。

**一对维度文件（各 skill 自包含，配对见 `using-sdd`）：**

| 机会扫描 `sdd-improve` | 交付审阅 `sdd-review` |
|------------------------|------------------------|
| `audit-dimensions.md` | `review-dimensions.md` |
| 全库或 branch | 仅本次 diff |
| 🔴🟡🟢 = 先修啥 | 🔴🟡🟢 = 能不能发 |

---

## 9. 维护说明

1. 本文不是上游官方文档，是 **pin 时点的解读**。  
2. 三个 pin 仓库升级：按 SOURCES 流程 diff，再改本文对应节。  
3. [shadcn/improve](https://github.com/shadcn/improve) 无 pin：清单大变时对照仓库更新 §7 与 `audit-dimensions.md`。  
4. 行为以 `skills/**` 为准；先改 skill，再改本文与 [software-engineering-rationale.md](./software-engineering-rationale.md)。  
5. 许可证以 THIRD_PARTY_NOTICES 为准。

---

## 10. 链接

- [SOURCES.md](../../SOURCES.md)  
- [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md)  
- [shadcn/improve](https://github.com/shadcn/improve)  
- [using-sdd Disambiguation](../../skills/using-sdd/SKILL.md#disambiguation)  
- [superpowers @ 6fd45076](https://github.com/obra/superpowers/tree/6fd4507659784c351abbd2bc264c7162cfd386dc)  
- [agent-skills @ c076972e](https://github.com/addyosmani/agent-skills/tree/c076972e2626fe2acc30b00a6c7240d4c5fb786a)  
- [mattpocock/skills @ be55a797](https://github.com/mattpocock/skills/tree/be55a7970319ede7965edbb02b5e41cba1ca82c9)
