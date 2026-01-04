from typing import Dict, List, Optional
from src.models.todo import TodoItem
from src.services.exceptions import TodoNotFound

class TodoService:
    def __init__(self) -> None:
        self._todos: Dict[int, TodoItem] = {}
        self._next_id: int = 1

    def add_todo(self, title: str) -> TodoItem:
        """Add a new todo item."""
        todo = TodoItem(id=self._next_id, title=title)
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo

    def list_todos(self) -> List[TodoItem]:
        """List all todo items."""
        return list(self._todos.values())

    def get_todo(self, todo_id: int) -> TodoItem:
        """Get a todo item by ID."""
        if todo_id not in self._todos:
            raise TodoNotFound(f"Todo with ID {todo_id} not found.")
        return self._todos[todo_id]

    def toggle_todo(self, todo_id: int) -> TodoItem:
        """Toggle the completion status of a todo item."""
        todo = self.get_todo(todo_id)
        todo.is_completed = not todo.is_completed
        return todo

    def update_todo(self, todo_id: int, title: str) -> TodoItem:
        """Update the title of a todo item."""
        todo = self.get_todo(todo_id)
        todo.title = title
        return todo

    def delete_todo(self, todo_id: int) -> None:
        """Delete a todo item."""
        if todo_id not in self._todos:
            raise TodoNotFound(f"Todo with ID {todo_id} not found.")
        del self._todos[todo_id]
