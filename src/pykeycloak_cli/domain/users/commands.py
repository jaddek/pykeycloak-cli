# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
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


@app.command()
def subset(
    ctx: Context,
    limit: Annotated[int, Option(...)],
    offset: Annotated[int, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _subset_async(
            service=service,
            limit=limit,
            offset=offset,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def all(
    ctx: Context,
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
    frame: Annotated[int | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _all_async(
            service=service,
            fields=fields,
            exclude=exclude_fields,
            frame=frame if frame else 100,
        )
    )


@app.command()
def count(
    ctx: Context,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _count_async(
            service=service,
        )
    )


@app.command()
def by_id(
    ctx: Context,
    user_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _by_id_async(
            service=service,
            user_id=user_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def by_role(
    ctx: Context,
    role: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _by_role_async(
            service=service,
            role=role,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def create(
    ctx: Context,
    username: Annotated[str, Option(...)],
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _create_async(
            service=service,
            username=username,
        )
    )


@app.command()
def update(
    ctx: Context,
    user_id: Annotated[str, Option(...)],
    first_name: Annotated[str, Option(...)],
    last_name: Annotated[str, Option(...)],
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _update_async(
            service=service,
            user_id=user_id,
            last_name=last_name,
            first_name=first_name,
        )
    )


@app.command()
def enable(
    ctx: Context,
    user_id: Annotated[str, Option(...)],
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(_enable_async(service=service, user_id=user_id))


@app.command()
def disable(
    ctx: Context,
    user_id: Annotated[str, Option(...)],
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _disable_async(
            service=service,
            user_id=user_id,
        )
    )


@app.command()
def delete(
    ctx: Context,
    user_id: Annotated[str, Option(...)],
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _delete_async(
            service=service,
            user_id=user_id,
        )
    )


@app.command()
def update_password(
    ctx: Context,
    user_id: Annotated[str, Option(...)],
    pwd: Annotated[str, Option(...)],
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(_update_password_async(service=service, user_id=user_id, pwd=pwd))
