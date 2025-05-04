# services/task_service.py

from repository.json_repository import TaskRepository
from cli.status import TaskStatus

# Instanciamos un repositorio (debería ser apuntando al JSON de tareas, pero próximamente...)
repo = TaskRepository()

def add_task(username: str, description: str) -> TaskStatus:
    """
    Servicio para agregar una tarea a un usuario.
    Devuelve TaskStatus.SUCCESS siempre que el repositorio funcione.
    """
    return repo.add(username, description)

def list_tasks(username: str) -> list[dict]:
    """
    Servicio para obtener las tareas de un usuario.
    """
    return repo.list(username)

def complete_task(username: str, task_id: int) -> TaskStatus:
    """
    Servicio para marcar una tarea como completada.
    Devuelve TaskStatus.SUCCESS, NO_TASKS o NOT_FOUND según proceda.
    """
    return repo.complete(username, task_id)

def delete_task(username: str, task_id: int) -> TaskStatus:
    """
    Servicio para eliminar una tarea.
    Devuelve TaskStatus.SUCCESS, NO_TASKS o NOT_FOUND según proceda.
    """
    return repo.delete(username, task_id)