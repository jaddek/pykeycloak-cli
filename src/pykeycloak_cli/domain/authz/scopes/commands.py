# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

import asyncio
from typing import Annotated

from pykeycloak.core.protocols import KeycloakServiceFactoryProtocol
from typer import Context, Option, Typer

from .services import (
    _all,
)

app: Typer = Typer(help="Keycloak Scopes commands")


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
