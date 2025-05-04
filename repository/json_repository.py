# repository/json_repository.py

import json
from pathlib import Path
from cli.status import TaskStatus

class TaskRepository:
    """
    Repositorio que gestiona la persistencia de tareas en un archivo JSON.
    Cada usuario tiene su propia lista de tareas bajo su clave de username.
    """

    def __init__(self):
        # Definimos la ruta al archivo donde guardaremos tareas
        self.file = Path(__file__).parent.parent / "data" / "tasks.json"

    def _load(self) -> dict:
        """
        Carga y devuelve el diccionario completo de datos de tareas.
        Si el archivo no existe o está vacío, devuelve {}.
        """
        if not self.file.exists():
        # Si no existe users.json, devolvemos {}
            return {}
    # Abrimos el archivo en modo lectura y parseamos el JSON
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Si JSON corrupto, renombrar backup y comenzar limpio
            backup = self.file.with_suffix(".json.bak")
            self.file.rename(backup)
            return {}

    def _save(self, tasks: dict) -> None:
        """
        Guarda en disco el diccionario de datos de tareas.
        Crea la carpeta data/ si no existe.
        """
        self.file.parent.mkdir(parents=True, exist_ok=True)
        # Abrimos el archivo en modo escritura y volcamos el JSON
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)

    def add(self, user: str, desc: str) -> TaskStatus:
        """
        Agrega una nueva tarea para el usuario.
        Genera un ID incremental.
        """
        data = self._load()
        tasks = data.setdefault(user, [])
        new_id = (tasks[-1]["id"] + 1) if tasks else 1
        tasks.append({"id": new_id, "desc": desc, "done": False})
        self._save(data)
        return TaskStatus.SUCCESS

    def list(self, user: str) -> list[dict]:
        """
        Devuelve la lista de tareas para el usuario.
        Si no hay usuario, devuelve lista vacía.
        """
        data = self._load()
        return data.get(user, [])

    def complete(self, user: str, tid: int) -> TaskStatus:
        """
        Marca como completada la tarea con ID `tid` del usuario.
        """
        data = self._load()
        tasks = data.get(user)
        if not tasks:
            return TaskStatus.NO_TASKS
        for task in tasks:
            if task["id"] == tid:
                task["done"] = True
                self._save(data)
                return TaskStatus.SUCCESS
        return TaskStatus.NOT_FOUND

    def delete(self, user: str, tid: int) -> TaskStatus:
        """
        Elimina la tarea con ID `tid` del usuario.
        """
        data = self._load()
        tasks = data.get(user)
        if not tasks:
            return TaskStatus.NO_TASKS
        filtered = [t for t in tasks if t["id"] != tid]
        if len(filtered) == len(tasks):
            return TaskStatus.NOT_FOUND
        data[user] = filtered
        self._save(data)
        return TaskStatus.SUCCESS