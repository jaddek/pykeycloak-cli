# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from pykeycloak.services.representations import SessionRepresentation
from rich.console import Console

from pykeycloak_cli.representations.console_utils import view_resource_list

console = Console()


async def _all_async(
    service: KeycloakServiceFactoryProtocol,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service.auth.client_login_async()

    sessions_list = await service.sessions.get_client_sessions_async()

    table = view_resource_list(
        resource_type=SessionRepresentation,
        resource_list=enumerate(sessions_list, start=1),
        resource_count=len(sessions_list),
        fields=fields,
        exclude=exclude,
        frame=frame,
    )

    console.print(table)


async def _count_async(
    service: KeycloakServiceFactoryProtocol,
) -> None:
    await service.auth.client_login_async()

    count = await service.sessions.get_client_sessions_count_async()

    console.print(count)


async def _stats_async(
    service: KeycloakServiceFactoryProtocol,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service.auth.client_login_async()

    sessions_list = await service.sessions.get_client_session_stats_async()

    table = view_resource_list(
        resource_type=SessionRepresentation,
        resource_list=enumerate(sessions_list, start=1),
        resource_count=len(sessions_list),
        fields=fields,
        exclude=exclude,
        frame=frame,
    )

    console.print(table)


async def _offline_sessions_async(
    service: KeycloakServiceFactoryProtocol,
    user_id: str,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service.auth.client_login_async()

    sessions_list = await service.sessions.get_client_user_offline_sessions_async(
        user_id=user_id
    )

    table = view_resource_list(
        resource_type=SessionRepresentation,
        resource_list=enumerate([sessions_list], start=1),
        resource_count=len([sessions_list]),
        fields=fields,
        exclude=exclude,
        frame=frame,
    )

    console.print(table)


async def _user_sessions_async(
    service: KeycloakServiceFactoryProtocol,
    user_id: str,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service.auth.client_login_async()

    sessions_list = await service.sessions.get_user_sessions_async(user_id=user_id)

    table = view_resource_list(
        resource_type=SessionRepresentation,
        resource_list=enumerate(sessions_list, start=1),
        resource_count=len(sessions_list),
        fields=fields,
        exclude=exclude,
        frame=frame,
    )

    console.print(table)


async def _delete_session_by_id_async(
    service: KeycloakServiceFactoryProtocol,
    session_id: str,
    is_offline: bool = False,
) -> None:
    await service.auth.client_login_async()

    await service.sessions.delete_session_by_id_async(
        session_id=session_id, is_offline=is_offline
    )

    console.print("ok")


async def _delete_all_sessions_async(
    service: KeycloakServiceFactoryProtocol,
) -> None:
    await service.auth.client_login_async()

    await service.sessions.logout_all_users_async()

    console.print("ok")


async def _delete_users_sessions_async(
    service: KeycloakServiceFactoryProtocol,
    user_id: str,
) -> None:
    await service.auth.client_login_async()

    await service.sessions.remove_user_sessions_raw_async(user_id=user_id)


async def _client_async(
    service: KeycloakServiceFactoryProtocol,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service.auth.client_login_async()

    sessions_list = await service.sessions.get_client_sessions_async()

    table = view_resource_list(
        resource_type=SessionRepresentation,
        resource_list=enumerate(sessions_list, start=1),
        resource_count=len(sessions_list),
        fields=fields,
        exclude=exclude,
        frame=frame,
    )

    console.print(table)
