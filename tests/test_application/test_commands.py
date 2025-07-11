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

    def get_by_id(self, task_id: TaskId) -> Task | None:
        return self.tasks.get(task_id.value)

    def update(self, task: Task):
        if task.id.value in self.tasks:
            self.tasks[task.id.value] = task
        else:
            raise ValueError(f"Task with ID {task.id.value} not found.")

    def remove(self, task_id: TaskId):
        if task_id.value in self.tasks:
            del self.tasks[task_id.value]
        else:
            raise ValueError(f"Task with ID {task_id.value} not found.")


def test_add_task_command_handler_adds_task_to_repository():
    repository = MockTaskRepository()
    handler = AddTaskCommandHandler(repository)
    command = AddTaskCommand("Buy groceries")

    handler.handle(command)

    assert len(repository.tasks) == 1
    task_in_repo = next(iter(repository.tasks.values()))
    assert task_in_repo.title == "Buy groceries"
    assert task_in_repo.status == TaskStatus.PENDING


def test_edit_task_command_handler_edits_task_title():
    repository = MockTaskRepository()
    # Add a task first
    task_id = repository.get_next_id()
    original_task = Task(id=task_id, title="Original Task", description="Original Description", status=TaskStatus.PENDING)
    repository.add(original_task)

    # Now try to edit it
    from todo_app.application.commands import EditTaskCommand, EditTaskCommandHandler
    command = EditTaskCommand(task_id.value, "Edited Task")
    handler = EditTaskCommandHandler(repository)
    handler.handle(command)

    edited_task = repository.get_by_id(task_id)
    assert edited_task is not None
    assert edited_task.title == "Edited Task"
    assert edited_task.status == TaskStatus.PENDING


def test_remove_task_command_handler_removes_task():
    repository = MockTaskRepository()
    # Add a task first
    task_id = repository.get_next_id()
    task_to_remove = Task(id=task_id, title="Task to remove", description="Description", status=TaskStatus.PENDING)
    repository.add(task_to_remove)

    # Now try to remove it
    from todo_app.application.commands import RemoveTaskCommand, RemoveTaskCommandHandler
    command = RemoveTaskCommand(task_id.value)
    handler = RemoveTaskCommandHandler(repository)
    handler.handle(command)

    removed_task = repository.get_by_id(task_id)
    assert removed_task is None


def test_complete_task_command_handler_marks_task_as_completed():
    repository = MockTaskRepository()
    # Add a task first
    task_id = repository.get_next_id()
    task_to_complete = Task(id=task_id, title="Task to complete", description="Description", status=TaskStatus.PENDING)
    repository.add(task_to_complete)

    # Now try to complete it
    from todo_app.application.commands import CompleteTaskCommand, CompleteTaskCommandHandler
    command = CompleteTaskCommand(task_id.value)
    handler = CompleteTaskCommandHandler(repository)
    handler.handle(command)

    completed_task = repository.get_by_id(task_id)
    assert completed_task is not None
    assert completed_task.status == TaskStatus.COMPLETED