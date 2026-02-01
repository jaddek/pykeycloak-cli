# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.realm import Realm
from pykeycloak.factories import KeycloakServiceFactory
from rich.console import Console
from typer import Context, Option, Typer

from .services import (
    _all_async,
    _by_id_async,
    _by_role_async,
    _count_async,
    _create_async,
    _delete_async,
    _disable_async,
    _enable_async,
    _subset_async,
    _update_async,
    _update_password_async,
)

app: Typer = Typer(help="Keycloak user commands")
console = Console()


@app.command()
def subset(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    limit: Annotated[int, Option(...)],
    offset: Annotated[int, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _subset_async(
            service_factory=service_factory,
            limit=limit,
            offset=offset,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def all(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
    frame: Annotated[int | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _all_async(
            service_factory=service_factory,
            fields=fields,
            exclude=exclude_fields,
            frame=frame if frame else 100,
        )
    )


@app.command()
def count(
    ctx: Context,
    realm: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _count_async(
            service_factory=service_factory,
        )
    )


@app.command()
def by_id(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _by_id_async(
            service_factory=service_factory,
            user_id=user_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def by_role(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    role: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _by_role_async(
            service_factory=service_factory,
            role=role,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def create(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    username: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _create_async(
            service_factory=service_factory,
            username=username,
        )
    )


@app.command()
def update(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    first_name: Annotated[str, Option(...)],
    last_name: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _update_async(
            service_factory=service_factory,
            user_id=user_id,
            last_name=last_name,
            first_name=first_name,
        )
    )


@app.command()
def enable(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(_enable_async(service_factory=service_factory, user_id=user_id))


@app.command()
def disable(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _disable_async(
            service_factory=service_factory,
            user_id=user_id,
        )
    )


@app.command()
def delete(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _delete_async(
            service_factory=service_factory,
            user_id=user_id,
        )
    )


@app.command()
def update_password(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    pwd: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _update_password_async(
            service_factory=service_factory, user_id=user_id, pwd=pwd
        )
    )
