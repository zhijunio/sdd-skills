# Third loop: todo-web (sdd-architect)

Date: 2026-06-09
Consumer repo: `zhijunio/todo-web`（本地 `~/github/todo-web`）
Increment (one sentence): 测试夹具接缝 — 统一 Todo 测试 seed/clear，减少 Repository 直连与重复 `@BeforeEach`

## Environment

- Agent(s): Cursor
- skills install scope: project（`.agents/skills/`）
- sdd-skills ref: `main` @ merge PR #2（闭环时 skill 名为 **`sdd-deepen`**，已更名为 **`sdd-architect`**）
- Consumer branch: `codex/implement-todo-web`
- Consumer delivery commit: `049e598`
- Prior loops: [todo-web-0.1.0.md](./todo-web-0.1.0.md)（`v0.1.0`）

## Stage log

| Stage | Used | Pass | Notes |
|-------|------|------|-------|
| **sdd-architect** | yes | yes | 4 候选；推荐 #1 Test fixtures；无 CONTEXT/ADR |
| using-sdd | yes | yes | deepen #1 → sdd-spec |
| sdd-grill | skip | yes | trade-off 已在 deepen 收敛 |
| sdd-spec | yes | yes | 用户批准 2026-06-09 |
| sdd-plan | yes | yes | 单 slice |
| sdd-build | yes | yes | `TodoTestFixtures` + 5 类迁移，25 tests |
| sdd-review | yes | yes | 无 must-fix |
| sdd-ship | yes | yes | `./mvnw test` 25 pass；commit `049e598` |

## sdd-architect deliverable (summary)

| # | Area | Problem | Direction | Strength |
|---|------|---------|-----------|----------|
| 1 | `src/test/.../todo/*` | 5 类重复 `clearTodos()` + web 测试经 `TodoRepository` seed，绕过 Service | 引入 `TodoTestFixtures`（或 test 基类）统一 clear/seed | **Strong** |
| 2 | Form vs Service | `trim` 在 Service，`@NotBlank` 在 Form；边界分散 | 单点规范化 + 对齐校验测试 | Worth exploring |
| 3 | Web tests | 全 `@SpringBootTest` | 部分 `@WebMvcTest` 切片 | Worth exploring |
| 4 | `TodoService` | 薄门面 + 透传 `TodoRepository` | 维持现状（小项目可接受） | Speculative |

**Top recommendation:** #1 — 行为不变，测试接缝更清晰。

## Friction (sdd-architect)

| ID | Stage | Severity | Description | Fix in sdd-skills? |
|----|-------|----------|-------------|-------------------|
| D1 | sdd-architect | nice | 无 CONTEXT/ADR 时仍顺畅；需在闭环记录中显式注明（验证 AC-3） | no |
| D2 | sdd-architect | nice | 对话交付后需人工复制摘要进 `consumer-loops/*.md`（无默认落盘） | no — by design |
| D3 | install | nice | consumer 仅增量装 `sdd-architect`，core skills 仍为旧 ref | no — consumer 自行 pin |

## Friction (core loop)

| ID | Stage | Severity | Description | Fix in sdd-skills? |
|----|-------|----------|-------------|-------------------|
| F1 | sdd-plan | should | plan 要求 slice 前 commit spec/plan，与 spec+实现合并为 `049e598` | no — consumer 纪律 |
| F2 | sdd-architect | nice | 对话摘要需人工写入闭环记录（D2 再现） | no — by design |

## Verdict

- [x] Pass (deepen + full loop + approved spec/plan)
- [ ] Blocked — reason:

## Follow-ups

- [x] todo-web test-fixtures 增量（`049e598`）
- [x] 本仓 **`v0.2.0`** tag 已发布（2026-06-09）
