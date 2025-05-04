# cli/status.py

from enum import IntEnum

class AuthStatus(IntEnum):
    """Códigos de resultado para operaciones de autenticación."""
    SUCCESS = 0
    USER_EXISTS = 1
    USER_NOT_FOUND = 2
    WRONG_PASSWORD = 3

class TaskStatus(IntEnum):
    """Códigos de resultado para operaciones de gestión de tareas."""
    SUCCESS = 0
    NOT_FOUND = 1
    NO_TASKS = 2