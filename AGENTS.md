# AGENTS.md

本仓是 **zhijunio/sdd-skills**：给 AI Agent 用的 Markdown skill 包，不是可运行应用。人类说明见 [README.md](README.md)。每个 skill 的契约是 `skills/<name>/SKILL.md`。相关时再读：[CONTEXT.md](CONTEXT.md)、[docs/adr/0001-sdd-skill-pack-shape.md](docs/adr/0001-sdd-skill-pack-shape.md)、[CHANGELOG.md](CHANGELOG.md)。

## Context

- 包形态（ADR）：交付环 `sdd-spec` → `sdd-plan` → `sdd-build` → **Stop**；`sdd-review` 与 `sdd-improve` **独立**，不要求先走 Spec/Plan/Build。
- Skill 总数与 id 以 [`skills/`](skills/) 目录为唯一来源（当前 9 个）。不要在本文件维护会腐烂的全表。
- Skill 指令正文用 **English**。对用户的 Present 用对话语言（见各 skill Present）。
- 一阶段结束必须 **Stop**，等用户再 `@`。禁止自动串环，也禁止把 Stop 自动路由到 `sdd-review` / `sdd-improve` / 非 SDD 工具。
- 除非用户要求：不要新增 hooks、slash commands、中央路由文档、运行时状态文件。
- 不需要嵌套 `AGENTS.md`。

## Structure

| 路径 | 用途 |
| --- | --- |
| `skills/<name>/SKILL.md` | 运行时契约 |
| `skills/<name>/references/` | 该 skill 模板/基线（如有）；Standards 共享基线在 `skills/sdd-review/references/` |
| `docs/prompts/` | Cursor prompt；与 skill 内容对齐时 **互不交叉链接**；配对关系由维护校验脚本维护 |
| `docs/adr/` | ADR |
| `docs/design/` | 维护者设计笔记 |
| `scripts/check-skills.sh` | 统一检查技能清单、frontmatter 结构、README 清单、路由、配对 prompt 和 Markdown 文件/锚点 |
| `.github/workflows/check.yml` | 对 skills/scripts 及全部 Markdown 变更跑统一校验 |

消费方可用 `docs/sdd/00N-<topic>-spec.md` / `00N-<topic>-plan.md`，其中 `00N` 为项目内递增的三位编号。本维护仓 **不强制** 每次改动都走 SDD；有对应契约时再读。

## Commands

无应用 build / lint / format / 测试框架。

**primary（开 PR 前）：**

依赖 Bash 3.2+ 与 Python 3（仅标准库）。

```bash
./scripts/check-skills.sh
```

可选试装：`npx skills@latest add zhijunio/sdd-skills --list` 或 `-a cursor -y`。

不要发明 `npm test` / `pytest` / `mvn verify`。改过的 Markdown 抽查相对链接。

## Commit & PR

- 默认分支 `main`；经 PR 合入；不要直接推新工作到 `main`。
- **新提交** 用 `feat:` / `fix:` / `docs:` / `chore:` / `refactor:`（可带 scope）；一逻辑一提交。历史可见 `ci:`、`feature:` — 不要求改写历史。
- **新分支** 优先 `feature/`、`fix/`、`docs/` + 主题（历史亦有 `feat/`）。
- 用户可见变更写入 [CHANGELOG.md](CHANGELOG.md) `[Unreleased]`。
- 未经明确要求：不要 force-push `main`、改 git config、跳过 hooks。

改 `SKILL.md`：`description` 只写触发条件；正文短，大段进 `references/`；保留 `AC-n`、skill id、`file:line`、🔴/🟡/🟢；`sdd-review` 与 `sdd-improve` 用 When/Skip 互链且 Standards 维度同步；增删 skill 时同步校验命令与 README；配对 prompt 同改、无交叉链接。

## Agent notes

**做：** 先读目标 `SKILL.md`（及 `references/`）；实质行为变更自试；人类上手链 README，勿在此写营销文。

**不做：**

- 用 `sdd-improve` 当交付门禁，或用 `sdd-review` 做整仓扫描（角色相反）。
- 无用户 `@` 串阶段，或把交付环 Stop 自动路由到独立 skill。
- 把 git push/PR/merge 当成包内 SDD 阶段（ADR：不接管 Git）。
- 恢复已退役 skill id（见 CHANGELOG Removed）；替代：`sdd-improve`、`sdd-review`、上游 design-interview、环止于 `sdd-build`。
