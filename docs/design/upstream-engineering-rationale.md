# 上游仓库：软件工程方法与思考

Status: **living document**（随 [SOURCES.md](../../SOURCES.md) pin commit 更新而修订）

Snapshot: **2026-06-08**（与 [SOURCES.md](../../SOURCES.md) 记录一致）

下列描述对应 SOURCES 中 pin 的三仓库 commit，**不是**上游 live `main` 的实时镜像。

Related: [software-engineering-rationale.md](./software-engineering-rationale.md)（本仓取舍）· [project-decisions.md](./project-decisions.md)（skill 映射）

---

## 1. 为何单独记录

[SOURCES.md](../../SOURCES.md) 记录 **哪个上游 skill 映射到哪个本地 skill**。  
本文件记录 **上游背后的工程观**：他们试图修复什么失败模式、默认假设是什么。

用途：

- 理解 **为何** sdd-skills 融合而非复制  
- 上游升级时，判断是 **吸收思想** 还是 **噪音**  
- 避免把 **平台绑定** 或 **重基础设施** 误当作 SDD 必需  

---

## 2. 三仓库一句话

| 仓库 | Pin commit | 工程观关键词 |
|------|------------|--------------|
| [obra/superpowers](https://github.com/obra/superpowers) | `6fd4507659784c351abbd2bc264c7162cfd386dc` | **全自动方法论**、spec→plan→subagent 长自治、TDD/YAGNI/DRY |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | `c076972e2626fe2acc30b00a6c7240d4c5fb786a` | **生产级技能目录**、生命周期 slash 命令、spec before code |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `be55a7970319ede7965edbb02b5e41cba1ca82c9` | **小 skill 可组合**、grill 对齐、CONTEXT/ADR、经典工程书 |

---

## 3. 共同主题（跨上游）

1. **Spec / 计划先于大量写码** — 降低 misalignment。  
2. **TDD 或测试作为反馈环** — Agent「盲飞」时用 red-green 约束。  
3. **Skill = 可复用工作流** — 不是一次性 prompt。  
4. **Review / verification 与 implementation 分离** — 不同「角色」或阶段。  

**分歧：**

| 维度 | superpowers | agent-skills | matt |
|------|-------------|--------------|------|
| 自动化程度 | 高（自动触发、subagent 长跑） | 中（命令 + 自动触发） | 低（小 skill，人选用） |
| 平台绑定 | 强（多 harness 插件） | 强（多 IDE 文档） | 弱（skills.sh 安装） |
| 域文档 CONTEXT | 无一等文件 | 无 | **有**（grill-with-docs） |
| 状态 / worktree | worktree、子 agent 状态 | 因 skill 而异 | issue 标签、本地配置 |

---

## 4. obra/superpowers

### 4.1 核心叙事（README）

> Agent 不应一开工就写码；先 **问清真正要做什么** → 展示 **可读 spec 块** → 用户批准 → 写 **junior 也能跟的计划**（强调 **真 TDD、YAGNI、DRY**）→ **subagent-driven-development** 自治数小时。

**隐含假设：**

- 用户愿意走 **完整环**  
- **Subagent + 自动 skill 触发** 可接受  
- Plan 要 **足够细**（「零 codebase 上下文的外包工程师」）  

### 4.2 代表性 skill 思想

| Skill | 思考要点 |
|-------|----------|
| **brainstorming** | 设计前先探索；visual companion 等 |
| **writing-plans** | Plan 含文件地图、2–5 分钟步长；**DRY/YAGNI/TDD**；默认 `docs/superpowers/plans/` |
| **using-git-worktrees** | 隔离执行与 dirty working tree |
| **subagent-driven-development** | 每 task 独立 agent；implementer + reviewer 子角色 |
| **test-driven-development** | Red-green-refactor 纪律 |
| **requesting-code-review / verification-before-completion** | Review 与「完成前验证」分离 |
| **finishing-a-development-branch** | 合并/清理分支的显式阶段 |

### 4.3 sdd-skills 的取舍

**吸收：** TDD、plan 垂直切片思想、review 只读、ship 前 fresh verification、brainstorm/grill 前澄清。  

**刻意不吸收：** 自动链式 invoke、worktree 强制、subagent 编排、superpowers 专用 plan 路径、session hook 注入。

---

## 5. addyosmani/agent-skills

### 5.1 核心叙事（README）

> **Production-grade engineering skills** — 编码 senior 工程师在 **各开发阶段** 的工作流与质量门禁，让 Agent **一致** 遵循。

**生命周期命令（概念模型）：**

| 阶段 | 原则 |
|------|------|
| `/spec` | Spec before code |
| `/plan` | Small, atomic tasks |
| `/build` | One slice at a time |
| `/test` | Tests are proof |
| `/review` | Improve code health |
| `/code-simplify` | Clarity over cleverness |
| `/ship` | Faster is safer |

另：**领域 skill 自动触发**（API 设计、前端等）— 大 catalog，按任务类型挂载。

### 5.2 思考要点

- **广覆盖** — SDD 只是众多 skill 之一（`spec-driven-development` 等）。  
- **平台安装文档** — Cursor / Gemini / Copilot 等各一套（与本仓 **平台中立** 对比鲜明）。  
- **「证明」导向** — `/test` 独立强调 tests as proof（本仓把验证 mainly 放在 build + ship）。  

### 5.3 sdd-skills 的取舍

**吸收：** spec→plan→build→review→ship 环、`using-agent-skills` 式路由、spec/plan 分解、incremental implementation。  

**不吸收：** slash 命令体系、大 catalog 自动触发、平台 setup 文档、独立 `/test` / `/code-simplify` stage（本仓合并进 build/review/ship）。

---

## 6. mattpocock/skills

### 6.1 核心叙事（README）

> **Skills for real engineers** — 小、可改编、可组合；**反对** GSD/BMAD/Spec-Kit 等 **拿走控制** 的流程框架。

**四大失败模式与修复：**

| # | 失败模式 | 修复 | 工程书锚点 |
|---|----------|------|------------|
| 1 | Agent 没做对你要的 | **grill-me / grill-with-docs** 采访式对齐 | Pragmatic Programmer — 没人一开始就知道自己要什么 |
| 2 | Agent 太啰嗦 | **CONTEXT.md** 共享域语言 | Evans — Ubiquitous Language |
| 3 | 代码不工作 | **TDD**、**diagnose** 反馈环 | Pragmatic Programmer — 小步、反馈速率 |
| 4 | 泥球架构 | **improve-codebase-architecture**、to-prd、zoom-out | Beck — 每日投资设计；Ousterhout — 深模块 |

### 6.2 CONTEXT + ADR（grill-with-docs）

- **grill-with-docs** = grill-me + **inline 更新** `CONTEXT.md` 与 ADR。  
- **CONTEXT-FORMAT**：术语 + `_Avoid_`；单域根 `CONTEXT.md`；多域 **`CONTEXT-MAP.md`** + 各域 `CONTEXT.md`。  
- **setup-matt-pocock-skills**：每 repo 配置 issue tracker、标签、域文档布局 — **消费者 skill 先读 CONTEXT/ADR**。  
- **Lazy create**：无 CONTEXT 时 **静默继续**，术语落定再建。

### 6.3 其他工程 skill 思想

| Skill | 要点 |
|-------|------|
| **tdd** | 垂直 slice + red-green-refactor |
| **to-issues** | Plan/PRD → 可独立 grab 的 GitHub issues |
| **to-prd** | 从对话 **合成** PRD issue（非采访） |
| **diagnose** | reproduce → minimise → hypothesise → instrument → fix |
| **improve-codebase-architecture** | CONTEXT + ADR  informed 重构机会 |
| **triage** | Issue 状态机 + 标签词汇 |

### 6.4 sdd-skills 的取舍

**吸收：** grill-me 一问一答、brainstorm 探索、to-prd/to-issues 的 spec/plan 精神、tdd、review 实践。  

**部分吸收 / proposed：** CONTEXT、ADR — 见 [context-adr-workflow.md](./context-adr-workflow.md)（**未** inline grill 写 ADR；**未** setup-matt 式 per-repo scaffold）。  

**不吸收：** issue tracker 绑定、triage 状态机、diagnose/zoom-out/prototype 等 **非 SDD 环** skill 进本仓。

---

## 7. 对照：上游 vs sdd-skills

```text
           superpowers          agent-skills           matt              sdd-skills
自动化     高                   中                     低                低（用户选 stage）
产物路径   superpowers/plans    因 skill 而异          issues/PRD        docs/sdd/*-spec/plan
域语言     无 CONTEXT           无                     CONTEXT+ADR       optional（proposed）
平台       插件生态             多 IDE 文档            skills.sh         平台中立 Markdown
Skill 数   多                   很多                   多                **7**（刻意减熵）
```

**本仓合成公式（见 [software-engineering-rationale.md](./software-engineering-rationale.md)）：**

> superpowers 的 **阶段纪律** + agent-skills 的 **生命周期清晰** + matt 的 **grill 与域语言（可选）** − **自动编排与平台锁**。

---

## 8. 维护说明

1. **不要** 把本文当作上游官方文档 — 它是 **pin commit 时的解读**。  
2. 上游升级：按 [SOURCES.md — Updating](../../SOURCES.md#updating)  diff 行为，再 **选择性** 更新本节与 Local decisions。  
3. 若上游 README 叙事变化，更新 **§3–6** 与 pin commit 日期。  
4. 本文件 **不** 替代 THIRD_PARTY_NOTICES 或许可证信息。

---

## 9. 参考链接

- [SOURCES.md](../../SOURCES.md)
- [superpowers @ 6fd45076](https://github.com/obra/superpowers/tree/6fd4507659784c351abbd2bc264c7162cfd386dc)
- [agent-skills @ c076972e](https://github.com/addyosmani/agent-skills/tree/c076972e2626fe2acc30b00a6c7240d4c5fb786a)
- [mattpocock/skills @ be55a797](https://github.com/mattpocock/skills/tree/be55a7970319ede7965edbb02b5e41cba1ca82c9)
- matt：`skills/engineering/grill-with-docs/CONTEXT-FORMAT.md`（pin 同上）
