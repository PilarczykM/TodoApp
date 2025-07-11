from typer.testing import CliRunner

from todo_app.main import app

runner = CliRunner()

def test_add_command_creates_task():
    result = runner.invoke(app, ["add", "Buy groceries"])
    assert result.exit_code == 0
    assert "Task 'Buy groceries' added." in result.stdout
