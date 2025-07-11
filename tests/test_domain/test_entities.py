from todo_app.domain.entities import Task, TaskStatus


def test_task_creation():
    """Test that a Task can be created with a title, description, and default status."""
    # Given
    title = "Buy milk"
    description = "Remember to buy milk"

    # When
    task = Task(title=title, description=description)

    # Then
    assert task.title == title
    assert task.description == description
    assert task.status == TaskStatus.PENDING
