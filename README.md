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

To get started with TodoApp, you'll need to have Python 3.10+ installed.

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
    pip install -r requirements.txt
    ```
4.  **Run the application**:
    ```bash
    python src/main.py --help
    ```

## Usage

Here are some examples of how to use TodoApp:

*   **Add a new task**:
    ```bash
    python src/main.py add "Buy milk"
    ```
*   **List all tasks**:
    ```bash
    python src/main.py list
    ```
*   **Complete a task**:
    ```bash
    python src/main.py complete <task-id>
    ```

## Roadmap

| Version | Scope                          | Target Date |
| ------- | ------------------------------ | ----------- |
| **2.3** | Persistence adapter for SQLite | Aug 2025    |
| **2.4** | Tagging & search               | Nov 2025    |
| **2.5** | Cross-platform packaging       | Jan 2026    |