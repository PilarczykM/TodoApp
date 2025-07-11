import typer
from rich.console import Console
from rich.table import Table

from todo_app.application.commands import (
    AddTaskCommand,
    AddTaskCommandHandler,
    CompleteTaskCommand,
    CompleteTaskCommandHandler,
    EditTaskCommand,
    EditTaskCommandHandler,
    RemoveTaskCommand,
    RemoveTaskCommandHandler,
)
from todo_app.application.exceptions import TaskNotFoundError
from todo_app.application.queries import (
    ListTasksQuery,
    ListTasksQueryHandler,
    ShowTaskQuery,
    ShowTaskQueryHandler,
)
from todo_app.domain.entities.task import TaskStatus
from todo_app.infrastructure.persistence.in_memory import InMemoryTaskRepository

console = Console()

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
    console.print(
        f"[green]Task '{task}' added with ID: {command.task_id.value}.[/green]"
    )


@app.command()
def edit(task_id: str, new_title: str):
    """Edit an existing task."""
    try:
        command = EditTaskCommand(task_id, new_title)
        edit_task_command_handler.handle(command)
        console.print(f"[green]Task {task_id} edited to '{new_title}'.[/green]")
    except TaskNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")


@app.command()
def remove(task_id: str):
    """Remove a task."""
    try:
        command = RemoveTaskCommand(task_id)
        remove_task_command_handler.handle(command)
        console.print(f"[green]Task {task_id} removed.[/green]")
    except TaskNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")


@app.command()
def complete(task_id: str):
    """Mark a task as completed."""
    try:
        command = CompleteTaskCommand(task_id)
        complete_task_command_handler.handle(command)
        console.print(f"[green]Task {task_id} marked as completed.[/green]")
    except TaskNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")


@app.command()
def list(
    status: TaskStatus = typer.Option(
        None, "--status", "-s", help="Filter tasks by status (pending or completed)."
    ),
):
    """List all tasks."""
    query = ListTasksQuery(status=status)
    tasks = list_tasks_query_handler.handle(query)
    if tasks:
        table = Table(title="[bold blue]Your Tasks[/bold blue]")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Status", style="green")

        for task in tasks:
            status_color = "green" if task.status == TaskStatus.COMPLETED else "yellow"
            table.add_row(
                str(task.id.value),
                task.title,
                f"[{status_color}]{task.status.value.upper()}[/{status_color}]",
            )
        console.print(table)
    else:
        console.print("[yellow]No tasks found.[/yellow]")


@app.command()
def show(task_id: str):
    """Show details of a single task."""
    try:
        query = ShowTaskQuery(task_id)
        task = show_task_query_handler.handle(query)
        if task:
            console.print(
                "[bold blue]Task Details:[/bold blue]"
            )
            console.print(f"  [cyan]ID:[/cyan] {task.id.value}")
            console.print(f"  [magenta]Title:[/magenta] {task.title}")
            console.print(f"  [yellow]Description:[/yellow] {task.description}")
            status_color = "green" if task.status == TaskStatus.COMPLETED else "yellow"
            console.print(
                f"  [green]Status:[/green] "
                f"[{status_color}]{task.status.value.upper()}[/{status_color}]"
            )
        else:
            console.print(f"[red]Task with ID {task_id} not found.[/red]")
    except TaskNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
