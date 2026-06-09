# CONTEXT 与 ADR 工作流方案 — 决策记录

Status: **proposed**（设计共识；L2 技能改动尚未实现）

Date: 2026-06-08

Parent: [project-decisions.md](./project-decisions.md)

Scope: 使用 SDD 技能集的项目中，可选域文档 `CONTEXT.md` 与架构决策 `docs/adr/` 如何与默认 spec/plan workflow 共存。不适用于本仓库 `sdd-skills` 自身维护（继续用 `AGENTS.md` + `SOURCES.md`）。

---

## 背景

- 默认 SDD 产物仅 **spec + plan**（见 [README.md](../../README.md#minimal-artifacts)）。
- **L1 已落地**（`397aa90`）：`spec-template` 可选 **Decisions**、**Related ADRs**；README optional ADR 一句；**Constraints**、**Revision log**、**Current Context** 已在模板/skills 中。
- **L2 未实现**：grill 写 CONTEXT/ADR、多 skill Prerequisites 读 CONTEXT/ADR（见下文 north star）。
- 决策过程：多轮 **sdd-grill**；上游对照见 [upstream-engineering-rationale.md §6](./upstream-engineering-rationale.md#6-mattpocockskills)。

---

## 决策过程摘要

### A. ADR（Architecture Decision Records）

| # | 问题 | 结论 |
|---|------|------|
| A1 | ADR 指哪一层 | **B** — 使用 SDD 的项目工作流产物，非本仓 maintainer 文档 |
| A2 | 补什么洞 | **A+B** — 跨 feature 架构决策 + 单次重大 trade-off |
| A3 | 如何交付 | 曾议 **扩 sdd-spec**；后并入统一方案（见下文） |
| A4 | 何时写 ADR vs spec Constraints | **A** — 跨后续 feature 仍有效，或 reversal 成本高 → ADR；仅本变更 → Constraints / Decisions |
| A5 | 路径命名 | **A** — `docs/adr/0001-short-title.md` |
| A6 | 是否默认第三产物 | **A** — **可选**；默认仍 spec + plan |
| A7 | 如何 supersede | 先 **Status 机** → 后改为 **1** — 新 ADR 写 `Supersedes: ADR-0003`；**旧 ADR 正文不改**；不要 Proposed/Accepted 状态机 |
| A8 | 是否必要 | **否（0.1.0 前）** — 合理但需第二次闭环证据；L1 模板/README 即可 |

**ADR 分层（最终）：**

| 内容 | 位置 |
|------|------|
| 本变更 trade-off | spec **Constraints** / 可选 **Decisions** |
| 跨 feature、难 reversal | **`docs/adr/NNNN-....md`**，spec **Related ADRs** 只链不贴正文 |

---

### B. CONTEXT.md

| # | 问题 | 结论 |
|---|------|------|
| B1 | 指哪一层 | **B** — 使用 SDD 的项目根目录（及多域子路径） |
| B2 | 补什么洞 | **A** — 稳定域语言、模块边界、命名（**非**单次变更事实） |
| B3 | 如何落地 | **A** — 可选 artifact；spec **Current Context 只写增量** |
| B4 | 何时才建 | **A** — 多篇 spec 重复术语，或多人/agent 协作易漂移 |
| B5 | 谁维护 | 先 **仅 sdd-spec** → 后统一方案改为 **grill 写 Language，spec 兜底** |
| B6 | 与 ADR 划界 | **A** — CONTEXT = **是什么**；ADR = **为什么**；spec Decisions = **本变更** |
| B7 | 多域 | 对齐 matt — **`CONTEXT-MAP.md` + 每域 `CONTEXT.md`**；单域则根目录一份即可 |
| B8 | 0.1.0 落地程度 | **A** — 最小：README + `spec-template` 注释（L1） |

---

### C. 仅更新 ADR、不要 spec

| 问题 | 结论 |
|------|------|
| 纯架构决策、无 feature 边界 | **合理**；不应逼空 spec |
| 写入方 | **`sdd-grill`** 直接写/ supersede ADR 后 **stop**（不强制 `sdd-spec`） |
| 决策绑 AC | 仍走 **`sdd-spec`** + 链 ADR |

---

### D. grill 是否可改 CONTEXT

| 方案 | 结论 |
|------|------|
| 仅 spec 写 | 术语定稿晚，易丢 |
| grill 写所有 design docs | 边界糊 |
| **折中（采纳）** | grill 可改 **`CONTEXT.md` 的 Language 段**；纯架构时 grill 可写 ADR（见 north star §2） |

---

## 统一方案（north star）

### 1. 三类产物

| 产物 | 回答 | 默认 |
|------|------|------|
| spec / plan | 这次 **做什么、怎么验** | ✅ 必填 |
| CONTEXT | 项目 **怎么说** | 可选 |
| ADR | **为什么** 这样选架构 | 可选 |

### 2. 谁写

| 技能 | CONTEXT | ADR | spec / plan |
|------|---------|-----|-------------|
| **sdd-grill** | ✅ 仅 **Language** | ✅ **纯架构、无 feature** 时 | ❌ |
| **sdd-spec** | ✅ grill 未覆盖时 **兜底** | ✅ **绑 AC** 或链已有 ADR | ✅ |
| 其它 | ❌ → escalation | ❌ → grill / spec | 各守本业 |

**grill Stop：**

- 纯架构已落 ADR → **stop**（不 invoke spec）
- 还要行为契约 → **`sdd-spec`**
- plan 需压测 → **`sdd-plan`**

### 3. 谁读（存在才读，缺失则静默继续）

| 技能 | 读 CONTEXT | 读 ADR |
|------|------------|--------|
| sdd-grill | ✅ 相关域 | ✅ 触达区域 |
| sdd-spec | ✅ | ✅ |
| sdd-plan | ✅ | ⚠️ 相关则读 |
| sdd-build | ✅ | ⚠️ 相关则读 |
| sdd-review | ⚠️ 可选 | ⚠️ 可选 |
| using-sdd / sdd-ship | ❌ 一般不读 | ❌ |

Prerequisites 建议统一句式：

> 若存在 `CONTEXT.md` / `CONTEXT-MAP.md` 及相关的 `docs/adr/`，先读与本次 increment 相关的部分；缺失则继续。

### 4. spec 内结构（不重复持久文档全文）

```text
Current Context   ← 本变更事实（增量；可链 CONTEXT）
Constraints       ← 本变更 trade-off
Decisions         ← 本变更 rejected（可选）
Related ADRs      ← 只链 ADR-NNNN
Revision log      ← spec 原地修订（已实现）
```

### 5. 多域布局（对齐 matt）

**单域（大多数项目）：**

```text
/
├── CONTEXT.md
└── docs/adr/
```

**多域：**

```text
/
├── CONTEXT-MAP.md
├── docs/adr/                    ← 系统级决策
└── src/<domain>/
    ├── CONTEXT.md
    └── docs/adr/                ← 域内决策（可选）
```

（`docs/context/<domain>.md` 亦可，但须有根索引；优先与 matt 的 `CONTEXT-MAP.md` 对齐。）

### 6. ADR 格式要点

- 段落：**Context · Decision · Consequences · Rejected alternatives**
- 可选顶栏：**`Supersedes: ADR-0003`**
- **无** Status 状态机；旧 ADR 正文不因 supersede 而改

### 7. CONTEXT 格式要点（参考 matt `CONTEXT-FORMAT.md`）

- **Language** 段：术语定义 + **`_Avoid_`** 禁用同义词
- 只收 **项目特有概念**，不收通用编程词
- 多域时由 **CONTEXT-MAP** 指向各域文件

---

## 被拒方案

| 方案 | 原因 |
|------|------|
| 新 skill `sdd-adr` / `sdd-context` | 7 技能 sprawl |
| ADR / CONTEXT 与 spec 并列必填 | 违背轻量 SDD |
| 全部 ADR 或决策塞进 spec 正文 | 跨 feature 引用与 supersede 混乱 |
| 「比过方案就写 ADR」 | 几乎每 spec 一篇 ADR |
| Proposed/Accepted ADR 状态机 | 过重；watchlist 已选 Supersedes-only |
| 仅 README 提及、不改 skill | agent 难稳定触发（仅作 L1 补充，非终态） |
| 本仓 dogfood 根目录 CONTEXT | `SOURCES.md` 已承担 maintainer 决策记录 |

---

## 合理性与必要性

| 维度 | 结论 |
|------|------|
| **是否合理** | ✅ 作为 optional 外挂与 north star 合理 |
| **是否必要（默认）** | ❌ 小项目 / 单 spec：**不必** |
| **何时有必要** | 多篇 spec 术语重复；多 agent 漂移；纯架构 ADR-only；第二次闭环证明 Constraints 不够 |

---

## 实现分层

| 层级 | 内容 | 状态 |
|------|------|------|
| **L0** | spec + plan；Current Context / Constraints / Revision | ✅ 已在 skill 中 |
| **L1** | `spec-template`：Decisions、Related ADRs；README optional ADR | ✅ `397aa90` |
| **L1+** | CONTEXT / CONTEXT-MAP 注释；Current Context 增量说明 | ⏳ 待做 |
| **L2** | `sdd-grill` 窄写 CONTEXT Language + 纯 ADR；`sdd-spec/plan/build` Prerequisites 读 CONTEXT/ADR | ❌ 未实现 |
| **L3** | `context-template`、`adr-template`；`sdd-review` 可选术语维度 | ❌ 等有证据再做 |

**触发 L2 的信号（需满足多条）：**

1. 多篇 spec 重复同一术语/边界  
2. agent 或多人协作命名反复漂移  
3. 纯架构变更频繁逼出「空 spec」  
4. 第二次 SDD 闭环明确 spec Constraints 不足以承载跨 feature 决策  

---

## 与本仓库的关系

- **仍 7 技能**；不增状态机；不 auto-invoke。
- 改 skill 后须 `python3 tests/check.py`；若吸收上游 matt 行为变化，同步 [SOURCES.md](../../SOURCES.md)。
- 本文件为 **设计决策记录**，非 SDD 默认必填产物；实现前可再开 grill 或 `sdd-spec` 写 AC。

---

## 参考

- [README.md — Minimal Artifacts](../../README.md#minimal-artifacts)
- [spec-template.md](../../skills/sdd-spec/spec-template.md)
- [upstream-engineering-rationale.md §6](./upstream-engineering-rationale.md#6-mattpocockskills)
- [docs/design/README.md](./README.md)
