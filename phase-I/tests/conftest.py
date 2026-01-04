import pytest
from src.services.todo_service import TodoService

@pytest.fixture
def todo_service():
    return TodoService()
