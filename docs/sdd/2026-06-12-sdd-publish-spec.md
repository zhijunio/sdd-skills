# sdd-publish

## Goal

在**任意 git 仓库**中，当用户明确要求远程集成时，以**分步 Present → 确认 → 执行**将变更推送到远程（push / PR / merge / tag / GitHub Release）。可选 post-loop 卫星，**可单独 `@`**，**不依赖** `@sdd-verify`；与 verify 分工，不破坏「验收与发布分离」纪律。

## Scope

- 在 `skills/sdd-publish/` 新增 **post-loop 可选卫星**（与 `sdd-worktree` pre-loop 对称）；**不**并入六段核心环，**不**自动链下一 skill。
- 技能仅在用户 **`@` 触发**且声明集成意图（push、PR、merge、发版等）后运行。
- **流水线步骤**（用户可点名子集；默认不连做 merge/tag/release）：
  1. **门禁** — 只读探测前置条件（Req §2）；
  2. **Push** — `git push`（含 `-u` 首次上游）；
  3. **Open PR** — `gh pr create`（`gh` 可用时执行；否则 Present 可复制命令）；
  4. **CI 展示** — `gh pr checks` / `gh pr view`（仅展示，不 babysit 修 CI）；
  5. **Merge PR** — `gh pr merge`（须单独确认；CI failed/pending 默认 stop）；
  6. **同步默认分支** — merge 后 `checkout` + `pull` 默认分支（通常 `main`），再 tag（Req §7）；
  7. **Tag** — 本地 `git tag` + `git push origin <tag>`（版本取自 CHANGELOG，打在默认分支当前 HEAD）；
  8. **GitHub Release** — `gh release create`（`gh` 可用时）；
  9. **可选 README pin** — 仅当仓库存在「Recommended pin」类段落且用户确认时更新。
- **执行模式：** 每步 **Present** 命令、目标与风险 → **单步确认** → 再执行该步 mutating 命令；未确认前仅只读探测。
- 成功后 **Stop**；无默认下一 skill（集成完成）。
- 合并本技能后同步 `sdd-verify` **Stop** hand off、README（含 Mermaid post-loop 节点）、AGENTS、SOURCES、engineering-rationale（见 AC-13）。

## Non-goals

- 不替代 `sdd-verify` 验收；不撰写 verify 级验收摘要。发版相关 **CHANGELOG 升格**（`[Unreleased]` → 版本段）须在 Present 确认后由本技能执行（Req §11）。
- 不修 CI、不 triage PR 评论、不 force push、不 `main`/`master` 直推、不改 git config、未授权 amend/rebase。
- 不自动链式执行 merge → tag → release；不 babysit CI 循环（归 Cursor 其他能力）。
- 不做 npm/docker/云平台 deploy；不替代 Cursor 用户规则里的 `creating-pull-requests`（二者可共存：规则管格式，本技能管 SDD 门禁与 Present/Stop）。
- 不做 superpowers 式自动发版编排或 session hook。

## Current Context

**技能载体（本仓库 sdd-skills）**

- 现有 **九 skill**（含 `sdd-worktree`）：六段核心环 + **四颗**可选卫星（`sdd-worktree` pre-loop、`sdd-publish` 待增 post-loop、`sdd-zoom`、`sdd-audit`）；`sdd-verify` 明确 **No push, PR, publish, or deploy unless separately requested**。
- Grill 共识（2026-06-12）：集成阶段独立 `sdd-publish`，非扩写 `sdd-verify`；常见在 verify 之后，但**非硬前置**。
- 新增第 10 个目录须同步治理文档——列入本 spec 交付（AC-13）。

**技能运行时（目标 git 仓库）**

- 假设已配置 `origin` 远程；GitHub 场景下可选 `gh` CLI 已认证。
- 常见保护：`main` 仅 PR 合并；topic 分支开发（可与 `sdd-worktree` 衔接，非硬依赖）。
- Agent 通过 shell 执行 git；`gh` 不可用时 PR/merge/release 步骤降级为 **Present 命令清单**（Req §10）。

## Requirements

1. 技能必须先只读探测：`git rev-parse --is-inside-work-tree`、`git status`、`git branch -vv`、`git remote -v`、`git log -1 --oneline`；有 PR 上下文时再读 `gh pr view`（若 `gh` 可用）。
2. **门禁 hard stop**（不满足则不得执行任何 mutating git/gh 命令）：
   - 非 git 仓库；
   - **当前工作区存在未提交改动**（含未跟踪文件计入脏树时按 `git status` 判定）→ 提示 commit 或 stash；stash 后须**重新 `@sdd-publish`**（同 `sdd-worktree` 纪律）；
   - 当前分支为 `main` 或 `master` 且意图为 push 新 work — 必须 stop，提示用 topic 分支 + PR（生产默认分支识别：存在 `main` 用 `main`，否则 `master`）；
   - 用户未声明集成意图（仅问「能发吗」而未选步骤）→ Present 步骤菜单后等待点名；
   - 用户请求 force push、直接推 `main`、改 git config — stop 并拒绝。
