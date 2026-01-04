from src.models.todo import TodoItem
from src.services.exceptions import TodoNotFound
import pytest

def test_add_todo(todo_service):
    todo = todo_service.add_todo("Buy milk")
    assert isinstance(todo, TodoItem)
    assert todo.id == 1
    assert todo.title == "Buy milk"
    assert todo.is_completed is False
    
    todo2 = todo_service.add_todo("Walk dog")
    assert todo2.id == 2

def test_list_todos(todo_service):
    assert todo_service.list_todos() == []
    
    todo1 = todo_service.add_todo("Task 1")
    todo2 = todo_service.add_todo("Task 2")
    
    todos = todo_service.list_todos()
    assert len(todos) == 2
    assert todos[0] == todo1
    assert todos[1] == todo2

def test_get_todo(todo_service):
    todo = todo_service.add_todo("Test")
    fetched = todo_service.get_todo(todo.id)
    assert fetched == todo

def test_get_todo_not_found(todo_service):
    with pytest.raises(TodoNotFound):
        todo_service.get_todo(999)

def test_toggle_todo(todo_service):
    todo = todo_service.add_todo("Toggle me")
    assert todo.is_completed is False
    
    updated = todo_service.toggle_todo(todo.id)
    assert updated.is_completed is True
    assert todo.is_completed is True # Check in-place or returned object
    
    updated = todo_service.toggle_todo(todo.id)
    assert updated.is_completed is False

def test_toggle_todo_not_found(todo_service):
    with pytest.raises(TodoNotFound):
        todo_service.toggle_todo(999)

def test_update_todo(todo_service):
    todo = todo_service.add_todo("Old Title")
    updated = todo_service.update_todo(todo.id, "New Title")
    assert updated.title == "New Title"
    assert todo.title == "New Title"

def test_update_todo_not_found(todo_service):
    with pytest.raises(TodoNotFound):
        todo_service.update_todo(999, "New Title")

def test_delete_todo(todo_service):
    todo = todo_service.add_todo("Delete me")
    assert len(todo_service.list_todos()) == 1
    
    todo_service.delete_todo(todo.id)
    assert len(todo_service.list_todos()) == 0

def test_delete_todo_not_found(todo_service):
    with pytest.raises(TodoNotFound):
        todo_service.delete_todo(999)