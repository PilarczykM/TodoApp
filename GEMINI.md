# Gemini Agent Configuration for TodoApp

This document provides guidelines for the Gemini AI agent to follow while working on the TodoApp project. The primary goal is to ensure consistent, high-quality development adhering to Test-Driven Development (TDD) and a structured commit workflow.

## Core Principles

1.  **Outside-In TDD is Mandatory**: All development must start with a test. Begin with a high-level (e.g., end-to-end CLI) test that fails, then write the minimum necessary code across the application, domain, and infrastructure layers to make it pass.
2.  **Micro-Commits per Sub-task**: Commit after each sub-task from the `docs/tasks/*.md` files is successfully completed and verified. This creates a clean, atomic history.
3.  **DDD and Clean Architecture**: Strictly respect the separation of concerns between the Domain, Application, and Infrastructure layers. The Domain must not depend on any outer layer.
4.  **Always Verify**: After any code change, run the relevant tests and quality checks (`pytest`, `ruff`) to ensure the change is safe and correct.

## Development Workflow

Follow this sequence for every sub-task:

1.  **Select Task**: Identify the next uncompleted sub-task from the ordered files in `docs/tasks/`.
2.  **Write Failing Test**: Create a new test file or add a new test case that specifically validates the requirement of the sub-task. The test should fail with a clear and expected error.
3.  **Run Test to Confirm Failure**: Execute `pytest path/to/your/test.py` and ensure it fails as anticipated.
4.  **Implement Minimal Code**: Write the absolute minimum amount of code required to make the failing test pass. This may involve creating or modifying classes and functions in `src/todo_app`.
5.  **Run Test to Confirm Pass**: Execute `pytest` again to ensure the test now passes.
6.  **Run Quality Checks**: Run `ruff check .` and `ruff format .` to lint and format the new code. Fix any issues that are reported.
7.  **Commit Changes**: Once all checks pass, stage and commit the changes.
    -   `git add .`
    -   `git commit -m "..."` (See commit message style below)
8.  **Update Task List**: Mark the sub-task as complete (`[x]`) in its respective markdown file in `docs/tasks/`.

## Tooling & Commands

-   **Run All Tests**: `pytest`
-   **Run Specific Tests**: `pytest tests/path/to/test_file.py`
-   **Run Tests with Coverage**: `pytest --cov=src/todo_app tests/`
-   **Lint and Type-Check**: `ruff check .`
-   **Format Code**: `ruff format .`
-   **Install Dependency**: `uv pip install <package_name>`
-   **Sync Dependencies**: `uv pip sync pyproject.toml`

## Commit Message Style

Use the [Conventional Commits](https://www.conventionalcommits.org/) format. This helps maintain a clear and descriptive git history.

**Format**: `<type>(<scope>): <subject>`

**Common Types**:
-   `feat`: A new feature (e.g., implementing a command).
-   `fix`: A bug fix.
-   `test`: Adding or improving tests.
-   `refactor`: Code changes that neither fix a bug nor add a feature.
-   `docs`: Changes to documentation (`.md` files).
-   `style`: Code style changes (formatting).
-   `build`: Changes that affect the build system or external dependencies.

**Example Scopes**:
-   `domain`: Changes to the domain layer.
-   `app`: Changes to the application layer.
--   `infra`: Changes to the infrastructure layer (CLI, persistence).
-   `cli`: Specific to the command-line interface.
-   `ci`: Changes to CI/CD configuration.

**Example Commit Messages**:

```
test(cli): Add failing e2e test for 'todo add' command
feat(domain): Implement Task entity with status management
fix(app): Ensure task title validation handles unicode
refactor(infra): Simplify InMemoryRepository implementation
docs(tasks): Complete task 1.4
```
