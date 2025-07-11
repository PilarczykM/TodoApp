import uuid

from todo_app.application.queries.queries import ListTasksQuery, ListTasksQueryHandler
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

    def get_all(self):
        return list(self.tasks.values())


def test_list_tasks_query_handler_returns_all_tasks():
    repository = MockTaskRepository()
    task1 = Task(id=repository.get_next_id(), title="Task 1", description="Desc 1", status=TaskStatus.PENDING)
    task2 = Task(id=repository.get_next_id(), title="Task 2", description="Desc 2", status=TaskStatus.COMPLETED)
    repository.add(task1)
    repository.add(task2)

    handler = ListTasksQueryHandler(repository)
    query = ListTasksQuery()
    tasks = handler.handle(query)

    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks

def test_list_tasks_query_handler_returns_completed_tasks():
    repository = MockTaskRepository()
    task1 = Task(id=repository.get_next_id(), title="Task 1", description="Desc 1", status=TaskStatus.PENDING)
    task2 = Task(id=repository.get_next_id(), title="Task 2", description="Desc 2", status=TaskStatus.COMPLETED)
    repository.add(task1)
    repository.add(task2)

    handler = ListTasksQueryHandler(repository)
    query = ListTasksQuery(status=TaskStatus.COMPLETED)
    tasks = handler.handle(query)

    assert len(tasks) == 1
    assert task2 in tasks
    assert task1 not in tasks
