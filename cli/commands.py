# cli/commands.py

import click
from cli.auth_cli import signup_cmd, login_cmd

@click.group()
def cli():
    """AuthGuard CLI - Gestor seguro de autenticación."""
    pass

# Registramos los subcomandos
cli.add_command(signup_cmd)
cli.add_command(login_cmd)

if __name__ == "__main__":
    cli()