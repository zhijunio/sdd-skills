# SDD Skills

[![License](https://img.shields.io/github/license/zhijunio/sdd-skills)](LICENSE)
[![check](https://github.com/zhijunio/sdd-skills/actions/workflows/check.yml/badge.svg)](https://github.com/zhijunio/sdd-skills/actions/workflows/check.yml)

面向 Agent 的 **Spec-Driven Development（SDD）** 技能包：纯 Markdown，无状态机、无内置项目管理、不接管 Git 工作流。你在对话里 **`@`** 某一个 skill，跑完该阶段后 **Stop**，再决定是否 `@` 下一个。

人类上手读本文；Agent 操作契约见 [AGENTS.md](AGENTS.md)。术语见 [CONTEXT.md](CONTEXT.md)。包形态决策见 [docs/adr/0001-sdd-skill-pack-shape.md](docs/adr/0001-sdd-skill-pack-shape.md)。

## 它解决什么问题

一次改动先写成可验收契约，再拆成可测垂直切片，再测试优先落地；质量报告与仓库改进扫描可单独使用，不必绑在交付环上。

- **交付环**：`sdd-spec` → `sdd-plan` → `sdd-build` → Stop（用户显式审批；不自动串阶段）
- **独立质量**：`sdd-review`（增量双轴报告）、`sdd-improve`（广范围 Standards 候选）
- **独立工具**：README / AGENTS / 解释代码 / 入职计划 / 过度工程审计 — 与 SDD 环无耦合

完整 skill 目录以 [`skills/`](skills/) 为准（当前 **10** 个）。

## 安装

**primary**（试装 / 列清单，见 [AGENTS.md](AGENTS.md)）：

```bash
npx skills@latest add zhijunio/sdd-skills --list
npx skills@latest add zhijunio/sdd-skills -a cursor -y
```

`npx skills@latest` 来自 [skills CLI](https://github.com/vercel-labs/skills)（仓库 [CHANGELOG](CHANGELOG.md) 有记载）。按需加 `-s <skill-id>` 只装子集；钉版本可用已发布 tag，例如 `zhijunio/sdd-skills@v0.3.1`（tag 存在于本仓；该版本 skill 集合与当前 `main` 不同）。

**also OK：** 把 `skills/<name>/`（含 `references/`）拷进你所用 Agent 的 skills 目录。

## 怎么用（交付环）

示意（**illustrative**）：

```mermaid
flowchart LR
  spec[sdd-spec] --> plan[sdd-plan]
  plan --> build[sdd-build]
  build --> stop[Stop]
```

1. `@sdd-spec` — 行为契约与 `AC-n`
2. 对话里 **Approval** 后 `@sdd-plan` — 覆盖全部 AC 的垂直切片
3. Approval 后 `@sdd-build` — 测试优先实现 + 收尾验证
4. **Stop** — 需要质量报告再 `@sdd-review`；需要广范围改进候选再 `@sdd-improve`（二者均非环内强制阶段）

消费方项目里常用约定（本维护仓不强制）：

```text
docs/sdd/YYYY-MM-DD-<topic>-spec.md
docs/sdd/YYYY-MM-DD-<topic>-plan.md
```

## Skills 一览

正文为英文；下表「何时用」取自各 `SKILL.md` 的 `description`。

### 交付环

| Skill | 何时用 |
| --- | --- |
| [`sdd-spec`](skills/sdd-spec/SKILL.md) | 需要持久行为契约、范围、验收标准与技术约束，再进入实现规划 |
| [`sdd-plan`](skills/sdd-plan/SKILL.md) | 已批准 Spec 要拆成可测垂直切片 |
| [`sdd-build`](skills/sdd-build/SKILL.md) | 已批准 Plan 可测试优先实现，或按 review 发现修复且不改已接受行为 |

### SDD 独立

| Skill | 何时用 |
| --- | --- |
| [`sdd-review`](skills/sdd-review/SKILL.md) | 自固定点起的分支/PR/「review since X」双轴 Standards/Spec 质量报告（非整仓 improve） |
| [`sdd-improve`](skills/sdd-improve/SKILL.md) | 仓库/模块/区域/分支的广范围 Standards 扫描，热点优先候选（非增量交付评审） |

### 非 SDD

| Skill | 何时用 |
| --- | --- |
| [`create-readme`](skills/create-readme/SKILL.md) | 编写或修订给人看的 README.md |
| [`create-agentsmd`](skills/create-agentsmd/SKILL.md) | 编写或修订 AGENTS.md |
| [`explain-code`](skills/explain-code/SKILL.md) | 解释选中代码或片段 |
| [`onboarding-plan`](skills/onboarding-plan/SKILL.md) | 新贡献者分阶段入职计划 |
| [`ponytail-audit`](skills/ponytail-audit/SKILL.md) | 仅过度工程：排序删除/简化/换 stdlib·native；一次性报告，不自动改代码 |

部分 skill 在 [`docs/prompts/`](docs/prompts/) 有内容对齐的 Cursor prompt（文件独立、与 skill **无交叉链接**）。另有仅 prompt、无 skill 的文件（如 `review-code.prompt.md`）— 有对应 skill 时优先用 skill。

## 仓库里有什么

| 路径 | 用途 |
| --- | --- |
| `skills/<name>/SKILL.md` | 运行时契约 |
| `skills/<name>/references/` | 该 skill 模板/基线（如有） |
| `docs/prompts/` | Cursor prompts |
| `docs/adr/` | ADR |
| `docs/design/` | 维护者设计笔记 |
| `docs/references.md` | 上游灵感链接 |
| `scripts/check-skills.sh` | 交叉 skill 链接检查 |
| `.github/workflows/check.yml` | CI：对 `skills/**` / `scripts/**` 跑上述脚本 |

无应用运行时、无 `package.json` 测试脚本。

## 维护者校验

**primary**（[AGENTS.md](AGENTS.md)）：

```bash
test "$(find skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l)" -eq 10
test ! -e skills/repo-audit
test ! -e skills/repo-audit-full
test ! -e skills/sdd-grill
test ! -e skills/git-release
test ! -e skills/sdd-ship
test ! -e skills/sdd-verify
test ! -e skills/sdd-audit
test -f skills/sdd-improve/SKILL.md
test -f skills/sdd-review/SKILL.md
```

**also OK：**

```bash
./scripts/check-skills.sh
```

向 `main` 开 PR；用户可见变更记入 [CHANGELOG.md](CHANGELOG.md) `[Unreleased]`。

## 当前 main 相对已发布 tag

相对 `v0.3.1`，`[Unreleased]` 中已移除/改名的 id 包括：`sdd-ship` / `sdd-verify` / `git-release`、`sdd-audit` / `repo-audit-full`、`repo-audit`（并入 `sdd-review`）、`sdd-grill` / `sdd-zoom` 等 — 细节以 [CHANGELOG.md](CHANGELOG.md) 为准。

## 文档

| 文档 | 用途 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Agent / 维护者操作指南 |
| [CONTEXT.md](CONTEXT.md) | 领域用语 |
| [docs/adr/0001-sdd-skill-pack-shape.md](docs/adr/0001-sdd-skill-pack-shape.md) | 包形态 |
| [CHANGELOG.md](CHANGELOG.md) | 变更历史 |
| [docs/references.md](docs/references.md) | 上游来源 |

上游灵感（见 `docs/references.md`）：[mattpocock/skills](https://github.com/mattpocock/skills)、[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)、[shadcn/improve](https://github.com/shadcn/improve)、[obra/superpowers](https://github.com/obra/superpowers/)、[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)。

## License

MIT — [LICENSE](LICENSE)（Copyright 2026 zhijunio）。
