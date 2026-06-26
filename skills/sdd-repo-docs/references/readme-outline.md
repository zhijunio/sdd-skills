# README outline

Pick **one repo shape** during recon of the **target repo** (labels below are for planning — not fixed README titles). **·** = include when applicable; **○** = optional; **—** = skip unless user asks.

Typical flow: title → **badges** (optional) → pitch → … — see [badges.md](badges.md).

Split vs AGENTS: [docs-split.md](docs-split.md). Hub rules: [docs-split.md § Existing doc hubs](docs-split.md#existing-doc-hubs-recon-first). Quality: [readme-authoring.md](readme-authoring.md).

## README depth

After picking a **shape**, choose **depth** from recon:

| Depth | When | Outline |
| --- | --- | --- |
| **Thin** | User hub (`wiki/`, `user-guide.md`, …) owns Features / quick start | Shape table below — link, do not copy hub |
| **Full** | Root README is **canonical** onboarding (no hub, or user asks for comprehensive README) | [Full library / platform](#full-library--platform-canonical-readme) section order |

Same repo may use **thin** monorepo root README + **full** app/library on a nested package README.

## full library / platform (canonical README)

Proven section flow (e.g. [microsphere-java](https://github.com/microsphere-projects/microsphere-java)) when README carries full human onboarding — **monorepo** or **app/library** shape. Use these **`##` titles** when recon fits; adapt labels (`Modules` vs `Packages`, `Getting Started` vs `Install`).

| Order | Heading | Notes |
| --- | --- | --- |
| 1 | **`#` Title** | Project name as H1 |
| 2 | **Badges** ○ | [badges.md](badges.md) — CI, license, registry, coverage when recon confirms |
| 3 | **Table of contents** ○ | Anchor list when ~8+ sections below |
| 4 | **`##` Introduction** | 1–2 paragraphs: purpose, ecosystem link, who it is for — expands one-line pitch |
| 5 | **`##` Features** | Short capability bullets |
| 6 | **`##` Modules** | Reactor/module table — use **`Packages`** when recon prefers; optional **artifact ID** column (Maven/BOM) |
| 7 | **`##` Prerequisites** | Runtime from CI or manifest (Node, Python, Java, Go, …); package manager + wrapper when present (`mvnw`, `pnpm`, `uv`, …); **Docker** ○ when recon shows `Dockerfile` / compose as primary dev path |
| 8 | **`##` Getting Started** | Consumer onboarding from recon — **`###` Install** / **`###` Maven** / **`###` npm** / **`###` pip** / **`###` Docker`** as applicable; **`###` Usage Examples** ○ — link user guide for long tutorials |
| 9 | **`##` Building from Source** | Lead with *consumers need not clone* when registry artifacts exist; clone + `./mvnw` / platform commands; detail → **AGENTS.md** |
| 10 | **`##` Documentation** | `Resource` \| `Link` table; optional **`###` JavaDoc** / release-notes link lists |
| 11 | **`##` Contributing** | Numbered quick steps ○ + link `CONTRIBUTING.md` / conventions / **AGENTS.md** |
| 12 | **`##` Getting Help** | Issues, Discussions, support — links from recon |
| 13 | **`##` Maintainers** ○ | Table or bullets when public contacts matter; else one line → **AGENTS.md** |
| 14 | **`##` License** | SPDX or link |

**Hub present:** do **not** use full depth at root — switch to **thin** monorepo README; keep this outline for nested packages or when hub is retired.

**AGENTS split:** **Building from Source** commands canonical in **AGENTS**; README keeps consumer-first disclaimer + minimal clone/build. **Maintainer** merge checklist stays in **AGENTS**, not README **Maintainers** essay.

## app / library

Single app, CLI, or publishable package. **Full depth:** use [full library / platform](#full-library--platform-canonical-readme) headings (`Introduction`, `Getting Started`, …) instead of the modular rows below.

| Heading | Notes |
| --- | --- |
| **`#` Title** | Project name as H1 |
| **Badges** ○ | Under title — CI, license, registry version when recon confirms — [badges.md](badges.md) |
| *(pitch)* | One-line purpose directly under badges or title |
| **Table of contents** ○ | Anchor list — **only** when README is long and **not** thin/hub mode (~8+ sections); skip for monorepo thin README |
| **`##` Features** ○ | Short bullets — **skip if hub covers** |
| **`##` Prerequisites** ○ | JDK/runtime from CI matrix; package manager + wrapper (`mvnw`, `pnpm`, …) from recon — **skip if hub covers** |
| **`##` Install** | Copy-paste; link advanced setup — **skip if hub covers**; list **each** package manager recon supports (Maven + Gradle, npm + pnpm, …) |
| **`##` Usage** | Minimal working example — **skip if hub covers** |
| **`##` Configuration** ○ | Env var **names** only |
| **`##` API** ○ | Or link `docs/` |
| **`##` Development** | One line → root `AGENTS.md`; when artifacts are on a public registry, one line that consumers need not build from source — clone/build details in AGENTS |
| **`##` Documentation** ○ | `Resource` \| `Link` table to user guide / wiki; optional **JavaDoc** or API doc link list when `javadoc.io` or equivalent exists — **skip body copy from hub** |
| **`##` Getting Help** ○ | Issues, Discussions, support channels — links only when recon finds templates or enabled features |
| **`##` Contributing** | One line → `AGENTS.md` or `CONTRIBUTING.md` or conventions doc |
| **`##` License** | SPDX or link |

## collection

Many similar items in one repo (packages, plugins, modules, rules, …).

| Heading | Notes |
| --- | --- |
| **`#` Title** | Collection name as H1 |
| **Badges** ○ | [badges.md](badges.md) |
| *(pitch)* | Item count + one-line purpose |
| **`##` Design** ○ | Short principles; long rationale → link `docs/` |
| **`##` Workflow** ○ | Diagram when helpful |
| **`##` Table section** | **One canonical table** — natural heading from recon (`Skills`, `Packages`, …) |
| **`##` Install** | Installer command — **skip if hub covers** |
| **`##` Artifacts** ○ | Default paths or outputs for users |
| **`##` Changelog** ○ | Link `CHANGELOG.md` |
| **`##` Maintainers** | Link `AGENTS.md` |
| **`##` License** | |

Do not duplicate AGENTS **Commands** or **Maintainer** detail in README.

## monorepo (root)

| Heading | Notes |
| --- | --- |
| **`#` Title** | Monorepo name as H1 |
| **Badges** ○ | CI + license common — [badges.md](badges.md) |
| *(pitch)* | One-line purpose |
| **`##` Prerequisites** ○ | JDK/runtime from CI; build tool + wrapper — one line or bullets; **skip if hub covers** |
| **`##` Packages** | Table: path, purpose, package README link — optional **artifact ID** column for Maven/BOM when hub lacks reactor map |
| **`##` Documentation** | **Required when a user hub exists** — `Topic` \| `Link` table to wiki / docs; optional **JavaDoc** / **Release notes** sub-lists when recon finds `javadoc.io`, `release-notes.md`, etc. — do **not** duplicate Features or Install |
| **`##` Install** ○ | Workspace bootstrap — **skip if wiki hub covers consumer install**; multi package manager only when recon supports each |
| **`##` Development** ○ | One line → `AGENTS.md`; optional local toolchain hint (`.sdkmanrc`, `.nvmrc`, `.tool-versions`, …); when published on a registry, note that consumers need not clone — build commands stay in AGENTS |
| **`##` Getting Help** ○ | Issues / Discussions links when recon finds GitHub templates or community channels |
| **`##` Changelog** ○ | Link `CHANGELOG.md` |
| **`##` Contributing** | Conventions doc or `AGENTS.md` — label link when hub locale differs (e.g. `(中文)`) |
| **`##` License** | Note per-package if needed |

Nested package README: **app/library** or **collection** shape. Commands stay in package AGENTS, not root README.

## docs-only

| Heading | Notes |
| --- | --- |
| **`#` Title** | Site or corpus name as H1 |
| **Badges** ○ | CI / license if present — [badges.md](badges.md) |
| *(pitch)* | One-line purpose |
| **`##` Structure** | Directory map |
| **`##` Preview** ○ | Local build/serve |
| **`##` Contributing** | Link `AGENTS.md` |
| **`##` License** | |

## Length

Prefer scannable tables and bullets. Collection READMEs may be longer when the item table is the main content — still dedup against AGENTS and doc hubs.

**Thin README** (user hub owns onboarding): keep root README short — badges, pitch, Packages (if needed), Documentation table, pointers; no TOC, no inline usage essays. See [README depth](#readme-depth).

**Full README** (canonical onboarding): follow [full library / platform](#full-library--platform-canonical-readme) section order; **Table of contents** when section count makes scrolling costly.

## Picking a shape

| If the repo… | Shape | Typical depth |
| --- | --- | --- |
| Ships one installable app, CLI, or library | **app / library** | **Full** when README is only onboarding doc; **thin** when `docs/` hub exists |
| Ships many peer items under one installer or repo | **collection** | Usually **full** at root (item table is the README) |
| Is a workspace of multiple packages | **monorepo** (root + per-package README) | **Full** or **thin** at root — see hub rule |
| Is mostly documentation or static content | **docs-only** | N/A |
| Is a **monorepo + published platform** (BOM, starters) with `wiki/` or consumer docs | **monorepo** | **Thin** root + hub links — do not fork quick start |

When recon spans two shapes (e.g. app + heavy `docs/`), start **app / library** and pick **thin** or **full** depth — do not invent a sixth template beyond shapes + depth.

## Project type → shape + depth

Quick routing after recon — always confirm with tree and hubs:

| Project type | Shape | Depth | Notes |
| --- | --- | --- | --- |
| npm/PyPI/crates.io library, CLI | **app / library** | **Full** if README is canonical; **thin** if `docs/` / site owns onboarding | Registry badge when published |
| Spring/Maven/Gradle platform, BOM | **monorepo** or **app / library** | **Thin** if `wiki/` hub; **full** if README canonical (e.g. microsphere-java) | `Modules` / artifact ID when Maven |
| pnpm/turbo/Cargo workspace | **monorepo** | **Thin** or **full** at root — hub rule | **Packages** table; workspace install in Getting Started or **Install** |
| Skills, plugins, rules pack | **collection** | Usually **full** (table is the product) | Natural table heading from recon |
| Static site, ADR corpus, book repo | **docs-only** | N/A | Preview = local serve when recon finds build cmd |
| Web/mobile app (single package) | **app / library** | **Full** common | **Configuration** = env var names; deploy ○ |
| Infra (Terraform, K8s manifests) | **app / library** or **docs-only** | **Full** or **thin** | No fake install — link modules + `AGENTS` commands |
| Internal tool, no publish | **app / library** | **Full** or minimal | Skip registry badges; Getting Help ○ |
| Closed / non-GitHub git host | Any | Any | Badges from that host's CI or skip — [badges.md](badges.md) |

## Adaptation

Omit empty headings; state omissions in **Present**. Never paste AGENTS or hub docs verbatim into README. Authoring bounds: [readme-authoring.md](readme-authoring.md).
