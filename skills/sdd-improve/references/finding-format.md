# Finding Format

**Maintainers:** Sync **severity semantics**, **Report locale**, and **Verify** rules with **`sdd-review`** `finding-format.md` when those change. **Layout need not match** delivery review.

## Report locale

Skill instructions **English**. Report prose in the **user's language** (latest user turn when unclear).

- **Format:** any clear structure — tables, prose, or lists; **no** mandatory shared markdown skeleton across skills.
- **Keep literal:** category lens ids (e.g. `architecture`); skill ids; `file:line`; git literals; **🔴/🟡/🟢** (group titles may translate).

## Opportunity scan report

**Outcome:** conversation **findings report** — not a **delivery verdict**. Routing after **Confirm:** [closing-the-loop.md](closing-the-loop.md).

**Required content** (substance, not heading names):

1. **Scope** — effort, range, categories examined; recon facts (verify command, HEAD, tree, hotspots); **not audited** with reasons.
2. **Findings** — verified items with **Evidence**; **🔴/🟡/🟢** follow-up priority (not ship gate).
3. **Coverage** — what was walked; verify rejections / sampling limits.
4. **Next stage** — one route + rationale; required even when findings empty.

Profile merges into **Scope** — no separate Profile heading. Skips in **Recon — Not audited**, not Scope. Skeleton: [profile-guide.md](profile-guide.md).

## Severity (opportunity scan)

**Follow-up priority only** — does **not** gate **`sdd-ship`**. (Delivery review uses the same labels with a different meaning — [`sdd-review` — When/Skip](../../sdd-review/SKILL.md).)

| Severity | Use when |
| --- | --- |
| **🔴 must-fix** | HIGH-confidence correctness, security, or data-loss risk; missing verification baseline; unblocker |
| **🟡 should-fix** | Maintainability or test gap on important paths; MED+ confidence |
| **🟢 suggestion** | Docs/DX polish, LOW investigate, speculative architecture, awareness |

## Per-finding fields

**Evidence** required. Optional: Impact, Confidence (✅ HIGH · ⚠️ MED · ❓ LOW), Effort (S/M/L), Risk (🔴/🟡/🟢). Category **5** may add Strength (🟢 Strong · 🟡 Worth exploring · ⚪ Speculative). Branch scope → tag `introduced` or `pre-existing`. Prioritize: impact ÷ effort, discounted by confidence and fix-risk.

## Example layout (optional, minimal)

Do not treat as mandatory. **Confirm** is a Process step after Present — not part of this skeleton.

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

Optional when user asks direction (category 9): **Direction** bullets before Next stage. Multiple follow-ups: one-line **Dependency order**. Details: [closing-the-loop.md](closing-the-loop.md).

## Verify rules

Re-read every cited location before **Present**; rejections → **Coverage — Limits**.

## Disambiguation vs **delivery review**

Normative pairing — [`sdd-review` — When/Skip](../../sdd-review/SKILL.md). Shared **🔴/🟡/🟢** labels only; **meaning differs** — opportunity-scan severities rank follow-up priority only and **do not** gate **`sdd-ship`**.
