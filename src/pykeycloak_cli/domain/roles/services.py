# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from uuid import UUID

from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from pykeycloak.providers.payloads import (
    RoleAssignPayload,
    RolePayload,
)
from rich.console import Console

console = Console()


async def _client_roles_async(
    service: KeycloakServiceFactoryProtocol,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    data = await service.roles.get_client_roles_async()

    console.print(data)


#
async def _role_by_name_async(
    service: KeycloakServiceFactoryProtocol,
    role_name: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    data = await service.roles.get_role_by_name_async(role_name=role_name)

    console.print(data)


async def _create_role_async(
    service: KeycloakServiceFactoryProtocol,
    payload: RolePayload,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    await service.roles.create_role_async(payload=payload)

    console.print("Ok")


async def _delete_role_by_id_async(
    service: KeycloakServiceFactoryProtocol,
    role_id: UUID,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    await service.roles.delete_role_by_id_async(role_id=role_id)

    console.print("Ok")


async def _delete_role_by_name_async(
    service: KeycloakServiceFactoryProtocol,
    role_name: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    await service.roles.delete_role_by_name_async(role_name=role_name)

    console.print("Ok")


async def _update_role_by_name_async(
    service: KeycloakServiceFactoryProtocol,
    role_name: str,
    payload: RolePayload,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    await service.roles.update_role_by_name_async(role_name=role_name, payload=payload)

    console.print("Ok")


#
async def _assign_client_role_async(
    service: KeycloakServiceFactoryProtocol,
    user_id: str,
    role_name: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    role = await service.roles.get_role_by_name_async(role_name=role_name)

    await service.roles.assign_role_async(
        user_id=user_id,
        roles=[
            RoleAssignPayload(
                id=role.get("id"),
                name=role.get("name"),
            )
        ],
    )

    console.print("Ok")


async def _user_composites_roles_async(
    service: KeycloakServiceFactoryProtocol,
    user_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    data = await service.roles.get_composite_client_roles_of_user_async(user_id=user_id)

    console.print(data)


async def _user_available_roles_async(
    service: KeycloakServiceFactoryProtocol,
    user_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    data = await service.roles.get_available_client_roles_of_user_async(user_id=user_id)

    console.print(data)


async def _unassign_client_role_async(
    service: KeycloakServiceFactoryProtocol,
    user_id: str,
    role_name: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    role = await service.roles.get_role_by_name_async(role_name=role_name)

    await service.roles.unassign_role_async(
        user_id=user_id,
        roles=[
            RoleAssignPayload(
                id=role.get("id"),
                name=role.get("name"),
            )
        ],
    )

    console.print("Ok")


async def _user_roles_async(
    service: KeycloakServiceFactoryProtocol,
    user_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    await service.roles.get_user_roles_async(user_id=user_id)

    console.print("Ok")
