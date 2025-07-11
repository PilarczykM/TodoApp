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
    match = re.search(r"Task 'Task to edit' added with ID: ([0-9a-fA-F-]{36})", add_result.stdout)
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
    match = re.search(r"Task 'Task to remove' added with ID: ([0-9a-fA-F-]{36})", add_result.stdout)
    assert match is not None
    task_id = match.group(1)

    # Attempt to remove the task
    remove_result = runner.invoke(app, ["remove", task_id])
    assert remove_result.exit_code == 0
    assert f"Task {task_id} removed." in remove_result.stdout