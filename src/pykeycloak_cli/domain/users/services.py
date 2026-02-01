# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.providers.payloads import (
    CreateUserPayload,
    PasswordCredentialsPayload,
    UpdateUserPayload,
    UserUpdateEnablePayload,
    UserUpdatePasswordPayload,
)
from pykeycloak.providers.queries import GetUsersQuery
from rich.console import Console
from rich.table import Table
from typer import Typer

from ...registry import KeycloakServiceFactory

app: Typer = Typer(help="Keycloak user commands")
console = Console()


async def _subset_async(
    service_factory: KeycloakServiceFactory,
    limit: int,
    offset: int,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    default_headers = ["id", "email", "first_name", "last_name"]

    extra_fields = fields.split() if fields else []

    exclude_set = set(exclude.split()) if exclude else set()

    active_headers = [
        h for h in (default_headers + extra_fields) if h not in exclude_set
    ]

    user_list, users_count = await service_factory.users.get_users_async(
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


async def _all_async(
    service_factory: KeycloakServiceFactory,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service_factory.auth.client_login_async()

    default_headers = ["id", "email", "first_name", "last_name"]

    extra_fields = fields.split() if fields else []

    exclude_set = set(exclude.split()) if exclude else set()

    active_headers = [
        h for h in (default_headers + extra_fields) if h not in exclude_set
    ]

    user_list, users_count = await service_factory.users.get_all_users_async()

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


async def _count_async(
    service_factory: KeycloakServiceFactory,
) -> None:
    await service_factory.auth.client_login_async()

    count = await service_factory.users.get_users_count_async()

    console.print(count)


async def _by_id_async(
    service_factory: KeycloakServiceFactory,
    user_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    default_headers = ["id", "email", "first_name", "last_name"]

    extra_fields = fields.split() if fields else []

    exclude_set = set(exclude.split()) if exclude else set()

    active_headers = [
        h for h in (default_headers + extra_fields) if h not in exclude_set
    ]

    user = await service_factory.users.get_user_async(user_id=user_id)

    table = Table(title="Users (Total: 1)")
    table.add_column("#", justify="center", style="dim")

    for header in active_headers:
        table.add_column(header, justify="left")

    row_values = [str(getattr(user, key, "—")) for key in active_headers]
    table.add_row(str(1), *row_values)

    console.print(table)


async def _by_role_async(
    service_factory: KeycloakServiceFactory,
    role: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    ...


async def _create_async(service_factory: KeycloakServiceFactory, username: str) -> None:
    await service_factory.auth.client_login_async()

    result = await service_factory.users.create_user_async(
        payload=CreateUserPayload(username=username)
    )

    console.print(f"Created user Id: {result}")


async def _update_async(
    service_factory: KeycloakServiceFactory,
    user_id: str,
    first_name: str | None,
    last_name: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    await service_factory.users.update_user_async(
        user_id=user_id,
        payload=UpdateUserPayload(first_name=first_name, last_name=last_name),
    )

    await _by_id_async(service_factory, user_id=user_id, fields=None, exclude=None)


async def _enable_async(service_factory: KeycloakServiceFactory, user_id: str) -> None:
    await service_factory.auth.client_login_async()
    await service_factory.users.enable_user_async(
        user_id=user_id, payload=UserUpdateEnablePayload(enabled=True)
    )


async def _disable_async(service_factory: KeycloakServiceFactory, user_id: str) -> None:
    await service_factory.auth.client_login_async()

    await service_factory.users.enable_user_async(
        user_id=user_id, payload=UserUpdateEnablePayload(enabled=False)
    )


async def _delete_async(service_factory: KeycloakServiceFactory, user_id: str) -> None:
    await service_factory.auth.client_login_async()
    await service_factory.users.delete_user_async(user_id=user_id)


async def _update_password_async(
    service_factory: KeycloakServiceFactory, user_id: str, pwd: str
) -> None:
    await service_factory.auth.client_login_async()

    await service_factory.users.update_user_password_async(
        user_id=user_id,
        payload=UserUpdatePasswordPayload(
            credentials=[
                PasswordCredentialsPayload(
                    value=pwd,
                ).to_dict()
            ]
        ),
    )
