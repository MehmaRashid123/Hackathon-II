# Research & Decisions: In-Memory Python Console Todo App

**Feature**: In-Memory Python Console Todo App (Phase I)
**Date**: 2026-01-04

## Decisions

### 1. Data Structure for Todos

- **Decision**: Use a Python `dict` mapping `id -> TodoItem` along with a separate `list` for maintaining order (or rely on Python 3.7+ dict insertion order preservation).
- **Rationale**: 
  - `dict` provides O(1) lookup for Update, Toggle, and Delete operations by ID.
  - Python 3.7+ guarantees insertion order, so a standard `dict` supports both efficient lookup and ordered listing ("Add order").
  - Simplest structure that meets performance and ordering requirements.
- **Alternatives Considered**:
  - `list` only: Simple, but requires O(N) search for every update/delete operation.
  - `sqlite3` : Violates Phase I "In-Memory Only" constraint.

### 2. ID Generation Strategy

- **Decision**: Simple auto-incrementing Integer ID counter stored in the Service class.
- **Rationale**:
  - Deterministic and readable for users (entering `1` is easier than `a1b2...`).
  - Trivial to implement in-memory.
- **Alternatives Considered**:
  - UUID: Overkill for a session-based console app; harder to type.

### 3. Command Input Style

- **Decision**: Custom REPL (Read-Eval-Print Loop) using standard `input()` parsing.
- **Rationale**:
  - Provides a "shell-like" experience requested by "Console-based" constraint.
  - Easier to test deterministically than `curses` or complex TUI libraries.
  - Keeps dependencies zero (standard lib only).
- **Alternatives Considered**:
  - `argparse`: Good for one-off commands, but a REPL is better for a session-based "application" feel.
  - `Click`/`Typer`: External dependencies prohibited in Phase I constraints.

### 4. Error Handling Approach

- **Decision**: explicit `try/except` blocks in the Service layer raising custom domain exceptions (e.g., `TodoNotFound`), caught by the CLI layer to print user-friendly messages.
- **Rationale**:
  - Separates concerns: Logic layer signals *what* went wrong; Presentation layer decides *how* to show it.
  - Testable: Unit tests can verify exceptions are raised correctly.

## Clarifications Resolved

- **Module Boundaries**: 
  - `models`: Pure data classes (`dataclass`).
  - `services`: Logic for CRUD, state management, ID generation.
  - `cli`: `input()` loop, command parsing, print statements.
