# Implementation Plan: In-Memory Python Console Todo App (Phase I)

**Branch**: `001-console-todo-mvp` | **Date**: 2026-01-04 | **Spec**: [specs/001-console-todo-mvp/spec.md](spec.md)
**Input**: Feature specification from `specs/001-console-todo-mvp/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a Phase I compliant, in-memory, console-based Todo application in Python. This system will serve as the foundational logic for future web, AI, and cloud evolutions. It implements core CRUD operations (Add, List, Update, Toggle, Delete) without any external persistence, strictly adhering to the "Simplicity First" and "Explicit Phase Constraints" principles.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard Library only (e.g., `dataclasses`, `typing`, `sys`, `cmd` or `argparse`)
**Storage**: In-Memory (Python `list` or `dict` structures)
**Testing**: `pytest` (standard for Python ecosystem)
**Target Platform**: CLI / Console (Cross-platform)
**Project Type**: Single project (CLI tool)
**Performance Goals**: Startup < 0.5s, Instant response to commands
**Constraints**: 
- NO databases (SQL/NoSQL)
- NO file I/O for persistence
- NO external API calls
- Pure function logic separate from I/O

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Simplicity First**: Minimal abstractions? Yes, using simple classes/functions.
- [x] **Separation of Concerns**: Business logic separated from CLI? Yes, will design `TodoService` vs `TodoCLI`.
- [x] **Deterministic**: Predictable inputs/outputs? Yes, standard CLI loop.
- [x] **Incremental**: Forward compatible? Yes, logic reusable in Phase II.
- [x] **Phase I Constraints**: In-memory only? Yes. Console only? Yes.
- [x] **Development Standards**: Type hints? Yes. Docstrings? Yes.

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo-mvp/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/              # Data structures (TodoItem)
├── services/            # Business logic (TodoService)
└── cli/                 # User interaction (main.py / REPL)

tests/
├── unit/                # Logic tests
└── integration/         # CLI flow tests (simulated)
```

**Structure Decision**: Single project structure chosen. It perfectly fits the Phase I "Simplicity First" principle while establishing the `models/` vs `services/` separation required for Phase II reuse.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
