# TodoApp

**TodoApp** is a terminal application that enables task management from the command line. It focuses on speed, clarity, and best-practice architecture, using Test-Driven Development (TDD) and Command-Query Responsibility Segregation (CQRS).

## Key Features

*   **Add, Edit, Delete, and Complete Tasks**: Manage your tasks with simple commands.
*   **List and Filter Tasks**: View all your tasks or filter them by status (pending/done).
*   **Detailed Task View**: See all the information about a specific task.
*   **User-Friendly Interface**: Clear and colorful output for easy scanning.

## Tech Stack

*   **Language**: Python 3.10+
*   **Architecture**: Domain-Driven Design (DDD), Command-Query Responsibility Segregation (CQRS)
*   **Development**: Test-Driven Development (TDD)
*   **CLI**: Rich
*   **Data Validation**: Pydantic

## Getting Started

To get started with TodoApp, you'll need to have Python 3.10+ and `uv` installed.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/TodoApp.git
    ```
2.  **Navigate to the project directory**:
    ```bash
    cd TodoApp
    ```
3.  **Install dependencies**:
    ```bash
    uv sync
    ```
4.  **Run the application**:
    ```bash
    uv run python -m todo_app.main --help
    ```

## Usage

Here are some examples of how to use TodoApp:

*   **Add a new task**:
    ```bash
    uv run python -m todo_app.main add "Buy milk"
    ```
*   **List all tasks**:
    ```bash
    uv run python -m todo_app.main list
    ```
*   **Complete a task**:
    ```bash
    uv run python -m todo_app.main complete <task-id>
    ```
*   **Edit a task**:
    ```bash
    uv run python -m todo_app.main edit <task-id> "New title"
    ```
*   **Remove a task**:
    ```bash
    uv run python -m todo_app.main remove <task-id>
    ```
*   **Show task details**:
    ```bash
    uv run python -m todo_app.main show <task-id>
    ```

