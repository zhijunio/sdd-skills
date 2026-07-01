# Pipeline step notes

Referenced by [SKILL.md](../SKILL.md) step 5.

| Step | Notes |
| --- | --- |
| **Push** | Present remote, branch, `git push -u origin <branch>`; "push only" must not auto-run PR/merge/tag/release |
| **Open PR** | Title/body from `[Unreleased]` or recent commits; no `gh` → present full `gh pr create` command; label **step not executed** |
| **CI display** | Display only; failed/pending → default do not merge unless user accepts risk |
| **Merge** | Separate confirm; present merge method and target branch |
| **Sync default branch** | After merge, `checkout` + `pull` `main` or `master` before tag |
| **Tag** | Version must be explicit: user states `vX.Y.Z`, `CHANGELOG` draft, semver suggestion from `git describe --tags --abbrev=0` with confirm, or stop; tag-only on topic branch without merge → present explicitly; optional CHANGELOG promotion — edit only after confirm |
| **GitHub Release** | Notes from CHANGELOG for that version; no `gh` → command only |
| **README pin** | Only when repo documents a version pin and user confirms |

**No `gh` degradation:** do not claim a PR or release was created — present copyable commands.
