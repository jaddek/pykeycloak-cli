# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.providers.queries import GetUsersQuery
from rich.console import Console
from rich.table import Table
from typer import Option, Typer

from ..factories import service_factory

app: Typer = Typer(help="Keycloak user commands")
console = Console()


@app.command()
def subset(
    realm: Annotated[str, Option(...)],
    limit: Annotated[int, Option(...)],
    offset: Annotated[int, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    asyncio.run(
        _subset_async(
            realm=realm,
            limit=limit,
            offset=offset,
            fields=fields,
            exclude=exclude_fields,
        )
    )


async def _subset_async(
    realm: str, limit: int, offset: int, fields: str | None, exclude: str | None
) -> None:
    default_headers = ["id", "email", "first_name", "last_name"]

    extra_fields = fields.split() if fields else []

    exclude_set = set(exclude.split()) if exclude else set()

    active_headers = [
        h for h in (default_headers + extra_fields) if h not in exclude_set
    ]

    factory = service_factory(kc_realm=realm)
    await factory.auth.client_login_async()

    user_list, users_count = await factory.users.get_users_async(
        GetUsersQuery(max=limit, first=offset)
    )

    table = Table(title=f"Users (Total: {users_count})")
    table.add_column("#", justify="center", style="dim")

    for header in active_headers:
        table.add_column(header, justify="left")

    for i, _user in enumerate(user_list, start=offset + 1):
        row_values = [str(getattr(_user, key, "—")) for key in active_headers]
        table.add_row(str(i), *row_values)

    console.print(table)


@app.command()
def all(
    realm: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
    frame: Annotated[int | None, Option()] = None,
) -> None:
    asyncio.run(
        _all_async(
            realm=realm,
            fields=fields,
            exclude=exclude_fields,
            frame=frame if frame else 100,
        )
    )


async def _all_async(
    realm: str, fields: str | None, exclude: str | None, frame: int = 100
) -> None:
    default_headers = ["id", "email", "first_name", "last_name"]

    extra_fields = fields.split() if fields else []

    exclude_set = set(exclude.split()) if exclude else set()

    active_headers = [
        h for h in (default_headers + extra_fields) if h not in exclude_set
    ]

    factory = service_factory(kc_realm=realm)
    await factory.auth.client_login_async()

    user_list, users_count = await factory.users.get_all_users_async()

    table = Table(title=f"Users (Total: {users_count})", style="dim")
    table.add_column("#", justify="center", style="dim")

    for header in active_headers:
        table.add_column(header, justify="left")

    for i, _user in enumerate(user_list, start=1):
        row_values = [str(getattr(_user, key, "—")) for key in active_headers]
        table.add_row(str(i), *row_values)

        if i % frame == 0:
            ...

    console.print(table)


@app.command()
def by_id(
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    asyncio.run(
        _by_id_async(
            realm=realm, user_id=user_id, fields=fields, exclude=exclude_fields
        )
    )


async def _by_id_async(
    realm: str, user_id: str, fields: str | None, exclude: str | None
) -> None:
    default_headers = ["id", "email", "first_name", "last_name"]

    extra_fields = fields.split() if fields else []

    exclude_set = set(exclude.split()) if exclude else set()

    active_headers = [
        h for h in (default_headers + extra_fields) if h not in exclude_set
    ]

    factory = service_factory(kc_realm=realm)
    await factory.auth.client_login_async()

    user = await factory.users.get_user_async(user_id=user_id)

    table = Table(title="Users (Total: 1)")
    table.add_column("#", justify="center", style="dim")

    for header in active_headers:
        table.add_column(header, justify="left")

    row_values = [str(getattr(user, key, "—")) for key in active_headers]
    table.add_row(str(1), *row_values)

    console.print(table)
