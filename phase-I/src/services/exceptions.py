class TodoAppError(Exception):
    """Base exception for the application."""
    pass

class TodoNotFound(TodoAppError):
    """Raised when a todo item cannot be found."""
    pass
