# tests/test_auth.py

from services.auth_service import signup, login
from cli.status import AuthStatus
import shutil, os

def setup_function():
    # Antes de cada test, borramos la carpeta data completa
    if os.path.exists("data"):
        shutil.rmtree("data")

def test_signup_and_login_success():
    assert signup("alice", "password123") == AuthStatus.SUCCESS
    assert login("alice", "password123") == AuthStatus.SUCCESS

def test_duplicate_signup_fails():
    assert signup("bob", "pass") == AuthStatus.SUCCESS
    assert signup("bob", "otra") == AuthStatus.USER_EXISTS

def test_login_wrong_password():
    assert signup("carol", "secret") == AuthStatus.SUCCESS
    assert login("carol", "wrong") == AuthStatus.WRONG_PASSWORD

def test_login_nonexistent_user():
    assert login("noexiste", "nada") == AuthStatus.USER_NOT_FOUND