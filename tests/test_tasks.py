# tests/test_tasks.py

from services.task_service import add_task, list_tasks, complete_task, delete_task
from cli.status import TaskStatus
import shutil, os

def setup_function():
    # Antes de cada test, limpiamos todo: usuarios y tareas
    if os.path.exists("data"):
        shutil.rmtree("data")

def test_add_and_list_tasks():
    assert add_task("u1", "t1") == TaskStatus.SUCCESS
    tasks = list_tasks("u1")
    assert len(tasks) == 1
    assert tasks[0]["desc"] == "t1"
    assert tasks[0]["done"] is False

def test_complete_and_delete_task():
    add_task("u1", "t1")
    assert complete_task("u1", 1) == TaskStatus.SUCCESS
    tasks = list_tasks("u1")
    assert tasks[0]["done"] is True

    # Eliminar
    assert delete_task("u1", 1) == TaskStatus.SUCCESS
    assert list_tasks("u1") == []