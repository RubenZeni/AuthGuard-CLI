# cli/task_cli.py

import click
from services.task_service import add_task, list_tasks, complete_task, delete_task
from cli.status import TaskStatus

@click.group(name="task")
def task_group():
    """Grupo de comandos para la gestión de tareas."""
    pass

@task_group.command(name="add")
@click.argument("username")
@click.argument("description")
def add_cmd(username: str, description: str):
    """
    Agrega una nueva tarea para el usuario.
    """
    status = add_task(username, description)
    if status == TaskStatus.SUCCESS:
        click.echo(f"✅ Tarea agregada para '{username}'.")
    else:
        click.echo("❌ No se pudo agregar la tarea.")
    raise SystemExit(status)

@task_group.command(name="list")
@click.argument("username")
def list_cmd(username: str):
    """
    Lista todas las tareas del usuario, mostrando estado.
    """
    tasks = list_tasks(username)
    if not tasks:
        click.echo("ℹ️ No hay tareas para este usuario.")
        raise SystemExit(TaskStatus.NO_TASKS)
    for t in tasks:
        mark = "✅" if t["done"] else "🔲"
        click.echo(f"{t['id']}. {t['desc']} {mark}")
    raise SystemExit(TaskStatus.SUCCESS)

@task_group.command(name="done")
@click.argument("username")
@click.argument("task_id", type=int)
def done_cmd(username: str, task_id: int):
    """
    Marca como completada la tarea indicada por task_id.
    """
    status = complete_task(username, task_id)
    if status == TaskStatus.SUCCESS:
        click.echo(f"✅ Tarea {task_id} marcada como completada.")
    elif status == TaskStatus.NO_TASKS:
        click.echo("⚠️ El usuario no tiene tareas.")
    else:
        click.echo("❌ Tarea no encontrada.")
    raise SystemExit(status)

@task_group.command(name="delete")
@click.argument("username")
@click.argument("task_id", type=int)
def delete_cmd(username: str, task_id: int):
    """
    Elimina la tarea indicada por task_id.
    """
    status = delete_task(username, task_id)
    if status == TaskStatus.SUCCESS:
        click.echo(f"🗑️ Tarea {task_id} eliminada.")
    elif status == TaskStatus.NO_TASKS:
        click.echo("⚠️ El usuario no tiene tareas.")
    else:
        click.echo("❌ Tarea no encontrada.")
    raise SystemExit(status)