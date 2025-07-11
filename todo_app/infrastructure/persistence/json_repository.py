import json
import uuid
from pathlib import Path

from todo_app.application.exceptions import TaskNotFoundError
from todo_app.domain.entities.task import Task
from todo_app.domain.value_objects.task_id import TaskId


class JsonTaskRepository:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self._tasks: dict[TaskId, Task] = self._load_tasks()

    def _load_tasks(self) -> dict[TaskId, Task]:
        if not self.file_path.exists():
            return {}
        with open(self.file_path, "r") as f:
            data = json.load(f)
        tasks = {}
        for task_id_str, task_data in data.items():
            task_id = TaskId(task_id_str)
            tasks[task_id] = Task(**task_data)
        return tasks

    def _save_tasks(self):
        data = {str(task_id.value): task.model_dump(mode='json') for task_id, task in self._tasks.items()}
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def add(self, task: Task):
        self._tasks[task.id] = task
        self._save_tasks()

    def get_by_id(self, task_id: TaskId) -> Task | None:
        return self._tasks.get(task_id)

    def update(self, task: Task):
        if task.id in self._tasks:
            self._tasks[task.id] = task
            self._save_tasks()
        else:
            raise TaskNotFoundError(task.id.value)

    def remove(self, task_id: TaskId):
        if task_id in self._tasks:
            del self._tasks[task_id]
            self._save_tasks()
        else:
            raise TaskNotFoundError(task_id.value)

    def get_next_id(self) -> TaskId:
        return TaskId(str(uuid.uuid4()))

    def get_all(self) -> list[Task]:
        return list(self._tasks.values())
