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

from pykeycloak_cli.representation.users.console import view_user_list

from ...registry import KeycloakServiceFactory

console = Console()


async def _subset_async(
    service_factory: KeycloakServiceFactory,
    limit: int,
    offset: int,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service_factory.auth.client_login_async()

    users_list, users_count = await service_factory.users.get_users_async(
        GetUsersQuery(max=limit, first=offset)
    )

    table = view_user_list(
        users_list=enumerate(users_list, start=1),
        users_count=users_count,
        fields=fields,
        exclude=exclude,
        frame=frame,
    )

    console.print(table)


async def _all_async(
    service_factory: KeycloakServiceFactory,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service_factory.auth.client_login_async()

    users_list, users_count = await service_factory.users.get_all_users_async()

    table = view_user_list(
        users_list=enumerate(users_list, start=1),
        users_count=users_count,
        fields=fields,
        exclude=exclude,
        frame=frame,
    )

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
    user = await service_factory.users.get_user_async(user_id=user_id)

    table = view_user_list(
        users_list=enumerate([user], start=1),
        users_count=1 if user else 0,
        fields=fields,
        exclude=exclude,
    )

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

    user_id = await service_factory.users.create_user_async(
        payload=CreateUserPayload(username=username)
    )

    user = await service_factory.users.get_user_async(user_id=user_id)

    table = view_user_list(
        users_list=enumerate([user], start=1),
        users_count=1 if user is not None else 0,
        fields=None,
        exclude=None,
    )

    console.print(table)


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

    user = await service_factory.users.get_user_async(user_id=user_id)

    table = view_user_list(
        users_list=enumerate([user], start=1),
        users_count=1 if user is not None else 0,
        fields=None,
        exclude=None,
    )

    console.print(table)


async def _enable_async(service_factory: KeycloakServiceFactory, user_id: str) -> None:
    await service_factory.auth.client_login_async()
    await service_factory.users.enable_user_async(
        user_id=user_id, payload=UserUpdateEnablePayload(enabled=True)
    )

    user = await service_factory.users.get_user_async(user_id=user_id)

    table = view_user_list(
        users_list=enumerate([user], start=1),
        users_count=1 if user is not None else 0,
        fields="enabled",
        exclude=None,
    )

    console.print(table)


async def _disable_async(service_factory: KeycloakServiceFactory, user_id: str) -> None:
    await service_factory.auth.client_login_async()

    await service_factory.users.enable_user_async(
        user_id=user_id, payload=UserUpdateEnablePayload(enabled=False)
    )

    user = await service_factory.users.get_user_async(user_id=user_id)

    table = view_user_list(
        users_list=enumerate([user], start=1),
        users_count=1 if user is not None else 0,
        fields="enabled",
        exclude=None,
    )

    console.print(table)


async def _delete_async(service_factory: KeycloakServiceFactory, user_id: str) -> None:
    await service_factory.auth.client_login_async()
    await service_factory.users.delete_user_async(user_id=user_id)

    console.print("ok")


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

    console.print("ok")
