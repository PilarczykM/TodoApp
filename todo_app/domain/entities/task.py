import uuid
from dataclasses import dataclass, field
from enum import Enum


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
    id: uuid.UUID = field(default_factory=uuid.uuid4)
