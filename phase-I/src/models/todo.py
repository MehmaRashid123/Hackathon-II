from dataclasses import dataclass

@dataclass
class TodoItem:
    id: int
    title: str
    is_completed: bool = False
