# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

import typer
from pykeycloak.core.enums import (
    UrnIetfOauthUmaTicketPermissionResourceFormatEnum,
    UrnIetfOauthUmaTicketResponseModeEnum,
)
from pykeycloak.core.realm import Realm
from pykeycloak.factories import KeycloakServiceFactory
from pykeycloak.providers.payloads import UMAAuthorizationPayload
from typer import Context, Option, Typer

from .services import (
    _perms_async,
)

app: Typer = Typer(help="Keycloak Session commands")


def parse_permissions(values: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for value in values:
        try:
            key, items = value.split("=", 1)
        except ValueError as err:
            raise typer.BadParameter(
                "Permissions must be in the form key=val1,val2"
            ) from err
        result[key] = items.split(",")
    return result


@app.command()
def perms(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    audience: Annotated[str, Option(...)],
    access_token: Annotated[str, Option(...)],
    permissions: Annotated[
        list[str], Option(..., "--permission", help="Repeatable: role=perm1,perm2")
    ],
    response_mode: Annotated[
        str, Option(default=str(UrnIetfOauthUmaTicketResponseModeEnum.DECISION))
    ],
    permission_resource_format: Annotated[
        str, Option(UrnIetfOauthUmaTicketPermissionResourceFormatEnum.URI)
    ],
    permission_resource_matching_uri: Annotated[bool, Option(False)],
    response_include_resource_name: Annotated[bool, Option(False)],
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

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
            service_factory=service_factory,
            payload=payload,
        )
    )
