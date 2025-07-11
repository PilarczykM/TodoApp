import uuid
from dataclasses import dataclass, field
from enum import Enum

from todo_app.domain.value_objects.task_id import TaskId


class TaskStatus(Enum):
    """Represents the status of a task."""

    PENDING = "pending"
    COMPLETED = "completed"


@dataclass
class Task:
    """Represents a task in the TodoApp."""

    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    id: TaskId = field(default_factory=lambda: TaskId(uuid.uuid4()))
