# sdd-skills 项目决策记录

Status: **living document**（随仓库演进更新）

Last updated: 2026-06-09

本文件记录 **sdd-skills 仓库本身** 的设计目标、演化过程、各技能与关键文件的决策及被拒方案。

| 文档 | 内容 |
| --- | --- |
| [software-engineering-rationale.md](./software-engineering-rationale.md) | 本仓工程方法与思考（**why**） |
| [upstream-engineering-rationale.md](./upstream-engineering-rationale.md) | 三上游工程观与取舍（pin 快照） |
| [context-adr-workflow.md](./context-adr-workflow.md) | 使用方 optional CONTEXT/ADR（**proposed**） |

---

## 1. 项目目标

**做什么：**

- 提供 **轻量、平台中立** 的 Spec-Driven Development（SDD）Agent Skills。
- 覆盖交付环：**路由 →（可选）澄清 → spec → plan → build → review → ship**。
- 从 [mattpocock/skills](https://github.com/mattpocock/skills)、[obra/superpowers](https://github.com/obra/superpowers)、[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) **融合**想法，而非镜像上游目录。

**不做什么（Non-goals）：**

| 排除项 | 原因 |
|--------|------|
| 平台命令、hooks、persona、平台 manifest | [AGENTS.md](../../AGENTS.md) 平台中立 |
| 工作流状态机、active-increment 文件 | 避免变 PM 工具 |
| 自动串联下一阶段 skill | 每 skill stop 后由用户加载下一 skill |
| Git 工作流框架（强推 worktree、每 slice commit） | 保持可选、用户显式 |
| 调试/PR 拆分等「大全」skill | 非 SDD 环必需 |
| 为对齐上游 skill 数量而加 stage | [SOURCES.md — Why seven skills](../../SOURCES.md#why-seven-skills) |

---

## 2. 仓库结构与文件职责

```text
sdd-skills/
├── AGENTS.md              # 维护者约束（平台中立、自检、提交规范）
├── README.md              # 用户入口：workflow、技能表、Quick routing、Minimal Artifacts
├── SOURCES.md             # 上游快照 + 各 skill 来源与 Local decisions
├── THIRD_PARTY_NOTICES.md # 第三方许可
├── LICENSE
├── tests/check.py         # 无第三方依赖的仓库契约校验
├── skills/<name>/SKILL.md # 自包含技能（统一八段结构）
├── skills/sdd-spec/spec-template.md
├── skills/sdd-plan/plan-template.md
└── docs/design/           # 设计决策与方法论文档（非 SDD 默认产物）
    ├── README.md
    ├── software-engineering-rationale.md
    ├── upstream-engineering-rationale.md
    ├── project-decisions.md
    ├── context-adr-workflow.md
    └── consumer-loops/     # semver gate runbooks + per-project evidence
        ├── README.md
        ├── runbook-0.1.0.md
        ├── todo-web-0.1.0.md
        └── …
```

| 文件 | 决策 |
|------|------|
| **AGENTS.md** | skill 自包含；`SKILL.md` frontmatter 写触发条件；无真实用法证据不加状态字段；改 skill 跑 `check.py`；Conventional Commits + 中文 body |
| **README.md** |  workflow 图 + 技能表 + Quick routing → 链到 `using-sdd` 详例；Design 段列 non-goals |
| **SOURCES.md** | 记录三上游 **pin commit**；每 skill 映射来源 + **Local decisions**（本仓 maintainer 的「ADR 等价物」） |
| **tests/check.py** | 自动发现 `skills/*/SKILL.md`；校验 core 七技能齐全、frontmatter、八段标题、模板、本地链接 |
| **docs/design/** | 决策过程、方法论、proposed 子方案；**consumer-loops/** 存发版 gate 实证；**不**替代 `SKILL.md` |

---

## 3. 演化时间线

按时间顺序（旧 → 新）：

| 提交 | 决策摘要 |
|------|----------|
| `1417d7d` | 初始化 AGENTS、LICENSE |
| `2e1bcce` | **7 技能**初版：`using-sdd`、`sdd-brainstorm`、`sdd-spec`…`sdd-ship`（**尚无** `sdd-grill`） |
| `6281ff3` | README、SOURCES |
| `7d247e6` | spec **只产出** `docs/sdd/...-spec.md`；禁止 domain 文档替代 spec |
| `c8e000f` | review merge-base scope；pre-existing 非 must-fix；恢复平台中立基线 |
| `9427dc9` | spec/plan 模板写作指引 |
| `96f8969` | 新增 **`sdd-grill`** → **8 技能** |
| `1a407c7` | 澄清 brainstorm/grill 边界；build 回退；ship 输出模板 |
| `21a5622`, `ffa88b8` | grill 对齐 grill-me；可 standalone |
| `441844d` | README Quick routing、`using-sdd` Routing examples、Why seven/eight 文档 |
| `cce9a6a` | **8→7**：删除 `sdd-brainstorm`，并入 `sdd-grill`；**spec Revision** |
| `eb1472c` | 新增 `docs/design/`（project-decisions、context-adr） |
| `655508b` | README 链到 project-decisions |
| `397aa90` | spec-template Decisions/Related ADRs；README optional ADR |
| `8f41dfd`–`9349079` | 方法论文档、上游解读、design 检修 |
| `5926403` | README Installation 多 Agent 说明 |
| `d88c4ef` | 第二次闭环 runbook |
| `2d81023` | todo-web 闭环记录；**`v0.1.0`** tag |
| 2026-06-09 | **`v0.1.1`** — maintainer 轻量 SDD 实践借鉴（self-review、plan Risks；原独立仓库已退役）；PR #1 |
| 2026-06-09 | 消费者 **todo-web** 闭环 Pass — [todo-web-0.1.0.md](./consumer-loops/todo-web-0.1.0.md) |
| 2026-06-09 | **`v0.2.0`** — `sdd-architect` + `sdd-zoom`；todo-web 第三次闭环 — [todo-web-0.2.0.md](./consumer-loops/todo-web-0.2.0.md) |
| 2026-06-09 | **`v0.2.1`** — CI `check` workflow + consumer-loop 状态同步（无新 consumer gate） |

**版本门禁（设计稿共识）：** **`v0.1.0`** 已于 todo-web 第二次闭环后发布（2026-06-09）。此后新增 skill 或 major 行为变更，需新 consumer 闭环与摩擦证据；不为对齐而上新 skill。

---

## 4. 技能集演化：为何是 7 个 core + optional satellite

### 4.1 决策过程（grill 摘要）

| 问题 | 结论 |
|------|------|
| 扩仓目标 | 只补 SDD 流水线断档，不对齐上游数量 |
| 8 技能环是否有洞 | 暂无重复痛点 → 不加第 8 个 **core stage** |
| **`sdd-improve` satellite** | 2026-06-11 — 融合 shadcn/improve 审计 + architect category 5；**optional**，不进 core loop；**待** consumer trial |
| **`sdd-architect` satellite** | 2026-06-09 发布 → 2026-06-11 由 **`sdd-improve`** 接替并**删除** |
| brainstorm vs grill | 流程高度重叠（一问一答）→ **合并为 `sdd-grill`** |
| 合并后命名 | **`sdd-grill`**（保留 "grill me" 触发） |
| 合并后相位 | **Explore**（比方案、rejected）+ **Challenge**（压测 plan） |

### 4.2 被拒的第 8/9 skill 候选

`sdd-debug`、`sdd-pr`、`sdd-handoff`、`sdd-accept-risk`、`sdd-amend-spec`（独立）、`sdd-maintain`、仅因上游齐全而加的 stage 等 — 均无 **重复真实痛点**，违反 non-goals。

### 4.3 当前流水线

```text
using-sdd
  → sdd-grill (optional)
  → sdd-spec → user approval
  → sdd-plan → user approval
  → sdd-build
  → sdd-review → (findings) sdd-build | (pass) sdd-ship

Optional satellites (not in loop above): **`sdd-zoom`** — territory map; **`sdd-improve`** — codebase audit; route via `using-sdd`.
```

---

## 5. 各技能决策

统一结构：`Goal · When to Use · Prerequisites · Process · Red Flags · Verification · Output · Stop Conditions`。  
**Stop 后推荐下一 skill，不 auto-invoke。**

### 5.1 `using-sdd`

| 项 | 决策 |
|----|------|
| 来源 | superpowers `using-superpowers`；agent-skills `using-agent-skills` |
| 职责 | 从 artifact/diff **推断**阶段；**不**持久化状态 |
| 路由 | 一条 next skill；含 Pre-spec / Core / Review loop / **Escalation from build** |
| Escalation | slice 细节 → stay build；slice/验证变 → plan；AC/约束变 → **spec Revision** |
| 文档 | [Routing matrix](../../skills/using-sdd/SKILL.md#routing-matrix) 为详例源，README Quick routing 为入口短表 |

### 5.2 `sdd-grill`

| 项 | 决策 |
|----|------|
| 来源 | grill-me + superpowers brainstorming + interview-me / idea-refine |
| 合并 | 原 `sdd-brainstorm` 的探索比方案、rejected、边界收敛 |
| 交互 | **一次一问** + 每问带推荐答案；先读仓库再问你 |
| 产物 | 默认无磁盘 artifact；复杂时可写 `docs/sdd/...-clarify.md` |
| Standalone | 可脱离 SDD 用于任意决策 |
| Red Flags | **不写** spec/plan/code/design docs（**proposed 例外**：CONTEXT Language、纯 ADR — 见子文档，未写入 SKILL） |
| Stop | → `sdd-spec` 或 `sdd-plan` |

**brainstorm vs grill（历史边界，合并前）：** brainstorm 收敛多方向；grill 压测已有方案 — 现为一体两相。

### 5.3 `sdd-spec`

| 项 | 决策 |
|----|------|
| 来源 | brainstorming、spec-driven-development、to-prd |
| 产出 | **仅** `docs/sdd/YYYY-MM-DD-<topic>-spec.md` |
| 拒绝 | 用 CONTEXT/domain 文档**替代** spec（`7d247e6`） |
| 批准 | 显式用户批准；文件存在 ≠ 批准 |
| **Revision** | 原地改同一 spec；**Revision log**；非 AC 澄清 vs AC 变更分流；条件性回 plan |
| 模板 | [spec-template.md](../../skills/sdd-spec/spec-template.md)：Goal…AC、Constraints、可选 Decisions/Related ADRs、Revision log |
| Stop | 新 spec / 修订后 → `sdd-plan`（或回到 build/review） |

### 5.4 `sdd-plan`

| 项 | 决策 |
|----|------|
| 来源 | writing-plans、planning-and-task-breakdown、to-issues |
| 前置 | **已批准 spec** |
| 切片 | 15–60 分钟垂直 slice，非微任务 |
| 拒绝 | 独立追溯矩阵、workflow status |
| 产出 | `docs/sdd/YYYY-MM-DD-<topic>-plan.md` |
| 模板 | Slice / Goal / Acceptance / Verification |

### 5.5 `sdd-build`

| 项 | 决策 |
|----|------|
| 来源 | tdd、test-driven-development、incremental-implementation |
| 前置 | 已批准 spec + plan；读 AGENTS/README/linters（有则）；无风格说明 → spec/plan + touched 代码 |
| 方法 | red-green-refactor；slice 幂等；red 须 **intended behavior** |
| 回流 | review findings **只修 listed 项**，不扩 scope |
| 回退 | AC/约束变 → spec；slice/验证变 → plan；局部 → stay build |
| Stop | → **`sdd-review`**；禁止 premature **`sdd-ship`** / merge-ready 宣称 |
| 拒绝 | 强制 worktree、subagent、每 slice commit |

### 5.6 `sdd-review`

| 项 | 决策 |
|----|------|
| 来源 | requesting-code-review、verification-before-completion、code-review-and-quality |
| 模式 | **严格只读** |
| Scope 优先级 | 用户指定 → 任务/plan 记录 → staged（显式）→ 任务相关未提交 → **merge-base…HEAD** |
| 分支 | 不假设 `main`；用 `origin/HEAD` 或仓库约定 |
| Pre-existing | diff 外既有问题 → **out-of-scope 观察**，不得 must-fix |
| Plan | 有 plan 时 **Acceptance 逐条映射**（met/partial/missing/unclear） |
| 大 diff | ~30+ 文件或 >300 行 → triage 高风险区；**Limits** 写入 Assumptions |
| 维度 | Standards（CI 已 gate 不重复）；Architecture 与 **`sdd-improve`** 分界（全库/branch 体检 → improve；diff 内 → review） |
| Output | 固定标题：Scope、Strengths、Findings、Dimension Coverage、Assumptions & Gaps、Verdict |
| 验证 | 完整复验在 **`sdd-ship`** |

### 5.7 `sdd-ship`

| 项 | 决策 |
|----|------|
| 来源 | verification-before-completion、finishing-a-development-branch、shipping-and-launch |
| 前置 | spec、plan、review 结论、diff |
| 证据 | 按风险比例 Fresh verification |
| 交付 | commit/push/PR/release/**用户显式** |
| CHANGELOG | [CHANGELOG.md](../../CHANGELOG.md)；发版时由 `sdd-ship` 或显式维护更新 |
| 拒绝 | 静默发布 |

### 5.8 `sdd-improve`（optional satellite）

| 项 | 决策 |
|----|------|
| 来源 | [shadcn/improve](https://github.com/shadcn/improve) (MIT) 摘要 + Matt `improve-codebase-architecture`（category 5） |
| 定位 | **Optional satellite** — 不进 core 七阶段环；**非** delivery review |
| 产物 | **conversation findings report**；默认**不落盘**；无 `plans/` |
| 流程 | Profile (optional) → Audit → Verify → Present → Confirm → Stop；**无 Simplify 命名** |
| 边界 | vs **`sdd-review`**：机会扫描 vs increment diff 交付门禁 |
| CONTEXT/ADR | 有则读；无则继续；**不** inline 写 |
| Stop | → **`using-sdd`**；默认 **`sdd-spec`** / **`sdd-grill`** |
| Spec | [2026-06-11-sdd-improve-spec.md](../../docs/sdd/2026-06-11-sdd-improve-spec.md) |

### 5.9 `sdd-zoom`（optional satellite）

| 项 | 决策 |
|----|------|
| 来源 | Maintainer zoom-out 实践（consumer 会话中 unfamiliar territory 前置） |
| 定位 | **Optional satellite** — 不进 core 七阶段环 |
| 产物 | 对话 territory map；**Map 默认 Mermaid 关系图**（≥3 单元）；表列 role/inbound/outbound；默认**不落盘** |
| 边界 | **只描述**模块/caller/域词汇；**不给** refactor findings（→ **`sdd-improve`**）；与 improve 不同，zoom **鼓励** diagram deliverable |
| CONTEXT/ADR | 有则读；无则代码 + SDD artifact；**不** inline 写 |
| Stop | → **`using-sdd`**；常见下一环 spec / grill / improve |

---

## 6. 工作流与产物决策

### 6.1 默认必填产物

```text
docs/sdd/YYYY-MM-DD-<topic>-spec.md   # 用户批准
docs/sdd/YYYY-MM-DD-<topic>-plan.md   # 用户批准
```

### 6.2 默认可选产物

| 产物 | 说明 |
|------|------|
| `docs/sdd/...-clarify.md` | grill 复杂决策留存 |
| review 输出 | 对话内，非强制文件 |
| `docs/adr/`、`CONTEXT.md` | **可选**；见 [context-adr-workflow.md](./context-adr-workflow.md) |

### 6.3 本仓 maintainer 文档（非用户 SDD 产物）

| 文档 | 作用 |
|------|------|
| `SOURCES.md` | 上游映射 + Local decisions |
| `AGENTS.md` | 仓库维护约束 |
| `docs/design/*.md` | 决策过程、方法论、proposed 子方案 |

### 6.4 本仓 Git 工作流（maintainer）

| 项 | 决策 |
|----|------|
| **`main`** | **集成分支** — 禁止日常直接 commit/push |
| 开发 | `feat/*` / `fix/*` / `docs/*` 分支 → PR → merge |
| **PR 粒度** | **按主题合并，避免频繁 PR** — 一个 PR 一个可 review 主题；分支上可多条 atomic commit；发版准备 + watchlist/tag 收尾尽量同一 PR，不为小 doc 修单独开 PR |
| 验证 | PR 前 `python3 tests/check.py`；发版前 `sdd-ship` |
| Tag | 仅在 merge 后的 `main` 上打 semver tag |
| 与 skill non-goals 关系 | **不**强推 worktree、每 slice commit — 仅约束 **本仓** 集成方式 |
| GitHub | **`main` branch protection**（require PR）；**GitHub Actions** `check / validate` 跑 `tests/check.py`（GitLab 等价：`.gitlab-ci.yml`） |

**现状（2026-06-09）：** `main` branch protection 与 required check **`validate`** 已启用；日常开发走分支 + PR。

---

## 7. 跨切原则

1. **平台中立** — 技能自包含，无 Cursor/Claude 专用 manifest。  
2. **无状态机** — 不从 artifact 推断「当前阶段字段」写回磁盘。  
3. **一问一答** — grill（及原 brainstorm）采访式决策树。  
4. **证据门禁** — 新 stage / 持久状态 / L2 CONTEXT-ADR 需真实项目重复痛点。  
5. **不受单个下游项目绑架** — 外部 repo 闭环经验不反向改 skill 基线（`c8e000f`）。  
6. **上游融合** — 记录在 SOURCES；行为变更同步 pin commit 与 skill。

---

## 8. 待定与 Watchlist

| 项 | 状态 | 触发条件 |
|----|------|----------|
| **0.1.0 tag** | **已发布** `v0.1.0`（2026-06-09，todo-web 第二次闭环） |
| **0.1.1 tag** | **已发布** `v0.1.1`（2026-06-09，artifact 自检与 plan Risks） |
| **0.2.0 tag** | **已发布** `v0.2.0`（2026-06-09，todo-web 第三次闭环 + `sdd-zoom` 同批） | [todo-web-0.2.0.md](./consumer-loops/todo-web-0.2.0.md) |
| **0.2.1 tag** | **已发布** `v0.2.1`（2026-06-09，CI + runbook 状态同步） | 无 consumer gate |
| **`sdd-improve`** | **trial 进行中**（2026-06-11 maintainer 仓库机会扫描） | 替代 architect；见 [spec](../../docs/sdd/2026-06-11-sdd-improve-spec.md)；**待** consumer trial + semver tag |
| **`sdd-architect`** | **已删除**（2026-06-11）— 由 **`sdd-improve`** 接替 | 历史 [architect spec](../../docs/sdd/2026-06-09-sdd-architect-spec.md) |
| **`sdd-zoom`** | **已添加；v0.2.0 同批发布，gate 未覆盖** | 待第四次 consumer 闭环或重复 zoom-out 摩擦；见 [runbook-0.2.0.md](./consumer-loops/runbook-0.2.0.md) 脚注 |
| **CONTEXT/ADR L2** | proposed | 见 [context-adr-workflow.md](./context-adr-workflow.md) |
| **L1+ CONTEXT 注释** | **已做** | `spec-template` + README：`CONTEXT.md` / `docs/context/<domain>/`；Current Context 增量 |
| **context/adr-template** | 未做 | L3，有证据再做 |
| **sdd-ship ship-after checklist** | watchlist | 用户显式 push/PR 清单是否进 README |
| **`main` branch protection** | **已启用** | require PR（0 approvals）；`enforce_admins`；禁 force push / 删分支 |
| **CI `check.py`** | **已启用**（PR #5 merge；required check `validate`）；semver 记入 **`v0.2.1`** | `.github/workflows/check.yml`；GitLab 用 `.gitlab-ci.yml` 同等脚本 |

---

## 9. 维护约定

- 改 skill / 模板 → `python3 tests/check.py`  
- 吸收上游行为 → 更新 `SOURCES.md` + pin commit  
- 重大设计决策 → 更新 **本文件** 或 `docs/design/` 子文档  
- `SKILL.md` 保持 concise；长篇过程放 `docs/design/`，不塞进 skill  

---

## 10. 相关链接

- [README.md](../../README.md)
- [SOURCES.md](../../SOURCES.md)
- [AGENTS.md](../../AGENTS.md)
- [software-engineering-rationale.md](./software-engineering-rationale.md)
- [upstream-engineering-rationale.md](./upstream-engineering-rationale.md)
- [context-adr-workflow.md](./context-adr-workflow.md)
- [consumer-loops/](./consumer-loops/) — semver gate 运行手册与实证
