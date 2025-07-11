from dataclasses import dataclass
from enum import Enum
import uuid

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"

@dataclass
class Task:
    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    id: uuid.UUID = uuid.uuid4()
