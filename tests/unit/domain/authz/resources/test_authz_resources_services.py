from unittest.mock import AsyncMock, MagicMock

import pytest

from pykeycloak_cli.domain.authz.resources import services as resource_services


@pytest.mark.asyncio
async def test_all_prints_resources(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    data = [{"id": "r1"}]
    service.auth.client_login_async = AsyncMock()
    service.authz_resource.get_resources_async = AsyncMock(return_value=data)
    print_mock = MagicMock()
    monkeypatch.setattr(resource_services.console, "print", print_mock)

    await resource_services._all(service=service, fields=None, exclude=None)

    print_mock.assert_called_once_with(data)


@pytest.mark.asyncio
async def test_get_resource_by_id(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    data = {"id": "r1"}
    service.auth.client_login_async = AsyncMock()
    service.authz_resource.get_resource_by_id_async = AsyncMock(return_value=data)
    print_mock = MagicMock()
    monkeypatch.setattr(resource_services.console, "print", print_mock)

    await resource_services._get_resource_by_id(service=service, resource_id="r1", fields=None, exclude=None)

    service.authz_resource.get_resource_by_id_async.assert_awaited_once_with(resource_id="r1")
    print_mock.assert_called_once_with(data)


@pytest.mark.asyncio
async def test_get_resource_permissions_by_id(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    data = [{"permission": "p1"}]
    service.auth.client_login_async = AsyncMock()
    service.authz_resource.get_resource_permissions_async = AsyncMock(return_value=data)
    print_mock = MagicMock()
    monkeypatch.setattr(resource_services.console, "print", print_mock)

    await resource_services._get_resource_permissions_by_id(
        service=service, resource_id="r1", fields=None, exclude=None
    )

    service.authz_resource.get_resource_permissions_async.assert_awaited_once_with(resource_id="r1")
    print_mock.assert_called_once_with(data)
