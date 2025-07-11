from dataclasses import dataclass

from todo_app.domain.entities.task import Task
from todo_app.domain.value_objects.task_id import TaskId


@dataclass(frozen=True)
class AddTaskCommand:
    title: str


class AddTaskCommandHandler:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def handle(self, command: AddTaskCommand):
        task_id = self.task_repository.get_next_id()
        task = Task(title=command.title, description="", id=task_id)
        self.task_repository.add(task)
