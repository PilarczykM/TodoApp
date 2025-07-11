import typer

from todo_app.application.commands import AddTaskCommand, AddTaskCommandHandler
from todo_app.infrastructure.persistence.in_memory import InMemoryTaskRepository

app = typer.Typer()

task_repository = InMemoryTaskRepository()
add_task_command_handler = AddTaskCommandHandler(task_repository)

@app.command()
def add(task: str):
    """Adds a new task."""
    command = AddTaskCommand(task)
    add_task_command_handler.handle(command)
    print(f"Task '{task}' added.")
