# cli/auth_cli.py

import click
from services.auth_service import signup as signup_service, login as login_service

@click.command(name="signup")
@click.argument("username")
@click.argument("password")
def signup_cmd(username, password):
    """Registra un nuevo usuario."""
    result = signup_service(username, password)
    click.echo(result)

@click.command(name="login")
@click.argument("username")
@click.argument("password")
def login_cmd(username, password):
    """Inicia sesión con un usuario existente."""
    result = login_service(username, password)
    click.echo(result)