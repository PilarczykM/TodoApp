import uuid

from todo_app.application.commands import AddTaskCommand, AddTaskCommandHandler
from todo_app.domain.entities.task import Task, TaskStatus
from todo_app.domain.value_objects.task_id import TaskId


class MockTaskRepository:
    def __init__(self):
        self.tasks = {}

    def add(self, task: Task):
        self.tasks[task.id.value] = task

    def get_next_id(self) -> TaskId:
        return TaskId(uuid.uuid4())


def test_add_task_command_handler_adds_task_to_repository():
    repository = MockTaskRepository()
    handler = AddTaskCommandHandler(repository)
    command = AddTaskCommand("Buy groceries")

    handler.handle(command)

    assert len(repository.tasks) == 1
    task_in_repo = next(iter(repository.tasks.values()))
    assert task_in_repo.title == "Buy groceries"
    assert task_in_repo.status == TaskStatus.PENDING
