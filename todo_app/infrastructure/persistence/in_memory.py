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

    def get(self, task_id: TaskId) -> Task:
        """Retrieve a task by its ID."""
        return self._tasks.get(task_id)

    def get_next_id(self) -> TaskId:
        """Generate a new unique TaskId."""
        return TaskId(str(uuid.uuid4()))
