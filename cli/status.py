# cli/status.py

from enum import IntEnum

class AuthStatus(IntEnum):
    SUCCESS = 0
    USER_EXISTS = 1
    USER_NOT_FOUND = 2
    WRONG_PASSWORD = 3