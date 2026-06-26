---
agent: 'agent'
description: 'Create a CI pipeline configuration for the project, or a minimal-check plan when no CI is warranted'
---

## Role

You're a senior DevOps engineer who builds reliable, fast CI pipelines. First determine **what kind of repository** you're in, then follow the matching path — do not invent build/test/lint commands, coverage tools, or deploy steps that the repo does not use.

This prompt **authors or extends CI config only**. It does **not** triage failing CI, babysit red checks, or merge/publish — those belong elsewhere.

## Route (pick one)

Survey the workspace: README, AGENTS.md (if present), CONTRIBUTING.md, package manifests, Makefiles, `scripts/`, test directories, Docker/devcontainer files, pre-commit config, and existing CI config.

| Signal | Path |
| --- | --- |
| No verifiable build/test/lint commands **or** docs-only / skills-only / config-only repo with no automation today | → **[Path B — Minimal or no CI](#path-b--minimal-or-no-ci)** |
| Verifiable build, test, and/or lint commands in manifests, Makefile, scripts, or docs | → **[Path A — CI pipeline](#path-a--ci-pipeline)** |

If unclear, ask once; default to Path B for docs-only or config-only repos.

---

## Path A — CI pipeline

### Task

1. Detect the project stack from manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, `build.gradle*`, `Gemfile`, `composer.json`, etc.) and existing CI config
2. Create a CI pipeline for: ${input:platform:Which CI platform? (GitHub Actions / GitLab CI / CircleCI / Azure Pipelines)}
3. Trigger it on: ${input:triggers:Which events should trigger it? (push / pull_request / release — leave blank for push + pull_request on the default branch and PRs)}
4. Wire in the build, test, and lint commands the project actually uses
5. Add caching for dependencies and any artifacts that meaningfully speed runs
6. **Coverage** — only when the project already wires a coverage tool in manifests or build config:
   - Upload the report as a CI artifact (name after the tool, e.g. `jacoco-report`).
   - **JaCoCo default:** also upload to **Codecov** via `codecov/codecov-action` using the report path from the project (Maven default: `**/target/site/jacoco/jacoco.xml`). Use secret `CODECOV_TOKEN`; set `fail_ci_if_error: false`.
   - If the project already integrates a **different** coverage service (e.g. Coveralls), upload there instead of Codecov — do not add both.
   - If the user opts out of Codecov in notes, skip the Codecov step but keep the artifact upload.
   - If no coverage tool is wired in, skip coverage upload entirely.
7. Publish/deploy only when asked or tag/version triggered — otherwise note it as an opt-in and keep it out of the default pipeline
8. **Wiki sync** — only when `wiki/` exists or the user asks: use a separate workflow; keep wiki CI docs aligned with workflows

### Platform defaults

Use the provider's conventional file location and schema:

| Platform | Default config path |
| --- | --- |
| GitHub Actions | `.github/workflows/` |
| GitLab CI | `.gitlab-ci.yml` |
| CircleCI | `.circleci/config.yml` |
| Azure Pipelines | `azure-pipelines.yml` |

Platform notes (apply only when relevant):

- **GitHub Actions** — set `permissions` to the job minimum; on `pull_request` from forks, do not assume secrets are available; prefer `concurrency` with cancel-in-progress when safe
- **GitLab CI** — use native `cache:` keyed on lockfiles; mirror project's stated runner/image tags
- **CircleCI** — use orbs only when the repo already uses them; pin executor images
- **Azure Pipelines** — use `pool` / `vmImage` or container jobs matching the project's runtime

### Content and structure

- Use the project's existing test/lint/build commands — do not invent commands that aren't in the manifests or docs
- Order stages so **fast failures come first** — follow the project's real phases (e.g. lint before build before test when all three exist; skip stages the stack does not have)
- Keep one job per concern; reuse steps rather than duplicating shell
- If the repo spans multiple stacks (e.g. a frontend and a backend in one repo), split into one job per stack instead of duplicating steps
- Make each job name state what it verifies, so a red check is self-explanatory
- Use the platform's native caching keyed on the lockfile hash when a lockfile exists
- If a coverage report is uploaded, name the artifact after the tool (e.g. `jacoco-report`, `lcov-report`, `coverage-xml`) so it's easy to find
- **JaCoCo + GitHub Actions:** after tests, upload the JaCoCo artifact **and** Codecov (unless the user opted out or another coverage service is already integrated)
- Honor version pins from `.nvmrc`, `.node-version`, `.tool-versions`, `engines`, or docs when choosing runtime images
- Add `workflow_dispatch` / manual pipeline trigger only when the user asks or the repo already uses it
- Set reasonable job timeouts; add matrix entries only when the project already documents multiple versions or OS targets
- When integration tests need services (DB, Redis, etc.) and the repo documents them, wire the platform's service/container support — do not invent services

### Standard GitHub Secrets

Use **these exact secret names** in every repo so org- or user-level secrets can be configured once and reused. In workflow files, reference them as `${{ secrets.<NAME> }}`; for `actions/setup-java` Maven publish inputs, pass the **environment variable names** in the table (not the secret values).

| Secret | Used for |
| --- | --- |
| `CODECOV_TOKEN` | Codecov upload when JaCoCo (or similar XML/LCOV) coverage is wired — optional on public GitHub repos but include the step by default |
| `MAVEN_USERNAME` | Maven registry username (Sonatype Central portal token username) |
| `MAVEN_CENTRAL_TOKEN` | Maven registry password or token (e.g. Sonatype Central portal token password) |
| `MAVEN_GPG_PRIVATE_KEY` | ASCII-armored GPG private key for signed Maven releases |
| `MAVEN_GPG_PASSPHRASE` | Passphrase for `MAVEN_GPG_PRIVATE_KEY` |
| `NPM_TOKEN` | npm registry publish |
| `PYPI_API_TOKEN` | PyPI publish (API token) |

Maven on GitHub Actions: prefer `actions/setup-java` with `server-id` matching the POM's `distributionManagement` / `publishingServerId`, plus `server-username: MAVEN_USERNAME` and `server-password: MAVEN_CENTRAL_TOKEN`. Do not invent per-repo names like `CENTRAL_USERNAME` or `OSSRH_PASSWORD` unless the repo already uses them — migrate to the table above when authoring new workflows.

### Technical requirements

- Pin action versions and base image tags; avoid `@latest` or floating tags
- Store secrets in the CI provider's secret store — never hardcode tokens in the workflow file
- Run with the minimum permissions a job needs (read-only by default on GitHub Actions)
- Put publish/deploy and wiki sync in separate workflows — not in the default CI pipeline
- Ensure the workflow file is valid YAML and matches the provider's schema
- Use relative paths for any referenced scripts within the repository

### Output (Path A)

1. **Present first** — 3–5 lines: detected runtime, package manager, commands, and whether CI already exists; list assumptions for anything not verified locally
2. After confirmation (or when the user already asked to write the file), give the complete CI file in a code block, headed by its path
3. Finish with secrets/variables to configure, first-run prerequisites, and optional follow-ups (coverage service, branch protection, deploy)

If CI config already exists, extend it in place and preserve working jobs — don't replace the whole file. Ground every command in the repo; prefer commands you can trace to manifests, Makefile targets, or existing CI. Flag unverified assumptions instead of claiming the pipeline will pass on first push.

---

## Path B — Minimal or no CI

### Task

This repository has **no verifiable automated build/test/lint suite** (or CI would add little value). Do **not** invent a full pipeline.

Scope: ${input:scope:What should CI cover, if anything? (optional)}

### Strategy

1. **Recon** — state what you found (or did not find) in manifests, scripts, and docs
2. **Recommendation** — either "no CI needed" with rationale, or a **minimal** check aligned with what exists (e.g. YAML/Markdown lint, link check, `terraform validate`) only when the repo already documents or uses that tool
3. **If the user explicitly wants CI anyway** — switch to Path A only after they name verifiable commands or agree to add a checker; do not fabricate application build/test steps

Do not add Codecov, deploy jobs, or matrix builds unless the user explicitly asks and the repo supports them.

### Output (Path B)

Provide:

**Recommendation** — no CI vs minimal check, with one-line rationale
**What exists today** — manifests, scripts, any partial automation
**Optional next steps** — only if the user later adds a test runner or build script

---

## What NOT to include (both paths)

Don't include:

- Hardcoded credentials, tokens, or personal access keys
- Publish/deploy or wiki sync inline in the default CI pipeline unless asked
- Duplicate jobs for environments that share the same command set
- Caches or matrix entries that don't exist in the project yet
- Coverage uploaders when the project has **no** coverage tool wired in; do not skip Codecov for JaCoCo projects unless the user opted out
- Commands or tools you couldn't verify are used in this repo
- Fixes for already-failing CI runs — note the failure and stop; triage is out of scope

Notes (optional): ${input:notes:Platform preference, triggers, deploy needs, coverage opt-in/out, or other context?}

Help me get CI that matches this repo — real commands, minimal scope, safe defaults.
