# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.factories import KeycloakServiceFactory
from pykeycloak.providers.payloads import UMAAuthorizationPayload
from rich.console import Console

console = Console()


async def _perms_async(
    service_factory: KeycloakServiceFactory,
    payload: UMAAuthorizationPayload,
) -> None:
    await service_factory.auth.client_login_async()

    permissions = await service_factory.uma.get_uma_permissions_async(payload=payload)

    console.print(permissions)
