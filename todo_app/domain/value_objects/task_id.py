import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class TaskId:
    """Value object for Task ID."""

    value: uuid.UUID

    def __post_init__(self):
        """Initialize the TaskId value object."""
        if not isinstance(self.value, uuid.UUID):
            try:
                object.__setattr__(self, "value", uuid.UUID(str(self.value)))
            except ValueError as e:
                raise ValueError("Invalid UUID string for TaskId") from e

    def __str__(self):
        """Return the string representation of the TaskId."""
        return str(self.value)
