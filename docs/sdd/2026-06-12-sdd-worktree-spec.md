# sdd-worktree

## Goal

在**消费者项目的任意 git 仓库**中，用户开启新需求前，先获得一个与主分支隔离的开发上下文（独立 worktree 或 topic 分支），避免直接在主分支上继续开发。

## Scope

- 在 `skills/sdd-worktree/` 新增**第 3 颗可选卫星**技能（与 `sdd-zoom`、`sdd-improve` 并列）；**不**并入六段核心环，**不**自动链下一 skill。
- 技能在**用户 `@` 触发**后探测目标 git 仓库状态，选择 `git worktree` 或 `git branch` 路径。
- 默认优先 `git worktree`；非 git 仓库 hard stop；在 git 仓库内仅在 Requirements §3 列明的条件下回退 `git branch`。
- 分支命名：`feature/<topic>`、`fix/<topic>`、`docs/<topic>`；前缀规则见 Requirements。
- `topic` 从用户描述提取；提取不到时用仓库根 basename 的 **slug** 兜底（不用 cwd 叶子名）。
- 默认 worktree 路径：`../<repo-basename>-<topic>`（`<repo-basename>` 为仓库根**原始** basename，`<topic>` 为 slug 值；路径与仓库根目录同属父目录）；用户可在确认前指定相对 toplevel 或绝对路径覆盖。
- **执行模式：** 先 **Present** 拟定的基线、前缀、`topic`、完整 git 命令与落盘路径；**仅在用户明确确认后**执行会改变 git 状态的命令（`git worktree add`、`git checkout -b` 等）。未确认前只读探测。
- 成功后 **Stop**，默认 hand off **`sdd-spec`**；见 AC-10 的 grill 条件。
- 合并本技能后需同步维护者文档与 CI（见 **AC-11**）；README 工作流图标为 optional pre-loop 卫星。

## Non-goals

- 不写 spec、plan、代码实现或 review。
- 不提交、推送、开 PR、发版。
- 不清理脏工作区、不解决冲突、不重写历史、不删除已有 worktree/分支。
- 不并入 `sdd-grill`；必须可独立 `@` 触发。
- 不做 superpowers 式自动 worktree 编排、session hook、子 agent 或跨会话状态机（见 Decisions）。

## Current Context

**技能载体（本仓库 sdd-skills）**

