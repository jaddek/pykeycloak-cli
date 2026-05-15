# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from collections.abc import Sequence
from dataclasses import fields as dataclass_fields

from pykeycloak.services.representations import Representation
from rich.table import Table


def view_resource[T: Representation](
    resource: T,
    fields: str | None = None,
    exclude: str | None = None,
) -> Table:
    default_headers = [f.name for f in dataclass_fields(resource)]

    extra_fields = fields.split() if fields else []
    exclude_set = set(exclude.split()) if exclude else set()

    active_headers = list(
        dict.fromkeys(
            h for h in (default_headers + extra_fields) if h not in exclude_set
        )
    )

    table = Table(
        title=f"{type(resource).__name__}", style="cyan", expand=True, show_lines=True
    )

    table.add_column("Header", justify="left", overflow="fold")

    for key in active_headers:
        table.add_row(
            f"[bold magenta]{key}[/bold magenta]",
            style="on grey15",
            end_section=True,
        )
        table.add_row(str(getattr(resource, key, "—")), end_section=True)

    return table


def view_resource_list[T: Representation](
    resource_type: type[T],
    resource_list: Sequence[T],
    resource_count: int,
    fields: str | None = None,
    exclude: str | None = None,
    frame: int = 100,
) -> Table:
    default_headers = [f.name for f in dataclass_fields(resource_type)[:3]]

    extra_fields = fields.split() if fields else []
    exclude_set = set(exclude.split()) if exclude else set()

    active_headers = list(
        dict.fromkeys(
            h for h in (default_headers + extra_fields) if h not in exclude_set
        )
    )

    table = Table(
        title=f"{resource_type.__name__} (Total: {resource_count})",
        style="dim",
        expand=True,
    )
    table.add_column("#", justify="center", style="dim")

    for header in active_headers:
        table.add_column(header, justify="left")

    for i, resource in enumerate(resource_list, start=1):
        row_values = [str(getattr(resource, key, "—")) for key in active_headers]
        table.add_row(str(i), *row_values)

        if i % frame == 0:
            ...

    return table
