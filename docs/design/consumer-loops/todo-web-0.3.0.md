# Fourth loop: todo-web (sdd-improve)

Date: 2026-06-11
Consumer repo: `zhijunio/todo-web`（本地 `~/github/todo-web`）
Increment (one sentence): **`sdd-improve` 🟡#1** → WebMvcTest 切片迁移（mock `TodoService`，去掉 web 测试中的 `TodoRepository`）

## Environment

- Agent(s): Cursor
- skills install scope: project（`.agents/skills/`）
- sdd-skills ref: `main` @ merge commit（含 `sdd-improve`）
- Consumer branch: `codex/implement-todo-web` @ `60e00bb`
- Prior loops: [todo-web-first.md](./todo-web-first.md) → [todo-web-0.1.0.md](./todo-web-0.1.0.md) → [todo-web-0.2.0.md](./todo-web-0.2.0.md)

## Stage log

| Stage | Used | Pass | Notes |
|-------|------|------|-------|
| **sdd-improve** | yes | yes | standard；whole repo |
| Confirm (user) | yes | yes | 选定 🟡 **#1** WebMvcTest |
| hand off | yes | yes | `@sdd-spec` |
| sdd-grill | skip | yes | scope 已在 improve 收敛 |
| sdd-spec | yes | yes | `docs/sdd/2026-06-11-webmvc-slice-spec.md` |
| sdd-plan | yes | yes | 单 slice plan |
| sdd-build | yes | yes | 4 `*WebTest` + `TodoWebTestSupport` |
| sdd-review | yes | yes | code diff；无 must-fix |
| sdd-ship | yes | yes | `./mvnw test` 25 pass（Java 21-tem） |

## sdd-improve deliverable (summary)

**Pass path:** **A** — findings → SDD loop

### Context (abbrev.)

- **Effort:** standard
- **Range:** whole repo
- **User selected:** 🟡 #1 — Web 测试 `@SpringBootTest` → `@WebMvcTest`

### Findings addressed

| Group | Selected |
|-------|----------|
| 🟡 #1 WebMvcTest 切片 | ✅ implemented |
| 🟡 #2 Repository 断言 | ✅ 随 #1 一并去除（web 层 mock verify） |

### Delivery summary

- `@WebMvcTest(TodoController.class)` + `@Import(TodoExceptionHandler.class)` × 4
- `@MockitoBean TodoService`；`TodoWebTestSupport` 造 id-bearing stubs
- `TodoServiceTest` / `TodoWebApplicationTests` 仍 `@SpringBootTest`

### Report — Follow-up（摘录）

Stage 0 对话报告漏写 **Next stage**（trial 摩擦 I6）；补录如下：

```markdown
## Follow-up

### Next stage

**`sdd-spec`** — 有 🟡 findings（WebMvcTest / Repository 半迁移）；用户选定 follow-up 前需 AC。trade-off 仍开放 → **`sdd-grill`**。

### Dependency order

#1 WebMvcTest → #2 去 Repository 断言（可随 #1 一并解决）
```

用户 Confirm **`#1`** 后实际路由：`sdd-spec` → `sdd-plan` → `sdd-build` → `sdd-review` → `sdd-ship` ✅

## Friction (sdd-improve)

| ID | Severity | Description | Fix in sdd-skills? |
|----|----------|-------------|-------------------|
| I1 | nice | install 用本地 copy（`main` 尚无 improve） | no — 待 PR merge |
| I2 | nice | 对话 → 人工写 consumer-loops | no — by design |
| I3 | nice | improve 报告 → spec 标题/AC 顺畅 | no |
| I4 | nice | Confirm `#1` 一句即可开 loop | no |
| I5 | should | Stage 0 vs full Pass 分界 — 本次已闭环 Path A | no |
| I6 | should | 首次 Present 漏 **`### Next stage`**，直接进 Confirm | yes — `SKILL.md` / `finding-format.md` 已加厚 |

## Friction (core loop)

| ID | Stage | Severity | Description | Fix in sdd-skills? |
|----|-------|----------|-------------|-------------------|
| F1 | sdd-spec | nice | 用户 Confirm 即视为 spec 批准（trial 节奏） | no — consumer 纪律 |
| F2 | sdd-build | nice | `void` mock 须 `doThrow` 非 `when().thenThrow` | no — consumer 学习点 |

## Verdict

- [x] **Stage 0 Pass**
- [x] **Full loop Pass**（Path A — improve #1 → spec/plan/build/review/ship）
- [ ] Blocked — reason:

## Follow-ups

- [x] consumer 仓 `60e00bb` push `codex/implement-todo-web`
