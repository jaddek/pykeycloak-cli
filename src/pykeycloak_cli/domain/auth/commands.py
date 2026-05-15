# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
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
    username: Annotated[str, Option(...)],
    password: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _login_async(
            service=service,
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
    refresh_token: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _refresh_async(
            service=service,
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
    access_token: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _info_async(
            service=service,
            access_token=access_token,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def logout(
    ctx: Context,
    refresh_token: Annotated[str, Option(...)],
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _logout_async(
            service=service,
            refresh_token=refresh_token,
        )
    )


@app.command()
def introspect_rtp(
    ctx: Context,
    token: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _introspect_async(
            service=service,
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
    access_token: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _introspect_async(
            service=service,
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
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _certs_async(
            service=service,
        )
    )


@app.command()
def revoke(
    ctx: Context,
    refresh_token: Annotated[str, Option(...)],
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _revoke_async(
            service=service,
            refresh_token=refresh_token,
        )
    )
