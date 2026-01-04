# Quickstart: In-Memory Python Console Todo App

## Prerequisites
- Python 3.13+ installed (`python --version`)
- No external packages required.

## Running the App

1. Navigate to the project root:
   ```bash
   cd src
   ```

2. Start the CLI:
   ```bash
   python -m cli.main
   ```

## Usage Guide

The application accepts commands in a REPL loop.

| Action | Command Format | Example |
|--------|----------------|---------|
| **Add** | `add <text>` | `add Buy Milk` |
| **List** | `list` | `list` |
| **Complete** | `complete <id>` | `complete 1` |
| **Uncomplete** | `uncomplete <id>` | `uncomplete 1` |
| **Update** | `update <id> <new text>` | `update 1 Buy Oat Milk` |
| **Delete** | `delete <id>` | `delete 1` |
| **Help** | `help` | `help` |
| **Exit** | `exit` or `quit` | `exit` |

## Example Session

```text
> add Learn Python
[Success] Added todo #1: Learn Python

> add Build App
[Success] Added todo #2: Build App

> list
1. [ ] Learn Python
2. [ ] Build App

> complete 1
[Success] Marked todo #1 as complete

> list
1. [x] Learn Python
2. [ ] Build App

> exit
Goodbye!
```
