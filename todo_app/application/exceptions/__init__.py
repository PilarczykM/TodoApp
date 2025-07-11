from todo_app.domain.exceptions import DomainError


class ApplicationError(DomainError):
    """Base class for application-specific errors."""

    pass


class TaskNotFoundError(ApplicationError):
    """Exception raised when a task is not found."""

    def __init__(self, task_id: str):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found.")
