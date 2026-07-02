---
agent: 'agent'
description: 'Stress-test a plan or design through focused interview'
---

I want to stress-test a plan or design before building. Interview me one question at a time.

Plan or design: ${input:subject:What plan, feature, or design should we grill?}
Context (optional): ${input:context:Any constraints, deadline, or background?}

Walk the decision tree one branch at a time. For each question:

* Ask **one question only**; wait for my answer before the next
* Include your **recommended answer**
* If the answer is in the codebase, explore the repository instead of asking me

When we reach shared understanding (or I stop), summarize in this order:

* **Decisions** — choices we agreed on
* **Rejected** — options ruled out and why
* **Boundaries** — scope in / out, constraints, non-goals
* **Open** — unresolved items for a later pass

Ground recommendations in this repository when relevant. Do not write specs, plans, or product code in this session.
