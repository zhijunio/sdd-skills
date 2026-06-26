---
name: sdd-ci
description: Use when creating or extending CI pipeline config for a project—build, test, lint, coverage upload. Not triaging failing CI, babysitting red checks, merge, or publish unless the user asks separately.
---

# sdd-ci

## Role

You're a senior DevOps engineer who builds reliable, fast CI pipelines. First determine **what kind of repository** you're in, then follow the matching path — do not invent build/test/lint commands, coverage tools, or deploy steps that the repo does not use.

Authors or extends CI config only. Does not triage failing CI, babysit red checks, or merge/publish.

Write workflow files only when the user confirms. Default: present the plan and draft in chat.

## Route (pick one)

Survey the workspace: README, AGENTS.md (if present), CONTRIBUTING, package manifests, Makefiles, `scripts/`, test directories, Docker/devcontainer files, pre-commit config, and existing CI config.

| Signal | Path |
| --- | --- |
| No verifiable build/test/lint commands **or** docs-only / skills-only / config-only repo with no automation today | **Minimal or no CI** (below) |
| Verifiable build, test, and/or lint commands in manifests, Makefile, scripts, or docs | **CI pipeline** (below) |

If unclear, ask once; default to minimal or no CI for docs-only or config-only repos.

## CI pipeline

### Task

1. Detect the project stack from manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, `build.gradle*`, `Gemfile`, `composer.json`, etc.) and existing CI config
2. Create a CI pipeline — default **GitHub Actions** unless the user or existing CI specifies another platform
3. Trigger on **push to the default branch and pull_request** unless the user specifies otherwise
4. Wire in the build, test, and lint commands the project actually uses
5. Add caching for dependencies and any artifacts that meaningfully speed runs
6. **Coverage** — only when the project already wires a coverage tool in manifests or build config (see Coverage and the matching Stack conventions subsection)
7. Apply **Stack conventions** for each detected stack
8. Publish/deploy only when asked or tag/version triggered — otherwise note it as an opt-in and keep it out of the default pipeline
9. **Wiki sync** — only when `wiki/` exists or the user asks: use a separate workflow; keep wiki CI docs aligned with workflows

If CI config already exists, extend it in place and preserve working jobs — do not replace the whole file. Ground every command in the repo; flag unverified assumptions instead of claiming the pipeline will pass on first push.

### Platform defaults

| Platform | Config path |
| --- | --- |
| GitHub Actions | `.github/workflows/` |
| GitLab CI | `.gitlab-ci.yml` |
| CircleCI | `.circleci/config.yml` |
| Azure Pipelines | `azure-pipelines.yml` |

Platform notes (apply only when relevant):

- **GitHub Actions** — minimum `permissions`; on `pull_request` from forks, do not assume secrets are available; prefer `concurrency` with cancel-in-progress when safe; pin action versions — no `@latest`
- **GitLab CI** — native `cache:` keyed on lockfiles; mirror project's stated runner/image tags
- **CircleCI** — orbs only when the repo already uses them; pin executor images
- **Azure Pipelines** — `pool` / `vmImage` or container jobs matching the project's runtime

### Content and structure

Universal rules — stack-specific flags and paths live under **Stack conventions**.

- Use the project's existing test/lint/build commands — do not invent commands that aren't in the manifests or docs
- Order stages so **fast failures come first** — lint before build before test when all three exist; skip stages the stack lacks
- Keep one job per concern; reuse steps rather than duplicating shell
- If the repo spans multiple stacks, split into one job per stack
- Make each job name state what it verifies
- Use the platform's native caching keyed on the lockfile hash when a lockfile exists
- Honor version pins from `.nvmrc`, `.node-version`, `.tool-versions`, `engines`, or docs when choosing runtime images
- Add `workflow_dispatch` only when the user asks or the repo already uses it
- Set reasonable job timeouts; add matrix entries only when the project documents multiple versions or OS targets
- When integration tests need services the repo documents, wire the platform's service/container support — do not invent services

### Coverage

Apply only when a coverage tool is already wired in manifests or build config.

- Upload the report as a CI artifact — name after the tool (e.g. `jacoco-report`, `lcov-report`, `coverage-xml`)
- Default for **JaCoCo on GitHub Actions:** also upload to **Codecov** via `codecov/codecov-action`; secret `CODECOV_TOKEN`; `fail_ci_if_error: false` — report paths per **Maven** when applicable
- If the project already integrates a **different** coverage service (e.g. Coveralls), upload there instead of Codecov — do not add both
- If the user opts out of Codecov, skip the Codecov step but keep the artifact upload
- If no coverage tool is wired in, skip coverage upload entirely

### Stack conventions

Apply **only** subsections that match the detected stack. Do not apply Maven rules to a Node-only repo.

#### Maven

When `pom.xml`, `mvnw`, or existing CI uses Maven:

