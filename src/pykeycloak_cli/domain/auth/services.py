# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.factories import KeycloakServiceFactory
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
    service_factory: KeycloakServiceFactory,
    payload: UserCredentialsLoginPayload,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    token = await service_factory.auth.user_login_async(payload=payload)

    table = view_resource(
        resource=token,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _refresh_async(
    service_factory: KeycloakServiceFactory,
    payload: RefreshTokenPayload,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    token = await service_factory.auth.refresh_token_async(payload=payload)

    table = view_resource(
        resource=token,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _info_async(
    service_factory: KeycloakServiceFactory,
    access_token: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    info = await service_factory.auth.get_user_info_async(access_token=access_token)

    table = view_resource(
        resource=info,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _logout_async(
    service_factory: KeycloakServiceFactory,
    refresh_token: str,
) -> None:
    await service_factory.auth.client_login_async()

    await service_factory.auth.logout_async(refresh_token=refresh_token)

    console.print("ok")


async def _introspect_async(
    service_factory: KeycloakServiceFactory,
    payload: RTPIntrospectionPayload | TokenIntrospectionPayload,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    introspect = await service_factory.auth.introspect_token_async(payload=payload)

    table = view_resource(
        resource=introspect,
        fields=fields,
        exclude=exclude,
    )

    console.print(table)


async def _certs_async(
    service_factory: KeycloakServiceFactory,
) -> None:
    await service_factory.auth.client_login_async()

    certs = await service_factory.auth.get_certs_async()

    console.print(certs)


async def _revoke_async(
    service_factory: KeycloakServiceFactory,
    refresh_token: str,
) -> None:
    await service_factory.auth.client_login_async()

    await service_factory.auth.revoke_async(refresh_token=refresh_token)

    console.print("ok")
