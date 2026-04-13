# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from pykeycloak.providers.queries import FilterFindPolicyParams
from typer import Context, Option, Typer

from .services import (
    _all,
    _get_associated_roles_async,
    _get_policy_authorisation_scopes_async,
    _get_policy_by_name,
)

app: Typer = Typer(help="Keycloak clients commands")


@app.command()
def all(
    ctx: Context,
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _all(
            service=service,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def policy(
    ctx: Context,
    policy_name: Annotated[str | None, Option(...)] = None,
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    query = FilterFindPolicyParams(name=policy_name) if policy_name else None

    asyncio.run(
        _get_policy_by_name(
            service=service,
            query=query,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def policy_auth_scopes(
    ctx: Context,
    policy_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _get_policy_authorisation_scopes_async(
            service=service,
            policy_id=policy_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def associated_roles(
    ctx: Context,
    policy_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service: KeycloakServiceFactoryProtocol = ctx.obj.registry.get(ctx.obj.realm_otago)

    asyncio.run(
        _get_associated_roles_async(
            service=service,
            policy_id=policy_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )
