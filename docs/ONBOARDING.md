# Contributor Onboarding Plan

**Audience:** Experienced developer, new to this repository and the SDD-skills maintainer workflow.

**Goal:** Become productive maintaining or extending skills safely — without treating this repo like an application codebase.

Related: [README.md](../README.md) · [AGENTS.md](../AGENTS.md) · [docs/design/README.md](design/README.md)

---

## Phase 1 — Foundation

### What this repo is (5 minutes)

- **Not** an app — no `package.json`, no test runner, no deployable service.
- **Is** fifteen Markdown **agent skills** under `skills/<name>/SKILL.md`, plus maintainer design docs and minimal CI.
- Consumers install skills into **their** projects via the [skills CLI](https://github.com/vercel-labs/skills) — see [README — Installation](../README.md#installation).

### Environment setup

1. **Clone and branch**

   ```bash
   git clone git@github.com:zhijunio/sdd-skills.git
   cd sdd-skills
   git checkout main
   git pull origin main
   git checkout -b docs/your-first-task   # or feature/ / fix/
   ```

2. **Tools you need**

   | Tool | Why |
   | --- | --- |
   | `git` | Topic branches; PRs to `main` only |
   | `gh` (optional) | Issues, PR checks, merge — not required for doc-only edits |
   | Node.js (optional) | Only if you trial `npx skills@latest add zhijunio/sdd-skills` |
   | Cursor or another agent IDE (optional) | Try skills and `.github/prompts/` as a consumer would |

3. **Verify locally** (same as CI — run before every PR)

   ```bash
   test "$(find skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l)" -eq 14
   test ! -e skills/sdd-ship
   test -f skills/sdd-verify/SKILL.md
   ```

   **Troubleshooting**

   - Count ≠ 14 → a skill directory is missing `SKILL.md`, or a new skill was added without updating [`.github/workflows/check.yml`](../.github/workflows/check.yml).
   - `skills/sdd-ship` exists → remove it; current `main` uses **`sdd-verify`**.
   - `validate` fails on GitHub but passes locally → push latest commits; check branch is up to date with `main` (strict branch protection).

4. **Optional: trial install as a consumer**

   ```bash
   npx skills@latest add zhijunio/sdd-skills --list
   npx skills@latest add zhijunio/sdd-skills -s sdd-spec -s sdd-plan -a cursor -y
   ```

### Read first (in order)

| Order | Document | Time | Why |
| --- | --- | --- | --- |
| 1 | [README.md](../README.md) | ~15 min | Skills map, workflow diagram, install, maintainer verification |
| 2 | [AGENTS.md](../AGENTS.md) | ~10 min | Commands, commit/PR rules, agent pitfalls |
| 3 | [engineering-rationale §1.0](design/engineering-rationale.md#10-核心原则) | ~10 min | Six principles (中文) — why stages exist |
| 4 | One core skill, e.g. [`skills/sdd-spec/SKILL.md`](../skills/sdd-spec/SKILL.md) | ~10 min | How a runtime contract is written |
| 5 | [docs/design/SOURCES.md](design/SOURCES.md) | skim | Upstream pins — read when you touch borrowed prose |

**Phase 1 next steps**

- [ ] Clone repo and run the three `test` commands — all must pass.
- [ ] Skim [README — Skills](../README.md#skills) and name the six core loop skills from memory.
- [ ] Open `skills/sdd-review/SKILL.md` and find the **When/Skip** cross-link to `sdd-audit`.

---

## Phase 2 — Exploration

### Codebase map (hands-on)

1. **Skills tree**

   ```bash
   find skills -mindepth 2 -maxdepth 2 -name SKILL.md | sort
   ```

   Group into: **core loop** (6) · **loop satellites** (2) · **exploration** (2) · **meta** (5) — see [AGENTS.md — Structure](../AGENTS.md#structure).

2. **Prompt pairs** — several skills share content with [`.github/prompts/`](../.github/prompts/) (see [SOURCES — Skill and prompt pairs](../docs/design/SOURCES.md#skill-and-prompt-pairs)):

   - **Independent** — neither file links to the other
   - **Content parity** — update skill and prompt together when behavior changes

   | Skill | Prompt file |
   | --- | --- |
   | `sdd-readme` | `create-readme.prompt.md` |
   | `sdd-agents` | `create-agents-md.prompt.md` |
   | `sdd-ci` | `create-ci.prompt.md` |
   | `sdd-onboard` | `onboarding-plan.prompt.md` |
   | `sdd-explain` | `explain-code.prompt.md` |
   | `sdd-zoom` | `zoom-codebase.prompt.md` |
   | `sdd-grill` | `grill-me.prompt.md` |
   | `sdd-publish` | `publish-changes.prompt.md` |

   Other prompts (`review-code`, `generate-unit-tests`, `document-api`) have no dedicated skill — use when the task matches the prompt description.

3. **Historical increments** — browse `docs/sdd/*-spec.md` and `*-plan.md` for how this repo dogfoods SDD on itself.

4. **CI** — read [`.github/workflows/check.yml`](../.github/workflows/check.yml); job name **`validate`** is required by branch protection on `main`.

### Run workflows (no unit tests)

There is no `npm test`. Use CI parity instead:

```bash
test "$(find skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l)" -eq 14 \
  && test ! -e skills/sdd-ship \
  && test -f skills/sdd-verify/SKILL.md \
  && echo "validate: OK"
```

After editing Markdown, spot-check relative links in changed files manually.

Push a branch and open a draft PR to see **`validate`** and GitGuardian on GitHub Actions.

### Beginner-friendly first tasks

Suited to an experienced developer new to skills authoring:

| Task | Scope | What you learn |
| --- | --- | --- |
| Fix a broken relative link in README, AGENTS, or `references/` | 1–2 files | Link hygiene; prose-only review mindset |
| Align a paired skill and `.github/prompts/*.prompt.md` (same content, no cross-links) | 1 prompt + 1 skill | Prompt/skill parity |
| Add a **Spot-check** line to [CHANGELOG.md](../CHANGELOG.md) `[Unreleased]` after self-trial | 1 file | Maintainer verification |
| Tighten one skill **`description`** frontmatter (triggers only) | 1 `SKILL.md` | [AGENTS.md](../AGENTS.md) authoring rules |

### Open issues

No open issues verified at generation time (`gh issue list --repo zhijunio/sdd-skills --state open` returned empty).

Find work:

```bash
gh issue list --repo zhijunio/sdd-skills --state open
gh issue list --repo zhijunio/sdd-skills --state open --label "good first issue"
```

Or open a small docs PR from the tasks above.

**Phase 2 next steps**

- [ ] Run `find skills …` and label each skill by group (core / loop / exploration / meta).
- [ ] Read `sdd-audit` vs `sdd-review` — write one sentence on delivery review vs opportunity scan.
- [ ] Pick one beginner task and create a topic branch.

---

## Phase 3 — Integration

### Team process

1. **Branch** — `feature/`, `fix/`, or `docs/` + topic; do not commit new work on `main`.
2. **Commits** — one logical change per commit; `feat:` / `fix:` / `docs:` / `chore:` / `refactor:`.
3. **PR** — target `main`; wait for **`validate`** before merge.
4. **User-visible changes** — update [CHANGELOG.md](../CHANGELOG.md) `[Unreleased]`.
5. **Material skill changes** — maintainer self-trial (install skill, run one increment); note friction in PR or CHANGELOG.
6. **Upstream borrow** — update [SOURCES.md](design/SOURCES.md) and [THIRD_PARTY_NOTICES.md](design/THIRD_PARTY_NOTICES.md) when pinned behavior changes.

Full rules: [AGENTS.md — Commit & PR](../AGENTS.md#commit--pr).

### First contribution (recommended path)

**Warm-up PR (docs-only, ~30–60 min)**

1. Fix one link or typo in README, AGENTS, or a skill `references/` file.
2. Run local validate commands.
3. Open PR; confirm CI green.
4. Merge per maintainer policy.

**Second PR (skill-aware, half day)**

1. Pick one skill (e.g. `sdd-onboard` or `sdd-readme`).
2. Read skill + paired prompt + SOURCES entry.
3. Make a small scoped improvement (clarity, cross-link, example).
4. Self-trial: `@` the skill in Cursor on this repo or a toy consumer repo.
5. Add CHANGELOG note if user-visible.

### SDD loop on this repo (non-trivial changes)

Dogfood the delivery loop for behavior changes:

```text
sdd-spec → sdd-plan → sdd-build → sdd-review → sdd-verify
```

Optional beforehand: `sdd-worktree`, `sdd-grill`, `sdd-zoom`. Remote git only when you ask: `sdd-publish`.

Do **not** auto-chain stages — user **`@`** each skill explicitly.

### Early wins

- Green **`validate`** on your first merged PR.
- A docs fix noted in CHANGELOG `[Unreleased]`.
- Install and `@`-invoke one skill from this repo in Cursor.
- Explain **review vs audit** to another contributor in one paragraph.

**Phase 3 next steps**

- [ ] Open warm-up PR with local validate passing.
- [ ] After merge, pull `main` and delete the topic branch.
- [ ] Self-trial one satellite skill in a consumer repo this week.

---

## Quick reference

| Question | Answer |
| --- | --- |
| How many skills? | 14 — [README](../README.md#skills) |
| Verify before PR? | Three `test` commands in [AGENTS.md](../AGENTS.md#commands) |
| Renames? | `sdd-ship` → `sdd-verify`; `sdd-improve` → `sdd-audit` |
| Design rationale? | [engineering-rationale.md](design/engineering-rationale.md) |
| Consumer vs maintainer? | Consumers: README + install; maintainers: AGENTS + `docs/design/` |

*Aligned with [onboarding-plan.prompt.md](../.github/prompts/onboarding-plan.prompt.md) and skill [`sdd-onboard`](../skills/sdd-onboard/SKILL.md).*
