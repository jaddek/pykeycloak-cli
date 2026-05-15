# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from pykeycloak.services.representations import ClientRepresentation
from rich.console import Console

from pykeycloak_cli.representations.console_utils import view_resource_list

console = Console()


async def _all(
    service: KeycloakServiceFactoryProtocol,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    clients = await service.clients.get_clients_async()

    table = view_resource_list(
        resource_type=ClientRepresentation,
        resource_list=clients,
        resource_count=len(clients),
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _client(
    service: KeycloakServiceFactoryProtocol,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    client = await service.clients.get_client_async()

    table = view_resource_list(
        resource_type=ClientRepresentation,
        resource_list=[client],
        resource_count=1 if client else 0,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)
