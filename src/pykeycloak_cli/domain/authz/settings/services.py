# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from rich.console import Console

from pykeycloak_cli.representations.console_utils import view_resource

console = Console()


async def _all(
    service: KeycloakServiceFactoryProtocol,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    data = await service.authz.get_client_authz_settings_async()

    table = view_resource(
        resource=data,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)
