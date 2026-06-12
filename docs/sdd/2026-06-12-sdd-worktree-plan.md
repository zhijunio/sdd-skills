# sdd-worktree Implementation Plan

**Spec:** `docs/sdd/2026-06-12-sdd-worktree-spec.md`

**Status:** build complete (2026-06-12) — 待 `sdd-review`

## Risks / Dependencies

- 本仓无 `tests/check.py`；行为验收靠 **SKILL.md 自检清单 + 手动 git 场景**（在 `sdd-skills` 或消费者仓库）。
- Slice 8 改 `.github/workflows/check.yml` skill 计数 8→9；须与 Slice 1 同 PR 合并，否则 CI 红。
- OQ-1：recommended pin 发版前须 Slice 9 consumer spot-check；未做前 CHANGELOG 标 **experimental optional satellite**。
- `sdd-spec` / `sdd-grill` 的 **When/Skip** 互链在 Slice 7 一并改，避免单边引用。

## AC 映射总览

| AC | 主要切片 |
| --- | --- |
| AC-1 | 2 |
| AC-2 | 3 |
| AC-3 | 4 |
| AC-4 | 3 |
| AC-5 | 2, 6 |
| AC-6 | 2, 6 |
| AC-7 | 2, 6 |
| AC-8 | 7 |
| AC-9 | 5 |
| AC-10 | 7 |
| AC-11 | 8 |
| AC-12 | 1, 7 |
| AC-13 | 2, 3 |
| AC-14 | 1 |
| OQ-1 | 9 |

---

## Slice 1: 发布 `sdd-worktree` 技能骨架（评估顺序 + Present/Stop）

- Goal: `skills/sdd-worktree/SKILL.md` 可被 `@` 发现，含 English 指令、评估顺序、Present/Stop/Red flags、SDD 尾；无 mutating git 步骤细节可先占位引用 spec。
- Acceptance: AC-12（骨架）, AC-14
- Depends on: None
- Test or proof: 文件存在；frontmatter `description` 仅写触发条件；正文含 Constraints「评估顺序」七步（与 spec 一致）。
- Implementation outline:
  - 新建 `skills/sdd-worktree/SKILL.md`（参考 `sdd-zoom` 体量：短正文 + SDD 尾）。
  - `description`: 新需求开工前需隔离 git 上下文、或用户提 worktree/开分支 时触发。
  - 嵌入 **Present** 硬约束、**Stop** hand off 指针（详则 Slice 7）。
  - **Red flags**: 未确认即 mutating git、跳过评估顺序、自动链下一 skill、当 delivery gate 等。
- Verification: `test -f skills/sdd-worktree/SKILL.md && rg -q 'Present:' skills/sdd-worktree/SKILL.md && rg -q 'Evaluation order' skills/sdd-worktree/SKILL.md`
- Done: true

## Slice 2: 干净仓库 happy path — worktree 创建

- Goal: 干净 git 仓库、有 `main`、用户给出主题并确认后，技能 Present 完整 `git worktree add -b feature/<topic> …` 并执行。
- Acceptance: AC-1, AC-5（main 基线）, AC-6, AC-7（默认 `feature/`）, AC-13（确认前只读）
- Depends on: Slice 1
- Test or proof: 手动场景 A — 在 `sdd-skills` 干净工作区模拟：`@sdd-worktree` +「做 worktree 技能文档」→ Present 含 baseline/prefix/topic/path/命令 → 用户「确认」→ 仅此时执行 mutating 命令（可用 dry-run：Present 输出命令，人工核对未确认前无 `git worktree add`）。
- Implementation outline: 在 `SKILL.md` 写清：只读探测命令集（Req §1）、基线识别（§5）、prefix/topic 默认规则（§7–§9）、默认路径 `../<repo-basename>-<topic>`（§12）、worktree 命令模板（Constraints）。
- Verification: 场景 A 清单全勾；`rg -q 'git worktree add' skills/sdd-worktree/SKILL.md`
- Done: true

## Slice 3: Hard stop — 非 git、脏工作区、未确认

- Goal: 非仓库、未提交改动、用户未确认时均不执行 mutating git。
- Acceptance: AC-2, AC-4, AC-13
- Depends on: Slice 1
- Test or proof:
  - 场景 B：非 git 目录 → hard stop，无 `git branch`/`git worktree`。
  - 场景 C：有 unstaged 改动 → stop，提示 commit/stash；stash 后须重新 `@`。
  - 场景 D：Present 后用户未说确认 → 无 mutating 命令。
- Implementation outline: `SKILL.md` 增 hard stop 段（Req §2、§4、§15）；Red flags 对齐。
- Verification: 场景 B/C/D 清单全勾
- Done: true

## Slice 4: Branch 回退（弱隔离）

- Goal: worktree 不可用或用户拒绝时，改 `git checkout -b <prefix>/<topic> <baseline>`，输出回退原因并标注弱隔离。
- Acceptance: AC-3
- Depends on: Slice 2
- Test or proof: 场景 E — 用户明确「只要分支不要 worktree」→ Present 标明弱隔离 + `git checkout -b` 命令。
- Implementation outline: `SKILL.md` 写 Req §3 三条回退条件；强调**不含**路径占用回退。
- Verification: 场景 E 清单全勾；`rg -q 'weak isolation' skills/sdd-worktree/SKILL.md`
- Done: true

## Slice 5: 冲突处理（分支 vs 路径）

