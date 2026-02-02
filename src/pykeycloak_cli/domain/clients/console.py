# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from rich.table import Table


def view_clients_list(
    clients_list: enumerate,
    clients_count: int,
    fields: str | None,
    exclude: str | None,
    frame: int = 100,
) -> Table:
    default_headers = ["id", "name", "enabled"]

    extra_fields = fields.split() if fields else []

    exclude_set = set(exclude.split()) if exclude else set()

    active_headers = list(
        dict.fromkeys(
            [h for h in (default_headers + extra_fields) if h not in exclude_set]
        )
    )

    table = Table(title=f"Clients (Total: {clients_count})", style="dim")
    table.add_column("#", justify="center", style="dim")

    for header in active_headers:
        table.add_column(header, justify="left")

    for i, _client in clients_list:
        row_values = [str(getattr(_client, key, "—")) for key in active_headers]
        table.add_row(str(i), *row_values)

        if i % frame == 0:
            ...

    return table
