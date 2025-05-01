# services/auth_service.py

import json
from pathlib import Path
import bcrypt

# Definimos la ruta al archivo donde guardaremos usuarios
USERS_FILE = Path(__file__).parent.parent / "data" / "users.json"

def _load_users() -> dict:
    """
    Carga el diccionario de usuarios desde el JSON.
    Si el archivo no existe, devuelve un dict vacío.
    """
    if not USERS_FILE.exists():
        # Si no existe users.json, devolvemos {}
        return {}
    # Abrimos el archivo en modo lectura y parseamos el JSON
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Si está corrupto, renombramos y arrancamos limpio
            backup = USERS_FILE.with_suffix(".json.bak")
            USERS_FILE.rename(backup)
            return {}

def _save_users(users: dict) -> None:
    """
    Guarda el diccionario de usuarios en el JSON.
    Crea la carpeta data/ si no existe.
    """
    USERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    # Abrimos el archivo en modo escritura y volcamos el JSON
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

def signup(username: str, password: str) -> bool:
    """
    Registra un nuevo usuario:
    - Hace hash de la contraseña.
    - Guarda username: hashed_password en users.json.
    Devuelve True si fue exitoso, False si el usuario ya existe.
    """
    users = _load_users()
    if username in users:
        # No podemos re-crear un usuario existente
        return False

    # Generamos una salt aleatoria y hasheamos, codificando el password ya que bcrypt requiere bytes
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # Almacenamos el hash (en str) en el dict
    users[username] = {"password": hashed}
    _save_users(users)
    return True

def login(username: str, password: str) -> bool:
    """
    Verifica credenciales:
    - Carga el hash guardado para el username.
    - Compara con bcrypt.checkpw.
    Devuelve True si coincide, False en caso contrario o usuario inexistente.
    """
    users = _load_users()
    entry = users.get(username)
    if not entry:
        # Usuario no registrado
        return False

    # Convertimos el hash de nuevo a bytes
    hashed = entry["password"].encode("utf-8")
    # bcrypt.checkpw devuelve True si coinciden
    if bcrypt.checkpw(password.encode("utf-8"), hashed):
        return True
    return False