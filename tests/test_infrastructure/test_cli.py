from typer.testing import CliRunner

from todo_app.infrastructure.cli.main import app

runner = CliRunner()


def test_add_task():
    result = runner.invoke(app, ["add", "Test Task"])
    assert result.exit_code == 0
    assert "Task 'Test Task' added with ID:" in result.stdout


def test_edit_task_e2e_failing():
    # Add a task first and capture its ID
    add_result = runner.invoke(app, ["add", "Task to edit"])
    assert add_result.exit_code == 0
    import re

    match = re.search(
        r"Task 'Task to edit' added with ID: ([0-9a-fA-F-]{36})",
        add_result.stdout,
    )
    assert match is not None
    task_id = match.group(1)
    print(f"Captured Task ID: {task_id}")

    # Attempt to edit the task
    edit_result = runner.invoke(app, ["edit", task_id, "Edited Task"])
    assert edit_result.exit_code == 0
    assert f"Task {task_id} edited to 'Edited Task'." in edit_result.stdout


def test_remove_task_e2e_failing():
    # Add a task first and capture its ID
    add_result = runner.invoke(app, ["add", "Task to remove"])
    assert add_result.exit_code == 0
    import re

    match = re.search(
        r"Task 'Task to remove' added with ID: ([0-9a-fA-F-]{36})",
        add_result.stdout,
    )
    assert match is not None
    task_id = match.group(1)

    # Attempt to remove the task
    remove_result = runner.invoke(app, ["remove", task_id])
    assert remove_result.exit_code == 0
    assert f"Task {task_id} removed." in remove_result.stdout


def test_complete_task_e2e_failing():
    # Add a task first and capture its ID
    add_result = runner.invoke(app, ["add", "Task to complete"])
    assert add_result.exit_code == 0
    import re

    match = re.search(
        r"Task 'Task to complete' added with ID: ([0-9a-fA-F-]{36})",
        add_result.stdout,
    )
    assert match is not None
    task_id = match.group(1)

    # Attempt to complete the task
    complete_result = runner.invoke(app, ["complete", task_id])
    assert complete_result.exit_code == 0
    assert f"Task {task_id} marked as completed." in complete_result.stdout


def test_list_tasks_e2e_failing():
    # Add a few tasks
    runner.invoke(app, ["add", "Task 1"])
    runner.invoke(app, ["add", "Task 2"])
    runner.invoke(app, ["add", "Task 3"])

    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "Task 1" in result.stdout
    assert "Task 2" in result.stdout
    assert "Task 3" in result.stdout


def test_list_completed_tasks_e2e_failing():
    # Add tasks and complete one
    add_result_1 = runner.invoke(app, ["add", "Pending Task"])
    import re

    match_1 = re.search(
        r"Task 'Pending Task' added with ID: ([0-9a-fA-F-]{36})",
        add_result_1.stdout,
    )
    _ = match_1.group(1)

    add_result_2 = runner.invoke(app, ["add", "Completed Task"])
    match_2 = re.search(
        r"Task 'Completed Task' added with ID: ([0-9a-fA-F-]{36})", add_result_2.stdout
    )
    task_id_2 = match_2.group(1)
    runner.invoke(app, ["complete", task_id_2])

    result = runner.invoke(app, ["list", "--status", "completed"])
    assert result.exit_code == 0
    assert "Completed Task" in result.stdout
    assert "Pending Task" not in result.stdout


def test_show_task_e2e_failing():
    # Add a task
    add_result = runner.invoke(app, ["add", "Task to show"])
    import re

    match = re.search(
        r"Task 'Task to show' added with ID: ([0-9a-fA-F-]{36})", add_result.stdout
    )
    task_id = match.group(1)

    result = runner.invoke(app, ["show", task_id])
    assert result.exit_code == 0
    assert f"ID: {task_id}" in result.stdout
    assert "Title: Task to show" in result.stdout
    assert "Status: PENDING" in result.stdout