- 现有 **八 skill** 叙事：六段核心环 + `sdd-zoom` + `sdd-improve`；Markdown skills，无 Git hook / 运行时状态文件。
- [engineering-rationale §3.2](../../docs/design/engineering-rationale.md) 记录：**扔掉**的是 superpowers 的**自动** worktree 编排，而非「用户显式 `@` 的轻量开工隔离」。
- 新增第 9 个目录会触发 CI `validate` 计数、README/AGENTS/SOURCES/engineering-rationale 同步——列入本 spec 的交付范围。
- **Consumer evidence（治理）：** 发版 pin 前须在消费者仓库完成一次 spot-check（README [Maintainer verification](../../README.md#maintainer-verification)）；当前为**待验证假设**，见 Open Questions。

**技能运行时（用户的目标 git 仓库）**

- 用户约束：新需求不应直接在 `main`/`master`（或等价主分支）上提交。
- 分支前缀习惯：`feature/`、`fix/`、`docs/`。
- Agent 通过 shell 读 git 状态；平台中立，不依赖 Cursor 专有 worktree API。

## Requirements

1. 技能必须先只读探测目标仓库（`git rev-parse --is-inside-work-tree`、`git status`、`git branch`、`git worktree list` 等），再选择路径。
2. 若当前目录**不是** git 仓库（含 `rev-parse` 失败），技能必须 **hard stop**，提示用户在目标仓库根目录重试；**不得**回退 `git branch`。
3. 在 git 仓库内，技能必须默认优先 `git worktree`；仅在下列任一条件成立时回退 `git branch`（输出须标明触发的条件，并标注**弱隔离**，见 Decisions）：
   - `git worktree` 子命令不可用（Git 版本过旧等）；
   - 用户在本轮明确拒绝 worktree（要求仅开分支）；
   - 创建 worktree 的 shell 命令预检失败（权限、路径非法等；**不含**路径已占用——路径占用走 Req §10）。
4. 技能必须在**当前工作区存在未提交改动**时 **hard stop**：不创建 branch/worktree；提示用户先 **commit** 或 **stash**；若用户 stash，须**重新 `@sdd-worktree`** 后再继续（本回合不自动重试）。
5. 技能必须将 `main` 或 `master`（若两者并存，优先 `main`）识别为主分支基线。
6. 若既无 `main` 也无 `master`，必须以**当前分支**为基线；该非标准基线须在 Req §13 的 Present 中**醒目标出**，并与 §15 的执行确认**同轮一次完成**（不拆两轮问答）。
7. 技能必须按下列规则选择前缀（可在 Present 阶段请用户一次确认覆盖）：
   - 默认 `feature/`；
   - 用户描述含 bug / fix / regression / 修复 等 → `fix/`；
   - 用户描述明确仅文档/注释/README/CHANGELOG 且无行为变更 → `docs/`；
   - 歧义时默认 `feature/` 并在 Present 中标注「可改前缀」。
8. 技能生成的 `topic` 必须经过 slug 规则：小写 kebab-case；仅 `[a-z0-9-]`；连续 `-` 合并；首尾无 `-`；最长 48 字符；非法字符替换为 `-`；纯符号兜底为 `task`。
9. 无法从用户描述提取 `topic` 时，兜底取 `git rev-parse --show-toplevel` 所得路径 basename 的 **slug**（经 Req §8；与路径段 `<repo-basename>` 不同，见 Req §12）。
10. 当本地分支名 `<prefix>/<topic>` **已存在**，或拟用 worktree **路径已存在且非空 / 已被其他 worktree 占用**时，技能必须 **停止执行**（不自动回退 branch），**Present** 冲突信息，并按场景给出选项（不展示不适用的项）：
    - **始终可选：** 换 `topic`、取消；
    - **仅分支已存在时：** 复用已有分支（须用户确认且工作区干净）；
    - **仅路径占用且分支不存在时：** 换路径或换 `topic`（不提供「复用分支」）。
11. 技能必须支持独立触发，不依赖先走 `sdd-grill`。
12. 默认 worktree 路径为 `../<repo-basename>-<topic>`（路径相对于 `git rev-parse --show-toplevel` 解析）：`<repo-basename>` 为 toplevel 的**原始** basename（不做 slug）；`<topic>` 为 Req §8–§9 的 slug；用户可在确认前给出相对 toplevel 或绝对路径覆盖。
13. Present 阶段须展示可改的 `prefix`、`topic`、路径，并询问是否继续；用户可在此轮修改后再确认。
14. `SKILL.md` 指令正文为 **English**；**Present** 给用户的提示与确认语跟**用户语言**（与各 skill Present 硬约束一致）；含 **When/Skip** 与 `sdd-spec` / `sdd-grill` 互链（不重复 central routing doc）。
15. 用户确认执行：本轮出现明确肯定（如 确认、好的、yes、go，或等价短句）后，方可执行 mutating git 命令；未确认前仅允许只读 git 命令。

## Acceptance Criteria

- AC-1: 当用户在**干净**的 git 仓库中请求开启新需求并确认执行，且 Req §10 无冲突时，技能先识别基线，再执行 `git worktree add -b <prefix>/<topic> <path> <baseline>`（或回退后的 `git checkout -b <prefix>/<topic> <baseline>`），且执行前曾 **Present** 完整命令与路径。
- AC-2: 当当前目录不是 git 仓库时，技能 hard stop，不执行 `git branch` 或 `git worktree`，并提示在目标仓库内重试。
- AC-3: 当 Requirements §3 的 branch 回退条件任一成立且 Req §10 无冲突时，技能改走 `git branch` 路径，分支名为 `<prefix>/<topic>`，输出标明回退原因，并标注**弱隔离**（仅分支、同目录）。
- AC-4: 当工作区存在未提交改动时，技能不执行任何创建 branch/worktree 的命令，并提示 commit 或 stash；用户仅 stash 而未重新触发时，技能不自动继续。
- AC-5: 当存在 `main` 或 `master` 时，基线为其一（并存时 `main`）；两者皆无时，技能在 Present 中醒目标出当前分支基线，并与执行确认同轮一次完成（Req §6）后才执行变更。
- AC-6: 当用户描述含可识别主题时，`<topic>` 反映该主题且符合 slug 规则；无法提取时，使用仓库根 basename 的 slug 兜底。
- AC-7: 当用户描述含 bug/修复类关键词时，前缀为 `fix/`；明确纯文档变更时为 `docs/`；否则默认 `feature/`；Present 阶段用户显式改前缀时，以用户指定为准。
- AC-8: 当用户未先走 `sdd-grill` 时，技能仍可独立完成探测、Present、确认后执行。
- AC-9: 当 `<prefix>/<topic>` 已存在或 worktree 目标路径已占用时，技能不覆盖、不自动回退 branch，并按 Req §10 按场景 Present 选项（路径-only 冲突时不出现「复用分支」）。
- AC-10: 当隔离上下文创建成功后，技能 **Stop**；若用户**未提供**可识别需求描述（无主题句、无 fix/docs 关键词）**且** `topic` 为 slug 兜底值、Present 时用户仅回复「确认」而未改 topic，则 hand off `sdd-grill`；否则 hand off `sdd-spec`。
- AC-11: 当本变更合并入 `sdd-skills` 时，README（九 skill 叙事 + pre-loop 卫星图）、AGENTS、SOURCES、engineering-rationale（§3.3 增 `sdd-worktree` 映射）、CHANGELOG `[Unreleased]` 与 CI `validate` skill 计数均已更新。
- AC-12: `skills/sdd-worktree/SKILL.md` 指令为 English，含 **Present** 硬约束，且含 **When/Skip** 与 `sdd-spec` / `sdd-grill` 互链。
- AC-13: 当用户未明确确认时，技能不执行任何 mutating git 命令，仅完成 Req §1 的只读探测与 Req §13 的 Present（含可改 prefix/topic/路径与非标准基线说明）。
- AC-14: 技能行为遵循 Constraints「评估顺序」；任一步 hard stop 后不得跳过前置检查执行后续步骤。

## Constraints

- 与现有 SDD 风格一致：轻量、可中断、一阶段一输出；**不**自动链下一 skill。
- 不得将「创建隔离上下文」扩展为 spec/plan 流程。
- 不得在未确认时执行改变 git 状态的命令；不得默认修改主分支上的未提交内容。
- 输出须含可复制的 git 命令与下一步 hand off（skill id 字面量保留）。
- **评估顺序（固定）：**
  1. Req §2 非 git 仓库 → hard stop；
  2. Req §4 脏工作区 → hard stop；
  3. 解析基线（§5–§6）、前缀（§7）、`topic`（§8–§9）、路径（§12）；
  4. Req §10 分支名或路径冲突 → stop，Present 选项（**不**因路径占用回退 branch）；
  5. 无冲突时：若 Req §3 成立 → branch 回退（弱隔离）；否则 → worktree；
  6. Present（§13，含可改 prefix/topic/路径；若 §6 适用则醒目标出非标准基线）→ 用户确认（§15，同轮一次）→ 执行；
  7. Stop → AC-10 hand off。
- worktree 默认命令形态：`git worktree add -b <prefix>/<topic> <path> <baseline>`（`<baseline>` 为 Req §5–§6 识别的分支；`<path>` 中 `<repo-basename>` 为原始 basename）。
- 用户确认：明确肯定（确认、好的、yes、go 或等价短句）后方可执行 mutating 命令。
- 发版前须完成消费者 spot-check；未验证前 changelog 标为 experimental 可选卫星（见 Open Questions）。

## Decisions

- **独立卫星，非核心环第 7 阶段：** 用户 `@sdd-worktree` 开工；与 superpowers「session 自动 worktree + 子 agent」不同——此处是**显式、单次、可拒绝**的 git 隔离，保留 engineering-rationale「不借自动编排」原则。
- **建议后执行：** Present → 用户确认 → 再跑 mutating git；避免静默改仓库。
- **默认 worktree，branch 回退：** 非 git 仓库 hard stop（Req §2）；回退条件见 Requirements §3（不含路径占用）。**弱隔离：** branch 回退仅在当前 worktree 开分支，目录不隔离——Present 必须写明。
- **路径/分支冲突：** 统一走 Req §10 stop，**不**静默回退 branch（避免用户不知目录仍占用）。
- **前缀默认 `feature/`：** 用关键词规则 + Present 一次确认覆盖歧义。
- **脏工作区 hard stop：** stash 后须重新触发，防止状态漂移。
- **不并入 `sdd-grill`：** grill 管决策树；worktree 管 git 上下文——职责分离。
- **AC-10 示例：** 用户只说「开个 worktree」、topic 为仓库 slug 兜底、Present 后仅回「确认」→ `sdd-grill`；用户说「做登录 API」或 Present 中改了 topic → `sdd-spec`。
- **拒绝：** superpowers 式自动 worktree 链、Git hook、worktree 清理/生命周期管理、把 worktree 当 delivery gate。

## Open Questions

- **OQ-1（consumer evidence）：** 是否在消费者仓库完成 spot-check 后再标为 recommended satellite？计划阶段定验证记录落点（PR 链接或 CHANGELOG 一句）。不阻塞 plan；阻塞 recommended pin 发版。

## Revision log

- 2026-06-12 | 三轮评审：§3/§10 路径冲突拆清；评估顺序；basename 原始 vs topic slug；AC 重编号 | plan 可启动
- 2026-06-12 | 四轮 should-fix：路径相对 toplevel；Present 可改字段；前缀覆盖；AC-11 交付清单；AC-13/14；When/Skip；AC-10 示例 | AC 增至 14 条
- 2026-06-12 | 五轮 should-fix：§10 冲突选项按场景裁剪；§6 基线与 §15 同轮确认；AC-5/9/13 对齐 | 无 AC 编号变更
