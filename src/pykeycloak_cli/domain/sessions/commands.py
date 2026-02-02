# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.realm import Realm
from pykeycloak.factories import KeycloakServiceFactory
from typer import Context, Option, Typer

from .services import (
    _all_async,
    _count_async,
    _delete_all_sessions_async,
    _delete_session_by_id_async,
    _offline_sessions_async,
    _stats_async,
    _user_sessions_async,
)

app: Typer = Typer(help="Keycloak Session commands")


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
def stats(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
    frame: Annotated[int | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _stats_async(
            service_factory=service_factory,
            fields=fields,
            exclude=exclude_fields,
            frame=frame if frame else 100,
        )
    )


@app.command()
def offline(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
    frame: Annotated[int | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _offline_sessions_async(
            user_id=user_id,
            service_factory=service_factory,
            fields=fields,
            exclude=exclude_fields,
            frame=frame if frame else 100,
        )
    )


@app.command()
def user(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
    frame: Annotated[int | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _user_sessions_async(
            service_factory=service_factory,
            user_id=user_id,
            fields=fields,
            exclude=exclude_fields,
            frame=frame if frame else 100,
        )
    )


@app.command()
def delete_by_id(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    session_id: Annotated[str, Option(...)],
    is_offline: Annotated[bool, Option()] = True,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _delete_session_by_id_async(
            service_factory=service_factory,
            session_id=session_id,
            is_offline=is_offline,
        )
    )


@app.command()
def delete_all(
    ctx: Context,
    realm: Annotated[str, Option(...)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _delete_all_sessions_async(
            service_factory=service_factory,
        )
    )
