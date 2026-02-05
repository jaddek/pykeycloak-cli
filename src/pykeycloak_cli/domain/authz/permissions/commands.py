# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.realm import Realm
from pykeycloak.factories import KeycloakServiceFactory
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
    realm: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _all_async(
            service_factory=service_factory,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def permission_on_resource(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    permission_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _get_permission_based_on_resource_async(
            service_factory=service_factory,
            permission_id=permission_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def permission_on_scope(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    permission_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _get_permission_based_on_scope_async(
            service_factory=service_factory,
            permission_id=permission_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )
