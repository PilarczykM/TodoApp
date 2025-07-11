import uuid

import pytest

from todo_app.domain.value_objects import TaskId


def test_task_id_creation_from_uuid_string():
    """Test that a TaskId can be created from a valid UUID string."""
    # Given
    uuid_str = str(uuid.uuid4())

    # When
    task_id = TaskId(uuid_str)

    # Then
    assert str(task_id) == uuid_str


def test_task_id_creation_from_uuid_object():
    """Test that a TaskId can be created from a UUID object."""
    # Given
    uuid_obj = uuid.uuid4()

    # When
    task_id = TaskId(uuid_obj)

    # Then
    assert task_id.value == uuid_obj


def test_task_id_equality():
    """Test that two TaskId objects with the same value are considered equal."""
    # Given
    uuid_str = str(uuid.uuid4())
    task_id1 = TaskId(uuid_str)
    task_id2 = TaskId(uuid_str)

    # When & Then
    assert task_id1 == task_id2


def test_task_id_inequality():
    """Test that two TaskId objects with different values are considered unequal."""
    # Given
    task_id1 = TaskId(str(uuid.uuid4()))
    task_id2 = TaskId(str(uuid.uuid4()))

    # When & Then
    assert task_id1 != task_id2


def test_task_id_invalid_uuid_string():
    """Test that creating a TaskId with an invalid UUID string raises a ValueError."""
    # Given
    invalid_uuid_str = "invalid-uuid-string"

    # When / Then
    with pytest.raises(ValueError):
        TaskId(invalid_uuid_str)