- Goal: 分支已存在或路径占用时 stop，按场景 Present 选项（路径-only 无「复用分支」）。
- Acceptance: AC-9
- Depends on: Slice 2
- Test or proof:
  - 场景 F：`<prefix>/<topic>` 已存在 → 选项含换 topic / 复用 / 取消。
  - 场景 G：路径占用、分支不存在 → 选项含换路径 / 换 topic / 取消，**无**复用分支。
- Implementation outline: `SKILL.md` 嵌入 Req §10 三分支选项表。
- Verification: 场景 F/G 清单全勾
- Done: true

## Slice 6: 非标准基线、slug、前缀覆盖、Present 可改字段

- Goal: 无 main/master 时 Present 醒目标基线；topic slug、前缀 fix/docs、用户改 prefix/topic/路径均可在同轮 Present 处理。
- Acceptance: AC-5（无 main/master）, AC-6, AC-7
- Depends on: Slice 2
- Test or proof:
  - 场景 H：仅 `develop` 无 main/master → Present 标非标准基线，同轮一次确认。
  - 场景 I：描述含「修复」→ `fix/`；纯文档 → `docs/`；Present 中用户改前缀 → 以用户为准。
  - 场景 J：无主题描述 → topic 为仓库 basename slug。
- Implementation outline: `SKILL.md` 补 Req §6–§9、§13 slug 规则与可改字段说明。
- Verification: 场景 H/I/J 清单全勾
- Done: true

## Slice 7: Stop hand-off 与 When/Skip 互链

- Goal: 成功后 Stop；grill vs spec 路由可判定；`sdd-worktree` 可独立触发；`sdd-spec`/`sdd-grill` 互链。
- Acceptance: AC-8, AC-10, AC-12
- Depends on: Slice 1
- Test or proof:
  - 场景 K：仅「开个 worktree」+ slug 兜底 topic + 只回「确认」→ hand off `sdd-grill`。
  - 场景 L：「做登录 API」→ hand off `sdd-spec`。
  - `rg 'sdd-worktree' skills/sdd-spec/SKILL.md skills/sdd-grill/SKILL.md skills/sdd-worktree/SKILL.md` 有 When/Skip 互链。
- Implementation outline:
  - 完善 `sdd-worktree` **Stop**（AC-10 示例）。
  - `sdd-spec` **When/Skip**：可选先 `@sdd-worktree` 隔离上下文。
  - `sdd-grill` **When/Skip**：目标模糊时可先 worktree 再 grill（或反向 hand off 已足够则只互链）。
- Verification: 场景 K/L + 互链 grep 通过
- Done: true

## Slice 8: 维护者文档与 CI（九 skill）

- Goal: 仓库叙事、治理文档、CI 计数与 spec AC-11 一致。
- Acceptance: AC-11
- Depends on: Slice 1
- Test or proof: 文档与配置 diff 覆盖清单；CI 本地预检通过。
- Implementation outline:
  - `README.md`：九 skill、pre-loop 卫星 `sdd-worktree`（Mermaid 子图）。
  - `AGENTS.md`：八→九 skill 表述。
  - `SOURCES.md`：新增 `sdd-worktree` 小节（融合取用、无上游 pin 或注明 maintainer-authored）。
  - `docs/design/engineering-rationale.md` §3.3 增 `sdd-worktree` 映射行。
  - `.github/workflows/check.yml`：`eq 8` → `eq 9`。
  - `CHANGELOG.md` `[Unreleased]`：Added experimental optional `sdd-worktree`。
- Verification: `test "$(find skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l)" -eq 9`；`rg -q 'sdd-worktree' README.md AGENTS.md SOURCES.md docs/design/engineering-rationale.md`
- Done: true

## Slice 9: Consumer spot-check（闭合 OQ-1）

- Goal: 在消费者 git 仓库跑通一次完整 increment，记录摩擦；决定是否标 recommended satellite。
- Acceptance: OQ-1（spec Open Questions）
- Depends on: Slice 2–8 合并后
- Test or proof: 消费者仓库内 `@sdd-worktree` → 确认 → 隔离上下文 → hand off `sdd-spec`；无阻断摩擦。
- Implementation outline:
  - 选任意本地消费者 git 仓库（**不**写死项目名）。
  - 记录：Present 是否清晰、命令是否正确、hand off 是否合理。
  - 更新 `CHANGELOG.md` `[Unreleased]` 一句 spot-check 结论；若未通过则保持 experimental，不更新 README recommended pin。
- Verification: CHANGELOG 含 spot-check 记录；维护者清单勾选 [README — Maintainer verification](../../README.md#maintainer-verification)
- Done: true

---

## Ship

- 全片 `Done: true` 后 → `@sdd-review`（本 increment diff）→ `@sdd-ship`。
- 发版 pin：**待 OQ-1 通过**；否则仅合并 main，tag 延后或标 pre-release/experimental（与 CHANGELOG 一致）。

## Verified slices (build 时追加)

- 2026-06-12 | Slice 1 | `SKILL.md` + Evaluation order + Present — rg OK
- 2026-06-12 | Slice 2–7 | full `skills/sdd-worktree/SKILL.md` + spec/grill When/Skip — rg OK
- 2026-06-12 | Slice 8 | nine skills count=9; docs/CI updated
- 2026-06-12 | Slice 9 | CHANGELOG spot-check note; experimental pin unchanged
