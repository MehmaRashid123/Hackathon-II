import sys
from typing import NoReturn
from src.services.todo_service import TodoService
from src.services.exceptions import TodoNotFound

def main() -> NoReturn:
    service = TodoService()
    print("Welcome to Todo CLI! Type 'help' for commands, 'exit' to quit.")
    
    while True:
        try:
            command_line = input("> ").strip()
            if not command_line:
                continue
            
            parts = command_line.split(" ", 1)
            command = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""

            if command in ("exit", "quit"):
                print("Goodbye!")
                sys.exit(0)
            
            elif command == "help":
                print("\nAvailable commands:")
                print("  add <title>             - Add a new todo")
                print("  list                    - List all todos")
                print("  complete <id>           - Mark a todo as complete")
                print("  uncomplete <id>         - Mark a todo as incomplete")
                print("  update <id> <new title> - Update a todo's title")
                print("  delete <id>             - Delete a todo")
                print("  help                    - Show this help message")
                print("  exit                    - Exit the application\n")
            
            elif command == "add":
                if not args:
                    print("Error: Description required. Usage: add <title>")
                    continue
                todo = service.add_todo(args)
                print(f"[Success] Added todo #{todo.id}: {todo.title}")
            
            elif command == "list":
                todos = service.list_todos()
                if not todos:
                    print("No todos found.")
                else:
                    for todo in todos:
                        status = "[x]" if todo.is_completed else "[ ]"
                        print(f"{todo.id}. {status} {todo.title}")

            elif command in ("complete", "uncomplete"):
                if not args:
                    print(f"Error: ID required. Usage: {command} <id>")
                    continue
                try:
                    todo_id = int(args)
                    todo = service.get_todo(todo_id)
                    
                    if command == "complete" and not todo.is_completed:
                        service.toggle_todo(todo_id)
                        print(f"[Success] Marked todo #{todo_id} as complete")
                    elif command == "uncomplete" and todo.is_completed:
                        service.toggle_todo(todo_id)
                        print(f"[Success] Marked todo #{todo_id} as incomplete")
                    else:
                        status = "complete" if todo.is_completed else "incomplete"
                        print(f"Todo #{todo_id} is already {status}.")

                except ValueError:
                    print("Error: ID must be an integer.")
                    continue
                except TodoNotFound as e:
                    print(f"Error: {e}")

            elif command == "update":
                if not args:
                    print("Error: Usage: update <id> <new title>")
                    continue
                
                try:
                    parts = args.split(" ", 1)
                    if len(parts) < 2:
                        print("Error: Usage: update <id> <new title>")
                        continue
                    
                    todo_id = int(parts[0])
                    new_title = parts[1]
                    
                    todo = service.update_todo(todo_id, new_title)
                    print(f"[Success] Updated todo #{todo.id}: {todo.title}")
                    
                except ValueError:
                    print("Error: ID must be an integer.")
                    continue
                except TodoNotFound as e:
                    print(f"Error: {e}")

            elif command == "delete":
                if not args:
                    print("Error: ID required. Usage: delete <id>")
                    continue
                try:
                    todo_id = int(args)
                    service.delete_todo(todo_id)
                    print(f"[Success] Deleted todo #{todo_id}")
                except ValueError:
                    print("Error: ID must be an integer.")
                    continue
                except TodoNotFound as e:
                    print(f"Error: {e}")
            
            else:
                print(f"Unknown command: {command}")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
