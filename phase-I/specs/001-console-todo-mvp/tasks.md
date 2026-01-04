# Tasks: In-Memory Python Console Todo App (Phase I)

**Input**: Design documents from `specs/001-console-todo-mvp/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Tests**: Tests are included to verify logic and CLI behavior manually or via unit tests where specified.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure (src/models, src/services, src/cli, tests/unit)
- [x] T002 Initialize Python project with `uv init` (or standard `pyproject.toml`) in root
- [x] T003 [P] Configure `ruff` for linting in `pyproject.toml` or `ruff.toml`

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Define `TodoItem` dataclass in `src/models/todo.py`
- [x] T005 [P] Define custom exceptions (e.g. `TodoNotFound`) in `src/services/exceptions.py`
- [x] T006 Initialize `TodoService` class with empty state in `src/services/todo_service.py`
- [x] T007 [P] Create basic `main.py` entry point with REPL loop skeleton in `src/cli/main.py`
- [x] T008 Configure `pytest` structure in `tests/conftest.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

## Phase 3: User Story 1 - Add and View Todos (Priority: P1) 🎯 MVP

**Goal**: Users can add tasks and see them listed.

**Independent Test**: Run `python -m src.cli.main`, type `add Test`, then `list`, and verify output.

### Tests for User Story 1

- [x] T009 [P] [US1] Create unit test for `add_todo` in `tests/unit/test_todo_service.py`
- [x] T010 [P] [US1] Create unit test for `list_todos` in `tests/unit/test_todo_service.py`

### Implementation for User Story 1

- [x] T011 [US1] Implement `add_todo` method in `src/services/todo_service.py` (auto-increment ID)
- [x] T012 [US1] Implement `list_todos` method in `src/services/todo_service.py` (return dict values)
- [x] T013 [US1] Implement `add` command handler in `src/cli/main.py`
- [x] T014 [US1] Implement `list` command handler in `src/cli/main.py`
- [x] T015 [US1] Wire up REPL to call handlers for `add` and `list` in `src/cli/main.py`

**Checkpoint**: User Story 1 functional. App is usable as a read-only list after adding items.

## Phase 4: User Story 2 - Complete and Incomplete Todos (Priority: P1)

**Goal**: Users can mark tasks as done or pending.

**Independent Test**: Add task, `complete 1`, `list` (see [x]), `uncomplete 1`, `list` (see [ ]).

### Tests for User Story 2

- [x] T016 [P] [US2] Create unit test for `toggle_todo` in `tests/unit/test_todo_service.py`

### Implementation for User Story 2

- [x] T017 [US2] Implement `toggle_todo(id)` method in `src/services/todo_service.py`
- [x] T018 [US2] Implement `complete` and `uncomplete` command handlers in `src/cli/main.py`
- [x] T019 [US2] Update `list` display in `src/cli/main.py` to show [x] or [ ] status

**Checkpoint**: Tasks can now track state.

## Phase 5: User Story 3 - Update and Delete Todos (Priority: P2)

**Goal**: Users can modify or remove tasks.

**Independent Test**: `update 1 NewText` (verify list), `delete 1` (verify list empty).

### Tests for User Story 3

- [x] T020 [P] [US3] Create unit tests for `update_todo` and `delete_todo` in `tests/unit/test_todo_service.py`

### Implementation for User Story 3

- [x] T021 [US3] Implement `update_todo(id, title)` in `src/services/todo_service.py`
- [x] T022 [US3] Implement `delete_todo(id)` in `src/services/todo_service.py`
- [x] T023 [US3] Implement `update` command handler in `src/cli/main.py`
- [x] T024 [US3] Implement `delete` command handler in `src/cli/main.py`

**Checkpoint**: Full CRUD functionality available.

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T025 [P] Add error handling for non-numeric IDs in `src/cli/main.py`
- [x] T026 [P] Add `help` command in `src/cli/main.py`
- [x] T027 Code cleanup: Ensure strict type hints across all files
- [x] T028 Validate startup time < 0.5s manually
- [x] T029 Run full manual test plan from `quickstart.md`

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Phase 1. Blocks all stories.
- **User Stories (Phase 3+)**: Depends on Phase 2.
- **Polish**: Depends on all stories.

### Parallel Opportunities

- Unit tests can be written in parallel with implementation logic.
- Service logic and CLI handlers can be implemented in parallel by separate developers (contract-first).

## Implementation Strategy

1. **Phase 1 & 2**: Get the empty shell running.
2. **Phase 3 (MVP)**: Build the "Add & List" loop. This proves the core value.
3. **Phase 4**: Add state changes (Complete).
4. **Phase 5**: Add mutations (Update/Delete).
5. **Phase 6**: harden and polish.
