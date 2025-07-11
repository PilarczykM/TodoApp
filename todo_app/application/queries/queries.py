from dataclasses import dataclass
from typing import List

from todo_app.domain.entities.task import Task, TaskStatus
from todo_app.domain.value_objects.task_id import TaskId


@dataclass(frozen=True)
class ListTasksQuery:
    """Query to list tasks."""

    status: TaskStatus | None = None


class ListTasksQueryHandler:
    """Handles the ListTasksQuery."""

    def __init__(self, task_repository):
        self.task_repository = task_repository

    def handle(self, query: ListTasksQuery) -> List[Task]:
        """Execute the ListTasksQuery."""
        if query.status:
            return [task for task in self.task_repository.get_all() if task.status == query.status]
        return self.task_repository.get_all()


@dataclass(frozen=True)
class ShowTaskQuery:
    """Query to show a single task by ID."""

    task_id: str


class ShowTaskQueryHandler:
    """Handles the ShowTaskQuery."""

    def __init__(self, task_repository):
        self.task_repository = task_repository

    def handle(self, query: ShowTaskQuery) -> Task | None:
        """Execute the ShowTaskQuery."""
        task_id = TaskId(query.task_id)
        return self.task_repository.get_by_id(task_id)
