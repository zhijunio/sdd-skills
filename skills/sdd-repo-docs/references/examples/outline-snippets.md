# Outline snippets

Illustrative **heading shapes only** — generate from **target repo recon**; do not copy verbatim.

## README — app / library (excerpt)

```markdown
# Acme Widget

[![CI](https://github.com/acme/widget/actions/workflows/ci.yml/badge.svg)](https://github.com/acme/widget/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/acme/widget)](LICENSE)

CLI for transforming widget configs locally and in CI.

## Install

npm install -g @acme/widget

## Usage

acme-widget validate ./config.yaml

## Development

See AGENTS.md for build and test commands.

## License

MIT
```

## README — collection (excerpt)

```markdown
# Acme Plugin Pack

[![CI](https://github.com/acme/plugin-pack/actions/workflows/ci.yml/badge.svg)](https://github.com/acme/plugin-pack/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/acme/plugin-pack)](LICENSE)

Twelve plugins for the Acme runtime.

## Plugins

| Item | Purpose |
| --- | --- |
| `auth` | OAuth helpers |
| `cache` | Redis-backed cache |

## Install

npm install @acme/plugin-pack

## Maintainers

See AGENTS.md for maintainer and release rules.
```

## README — monorepo thin + hub (excerpt)

When `wiki/` or consumer docs own Features and quick start:

```markdown
# Acme Platform

[![CI](https://github.com/acme/platform/actions/workflows/ci.yml/badge.svg)](https://github.com/acme/platform/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/acme/platform)](LICENSE)

Composable libraries for Acme runtime extensions.

## Packages

| Path | Purpose |
| --- | --- |
| `acme-bom/` | BOM for consumers |
| `acme-core/` | Shared utilities |

## Documentation

User guides (synced to GitHub Wiki on push to `main`):

| Topic | Link |
| --- | --- |
| Overview and quick start | [wiki/Home.md](wiki/Home.md) |
| Consumer guide | [wiki/acme-bom/Consumer-Guide.md](wiki/acme-bom/Consumer-Guide.md) |

## Development

See [AGENTS.md](AGENTS.md). Local JDK: `.sdkmanrc` — run `sdk env` when using SDKMAN.

## Contributing

Implementation rules (中文): [docs/acme-conventions.md](docs/acme-conventions.md).

## License

Apache-2.0
```

Do **not** copy Features, install XML, or Group ID / BOM tables from the hub.

## README — full library / platform (canonical)

Section order from proven OSS library READMEs (e.g. microsphere-java). Fictional Acme — generate from recon:

```markdown
# Acme Java Framework

[![CI](...)] [![Codecov](...)] ![Maven Central](...) [![License](...)](LICENSE)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- …

## Introduction

Foundational library for the Acme ecosystem. …

## Features

- **Utilities** — …
- **Annotation processing** — …

## Modules

| Module | Artifact ID | Purpose |
| --- | --- | --- |
| acme-core | `acme-core` | Core utilities |

## Prerequisites

- **Java** 8+ (CI: 8, 11, 17, 21)
- **Maven** 3.6+ or `./mvnw`

## Getting Started

### Maven

… BOM + dependency XML …

### Usage Examples

… minimal snippet …

## Building from Source

Artifacts are on Maven Central — consumers need not clone. To contribute:

git clone … && ./mvnw verify

Full commands: [AGENTS.md](AGENTS.md).

## Documentation

| Resource | Link |
| --- | --- |
| User guide | [user-guide.md](user-guide.md) |

### JavaDoc

- [acme-core](https://javadoc.io/doc/io.acme/acme-core)

## Contributing

1. Fork and branch. 2. Add tests. 3. `./mvnw test`. 4. PR to `main`.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Getting Help

- [Open an issue](…) · [Discussions](…)

## Maintainers

| Name | Role |
| --- | --- |
| … | Lead |

## License

Apache-2.0
```

Use **thin** monorepo README instead when `wiki/` or equivalent hub owns Introduction / Features / Getting Started.

## AGENTS.md (excerpt)

```markdown
# Repository Guidelines

Acme monorepo. Onboarding: README.

## Context

TypeScript monorepo for Acme cloud tools. Human onboarding: README Install and Usage.

## Structure

- `packages/` — publishable libraries
- `apps/` — deployable services
- `tools/` — internal scripts

## Commands

From repo root: `pnpm install`, `pnpm test`, `pnpm lint`.

## Style

Prettier + ESLint; run `pnpm lint` before PR.

## Commit & PR

Conventional commits (`feat:`, `fix:`); PR needs green CI and summary.

## Maintainer

- Bump version in `package.json` before release tag
- Update CHANGELOG for user-visible changes

## Related

README · CONTRIBUTING
```

## CLAUDE.md (stub)

```markdown
# Claude Code

Repository agent instructions: AGENTS.md (link at repo root).

Do not duplicate content here — edit AGENTS.md only.
```
