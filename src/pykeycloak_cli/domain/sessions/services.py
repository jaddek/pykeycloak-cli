# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.factories import KeycloakServiceFactory
from pykeycloak.services.representations import SessionRepresentation
from rich.console import Console

from pykeycloak_cli.representations.console_utils import view_resource_list

console = Console()


async def _all_async(
    service_factory: KeycloakServiceFactory,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service_factory.auth.client_login_async()

    sessions_list = await service_factory.sessions.get_client_sessions_async()

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
    service_factory: KeycloakServiceFactory,
) -> None:
    await service_factory.auth.client_login_async()

    count = await service_factory.sessions.get_client_sessions_count_async()

    console.print(count)


async def _stats_async(
    service_factory: KeycloakServiceFactory,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service_factory.auth.client_login_async()

    sessions_list = await service_factory.sessions.get_client_session_stats_async()

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
    service_factory: KeycloakServiceFactory,
    user_id: str,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service_factory.auth.client_login_async()

    sessions_list = (
        await service_factory.sessions.get_client_user_offline_sessions_async(
            user_id=user_id
        )
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
    service_factory: KeycloakServiceFactory,
    user_id: str,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service_factory.auth.client_login_async()

    sessions_list = await service_factory.sessions.get_user_sessions_async(
        user_id=user_id
    )

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
    service_factory: KeycloakServiceFactory,
    session_id: str,
    is_offline: bool = False,
) -> None:
    await service_factory.auth.client_login_async()

    await service_factory.sessions.delete_session_by_id_async(
        session_id=session_id, is_offline=is_offline
    )

    console.print("ok")


async def _delete_all_sessions_async(
    service_factory: KeycloakServiceFactory,
) -> None:
    await service_factory.auth.client_login_async()

    await service_factory.sessions.logout_all_users_async()

    console.print("ok")


async def _client_async(
    service_factory: KeycloakServiceFactory,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> None:
    await service_factory.auth.client_login_async()

    # Assuming there's a method to get client sessions for the current client
    # This might need adjustment based on the actual Keycloak API
    sessions_list = await service_factory.sessions.get_client_sessions_async()

    table = view_resource_list(
        resource_type=SessionRepresentation,
        resource_list=enumerate(sessions_list, start=1),
        resource_count=len(sessions_list),
        fields=fields,
        exclude=exclude,
        frame=frame,
    )

    console.print(table)
