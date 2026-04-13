# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from types import SimpleNamespace

import typer
from pykeycloak.core.realm import RealmClient
from pykeycloak.pykeycloak import PyKeycloak

from .domain.auth.commands import app as auth_app
from .domain.authz.permissions.commands import app as permissions_app
from .domain.authz.policies.commands import app as policies_app
from .domain.authz.resources.commands import app as resources_app
from .domain.authz.scopes.commands import app as scopes_app
from .domain.authz.settings.commands import app as settings_app
from .domain.clients.commands import app as clients_app
from .domain.roles.commands import app as roles_app
from .domain.sessions.commands import app as sessions_app
from .domain.uma.commands import app as uma_app
from .domain.users.commands import app as users_app

app = typer.Typer()


@app.callback()
def main(
    ctx: typer.Context,
    realm: str = typer.Option(
        ..., "--realm", "-r", envvar="KEYCLOAK_REALM", help="Keycloak realm name"
    ),
) -> None:
    __pkc = PyKeycloak()
    __pkc.register(key=realm, realm_client=RealmClient.from_env(client_name=realm))

    ctx.obj = SimpleNamespace(
        registry=__pkc,
        realm_otago=realm,
    )


app.add_typer(users_app, name="users")
app.add_typer(clients_app, name="clients")
app.add_typer(sessions_app, name="sessions")
app.add_typer(uma_app, name="uma")
app.add_typer(auth_app, name="auth")
app.add_typer(roles_app, name="roles")
app.add_typer(permissions_app, name="authz.permissions")
app.add_typer(policies_app, name="authz.policies")
app.add_typer(resources_app, name="authz.resources")
app.add_typer(scopes_app, name="authz.scopes")
app.add_typer(settings_app, name="authz.settings")
