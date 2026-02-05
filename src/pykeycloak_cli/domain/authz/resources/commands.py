# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.realm import Realm
from pykeycloak.factories import KeycloakServiceFactory
from typer import Context, Option, Typer

from .services import (
    _all,
    _get_resource_by_id,
    _get_resource_permissions_by_id,
)

app: Typer = Typer(help="Keycloak clients commands")


@app.command()
def all(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _all(
            service_factory=service_factory,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def resource(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    resource_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _get_resource_by_id(
            service_factory=service_factory,
            resource_id=resource_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def resource_permissions(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    resource_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _get_resource_permissions_by_id(
            service_factory=service_factory,
            resource_id=resource_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )
