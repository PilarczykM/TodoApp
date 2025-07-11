from dataclasses import dataclass

from todo_app.domain.entities.task import Task


@dataclass(frozen=True)
class AddTaskCommand:
    """Command to add a new task."""

    title: str


class AddTaskCommandHandler:
    """Handles the AddTaskCommand."""

    def __init__(self, task_repository):
        self.task_repository = task_repository

    def handle(self, command: AddTaskCommand):
        """Execute the AddTaskCommand."""
        task_id = self.task_repository.get_next_id()
        task = Task(title=command.title, description="", id=task_id)
        self.task_repository.add(task)
