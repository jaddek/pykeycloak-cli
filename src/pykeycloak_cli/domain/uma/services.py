# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from pykeycloak.providers.payloads import UMAAuthorizationPayload
from rich.console import Console

console = Console()


async def _perms_async(
    service: KeycloakServiceFactoryProtocol,
    payload: UMAAuthorizationPayload,
) -> None:
    await service.auth.client_login_async()

    permissions = await service.uma.get_uma_permissions_async(payload=payload)

    console.print(permissions)
