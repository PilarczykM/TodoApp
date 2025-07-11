import pytest
from todo_app.domain.entities.task import Task, TaskStatus
from todo_app.domain.value_objects.task_id import TaskId
from todo_app.infrastructure.persistence.in_memory import InMemoryTaskRepository

def test_in_memory_task_repository_adds_task():
    repository = InMemoryTaskRepository()
    task_id = repository.get_next_id()
    task = Task(title="Test Task", description="A test description", status=TaskStatus.PENDING, id=task_id)
    repository.add(task)
    assert repository.get(task_id) == task

def test_in_memory_task_repository_generates_unique_ids():
    repository = InMemoryTaskRepository()
    id1 = repository.get_next_id()
    id2 = repository.get_next_id()
    assert id1 != id2
