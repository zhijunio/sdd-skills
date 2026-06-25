# sdd-publish Implementation Plan

**Spec:** `docs/sdd/2026-06-12-sdd-publish-spec.md`

**Status:** build complete (2026-06-12) — 待 `sdd-review`

## Risks / Dependencies

- 本仓无 `tests/check.py`；行为验收靠 **SKILL.md 自检清单 + 手动 git/gh 场景**（在 `sdd-skills` 或消费者仓库）。
- Slice 9 改 `.github/workflows/check.yml` skill 计数 9→10；须与 Slice 1 同 PR 合并，否则 CI 红。
- OQ-1：recommended pin 发版前须 Slice 10 consumer spot-check；未做前 CHANGELOG 标 **experimental optional satellite**。
- `sdd-verify` **Stop** hand off 在 Slice 8 改，避免 ship 仍只写「no push」而无 publish 指针。
- 含 `gh` 的步骤（PR/CI/merge/release）在 CI 环境可能无 token — 验收以 Present 降级路径 + 本地有 `gh` 场景为主。

## AC 映射总览

| AC | 主要切片 |
| --- | --- |
| AC-1 | 2 |
| AC-2 | 3 |
| AC-3 | 4 |
| AC-4 | 4 |
| AC-5 | 5 |
| AC-6 | 5 |
| AC-7 | 6 |
| AC-8 | 6 |
| AC-9 | 7 |
| AC-10 | 2, 3, 4 |
| AC-11 | 6 |
| AC-12 | 7 |
| AC-13 | 8, 9 |
| AC-14 | 1, 8 |
| AC-15 | 1, 2 |
| OQ-1 | 10 |

---

## Slice 1: 发布 `sdd-publish` 技能骨架（评估顺序 + Present/Stop）

- Goal: `skills/sdd-publish/SKILL.md` 可被 `@` 发现，含 English 指令、九步流水线索引、评估顺序、Present/Stop/Red flags、SDD 尾。
- Acceptance: AC-14（骨架）, AC-15
- Depends on: None
- Test or proof: 文件存在；frontmatter `description` 仅写触发条件；正文含 Constraints「评估顺序」五步（与 spec 一致）及流水线序（push → PR → CI → merge → sync default → tag → release → pin）。
- Implementation outline:
  - 新建 `skills/sdd-publish/SKILL.md`（参考 `sdd-worktree` 体量）。
  - `description`: ship 通过后用户明确要求 push/PR/merge/tag/release 时触发。
  - 嵌入 **Present** 硬约束、**Stop**（集成结束、无下一 skill）。
  - **Red flags**: 未确认 mutating、跳过门禁、自动链 merge→tag、CI babysit、force push、推 main 新 work 等。
- Verification: `test -f skills/sdd-publish/SKILL.md && rg -q 'Present:' skills/sdd-publish/SKILL.md && rg -q 'Evaluation order' skills/sdd-publish/SKILL.md`
- Done: true

## Slice 2: 门禁 hard stop（只读探测 + 前置 skill hand off）

- Goal: 非 git、脏树、无集成意图、ship/review 未过、main 上新 push、force push 等一律 hard stop；探测命令集与 spec Req §1–§2 一致。
- Acceptance: AC-1, AC-10, AC-15（门禁先于一切）
- Depends on: Slice 1
- Test or proof:
  - 场景 A：非 git 目录 → hard stop，无 mutating。
  - 场景 B：未提交/未跟踪（`git status` 脏）→ stop，提示 commit/stash；stash 后须重新 `@`。
  - 场景 C：无 verify 摘要且用户未肯定 verify/review → hand off `sdd-review` / `sdd-verify` / `sdd-build`。
  - 场景 D：在 `main` 意图 push 新 work → stop，提示 topic 分支 + PR。
  - 场景 E：仅问「能发吗」未选步骤 → Present 步骤菜单，等待点名。
- Implementation outline: `SKILL.md` 增 read-only probe 列表、hard stop 表、步骤菜单（Req §9 子集入口）。
- Verification: 场景 A–E 清单全勾；`rg -q 'hard stop' skills/sdd-publish/SKILL.md`
- Done: true

## Slice 3: Push 子集（仅 push，不链后续）

