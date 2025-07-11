import uuid
from typing import Dict

from todo_app.domain.entities.task import Task
from todo_app.domain.value_objects.task_id import TaskId


class InMemoryTaskRepository:
    def __init__(self):
        self._tasks: Dict[TaskId, Task] = {}

    def add(self, task: Task):
        self._tasks[task.id] = task

    def get(self, task_id: TaskId) -> Task:
        return self._tasks.get(task_id)

    def get_next_id(self) -> TaskId:
        return TaskId(str(uuid.uuid4()))
