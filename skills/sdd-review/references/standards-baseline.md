# Standards baseline

Repo-documented standards override this list. Paste [smell-baseline.md](smell-baseline.md) into the Standards sub-agent (smells belong under **Structure**).

| Dimension | Look for |
| --- | --- |
| **Correctness** | Real inputs, edge cases, failures, state, lifecycle. **When the diff has signals:** security, concurrency, data/migration, performance. |
| **Structure** | Boundaries, dependency direction, half migrations, dead code, parallel APIs, large duplication — **and all Fowler smells** in [smell-baseline.md](smell-baseline.md). |
| **Verification** | Behavior-focused tests cover the change; CI/local proof; prefer recorded close-out or suite evidence when present. |
| **Traceability** | Spec/plan/CHANGELOG/links, public APIs, config keys, package names, migration paths, install/setup, tooling, DX — still match the tree. |

**Binding:** documented-standard breaches may be hard; baseline dimensions and Fowler smells are judgement calls unless they also break a documented standard or an `AC-n`. Skip tooling-enforced style. Smells alone default to 🟢/🟡 — not 🔴 without AC or a documented hard rule.
