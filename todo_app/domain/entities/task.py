import uuid
from enum import Enum

from pydantic import BaseModel, Field

from todo_app.domain.value_objects.task_id import TaskId


class TaskStatus(Enum):
    """Represents the status of a task."""

    PENDING = "pending"
    COMPLETED = "completed"


class Task(BaseModel):
    """Represents a task in the TodoApp."""

    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    id: TaskId = Field(default_factory=lambda: TaskId(uuid.uuid4()))
