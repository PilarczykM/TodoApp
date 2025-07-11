import uuid
from dataclasses import dataclass

@dataclass(frozen=True)
class TaskId:
    value: uuid.UUID

    def __post_init__(self):
        if not isinstance(self.value, uuid.UUID):
            try:
                object.__setattr__(self, 'value', uuid.UUID(str(self.value)))
            except ValueError as e:
                raise ValueError(f"Invalid UUID string for TaskId: {self.value}") from e

    def __str__(self):
        return str(self.value)
