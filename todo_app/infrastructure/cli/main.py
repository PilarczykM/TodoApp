import typer

from todo_app.application.commands import AddTaskCommand, AddTaskCommandHandler, EditTaskCommand, EditTaskCommandHandler
from todo_app.infrastructure.persistence.in_memory import InMemoryTaskRepository

app = typer.Typer()

task_repository = InMemoryTaskRepository()
add_task_command_handler = AddTaskCommandHandler(task_repository)
edit_task_command_handler = EditTaskCommandHandler(task_repository)


@app.command()
def add(task: str):
    """Add a new task."""
    command = AddTaskCommand(task)
    add_task_command_handler.handle(command)
    print(f"Task '{task}' added with ID: {command.task_id.value}.")


@app.command()
def edit(task_id: str, new_title: str):
    """Edit an existing task."""
    command = EditTaskCommand(task_id, new_title)
    edit_task_command_handler.handle(command)
    print(f"Task {task_id} edited to '{new_title}'.")


@app.command()
def remove(task_id: str):
    """Remove a task."""
    print(f"Task {task_id} removed.")
