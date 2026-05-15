from unittest.mock import AsyncMock, MagicMock

import pytest

from pykeycloak_cli.domain.authz.policies import services as policy_services


@pytest.mark.asyncio
async def test_all_uses_authz_policy_service(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.authz_policy.get_policies_async = AsyncMock(return_value=[{"id": "p1"}])
    print_mock = MagicMock()
    monkeypatch.setattr(policy_services.console, "print", print_mock)

    await policy_services._all(service=service, fields=None, exclude=None)

    service.auth.client_login_async.assert_awaited_once()
    service.authz_policy.get_policies_async.assert_awaited_once()
    print_mock.assert_called_once_with([{"id": "p1"}])


@pytest.mark.asyncio
async def test_get_policy_by_name_forwards_query(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    query = object()
    result = {"id": "p2"}
    service.auth.client_login_async = AsyncMock()
    service.authz_policy.get_policy_by_name_async = AsyncMock(return_value=result)
    print_mock = MagicMock()
    monkeypatch.setattr(policy_services.console, "print", print_mock)

    await policy_services._get_policy_by_name(service=service, query=query, fields=None, exclude=None)

    service.authz_policy.get_policy_by_name_async.assert_awaited_once_with(query=query)
    print_mock.assert_called_once_with(result)


@pytest.mark.asyncio
async def test_get_policy_authorisation_scopes(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    result = [{"scope": "s1"}]
    service.auth.client_login_async = AsyncMock()
    service.authz_policy.get_policy_authorisation_scopes_async = AsyncMock(return_value=result)
    print_mock = MagicMock()
    monkeypatch.setattr(policy_services.console, "print", print_mock)

    await policy_services._get_policy_authorisation_scopes_async(
        service=service, policy_id="pid", fields=None, exclude=None
    )

    service.authz_policy.get_policy_authorisation_scopes_async.assert_awaited_once_with(policy_id="pid")
    print_mock.assert_called_once_with(result)


@pytest.mark.asyncio
async def test_get_associated_roles(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    result = [{"name": "role"}]
    service.auth.client_login_async = AsyncMock()
    service.authz_policy.get_associated_roles_async = AsyncMock(return_value=result)
    print_mock = MagicMock()
    monkeypatch.setattr(policy_services.console, "print", print_mock)

    await policy_services._get_associated_roles_async(
        service=service, policy_id="pid", fields=None, exclude=None
    )

    service.authz_policy.get_associated_roles_async.assert_awaited_once_with(policy_id="pid")
    print_mock.assert_called_once_with(result)
