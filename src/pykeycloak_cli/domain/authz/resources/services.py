# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from rich.console import Console

console = Console()


async def _all(
    service: KeycloakServiceFactoryProtocol,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    clients = await service.authz_resource.get_resources_async()

    console.print(clients)


async def _get_resource_by_id(
    service: KeycloakServiceFactoryProtocol,
    resource_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    data = await service.authz_resource.get_resource_by_id_async(
        resource_id=resource_id
    )

    console.print(data)


async def _get_resource_permissions_by_id(
    service: KeycloakServiceFactoryProtocol,
    resource_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    data = await service.authz_resource.get_resource_permissions_async(
        resource_id=resource_id
    )

    console.print(data)
