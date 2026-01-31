import typer

from pykeycloak_cli.commands.users import app as users_app

app = typer.Typer()

app.add_typer(users_app, name="users")

if __name__ == "__main__":
    app()
