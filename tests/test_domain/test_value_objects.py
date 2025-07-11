import pytest
import uuid

from todo_app.domain.value_objects import TaskId

def test_task_id_creation_from_uuid_string():
    # Given
    uuid_str = str(uuid.uuid4())

    # When
    task_id = TaskId(uuid_str)

    # Then
    assert str(task_id) == uuid_str

def test_task_id_creation_from_uuid_object():
    # Given
    uuid_obj = uuid.uuid4()

    # When
    task_id = TaskId(uuid_obj)

    # Then
    assert task_id.value == uuid_obj

def test_task_id_equality():
    # Given
    uuid_str = str(uuid.uuid4())
    task_id1 = TaskId(uuid_str)
    task_id2 = TaskId(uuid_str)

    # When & Then
    assert task_id1 == task_id2

def test_task_id_inequality():
    # Given
    task_id1 = TaskId(str(uuid.uuid4()))
    task_id2 = TaskId(str(uuid.uuid4()))

    # When & Then
    assert task_id1 != task_id2

def test_task_id_invalid_uuid_string():
    # Given
    invalid_uuid_str = "invalid-uuid-string"

    # When / Then
    with pytest.raises(ValueError):
        TaskId(invalid_uuid_str)
