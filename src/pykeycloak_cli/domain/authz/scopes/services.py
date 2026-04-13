# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from pykeycloak.services.representations import ScopeRepresentation
from rich.console import Console

from pykeycloak_cli.representations.console_utils import view_resource_list

console = Console()


async def _all(
    service: KeycloakServiceFactoryProtocol,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    data = await service.authz_scope.get_client_authz_scopes_async()

    table = view_resource_list(
        resource_type=ScopeRepresentation,
        resource_list=enumerate(data, start=1),
        resource_count=len(data),
        fields=fields,
        exclude=exclude,
    )

    console.print(table)
