# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from pykeycloak.providers.payloads import (
    RefreshTokenPayload,
    RTPIntrospectionPayload,
    TokenIntrospectionPayload,
    UserCredentialsLoginPayload,
)
from rich.console import Console

from pykeycloak_cli.representations.console_utils import view_resource

console = Console()


async def _login_async(
    service: KeycloakServiceFactoryProtocol,
    payload: UserCredentialsLoginPayload,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    token = await service.auth.user_login_async(payload=payload)

    table = view_resource(
        resource=token,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _refresh_async(
    service: KeycloakServiceFactoryProtocol,
    payload: RefreshTokenPayload,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    token = await service.auth.refresh_token_async(payload=payload)

    table = view_resource(
        resource=token,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _info_async(
    service: KeycloakServiceFactoryProtocol,
    access_token: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    info = await service.auth.get_user_info_async(access_token=access_token)

    table = view_resource(
        resource=info,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _logout_async(
    service: KeycloakServiceFactoryProtocol,
    refresh_token: str,
) -> None:
    await service.auth.client_login_async()

    await service.auth.logout_async(refresh_token=refresh_token)

    console.print("ok")


async def _introspect_async(
    service: KeycloakServiceFactoryProtocol,
    payload: RTPIntrospectionPayload | TokenIntrospectionPayload,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service.auth.client_login_async()

    introspect = await service.auth.introspect_token_async(payload=payload)

    table = view_resource(
        resource=introspect,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _certs_async(
    service: KeycloakServiceFactoryProtocol,
) -> None:
    await service.auth.client_login_async()

    certs = await service.well_known.get_certs_async()

    console.print(certs)


async def _revoke_async(
    service: KeycloakServiceFactoryProtocol,
    refresh_token: str,
) -> None:
    await service.auth.client_login_async()

    await service.auth.revoke_async(refresh_token=refresh_token)

    console.print("ok")
