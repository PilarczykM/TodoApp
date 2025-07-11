from typer.testing import CliRunner

from todo_app.infrastructure.cli.main import app

runner = CliRunner()

def test_add_task():
    result = runner.invoke(app, ["add", "Test Task"])
    assert result.exit_code == 0
    assert "Task 'Test Task' added." in result.stdout

def test_edit_task_e2e_failing():
    # Add a task first
    runner.invoke(app, ["add", "Task to edit"])
    # Attempt to edit the task
    result = runner.invoke(app, ["edit", "1", "Edited Task"])
    assert result.exit_code == 0
    assert "Task 1 edited to 'Edited Task'." in result.stdout