- Goal: 用户点名「只 push」并确认后，Present `git push -u origin <branch>` 并执行；不自动开 PR/merge/tag/release。
- Acceptance: AC-2, AC-10
- Depends on: Slice 2
- Test or proof: 场景 F — 干净 topic 分支、用户「只 push」+ 确认 → 仅 push；未确认前无 `git push`。
- Implementation outline: `SKILL.md` 写 Push 步（Req §3）；强调流水线子集（Req §9）。
- Verification: 场景 F 清单全勾；`rg -q 'git push' skills/sdd-publish/SKILL.md`
- Done: true

## Slice 4: Open PR 与无 `gh` 降级

- Goal: `gh` 可用时 Present 并执行 `gh pr create`；不可用时 Present 完整命令且不声称已创建。
- Acceptance: AC-3, AC-4, AC-10
- Depends on: Slice 3
- Test or proof:
  - 场景 G：`gh` 可用 + 确认开 PR → `gh pr create`，描述可追溯 CHANGELOG/commit。
  - 场景 H：无 `gh` + 要求开 PR → Present 命令 +「本步未执行」。
- Implementation outline: `SKILL.md` 写 Open PR 步（Req §4）与无 `gh` 降级（Req §10）。
- Verification: 场景 G/H 清单全勾；`rg -q 'gh pr create' skills/sdd-publish/SKILL.md`
- Done: true

## Slice 5: CI 展示与 Merge（单独确认 + CI 门禁）

- Goal: CI 步 Present `gh pr checks`；failed/pending 默认不 merge；merge 须单独确认；可显式承担风险后再 merge。
- Acceptance: AC-5, AC-6
- Depends on: Slice 4
- Test or proof:
  - 场景 I：CI failed → 默认 stop merge，直至通过或用户承担风险并再确认。
  - 场景 J：用户单独确认 merge → Present merge 方式后 `gh pr merge`（或网页路径说明）。
- Implementation outline: `SKILL.md` 写 CI 步（Req §5）、Merge 步（Req §6）。
- Verification: 场景 I/J 清单全勾；`rg -q 'gh pr checks' skills/sdd-publish/SKILL.md && rg -q 'gh pr merge' skills/sdd-publish/SKILL.md`
- Done: true

## Slice 6: 同步默认分支、Tag、CHANGELOG 升格与版本解析

- Goal: merge 后 Present `checkout` + `pull` 默认分支；按 Req §7 四级解析版本；含糊则 stop；升格 `[Unreleased]` 须确认后写入；tag 打在 Present 声明的 HEAD。
- Acceptance: AC-7, AC-8, AC-11
- Depends on: Slice 5
- Test or proof:
  - 场景 K：merge 已在本流程执行 → sync default → tag `vX.Y.Z` 与 Present 一致。
  - 场景 L：CHANGELOG 无版本线索 → 不 tag，提示补全。
  - 场景 M：用户确认升格 → `[Unreleased]` → `[vX.Y.Z] - <date>` 仅确认后改文件。
  - 场景 N：仅 topic 分支 tag（未 merge）→ Present 明示 tag 打在 `<branch>` HEAD 并经确认。
- Implementation outline: `SKILL.md` 写同步默认分支（Scope §6 / Req §7）、Tag（§7）、CHANGELOG 升格（§11）；版本解析优先级表。
- Verification: 场景 K–N 清单全勾；`rg -q 'git pull origin' skills/sdd-publish/SKILL.md && rg -q 'Unreleased' skills/sdd-publish/SKILL.md`
- Done: true

## Slice 7: GitHub Release 与 README pin（可选）

- Goal: `gh release create` 与 CHANGELOG 条目一致；recommended pin 段落存在且用户确认时才更新。
- Acceptance: AC-9, AC-12
- Depends on: Slice 6
- Test or proof:
  - 场景 O：`gh` 可用 + 确认 release → `gh release create`，notes 与 CHANGELOG 一致。
  - 场景 P：README 含 pin + 用户确认 → 更新 `@vX.Y.Z`；未确认或无段落 → skip。
- Implementation outline: `SKILL.md` 写 Release 步（Req §8）、README pin（Req §12）；无 `gh` 时 Present 不执行。
- Verification: 场景 O/P 清单全勾；`rg -q 'gh release create' skills/sdd-publish/SKILL.md`
- Done: true

