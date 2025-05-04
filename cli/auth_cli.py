# cli/auth_cli.py

import click
from services.auth_service import signup as signup_service, login as login_service
from cli.status import AuthStatus

MESSAGES = {
    AuthStatus.SUCCESS: {
        "signup": "✅ Usuario '{user}' creado exitosamente.",
        "login": "🔐 Bienvenido/a, {user}."
    },
    AuthStatus.USER_EXISTS: "⚠️ Usuario '{user}' ya existe.",
    AuthStatus.USER_NOT_FOUND: "❌ Usuario '{user}' no encontrado.",
    AuthStatus.WRONG_PASSWORD: "❌ Contraseña incorrecta."
}

@click.command(name="signup")
@click.argument("username")
@click.argument("password")
def signup_cmd(username, password):
    """Registra un nuevo usuario."""
    status = signup_service(username, password)
    if status == AuthStatus.SUCCESS:
        click.echo(MESSAGES[status]["signup"].format(user=username))
    else:
        click.echo(MESSAGES[status].format(user=username))
    # Exit code = status value (0 para SUCCESS, >0 para errores)
    raise SystemExit(status)

@click.command(name="login")
@click.argument("username")
@click.argument("password")
def login_cmd(username, password):
    """Inicia sesión con un usuario existente."""
    status = login_service(username, password)
    if status == AuthStatus.SUCCESS:
        click.echo(MESSAGES[status]["login"].format(user=username))
    else:
        click.echo(MESSAGES[status].format(user=username))
    raise SystemExit(status)