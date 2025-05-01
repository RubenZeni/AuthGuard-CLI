# services/auth_service.py

import bcrypt
import json
from pathlib import Path

# (más adelante iremos completando esta lógica)
def signup(username: str, password: str) -> bool:
    """
    Crea un nuevo usuario con password hasheado.
    Por ahora devuelve True como placeholder.
    """
    return True

def login(username: str, password: str) -> bool:
    """
    Verifica credenciales de usuario.
    Por ahora devuelve True como placeholder.
    """
    return True
