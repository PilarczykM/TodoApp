# 🧾 PRD - TodoApp (console application)

---

## 1. 🎯 Product Goal and Stakeholders

### 1.1. Product Vision

**TodoApp** is a terminal application that enables task management from the command line. It focuses on speed, clarity, and best-practice architecture, using Test-Driven Development (TDD) and Command-Query Responsibility Segregation (CQRS).

### 1.2. Success Metrics

- **Performance**: Operation time < 100 ms
- **Reliability**: Zero false-positive errors in the test suite
- **Usability**: 100 % of functionality available through the CLI
- **Maintainability**: Test coverage ≥ 90 %
- **User Experience**: No more than 3 steps to perform any action

---

## 2. 👥 User Stories & Acceptance Criteria

### 2.1. Epics & User Stories

#### Epic 1: Managing Tasks

- **US-001**: As a user, I want to add a new task with a title and an optional description so that I can track what I have to do.
- **US-002**: As a user, I want to edit an existing task so that I can update its information.
- **US-003**: As a user, I want to delete a task so that I can clean the list of outdated items.
- **US-004**: As a user, I want to mark a task as completed so that I can track my progress.

#### Epic 2: Browsing Tasks

- **US-005**: As a user, I want to see all my tasks in a clear format so that I can quickly assess my workload.
- **US-006**: As a user, I want to filter tasks by status (pending/done) so that I can focus on a specific type of task.
- **US-007**: As a user, I want to view the details of a specific task so that I can review all its information.

#### Epic 3: User Experience

- **US-008**: As a user, I want to receive readable error messages so that I can quickly correct my actions.
- **US-009**: As a user, I want colorful and readable output formatting so that I can more easily scan information.

### 2.2. Acceptance Criteria

#### AC-001: Adding a task

```gherkin
Given the user has access to the CLI
When they run the command "todo add 'Task title'"
Then the task is added with a unique ID
And a success message is displayed with the task ID
And the task has status PENDING
```

#### AC-002: Data validation

```gherkin
Given the user tries to add a task
When the title is empty or exceeds 200 characters
Then an error message is shown
And the task is not added
```

*…additional acceptance criteria continue in the same format…*

---

## 3. 🚦 Validation & Error Cases

| Case                   | Expected Behavior        | Error Code         |
| ---------------------- | ------------------------ | ------------------ |
| Empty title            | Show validation error    | VALIDATION\_ERROR  |
| Title > 200 chars      | Show validation error    | VALIDATION\_ERROR  |
| Invalid UUID           | Show format error        | INVALID\_UUID      |
| Task does not exist    | Show not-found error     | TASK\_NOT\_FOUND   |
| Task already completed | Show information message | ALREADY\_COMPLETED |
| Duplicate title        | Allow (no restriction)   | -                  |

### 3.2 UUID Validation Rules

```python
# Detailed UUID handling rules
- Full UUID (36 chars): always accepted
- UUID prefix (8 chars): accepted only if unique
- If the prefix is ambiguous: show an error with a list of matches
- Case-insensitive matching for UUIDs
```

---

## 4. 🧱 Technical & Design Assumptions

| Component            | Requirement                       |
| -------------------- | --------------------------------- |
| Programming language | Python 3.10+                      |
| Interface type       | Console (CLI)                     |
| Architecture         | Full Domain-Driven Design         |
| Code style           | Clean Code, SOLID, DRY, SRP       |
| Development process  | TDD - tests before implementation |
| Persistence          | In-memory (behind an interface)   |
| Data validation      | Pydantic at CLI level             |
| Error handling       | Layered exception hierarchy       |
| Documentation        | NumPy docstring style             |
| UI/CLI enhancements  | Rich library                      |

---

## 5. 📦 Domain Model

```
+--------------+        1         *        +------------+
|    Task      |------------------------->|  SubTask    |
+--------------+                          +------------+
| id: UUID     |                          | id: UUID   |
| title: str   |                          | title: str |
| description? |                          | status     |
| status       |                          +------------+
+--------------+
```

