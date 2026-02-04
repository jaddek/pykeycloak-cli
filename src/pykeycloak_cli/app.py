# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from types import SimpleNamespace

import typer
from pykeycloak.core.headers import HeadersFactory
from pykeycloak.core.realm import Realm, RealmClient
from pykeycloak.core.validator import KeycloakResponseValidator
from pykeycloak.dependancies import get_keycloak_client_wrapper_from_env
from pykeycloak.factories import KeycloakServiceFactory
from pykeycloak.providers.providers import KeycloakInMemoryProviderAsync

from .domain.auth.commands import app as auth_app
from .domain.clients.commands import app as clients_app
from .domain.sessions.commands import app as sessions_app
from .domain.uma.commands import app as uma_app
from .domain.users.commands import app as users_app
from .registry import KeycloakServiceRegistry

app = typer.Typer()


@app.callback()
def main(ctx: typer.Context) -> None:
    registry = KeycloakServiceRegistry()

    realm = Realm(name="otago")

    service_factory = KeycloakServiceFactory(
        provider=KeycloakInMemoryProviderAsync(
            realm=realm,
            realm_client=RealmClient.from_env(),
            headers=HeadersFactory(),
            wrapper=get_keycloak_client_wrapper_from_env(),
        ),
        validator=KeycloakResponseValidator(),
    )

    registry.register(realm=realm, factory=service_factory)

    ctx.obj = SimpleNamespace(
        registry=registry,
        realm_otago=realm,
    )


app.add_typer(users_app, name="users")
app.add_typer(clients_app, name="clients")
app.add_typer(sessions_app, name="sessions")
app.add_typer(uma_app, name="uma")
app.add_typer(auth_app, name="auth")
