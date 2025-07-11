import pytest
import json
from pathlib import Path
import uuid

from todo_app.application.exceptions import TaskNotFoundError
from todo_app.domain.entities.task import Task, TaskStatus
from todo_app.domain.value_objects.task_id import TaskId
from todo_app.infrastructure.persistence.json_repository import JsonTaskRepository

@pytest.fixture
def temp_json_file(tmp_path):
    file_path = tmp_path / "tasks.json"
    yield file_path
    if file_path.exists():
        file_path.unlink()

@pytest.fixture
def populated_repository(temp_json_file):
    repository = JsonTaskRepository(temp_json_file)
    task1 = Task(
        id=repository.get_next_id(),
        title="Task 1",
        description="Description 1",
        status=TaskStatus.PENDING,
    )
    task2 = Task(
        id=repository.get_next_id(),
        title="Task 2",
        description="Description 2",
        status=TaskStatus.COMPLETED,
    )
    repository.add(task1)
    repository.add(task2)
    return repository, task1, task2

def test_json_task_repository_adds_task(temp_json_file):
    repository = JsonTaskRepository(temp_json_file)
    task_id = repository.get_next_id()
    task = Task(
        id=task_id,
        title="Test Task",
        description="A test description",
        status=TaskStatus.PENDING,
    )
    repository.add(task)

    # Verify task is in repository
    retrieved_task = repository.get_by_id(task_id)
    assert retrieved_task == task

    # Verify task is in the JSON file
    with open(temp_json_file, "r") as f:
        data = json.load(f)
    assert str(task_id.value) in data
    assert data[str(task_id.value)]["title"] == "Test Task"

def test_json_task_repository_get_by_id(populated_repository):
    repository, task1, _ = populated_repository
    retrieved_task = repository.get_by_id(task1.id)
    assert retrieved_task == task1

def test_json_task_repository_get_by_id_not_found(temp_json_file):
    repository = JsonTaskRepository(temp_json_file)
    non_existent_id = TaskId(str(uuid.uuid4()))
    assert repository.get_by_id(non_existent_id) is None

def test_json_task_repository_update(populated_repository):
    repository, task1, _ = populated_repository
    task1.title = "Updated Task 1"
    repository.update(task1)

    retrieved_task = repository.get_by_id(task1.id)
    assert retrieved_task.title == "Updated Task 1"

    with open(repository.file_path, "r") as f:
        data = json.load(f)
    assert data[str(task1.id.value)]["title"] == "Updated Task 1"

def test_json_task_repository_update_not_found(temp_json_file):
    repository = JsonTaskRepository(temp_json_file)
    non_existent_task = Task(
        id=TaskId(str(uuid.uuid4())),
        title="Non Existent",
        description="",
        status=TaskStatus.PENDING,
    )
    with pytest.raises(TaskNotFoundError):
        repository.update(non_existent_task)

def test_json_task_repository_remove(populated_repository):
    repository, task1, task2 = populated_repository
    repository.remove(task1.id)

    assert repository.get_by_id(task1.id) is None
    assert repository.get_by_id(task2.id) == task2

    with open(repository.file_path, "r") as f:
        data = json.load(f)
    assert str(task1.id.value) not in data
    assert str(task2.id.value) in data

def test_json_task_repository_remove_not_found(temp_json_file):
    repository = JsonTaskRepository(temp_json_file)
    non_existent_id = TaskId(str(uuid.uuid4()))
    with pytest.raises(TaskNotFoundError):
        repository.remove(non_existent_id)

def test_json_task_repository_get_all(populated_repository):
    repository, task1, task2 = populated_repository
    all_tasks = repository.get_all()
    assert len(all_tasks) == 2
    assert task1 in all_tasks
    assert task2 in all_tasks

def test_json_task_repository_get_next_id():
    repository = JsonTaskRepository(Path("dummy.json")) # File path doesn't matter for this test
    id1 = repository.get_next_id()
    id2 = repository.get_next_id()
    assert id1 != id2
    assert isinstance(id1, TaskId)