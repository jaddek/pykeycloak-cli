# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.factories import KeycloakServiceFactory
from pykeycloak.services.representations import PermissionRepresentation
from rich.console import Console

from pykeycloak_cli.representations.console_utils import view_resource_list

console = Console()


async def _all_async(
    service_factory: KeycloakServiceFactory,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    data = await service_factory.authz_permission.get_permissions_async()

    table = view_resource_list(
        resource_type=PermissionRepresentation,
        resource_list=enumerate(data, start=1),
        resource_count=len(data),
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _get_permission_based_on_resource_async(
    service_factory: KeycloakServiceFactory,
    permission_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    data = await service_factory.authz_permission.get_permission_based_on_resource_by_id_async(
        permission_id=permission_id
    )

    console.print(data)


async def _get_permission_based_on_scope_async(
    service_factory: KeycloakServiceFactory,
    permission_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    data = await service_factory.authz_permission.get_permission_based_on_scope_by_id_async(
        permission_id=permission_id
    )

    console.print(data)
