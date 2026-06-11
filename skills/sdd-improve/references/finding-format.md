# Finding Format

**Maintainers:** Sync **severity semantics**, **Report locale**, and **Verify** with **`sdd-review`** `finding-format.md`. Layout need not match delivery review.

## Report locale

Skill instructions **English**. Report prose in the **user's language** (latest user turn when unclear) — hard rule at **Present** in `SKILL.md`.

- Layout: tables, prose, or lists — no mandatory shared skeleton.
- Keep literal: category lens ids; skill ids; `file:line`; git literals; **🔴/🟡/🟢** (group titles may translate).

## Required content

Conversation **findings report** — not a delivery verdict. After **Confirm:** [closing-the-loop.md](closing-the-loop.md).

1. **Scope** — effort, range, categories; recon (verify command, HEAD, tree, hotspots); **not audited** with reasons.
2. **Findings** — verified items + **Evidence**; **🔴/🟡/🟢** follow-up priority (not ship gate).
3. **Coverage** — dimensions walked; verify rejections / sampling limits.
4. **Next stage** — one route + rationale; required even when findings empty.

Profile merges into **Scope** — no `## Profile`. Skips → **Recon — Not audited**. Skeleton: [profile-guide.md](profile-guide.md).

## Severity

Follow-up priority only — does **not** gate **`sdd-ship`**. Same labels as **`sdd-review`**; meaning differs — delivery gate there only.

| Severity | Use when |
| --- | --- |
| **🔴 must-fix** | HIGH-confidence correctness, security, or data-loss; missing verify baseline; unblocker |
| **🟡 should-fix** | Maintainability or test gap on important paths; MED+ confidence |
| **🟢 suggestion** | Docs/DX polish, LOW investigate, speculative architecture |

## Per-finding fields

**Evidence** required. Optional: Impact, Confidence (✅ HIGH · ⚠️ MED · ❓ LOW), Effort (S/M/L), Risk. Category **5**: Strength (🟢 Strong · 🟡 Worth exploring · ⚪ Speculative). Branch scope → `introduced` / `pre-existing`. Prioritize: impact ÷ effort, discounted by confidence and fix-risk.

## Example (optional)

Not mandatory. **Confirm** follows **Present** — not in skeleton.

```markdown
## Context

### Recon
| Type | skills-only repo |
| Verification | `npm test` ✅ or none |
| HEAD | `abc1234` · `main` |
| Not audited | performance — no runtime |

### Scope
- **Effort:** standard · **Range:** whole repo · **Categories:** tests, architecture, docs

## Findings

### 🔴 must-fix
**1. tests** — No verification baseline.
- **Evidence:** `README.md` — no documented verify command
- **Confidence:** ✅ HIGH · **Effort:** S

### 🟡 should-fix
None.

## Coverage
**Examined:** tests, docs, architecture (hotspot-weighted).
**Limits:** No full-repo link scan.

## Follow-up
### Next stage
**`sdd-spec`** — AC needed for verification strategy.
```

Category **9** direction bullets when user asks. Multiple follow-ups: one-line **Dependency order** — [closing-the-loop.md](closing-the-loop.md).

## Verify

Re-read every cited location before **Present**; rejections → **Coverage — Limits**.
