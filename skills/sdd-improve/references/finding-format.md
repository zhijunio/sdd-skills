# Finding Format

**Maintainers:** Sync **severity semantics**, **Report locale**, and **Verify** rules with **`sdd-review`** `finding-format.md` when those change. **Layout need not match** delivery review.

## Report locale

Skill instructions **English**. Report prose in the **user's language** (latest user turn when unclear).

- **Format:** any clear structure — tables, prose, or lists; **no** mandatory shared markdown skeleton across skills.
- **Keep literal:** category lens ids (e.g. `architecture`); skill ids; `file:line`; git literals; **🔴/🟡/🟢** (group titles may translate).

## Opportunity scan report

**Outcome:** conversation **findings report** — not a **delivery verdict**. Follow-ups: [closing-the-loop.md](closing-the-loop.md).

**Required content** (substance, not heading names):

1. **Scope** — effort, range, categories examined; recon facts (verify command, HEAD, tree, hotspots); **not audited** with reasons.
2. **Findings** — verified items with **Evidence**; **🔴/🟡/🟢** follow-up priority (not ship gate).
3. **Coverage** — what was walked; verify rejections / sampling limits.
4. **Next stage** — one route + rationale ([closing-the-loop.md](closing-the-loop.md)); required even when findings empty.

**Example layout (optional):**

```markdown
# SDD Improve

## Context

### Recon

Read-only territory facts. Skips belong here — not in Scope.

| Item | Summary |
| --- | --- |
| **Type** | e.g. skills-only repo, Python app, monorepo |
| **Verification** | exact command + last result, e.g. `npm test` ✅ or `pytest -q` ✅ |
| **CI** | workflow file + job name, or "none" |
| **HEAD** | `git rev-parse --short HEAD` + branch name |
| **Working tree** | clean / N modified / ahead M of origin |
| **Hotspots** | paths or areas with recent churn or focus |
| **Not audited** | categories or areas skipped + project-specific reason |

### Scope

Profile (optional) merges here — **no `## Profile` heading**. **In-scope only.**

- **Effort:** standard
- **Range:** whole repo
- **Categories:** correctness, security, tests, architecture, dependencies, experience, docs

## Findings

One option: group under **🔴 / 🟡 / 🟢** severity (titles may translate). Each finding needs **Evidence**. Empty severity group → state none.

**Follow-up priority only** — does **not** gate **`sdd-ship`**. (Delivery review uses the same labels with a different meaning — [`sdd-review` — When/Skip](../../sdd-review/SKILL.md).)

| Severity | Use when |
| --- | --- |
| **🔴 must-fix** | HIGH-confidence correctness, security, or data-loss risk; missing verification baseline; unblocker |
| **🟡 should-fix** | Maintainability or test gap on important paths; MED+ confidence |
| **🟢 suggestion** | Docs/DX polish, LOW investigate, speculative architecture, awareness |

**Per-finding axes:**

| Axis | Values |
| --- | --- |
| **Confidence** | ✅ HIGH · ⚠️ MED · ❓ LOW |
| **Effort** (fix) | S · M · L |
| **Risk** (fix) | 🔴 HIGH · 🟡 MED · 🟢 LOW |
| **Strength** (category 5) | 🟢 Strong · 🟡 Worth exploring · ⚪ Speculative |

### 🔴 must-fix

**1. architecture · introduced** — Pass-through layer adds indirection without reuse.

- **Evidence:** `skills/foo.md:12` — thin wrapper re-exports parent with no added invariant
- **Impact:** Callers pay indirection cost; no shared reuse at the seam
- **Effort:** M
- **Confidence:** ✅ HIGH
- **Risk:** 🟢 LOW
- **Strength:** 🟡 Worth exploring

### 🟡 should-fix

**1. docs** — Install example omits optional satellites.

- **Evidence:** `README.md` — default install lists core loop only
- **Impact:** Consumers may miss `sdd-improve` / `sdd-zoom` without `-s` flags
- **Effort:** S
- **Confidence:** ✅ HIGH
- **Risk:** 🟢 LOW

### 🟢 suggestion

None.

## Coverage

Process meta — **not** findings. Same two subsections as **`sdd-review`**; content differs.

### Examined

What was walked: categories per **Context — Scope** (narrative or brief ✅/⏭️ list — format may differ from delivery review). Skips stay in **Context — Recon — Not audited** only — do not repeat here.

### Limits

**Verify** output: considered and rejected (by-design, mis-attributed evidence, duplicate). No credible findings → state what was examined. Large-repo sampling limits here if applicable.

## Follow-up

**Required:** state **Next stage** before Confirm — even when findings empty (none found → **`sdd-grill`** if trade-offs open, else explicit none-actionable). Do not end **Present** with Confirm only.

### Next stage

One **route** — [closing-the-loop.md](closing-the-loop.md). Name it and one-line why:

- **`sdd-spec`** / **`sdd-plan`** / **`sdd-build`** — per [closing-the-loop.md](closing-the-loop.md) when a skill adds value (default **`sdd-spec`** when AC missing)
- **`sdd-grill`** — trade-offs still open
- **`direct edit`** — user fixes ad-hoc **outside** SDD skills; improve **Stop**s; user verifies (e.g. `./mvnw test`); optional later **`sdd-review`**

**Not in-session implementation:** improve never edits product code. **SDD skills optional** for follow-up — not every finding needs spec, plan, or **`sdd-build`**.

### Direction

Optional — category 9 only; before **Next stage** when present; 2–4 bullets with **Evidence**.

### Dependency order

Optional — when ≥2 follow-ups; one line: `#1 → #5`. Omit when ≤1 actionable finding.
```

### Finding fields (when numbered)

Per item: category, summary, **Evidence** (required); optional Impact, Effort, Confidence, Risk; category 5 may add Strength; branch scope → `introduced` / `pre-existing` tag.

**Prioritization:** impact ÷ effort, discounted by confidence and fix-risk.

### Verify rules

Re-read every cited location before **Present**; rejections → **Coverage — Limits**.

## Disambiguation vs **delivery review**

Normative pairing — [`sdd-review` — When/Skip](../../sdd-review/SKILL.md). Shared **🔴/🟡/🟢** labels only; **meaning differs** — opportunity-scan severities rank follow-up priority only and **do not** gate **`sdd-ship`**.
