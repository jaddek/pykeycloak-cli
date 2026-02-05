# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.realm import Realm
from pykeycloak.factories import KeycloakServiceFactory
from typer import Context, Option, Typer

from .services import (
    _all,
)

app: Typer = Typer(help="Keycloak Authz Settings commands")


@app.command()
def all(
    ctx: Context,
    realm: Annotated[str, Option(...)],
    fields: Annotated[str | None, Option()] = None,
    exclude_fields: Annotated[str | None, Option()] = None,
) -> None:
    service_factory: KeycloakServiceFactory = ctx.obj.registry.get(Realm(name=realm))

    asyncio.run(
        _all(
            service_factory=service_factory,
            fields=fields,
            exclude=exclude_fields,
        )
    )