## Slice 8: `sdd-verify` Stop hand off 与 When/Skip 互链

- Goal: verify 通过后用户要集成时 hand off `sdd-publish`；`sdd-publish` 与 `sdd-verify` 互链完整；可选 `sdd-worktree` 叙事不冲突。
- Acceptance: AC-13（hand off 部分）, AC-14
- Depends on: Slice 1
- Test or proof:
  - `rg 'sdd-publish' skills/sdd-verify/SKILL.md skills/sdd-publish/SKILL.md` 有 When/Skip 互链。
  - verify **Stop** 或 **SDD:** 尾含「separately requested → `sdd-publish`」类指针，且不删原有 no-push 纪律。
- Implementation outline:
  - `skills/sdd-verify/SKILL.md`：**Stop** / **SDD:** 增 hand off `sdd-publish`（用户明确要求 push/PR/merge/tag/release 时）。
  - 完善 `sdd-publish` **When/Skip** 与 `sdd-verify` 链接。
- Verification: 互链 grep 通过；人工读 verify Stop 一句不矛盾
- Done: true

## Slice 9: 维护者文档与 CI（十 skill + Mermaid post-loop）

- Goal: 仓库叙事、治理文档、CI 计数与 spec AC-13 一致；README Mermaid 增 post-loop `sdd-publish` 节点（`SH --> PUB[sdd-publish]` 或等价）。
- Acceptance: AC-13
- Depends on: Slice 1
- Test or proof: 文档与配置 diff 覆盖清单。
- Implementation outline:
  - `README.md`：十 skill、四颗卫星（pre `sdd-worktree` + post `sdd-publish` + zoom + improve）；Mermaid 增 post-loop 边。
  - `AGENTS.md`：九→十 skill。
  - `SOURCES.md`：新增 `sdd-publish` 小节（maintainer-authored）。
  - `docs/design/engineering-rationale.md` §3.2 / §3.3 增 `sdd-publish` 映射行。
  - `.github/workflows/check.yml`：`eq 9` → `eq 10`。
  - `CHANGELOG.md` `[Unreleased]`：Added experimental optional `sdd-publish`。
- Verification: `test "$(find skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l)" -eq 10`；`rg -q 'sdd-publish' README.md AGENTS.md SOURCES.md docs/design/engineering-rationale.md`
- Done: true

## Slice 10: Consumer spot-check（闭合 OQ-1）

- Goal: 在消费者 git 仓库跑通 publish 子集（至少 push + PR Present），记录摩擦；决定是否标 non-experimental。
- Acceptance: OQ-1（spec Open Questions）
- Depends on: Slice 2–9 合并后
- Test or proof: 消费者仓库内 `@sdd-publish`（ship 已过的模拟上下文）→ 门禁 → Present push/PR → 无阻断摩擦。
- Implementation outline:
  - 选任意本地消费者 git 仓库（**不**写死项目名）。
  - 记录：步骤菜单、Present 清晰度、`gh` 降级是否合理。
  - 更新 `CHANGELOG.md` `[Unreleased]` 一句 spot-check 结论；未通过则保持 experimental，不 bump README recommended pin。
- Verification: CHANGELOG 含 spot-check 记录；[README — Maintainer verification](../../README.md#maintainer-verification) 清单可勾选
- Done: true

---

## Ship

- 全片 `Done: true` 后 → `@sdd-review`（本 increment diff）→ `@sdd-verify`。
- 发版 pin：**待 OQ-1 通过**；否则仅合并 main，tag 延后或保持 experimental（与 CHANGELOG 一致）。

## Verified slices (build 时追加)

- 2026-06-12 | Slice 1 | `SKILL.md` + Evaluation order + Present — rg OK
- 2026-06-12 | Slice 2–7 | full `skills/sdd-publish/SKILL.md` — rg OK; scenarios A–P covered in SKILL prose
- 2026-06-12 | Slice 8 | `sdd-verify` Stop/SDD hand off + `sdd-publish` When/Skip — rg OK
- 2026-06-12 | Slice 9 | ten skills count=10; docs/CI/CHANGELOG updated
- 2026-06-12 | Slice 10 | CHANGELOG spot-check note; experimental pin unchanged
