# SDD Skills

Lightweight, platform-neutral skills for spec-driven development.

The repository keeps the useful discipline of SDD without turning it into a
state machine, project manager, or Git workflow framework.

## Workflow

```text
using-sdd
  |
sdd-grill (optional)
  |
sdd-spec -> user approval
  |
sdd-plan -> user approval
  |
sdd-build
  |
sdd-review
  | findings: return to sdd-build
  | pass
sdd-ship
```

Each skill stops after its own output. Skills recommend the next stage but do
not invoke it automatically.

## Skills

| Skill | Use when |
| --- | --- |
| `using-sdd` | The correct SDD stage is unclear |
| `sdd-grill` | Goals, boundaries, trade-offs, or plan/design need decisions; user says "grill me" |
| `sdd-spec` | A durable behavior contract and acceptance criteria are needed |
| `sdd-plan` | An approved spec needs testable vertical slices |
| `sdd-build` | An approved plan is ready for test-first implementation |
| `sdd-review` | A defined diff needs independent read-only review |
| `sdd-ship` | A reviewed increment needs final acceptance evidence |

All seven skills can be installed independently. Some require artifacts rather
than other skills: `sdd-plan` needs an approved spec, `sdd-build` needs a spec
and plan, and `sdd-ship` needs a passed review.

## Quick routing

| If… | Start with |
| --- | --- |
| Unsure which stage fits | `using-sdd` |
| Goal, boundaries, trade-offs, or plan/design still open | `sdd-grill` |
| No approved spec yet | `sdd-spec` |
| Spec approved, no plan | `sdd-plan` |
| Plan approved, coding | `sdd-build` |
| Ready for read-only review | `sdd-review` |
| Review clear, need fresh verification | `sdd-ship` |

Full examples and edge cases: [skills/using-sdd/SKILL.md](skills/using-sdd/SKILL.md#routing-examples).

## Installation

Install with the skills CLI:

```bash
npx skills@latest add zhijunio/sdd-skills
```

Select the full set or individual skills in the installer.

For agents without installer support, copy the required `skills/<name>/`
directory into the agent's skills directory.

## Minimal Artifacts

Only two documents are required by default:

```text
docs/sdd/YYYY-MM-DD-<topic>-spec.md
docs/sdd/YYYY-MM-DD-<topic>-plan.md
```

Clarify, grill, and review documents are optional. The workflow does not require
status fields or a persistent active-increment file.

Cross-feature architecture decisions may live in `docs/adr/0001-short-title.md`
and be linked from spec **Related ADRs**; that layout is optional and not part
of the default two-document workflow.

## Review Scope

`sdd-review` can run with only a diff. A spec and plan improve traceability but
are optional. It never assumes `main`; the user-specified range or actual task
scope takes precedence.

## Changelog

`sdd-ship` may update an existing CHANGELOG when repository convention and
user-visible impact require it. It does not create a new format or release tool
without explicit instruction.

## Validation

```bash
python3 tests/check.py
```

The check validates the skill directories, frontmatter, required sections,
templates, and local links without third-party Python dependencies.

## Design

- No commands, hooks, personas, or platform-specific manifests.
- No runtime status machine.
- No automatic stage chaining.
- No required worktrees or per-slice commits.
- Spec and plan require explicit user approval.
- Review stays read-only.
- Ship verifies; it does not silently publish.

## Sources

The skills synthesize ideas from
[mattpocock/skills](https://github.com/mattpocock/skills),
[obra/superpowers](https://github.com/obra/superpowers), and
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).
See [SOURCES.md](SOURCES.md) and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

MIT

