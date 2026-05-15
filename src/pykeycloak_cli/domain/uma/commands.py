# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

import typer
from pykeycloak.core.enums import (
    UrnIetfOauthUmaTicketPermissionResourceFormatEnum,
    UrnIetfOauthUmaTicketResponseModeEnum,
)
from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from pykeycloak.providers.payloads import UMAAuthorizationPayload
from typer import Context, Option, Typer

from .services import (
    _perms_async,
)

app: Typer = Typer(help="Keycloak Session commands")


def parse_permissions(values: list[str]) -> list[str]:
    result = []
    for value in values:
        try:
            resource, scope = value.split("=", 1)
        except ValueError as err:
            raise typer.BadParameter(
                "Permissions must be in the form resource=scope"
            ) from err
        result.append(f"{resource}#{scope}")
    return result


@app.command()
def perms(
    ctx: Context,
    audience: Annotated[str, Option(...)],
    access_token: Annotated[str, Option(...)],
    permissions: Annotated[
        list[str], Option(..., "--permissions", help="Repeatable: role=perm1,perm2")
    ],
    response_mode: Annotated[
        UrnIetfOauthUmaTicketResponseModeEnum, Option()
    ] = UrnIetfOauthUmaTicketResponseModeEnum.DECISION,
    permission_resource_format: Annotated[
        UrnIetfOauthUmaTicketPermissionResourceFormatEnum, Option()
    ] = UrnIetfOauthUmaTicketPermissionResourceFormatEnum.URI,
    permission_resource_matching_uri: Annotated[bool, Option()] = False,
    response_include_resource_name: Annotated[bool, Option()] = False,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_key)

    payload = UMAAuthorizationPayload(
        audience=audience,
        permissions=parse_permissions(permissions),
        response_mode=response_mode,
        subject_token=access_token,
        permission_resource_format=permission_resource_format,
        permission_resource_matching_uri=permission_resource_matching_uri,
        response_include_resource_name=response_include_resource_name,
    )

    asyncio.run(
        _perms_async(
            service=service,
            payload=payload,
        )
    )
