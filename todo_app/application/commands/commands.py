from dataclasses import dataclass, field

from todo_app.domain.entities.task import Task, TaskStatus
from todo_app.domain.value_objects.task_id import TaskId
from todo_app.application.exceptions import TaskNotFoundError


@dataclass(frozen=True)
class AddTaskCommand:
    """Command to add a new task."""

    title: str
    task_id: TaskId = field(init=False)


class AddTaskCommandHandler:
    """Handles the AddTaskCommand."""

    def __init__(self, task_repository):
        self.task_repository = task_repository

    def handle(self, command: AddTaskCommand):
        """Execute the AddTaskCommand."""
        task_id = self.task_repository.get_next_id()
        task = Task(title=command.title, description="", id=task_id)
        self.task_repository.add(task)
        object.__setattr__(command, 'task_id', task_id)


@dataclass(frozen=True)
class EditTaskCommand:
    """Command to edit an existing task."""

    task_id: str
    new_title: str


class EditTaskCommandHandler:
    """Handles the EditTaskCommand."""

    def __init__(self, task_repository):
        self.task_repository = task_repository

    def handle(self, command: EditTaskCommand):
        """Execute the EditTaskCommand."""
        task_id = TaskId(command.task_id)
        task = self.task_repository.get_by_id(task_id)
        if task:
            task.title = command.new_title
            self.task_repository.update(task)
        else:
            raise TaskNotFoundError(command.task_id)


@dataclass(frozen=True)
class RemoveTaskCommand:
    """Command to remove an existing task."""

    task_id: str


class RemoveTaskCommandHandler:
    """Handles the RemoveTaskCommand."""

    def __init__(self, task_repository):
        self.task_repository = task_repository

    def handle(self, command: RemoveTaskCommand):
        """Execute the RemoveTaskCommand."""
        task_id = TaskId(command.task_id)
        self.task_repository.remove(task_id)


@dataclass(frozen=True)
class CompleteTaskCommand:
    """Command to mark a task as completed."""

    task_id: str


class CompleteTaskCommandHandler:
    """Handles the CompleteTaskCommand."""

    def __init__(self, task_repository):
        self.task_repository = task_repository

    def handle(self, command: CompleteTaskCommand):
        """Execute the CompleteTaskCommand."""
        task_id = TaskId(command.task_id)
        task = self.task_repository.get_by_id(task_id)
        if task:
            task.status = TaskStatus.COMPLETED
            self.task_repository.update(task)
        else:
            raise TaskNotFoundError(command.task_id)
