# Data Model: In-Memory Python Console Todo App

**Feature**: In-Memory Python Console Todo App (Phase I)
**Source**: Derived from `specs/001-console-todo-mvp/spec.md`

## Entities

### TodoItem

Represents a single task in the system.

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `id` | `int` | Yes | Unique identifier | Positive integer, auto-incremented |
| `title` | `str` | Yes | Task description | Non-empty, max 100 chars (soft limit) |
| `is_completed` | `bool` | Yes | Completion status | Default: `False` |

**Python Definition (Draft)**:
```python
from dataclasses import dataclass

@dataclass
class TodoItem:
    id: int
    title: str
    is_completed: bool = False
```

## State Management

### TodoService State

The central source of truth for the application session.

- **Storage**: `_todos: dict[int, TodoItem]`
- **Counter**: `_next_id: int` (starts at 1)

**Invariants**:
- IDs are unique within a session.
- IDs never reused in a session (simple increment).
- Data is lost when program terminates.