- Every `./mvnw` / `mvn` invocation in CI and publish workflows: **`-B -ntp`** before goals and profiles — e.g. `./mvnw -B -ntp validate`, `./mvnw -B -ntp -Pcoverage verify`, `./mvnw -B -ntp -Prelease deploy`
- Prefer `./mvnw` when the wrapper exists
- **Publish (GitHub Actions):** `actions/setup-java` with `server-id` matching the POM's `distributionManagement` / `publishingServerId`; `server-username: MAVEN_USERNAME`, `server-password: MAVEN_CENTRAL_TOKEN`
- **JaCoCo + Codecov:** `**/target/site/jacoco/jacoco.xml` (unit) and `**/target/site/jacoco-it/jacoco.xml` (Failsafe IT) when both exist

#### Gradle

When `build.gradle*`, `gradlew`, or existing CI uses Gradle:

- Prefer `./gradlew` when the wrapper exists
- CI invocations: **`--no-daemon`**; add **`--console=plain`** when logs should stay readable in CI
- Cache `.gradle/` keyed on wrapper and dependency lockfiles when present

#### Node.js

When `package.json` and npm/pnpm/yarn (or existing CI uses them):

- Lockfile-driven install — `npm ci`, `pnpm install --frozen-lockfile`, or `yarn install --immutable` — matching the repo's package manager; do not invent a manager the repo does not use
- Honor `.nvmrc`, `.node-version`, or `engines` for the runtime image
- Cache dependency dirs keyed on the lockfile the repo actually commits

#### Python

When `pyproject.toml`, `requirements.txt`, `Pipfile`, or existing CI uses Python tooling:

- Use the project's documented runner (`pytest`, `tox`, `nox`, `uv run`, etc.) — do not swap tools
- Pin Python from `.python-version`, `requires-python`, or docs when stated
- Cache virtualenv / pip / uv store keyed on lockfiles when present

#### Go

When `go.mod` or existing CI uses Go:

- **`go test ./...`** (or the repo's documented package scope) with **`-race`** only when the project already uses it
- Cache module download dir keyed on `go.sum`

Add new subsections here when a stack gains a verified, repeatable CI convention — keep universal rules out of this section.

### Standard GitHub Secrets

Use **these exact secret names** so org- or repo-level secrets can be reused. Reference as `${{ secrets.<NAME> }}`; for `actions/setup-java` Maven publish, pass the **environment variable names** below (not the secret values).

| Secret | Used for |
| --- | --- |
| `CODECOV_TOKEN` | Codecov upload when JaCoCo (or similar XML/LCOV) coverage is wired |
| `MAVEN_USERNAME` | Maven registry username (Sonatype Central portal token username) |
| `MAVEN_CENTRAL_TOKEN` | Maven registry password or token |
| `MAVEN_GPG_PRIVATE_KEY` | ASCII-armored GPG private key for signed Maven releases |
| `MAVEN_GPG_PASSPHRASE` | Passphrase for `MAVEN_GPG_PRIVATE_KEY` |
| `NPM_TOKEN` | npm registry publish |
| `PYPI_API_TOKEN` | PyPI publish (API token) |

Do not invent per-repo secret names like `CENTRAL_USERNAME` or `OSSRH_PASSWORD` unless the repo already uses them — migrate to the table above when authoring new workflows.

### Technical requirements

- Pin action versions and base image tags; avoid `@latest` or floating tags
- Store secrets in the CI provider's secret store — never hardcode tokens in the workflow file
- Run with the minimum permissions a job needs (read-only by default on GitHub Actions)
- Put publish/deploy and wiki sync in separate workflows — not in the default CI pipeline
- Ensure valid YAML matching the provider's schema
- Use relative paths for scripts within the repository

### Output

1. **Present first** — detected runtime, package manager, commands, existing CI, assumptions
2. After confirm — complete workflow file(s) with paths
3. Secrets to configure, first-run prerequisites, optional follow-ups (coverage service, branch protection, deploy)

## Minimal or no CI

When there is **no verifiable automated build/test/lint suite** (or CI would add little value), do **not** invent a full pipeline.

1. **Recon** — state what you found (or did not find) in manifests, scripts, and docs
2. **Recommendation** — "no CI needed" with rationale, or a **minimal** check aligned with what exists (e.g. YAML/Markdown lint, link check, `terraform validate`) only when the repo already documents or uses that tool
3. **If the user explicitly wants CI anyway** — switch to CI pipeline only after they name verifiable commands or agree to add a checker

Do not add Codecov, deploy jobs, or matrix builds unless the user explicitly asks and the repo supports them.

**Output:** recommendation; what exists today; optional next steps if a test runner appears later.

## What NOT to do

Do not:

- Hardcode credentials, tokens, or personal access keys
- Publish/deploy or wiki sync inline in the default CI pipeline unless asked
- Duplicate jobs for environments that share the same command set
- Add caches or matrix entries that don't exist in the project yet
- Add coverage upload when no coverage tool is wired in; do not skip Codecov for JaCoCo projects unless the user opted out
- Use commands or tools you couldn't verify exist in this repo
- Apply stack conventions for a stack the repo does not use (e.g. Maven `-B -ntp` on a Node-only repo)
- Triage or fix already-failing CI in this session

Help the user get CI that matches the repo — real commands, minimal scope, safe defaults.
