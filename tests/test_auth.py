# tests/test_auth.py

from services.auth_service import signup, login
import shutil
import os

def setup_function():
    # Antes de cada test, borramos la data vieja
    if os.path.exists("data/users.json"):
        shutil.rmtree("data")

def test_signup_and_login_success():
    assert signup("alice", "password123") is True
    assert login("alice", "password123") is True

def test_duplicate_signup_fails():
    assert signup("bob", "pass") is True
    assert signup("bob", "otra") is False

def test_login_wrong_password():
    assert signup("carol", "secret") is True
    assert login("carol", "wrong") is False

def test_login_nonexistent_user():
    assert login("noexiste", "nada") is False