3. **集成就绪探针**（非 verify/review 门禁；open PR / tag / release 需要 CHANGELOG 上下文时 **Present**）：
   - 只读探测 `CHANGELOG.md` 的 `[Unreleased]` 与 increment 范围；
   - **Present** 表格式探针：CHANGELOG 存在性、`[Unreleased]` 是否覆盖本 increment、用户点名步骤；会话有 verify 摘要时可引用，**无摘要不得挡** push/PR，仅可 **note** `@sdd-verify`；
   - **`[Unreleased]` 缺口**（可能有用户可见影响且为空）— 开 PR / tag 前 **Present** 四路径：① 继续（接受 commit 正文或推迟 tag/release）；② **Present** `[Unreleased]` 草案 → 用户确认后仅本地改文件；③ 可选建议 `@sdd-verify`（非默认 stop）；④ 仅挡 tag/release 步，push/PR 若已确认可继续；
   - release 步不得静默仅用 commit 当 notes。
4. **Push 步：** Present 远程名、分支名、`git push -u origin <branch>`（或等价）；用户确认后执行。
5. **Open PR 步：** Present PR 标题/正文要点（可摘自 CHANGELOG `[Unreleased]` 或最近 commit）；`gh` 可用时 `gh pr create`；否则 Present 完整 `gh pr create` 命令供用户自行执行，并标注「本步未执行」。
6. **CI 展示步：** `gh` 可用且存在 PR 时，Present `gh pr checks` 摘要；failed 或 pending → 默认 **不进入 merge**，提示修 CI 或用户**显式承担风险**后下一回合再 `@` merge。
7. **Merge 步：** 须**单独确认**；Present merge 方式（merge/squash/rebase）与目标分支；`gh pr merge` 或等价；CI 未通过且用户未显式承担风险 → stop。
8. **Tag 步：**
   - **版本解析**（按优先级，仍含糊则 stop）：① 用户 Present 指定 `vX.Y.Z`；② `CHANGELOG.md` 中 `[Unreleased]` 下已有 `## [X.Y.Z]` 草稿标题；③ `git describe --tags --abbrev=0` 的 semver patch 递增建议（Present 供确认，不静默采用）；④ 以上皆无 → stop，提示补 CHANGELOG。
   - **打 tag 基线：** 若本流程已执行 merge，须先 **Present** `git checkout <default>` + `git pull origin <default>`（`<default>` 为 `main` 或 `master`），确认 HEAD 为合并后顶端，再 `git tag -a vX.Y.Z`；未 merge 仅在 topic 分支发 tag 时须 Present 明示「tag 打在分支 `<branch>` 当前 HEAD」并经用户确认。
   - Present `git tag -a vX.Y.Z -m "..."` 与 `git push origin vX.Y.Z`；用户确认后执行。
8. **GitHub Release 步：** `gh` 可用时，Present `gh release create vX.Y.Z --notes "..."`（notes 可摘自 CHANGELOG 该版本条目；默认针对刚推送的 tag）；确认后执行；无 `gh` → Present 命令不执行。
9. **流水线子集：** 用户可说「只 push」「只开 PR」等 — 仅执行点名步骤，不偷偷后续步骤；未点名的后续步骤（含 tag/release）不得执行。
10. **无 `gh` 降级：** PR/merge/release 步骤不得假装已执行；须 Present 可复制命令 + 说明需本机 `gh` 或网页操作。
11. **CHANGELOG 升格（发版步可选子步）：** 在 tag 前，若存在 `[Unreleased]` 条目，Present 将其改为 `[vX.Y.Z] - YYYY-MM-DD`（日期由用户确认或当日）；**须用户确认**后才改文件；可与 tag 步同轮确认。
12. **README pin（可选）：** 若 `README.md`（或项目约定文件）含 recommended pin / install 示例中的 `@vX.Y.Z`，Present 是否替换为新 tag；用户确认后才编辑。
13. `SKILL.md` 为 **English**；**Present** 跟用户语言；含 **When/Skip** 与 **`sdd-verify`** 互链（可选 handoff，非硬前置）；**Red flags** 对齐 Non-goals。
14. 每步确认：明确肯定（确认、好的、yes、go 或等价）后，方可执行该步 mutating 命令。

## Acceptance Criteria

