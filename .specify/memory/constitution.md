# OTT Platform Constitution

## Core Principles

### 1. Library‑First
All feature work starts as a self‑contained Python package (library). Libraries must be importable, have their own `pyproject.toml`, and be independently testable.

### 2. CLI Interface
Every library exposes a command‑line entry point for automation. Standard I/O contracts: `stdin/args → stdout`; errors → `stderr`. JSON output is preferred for machine consumption.

### 3. Test‑First (NON‑NEGOTIABLE)
All new code must be covered by automated tests **before** implementation. The Red‑Green‑Refactor cycle is enforced; a failing test is required to merge any change.

### 4. Integration Testing
When a library touches external resources (databases, APIs, file systems) an integration test suite must verify end‑to‑end behavior.

### 5. Observability & Versioning
- **Logging**: Structured JSON logs at INFO level, DEBUG optional via flag.
- **Versioning**: Semantic versioning `MAJOR.MINOR.PATCH`. Breaking changes require a migration plan documented in `CHANGELOG.md`.

## Additional Constraints

- **Security**: All database credentials must be loaded from environment variables; never hard‑coded.
- **Performance**: Migration scripts must complete within 2 minutes on a dev machine (see Specification Success Criteria).
- **Compliance**: Code must pass `ruff` linting and `pytest` test suite with 100 % pass rate before PR merge.

## Governance
- The Constitution supersedes all other project artefacts.
- Amendments require a dedicated PR, approval from at least two senior maintainers, and an updated `CHANGELOG.md` entry.
- A `GOVERNANCE.md` file (generated from this section) is included in every release artifact.

**Version**: 1.0.0 | **Ratified**: 2026‑03‑01 | **Last Amended**: 2026‑03‑16
