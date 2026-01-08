# Todo Evolution - Phase I (In-Memory CLI)

A disciplined, AI-assisted implementation of a Todo application, starting as a pure in-memory Python console app and designed to evolve into a cloud-native system.

## Project Vision
This project demonstrates a 5-phase evolution:
1. **Phase I: In-Memory Python Console App (Current)**
2. Phase II: Full-Stack Web App (FastAPI/Next.js/PostgreSQL)
3. Phase III: AI-Powered Chatbot Integration
4. Phase IV: Local Kubernetes Deployment
5. Phase V: Advanced Cloud-Native Deployment

## Phase I Features
- **Add Todo**: Create new tasks with unique auto-incrementing IDs.
- **List Todos**: View all tasks with their current completion status.
- **Complete/Uncomplete**: Toggle the status of specific tasks.
- **Update**: Modify the title of existing tasks.
- **Delete**: Remove tasks from the list.
- **In-Memory**: Operates entirely in RAM (data resets on exit).

## Prerequisites
- **Python 3.13+**

## Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MehmaRashid123/Hackathon-II.git
   cd phase-I
   ```

2. **Initialize Environment** (Optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

## Running the Application

Start the CLI application using the following command from the root directory:

```bash
python -m src.cli.main
```

## Usage Guide

Once the CLI is running, you can use the following commands:

| Command | Description | Example |
|---------|-------------|---------|
| `add <title>` | Add a new todo | `add Buy groceries` |
| `list` | Show all todos | `list` |
| `complete <id>` | Mark as done | `complete 1` |
| `uncomplete <id>` | Mark as pending | `uncomplete 1` |
| `update <id> <text>` | Update title | `update 1 Buy oat milk` |
| `delete <id>` | Remove todo | `delete 1` |
| `help` | Show help | `help` |
| `exit` | Quit the app | `exit` |

## Development & Testing

### Project Structure
- `src/models/`: Data structures (TodoItem).
- `src/services/`: Business logic (TodoService).
- `src/cli/`: Interface logic (REPL loop).
- `specs/`: Phase documentation and design artifacts.

### Testing
The project uses `pytest` for unit testing the service layer.
```bash
python -m pytest
```

## Architecture Principles
- **Simplicity First**: No external dependencies or premature frameworks.
- **Separation of Concerns**: Logic is decoupled from the CLI interface.
- **Deterministic**: Predictable state management and ID generation.
- **Type Safety**: Full use of Python type hints and dataclasses.
