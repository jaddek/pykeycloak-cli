# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from typer import Context, Option, Typer

from .services import (
    _all_async,
    _get_permission_based_on_resource_async,
    _get_permission_based_on_scope_async,
)

app: Typer = Typer(help="Keycloak Authz Permissions commands")


@app.command()
def all(
    ctx: Context,
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _all_async(
            service=service,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def permission_on_resource(
    ctx: Context,
    permission_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _get_permission_based_on_resource_async(
            service=service,
            permission_id=permission_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def permission_on_scope(
    ctx: Context,
    permission_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    asyncio.run(
        _get_permission_based_on_scope_async(
            service=service,
            permission_id=permission_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )
