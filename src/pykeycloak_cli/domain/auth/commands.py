# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.realm import Realm
from pykeycloak.factories import KeycloakServiceFactory
from pykeycloak.providers.payloads import (
    RefreshTokenPayload,
    RTPIntrospectionPayload,
    TokenIntrospectionPayload,
    UserCredentialsLoginPayload,
)
from typer import Context, Option, Typer

from .services import (
    _certs_async,
    _info_async,
    _introspect_async,
    _login_async,
    _logout_async,
    _refresh_async,
    _revoke_async,
)

app: Typer = Typer(help="Keycloak Login commands")


@app.command()
def login(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    username: Annotated[str, Option(...)],
    password: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _login_async(
            service_factory=service_factory,
            payload=UserCredentialsLoginPayload(
                username=username,
                password=password,
            ),
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def refresh(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    refresh_token: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _refresh_async(
            service_factory=service_factory,
            payload=RefreshTokenPayload(
                refresh_token=refresh_token,
            ),
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def info(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    access_token: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _info_async(
            service_factory=service_factory,
            access_token=access_token,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def logout(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    refresh_token: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _logout_async(
            service_factory=service_factory,
            refresh_token=refresh_token,
        )
    )


@app.command()
def introspect_rtp(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    token: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _introspect_async(
            service_factory=service_factory,
            payload=RTPIntrospectionPayload(
                token=token,
            ),
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def introspect_token(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    access_token: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _introspect_async(
            service_factory=service_factory,
            payload=TokenIntrospectionPayload(
                token=access_token,
            ),
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def certs(
    ctx: Context,
    realm: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _certs_async(
            service_factory=service_factory,
        )
    )


@app.command()
def revoke(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    refresh_token: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _revoke_async(
            service_factory=service_factory,
            refresh_token=refresh_token,
        )
    )