*Additional entities (e.g. Tag, Project) may be added in future versions.*

---

## 6. ⚠️ Exception Hierarchy (excerpt)

```python
# Domain exceptions
class DomainError(Exception):
    """Base domain exception."""
    pass

class TaskNotFoundError(DomainError):
    """The task was not found."""
    pass

# Application exceptions
class ApplicationError(Exception):
    """Base application exception."""
    pass

class InvalidInputError(ApplicationError):
    """Input data validation failed."""
    pass

class AmbiguousUuidError(ApplicationError):
    """The UUID prefix is not unique."""
    pass
```

### 6.2 Error Response Format

```python
@dataclass
class ErrorResponse:
    error_code: str
    message: str
    details: Optional[str] = None
    suggestions: Optional[List[str]] = None
```

---

## 7. 🖥️ CLI UX Mock-ups (Rich)

```
> todo add "Buy milk"
┌─────────────────────────────────────────┐
│  ✅ Task added                          │
│                                         │
│  ID: ae34b1e9                           │
└─────────────────────────────────────────┘
```

```
> todo remove 12345678
┌────────────────────────────────────────────┐
│  ⚠️  Confirm deletion                      │
│                                            │
│  Are you sure you want to delete it? (y/N) │
└────────────────────────────────────────────┘
```

```
> todo complete invalid-uuid
┌─────────────────────────────────────────┐
│  ❌ UUID error                          │
│                                         │
│  The provided identifier is not         │
│  a valid or existing UUID               │
│                                         │
│  💡 Tip: Run 'todo list'                │
│     to see available IDs                │
└─────────────────────────────────────────┘
```

---

## 8. 🧠 CQRS & Application Layer

### 8.1 Command Handlers (example)

```python
class AddTaskCommandHandler:
    """Handles adding a new task."""

    def handle(self, command: AddTaskCommand) -> TaskDto:
        """
        1. Validate input
        2. Create Task aggregate
        3. Persist via repository
        4. Return DTO
        """
```

### 8.2 Query Handlers (example)

```python
class ListTasksQueryHandler:
    """Returns all tasks."""

    def handle(self, query: ListTasksQuery) -> List[TaskDto]:
        return self.repository.get_all()
```

---

## 9. 🗄️ Persistence Layer

Current version uses an in-memory repository behind an interface. Switching to a database (e.g. SQLite) in future versions will require implementing the same interface without changes in the application layer.

---

## 10. 📁 Suggested Folder Structure

```
todo_app/
├── domain/
│   ├── __init__.py
│   ├── entities/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── value_objects/
│   │   ├── __init__.py
│   │   └── task_id.py
│   └── exceptions/
│       ├── __init__.py
│       └── domain_exceptions.py
├── application/
│   ├── __init__.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── add_task_command.py
│   │   └── complete_task_command.py
│   ├── queries/
│   │   ├── __init__.py
│   │   ├── list_tasks_query.py
│   │   └── get_task_by_id_query.py
│   ├── use_cases/
│   │   ├── __init__.py
│   │   └── task_use_cases.py
│   ├── dto/
│   │   ├── __init__.py
│   │   └── task_dto.py
│   └── exceptions/
│       ├── __init__.py
│       └── application_exceptions.py
├── infrastructure/
│   ├── persistence/
│   │   ├── __init__.py
│   │   └── in_memory_repository.py
│   └── cli/
│       ├── __init__.py
│       └── rich_cli.py
└── main.py
```

---

## 11. 📆 Roadmap

| Version | Scope                          | Target Date |
| ------- | ------------------------------ | ----------- |
| **2.3** | Persistence adapter for SQLite | Aug 2025    |
| **2.4** | Tagging & search               | Nov 2025    |
| **2.5** | Cross-platform packaging       | Jan 2026    |

---

## 12. ✅ Definition of Done

1. All acceptance criteria satisfied
2. Test coverage ≥ 90 %, all tests green
3. Linting passes (ruff)
4. Up-to-date documentation
5. CI pipeline green on main branch
