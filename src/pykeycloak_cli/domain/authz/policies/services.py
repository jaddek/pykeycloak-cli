# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>
from pykeycloak.factories import KeycloakServiceFactory
from pykeycloak.providers.queries import FilterFindPolicyParams
from rich.console import Console

console = Console()


async def _all(
    service_factory: KeycloakServiceFactory,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    data = await service_factory.auth_policy.get_policies_async()

    console.print(data)


async def _get_policy_by_name(
    service_factory: KeycloakServiceFactory,
    query: FilterFindPolicyParams | None,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    data = await service_factory.auth_policy.get_policy_by_name_async(query=query)

    console.print(data)


async def _get_policy_authorisation_scopes_async(
    service_factory: KeycloakServiceFactory,
    policy_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    data = await service_factory.auth_policy.get_policy_authorisation_scopes_async(
        policy_id=policy_id
    )

    console.print(data)


async def _get_associated_roles_async(
    service_factory: KeycloakServiceFactory,
    policy_id: str,
    fields: str | None,
    exclude: str | None,
) -> None:
    await service_factory.auth.client_login_async()

    data = await service_factory.auth_policy.get_associated_roles_async(
        policy_id=policy_id
    )

    console.print(data)
