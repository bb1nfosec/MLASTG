# MLASTG Governance

This document describes how the MLSec Application Security Testing Guide
(MLASTG) is maintained, how decisions are made, and the stability guarantees
that adopters can rely on. It complements [CONTRIBUTING.md](CONTRIBUTING.md),
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md).

## Roles

- **Maintainers** — review and merge changes, cut releases, and safeguard the
  integrity of the standard. The current maintainer is [@bb1nfosec](https://github.com/bb1nfosec)
  (see [`.github/CODEOWNERS`](.github/CODEOWNERS) for path ownership).
- **Contributors** — anyone who opens an issue or pull request. See
  [CONTRIBUTING.md](CONTRIBUTING.md).

### Becoming a maintainer
Sustained, high-quality contributions (control authorship, test cases, accurate
ATLAS/framework mappings, tooling) over time may lead to an invitation from the
existing maintainers. Maintainers are added by consensus of the current
maintainers and recorded in `CODEOWNERS`.

## Decision-making

- Routine changes proceed by **lazy consensus**: a pull request that passes CI
  and review, with no unresolved objections, may be merged by a maintainer.
- Changes to the **standard's substance** — control text, IDs, levels, or
  ATLAS/framework mappings — require maintainer approval and must cite a source
  (MITRE ATLAS, NIST AI RMF, OWASP, or primary research) where applicable.
- Disagreements are resolved by discussion in the relevant issue/PR; if
  consensus cannot be reached, the maintainers make the final call.

## Versioning

MLASTG follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`)
for the repository as a whole, recorded in [CHANGELOG.md](CHANGELOG.md):

- **MAJOR** — backward-incompatible changes to control IDs, levels, or the
  `controls.json` schema.
- **MINOR** — new controls, tests, ATLAS mappings, or tooling features that are
  backward-compatible.
- **PATCH** — corrections, clarifications, and fixes that don't change meaning.

The `mlastg` CLI shares this version (see `pyproject.toml`).

## Control-ID stability policy

Adopters build assessments and tooling on control IDs, so they are treated as a
stable contract:

1. **Stable** — once a control ID (e.g. `MLASVS-LLM-001`) is published in a
   release, its identifier and core meaning do not change.
2. **No reuse** — retired IDs are never reassigned to a different control.
3. **Deprecation** — a control that is superseded is marked **Deprecated** with
   a pointer to its replacement, and kept in the documentation for at least one
   MAJOR version before removal.
4. **Additions** — new controls receive new, previously-unused IDs.
5. **Assurance levels** (L1/L2) may be raised between MAJOR versions only with a
   changelog entry; lowering a level is a MAJOR change.

The machine-readable [`controls.json`](docs/MLASVS/controls.json) is regenerated
from the documentation by
[`tools/generate_controls_register.py`](tools/generate_controls_register.py), so
the register never drifts from the standard.

## Releases

1. Update [CHANGELOG.md](CHANGELOG.md) (move items from *Unreleased* into the new
   version).
2. Ensure CI is green on `master` (test scripts, security scan, docs build).
3. Tag the release (`vMAJOR.MINOR.PATCH`) and publish a GitHub Release with the
   changelog section as notes.

## Security

Security issues are handled per [SECURITY.md](SECURITY.md) — via GitHub private
vulnerability reporting, **not** public issues.

## Licensing

Documentation and standard content are licensed under CC BY-SA 4.0
([`LICENSE`](LICENSE)); code (CLI, harnesses, tooling) under MIT
([`LICENSE-CODE`](LICENSE-CODE)).
