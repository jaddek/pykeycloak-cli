# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated
from uuid import UUID

from pykeycloak.core.realm import Realm
from pykeycloak.factories import KeycloakServiceFactory
from pykeycloak.providers.payloads import RolePayload
from typer import Context, Option, Typer

from .services import (
    _assign_client_role_async,
    _client_roles_async,
    _create_role_async,
    _delete_role_by_id_async,
    _delete_role_by_name_async,
    _role_by_name_async,
    _unassign_client_role_async,
    _update_role_by_name_async,
    _user_available_roles_async,
    _user_composites_roles_async,
    _user_roles_async,
)

app: Typer = Typer(help="Keycloak Client commands")


@app.command()
def roles(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _client_roles_async(
            service_factory=service_factory,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def role(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    role_name: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _role_by_name_async(
            service_factory=service_factory,
            role_name=role_name,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def create(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    name: Annotated[str, Option(...)],
    description: Annotated[str | None, Option(...)] = None,
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _create_role_async(
            service_factory=service_factory,
            payload=RolePayload(
                name=name,
                description=description,
            ),
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def update(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    role_name: Annotated[str, Option(...)],
    role_description: Annotated[str | None, Option(...)] = None,
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _update_role_by_name_async(
            service_factory=service_factory,
            role_name=role_name,
            payload=RolePayload(
                name=role_name,
                description=role_description,
            ),
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def delete_by_id(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    role_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _delete_role_by_id_async(
            service_factory=service_factory,
            role_id=UUID(role_id),
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def delete_by_name(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    role_name: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _delete_role_by_name_async(
            service_factory=service_factory,
            role_name=role_name,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def assign(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    role_name: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _assign_client_role_async(
            service_factory=service_factory,
            user_id=user_id,
            role_name=role_name,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def user_roles(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _user_roles_async(
            service_factory=service_factory,
            user_id=user_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def user_composites_roles(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _user_composites_roles_async(
            service_factory=service_factory,
            user_id=user_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def user_available_roles(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _user_available_roles_async(
            service_factory=service_factory,
            user_id=user_id,
            fields=fields,
            exclude=exclude_fields,
        )
    )


@app.command()
def unassign(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    user_id: Annotated[str, Option(...)],
    role_name: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _unassign_client_role_async(
            service_factory=service_factory,
            user_id=user_id,
            role_name=role_name,
            fields=fields,
            exclude=exclude_fields,
        )
    )
