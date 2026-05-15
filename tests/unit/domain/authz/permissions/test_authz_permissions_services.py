from unittest.mock import AsyncMock, MagicMock

import pytest

from pykeycloak_cli.domain.authz.permissions import services as permission_services


@pytest.mark.asyncio
async def test_all_async_renders_permissions(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    data = [object()]
    service.auth.client_login_async = AsyncMock()
    service.authz_permission.get_permissions_async = AsyncMock(return_value=data)
    captured: dict[str, object] = {}
    monkeypatch.setattr(permission_services, "view_resource_list", lambda **kwargs: captured.update(kwargs) or "table")

    await permission_services._all_async(service=service, fields=None, exclude=None)

    assert captured["resource_list"] == data
    assert captured["resource_count"] == 1


@pytest.mark.asyncio
async def test_get_permission_based_on_resource(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    result = {"id": "p1"}
    service.auth.client_login_async = AsyncMock()
    service.authz_permission.get_permission_based_on_resource_by_id_async = AsyncMock(return_value=result)
    print_mock = MagicMock()
    monkeypatch.setattr(permission_services.console, "print", print_mock)

    await permission_services._get_permission_based_on_resource_async(
        service=service, permission_id="p1", fields=None, exclude=None
    )

    service.authz_permission.get_permission_based_on_resource_by_id_async.assert_awaited_once_with(permission_id="p1")
    print_mock.assert_called_once_with(result)


@pytest.mark.asyncio
async def test_get_permission_based_on_scope(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    result = {"id": "p2"}
    service.auth.client_login_async = AsyncMock()
    service.authz_permission.get_permission_based_on_scope_by_id_async = AsyncMock(return_value=result)
    print_mock = MagicMock()
    monkeypatch.setattr(permission_services.console, "print", print_mock)

    await permission_services._get_permission_based_on_scope_async(
        service=service, permission_id="p2", fields=None, exclude=None
    )

    service.authz_permission.get_permission_based_on_scope_by_id_async.assert_awaited_once_with(permission_id="p2")
    print_mock.assert_called_once_with(result)
