import typer

from todo_app.application.commands import AddTaskCommand, AddTaskCommandHandler, EditTaskCommand, EditTaskCommandHandler, RemoveTaskCommand, RemoveTaskCommandHandler, CompleteTaskCommand, CompleteTaskCommandHandler
from todo_app.application.queries import ListTasksQuery, ListTasksQueryHandler, ShowTaskQuery, ShowTaskQueryHandler
from todo_app.infrastructure.persistence.in_memory import InMemoryTaskRepository
from todo_app.domain.entities.task import TaskStatus

app = typer.Typer()

task_repository = InMemoryTaskRepository()
add_task_command_handler = AddTaskCommandHandler(task_repository)
edit_task_command_handler = EditTaskCommandHandler(task_repository)
remove_task_command_handler = RemoveTaskCommandHandler(task_repository)
complete_task_command_handler = CompleteTaskCommandHandler(task_repository)
list_tasks_query_handler = ListTasksQueryHandler(task_repository)
show_task_query_handler = ShowTaskQueryHandler(task_repository)


@app.command()
def add(task: str):
    """Add a new task."""
    command = AddTaskCommand(task)
    add_task_command_handler.handle(command)
    print(f"Task '{task}' added with ID: {command.task_id.value}.")


@app.command()
def edit(task_id: str, new_title: str):
    """Edit an existing task."""
    try:
        command = EditTaskCommand(task_id, new_title)
        edit_task_command_handler.handle(command)
        print(f"Task {task_id} edited to '{new_title}'.")
    except TaskNotFoundError as e:
        print(f"Error: {e}")


@app.command()
def remove(task_id: str):
    """Remove a task."""
    try:
        command = RemoveTaskCommand(task_id)
        remove_task_command_handler.handle(command)
        print(f"Task {task_id} removed.")
    except TaskNotFoundError as e:
        print(f"Error: {e}")


@app.command()
def complete(task_id: str):
    """Mark a task as completed."""
    try:
        command = CompleteTaskCommand(task_id)
        complete_task_command_handler.handle(command)
        print(f"Task {task_id} marked as completed.")
    except TaskNotFoundError as e:
        print(f"Error: {e}")


@app.command()
def list(status: TaskStatus = typer.Option(None, "--status", "-s", help="Filter tasks by status (pending or completed).")):
    """List all tasks."""
    query = ListTasksQuery(status=status)
    tasks = list_tasks_query_handler.handle(query)
    if tasks:
        for task in tasks:
            print(f"ID: {task.id.value} | Title: {task.title} | Status: {task.status.value.upper()}")
    else:
        print("No tasks found.")

@app.command()
def show(task_id: str):
    """Show details of a single task."""
    try:
        query = ShowTaskQuery(task_id)
        task = show_task_query_handler.handle(query)
        if task:
            print(f"ID: {task.id.value}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {task.status.value.upper()}")
        else:
            print(f"Task with ID {task_id} not found.")
    except TaskNotFoundError as e:
        print(f"Error: {e}")



