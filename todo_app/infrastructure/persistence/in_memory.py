import uuid

from todo_app.domain.entities.task import Task
from todo_app.domain.value_objects.task_id import TaskId


class InMemoryTaskRepository:
    """In-memory implementation of the TaskRepository."""

    def __init__(self):
        """Initialize the in-memory repository."""
        self._tasks: dict[TaskId, Task] = {}

    def add(self, task: Task):
        """Add a task to the repository."""
        self._tasks[task.id] = task

    def get_by_id(self, task_id: TaskId) -> Task | None:
        """Retrieve a task by its ID."""
        return self._tasks.get(task_id)

    def update(self, task: Task):
        """Update an existing task."""
        if task.id in self._tasks:
            self._tasks[task.id] = task
        else:
            raise ValueError(f"Task with ID {task.id.value} not found.")

    def remove(self, task_id: TaskId):
        """Remove a task from the repository."""
        if task_id in self._tasks:
            del self._tasks[task_id]
        else:
            raise ValueError(f"Task with ID {task_id.value} not found.")

    def get_next_id(self) -> TaskId:
        """Generate a new unique TaskId."""
        return TaskId(str(uuid.uuid4()))