- AC-1: 当门禁（Req §2）不满足时，技能 hard stop，不 push、不调用 `gh`；脏树/`main` 上新 work 等场景 hand off `sdd-worktree` 等（**不因**无 verify 摘要而 stop）。
- AC-2: 当用户点名仅 push 并确认时，技能 Present push 命令后执行 `git push`，且不自动开 PR/merge/tag/release。
- AC-3: 当 `gh` 可用且用户确认开 PR 时，技能 Present 并执行 `gh pr create`（或等价参数），且 PR 描述与 CHANGELOG/commit 可追溯。
- AC-4: 当 `gh` 不可用且用户要求开 PR 时，技能 Present 完整 `gh pr create` 命令且不声称 PR 已创建。
- AC-5: 当用户请求 CI 展示且 `gh` 可用时，技能 Present `gh pr checks` 摘要；failed/pending 时默认不进入 merge，除非用户显式承担风险并再次确认 merge。
- AC-6: 当用户确认 merge 时，技能单独 Present merge 选项后执行 `gh pr merge`（或说明网页合并路径）。
- AC-7: 当 CHANGELOG 版本按 Req §7 可解析且用户确认 tag 步时，技能在 Present 声明的基线 HEAD 上创建并推送 `vX.Y.Z` tag。
- AC-8: 当 CHANGELOG 版本按 Req §7 仍无法解析时，技能不创建 tag/release，并提示补全 CHANGELOG。
- AC-9: 当 `gh` 可用且用户确认 release 步时，技能 Present 并执行 `gh release create`，notes 与 CHANGELOG 条目一致。
- AC-10: 当用户未对某步逐步确认时，技能不执行该步 mutating git/gh 命令。
- AC-11: 当用户确认 CHANGELOG 升格时，技能将 `[Unreleased]` 改为 `[vX.Y.Z] - <date>` 且仅在该步确认后写入文件。
- AC-12: 当仓库含 recommended pin 段落且用户确认时，技能更新 pin 为新版 `vX.Y.Z`；未确认或不存在该段落则 skip。
- AC-13: 当本变更合并入 `sdd-skills` 时，`sdd-verify` **Stop** 已 hand off `sdd-publish`；README（十 skill + Mermaid post-loop）、AGENTS、SOURCES、engineering-rationale §3.3、CHANGELOG `[Unreleased]` 已更新。
- AC-14: `skills/sdd-publish/SKILL.md` 为 English，含 **Present**、**When/Skip** 与 `sdd-verify` 互链，且含分步流水线、无 `gh` 降级与 merge 后同步默认分支说明。
- AC-15: 技能行为遵循 Constraints「评估顺序」；门禁未过不得执行后续步骤；多步时顺序不颠倒（push 在 PR 前，merge 在 tag 前，同步默认分支在 tag 前）。
- AC-16: 当无 verify 摘要时，技能**不得**因缺少 verify 而挡 push/PR；open PR / tag / release 前按 Req §3 **Present** 集成就绪探针与 CHANGELOG 缺口四路径；有用户可见影响且 `[Unreleased]` 空时 tag/release 不得静默继续。

## Constraints

- 轻量、可中断；一步一确认；**不**自动链下一 skill 或下一步。
- **评估顺序（固定）：**
  1. Req §2 门禁 → hard stop；
  2. 用户点名步骤子集（Req §9）；
  3. 多步时保持流水线序：push → open PR → CI 展示 → merge → **同步默认分支**（merge 后、tag 前）→ tag → release → README pin（跳过未点名步）；
  4. 对每步：Present → 确认（§14）→ 执行 → 可选 **Stop**（用户可下一会话继续）；
  5. 全部完成 → **Stop**（集成结束）。
- 禁止：force push、`git push --force`、推 `main` 上新 work、未确认 mutating、`git config` 修改。
- 与 `sdd-verify` 分工：verify 产出验收摘要与 `[Unreleased]` 草案（可选）；publish 可消费后者用于 PR notes / tag / release，**不依赖** verify 会话。

## Decisions

- **独立 `sdd-publish`，非扩写 `sdd-verify`：** 验收与远程集成分离；grill 2026-06-12 全票 A。
- **Post-loop 卫星：** 与 `sdd-worktree`（pre-loop）对称；均不进入六段环。
- **Git 通用 + `gh` 增强：** 无 `gh` 时 push/tag 可执行，PR/merge/release Present 命令（解决 grill OQ-2）。
- **分步确认：** merge/tag/release 不默认连做；CI 展示不触发自动 merge。
- **版本以 CHANGELOG 为准：** tag/release 与可选升格绑定 `[Unreleased]`（解决 grill OQ-3）；merge 后 tag 打在默认分支同步后的 HEAD。
- **拒绝：** 扩进 ship、一次确认跑全流程、CI babysit、force push、平台 DevOps 全家桶。

## Open Questions

- ~~**OQ-1（consumer evidence）：**~~ **Closed (2026-06-25):** 不要求独立消费者仓库 spot-check；maintainer self-trial + CHANGELOG 记录即可。

## Revision log

- 2026-06-12 | 初稿：grill 共识落 spec | plan 待启动
- 2026-06-12 | 评审 should-fix：§10 引用、四卫星叙事、脏树/worktree 对齐、版本解析、merge 后 tag 基线、AC 增至 15 | plan 可启动
- 2026-06-12 | 二轮评审 + 用户批准；补 experimental Scope、AC-13 交叉引用 | plan 已起草
- 2026-06-25 | Verify readiness checklist：review/verify 门禁拆分、无 verify 摘要时 Present CHANGELOG 探针与四路径 | AC-16
- 2026-06-25 | **Breaking rename:** `sdd-ship` → `sdd-verify`；`sdd-publish` 不变 | AC-13 交叉引用已更新
- 2026-06-25 | 卫星独立：移除 verify/review 硬门禁；**Integration readiness** 仅 CHANGELOG 探针；无 verify 摘要不挡 push/PR | AC-16 修订
- 2026-06-25 | OQ-1 闭合：不要求独立消费者仓库 spot-check | experimental 门禁移除
