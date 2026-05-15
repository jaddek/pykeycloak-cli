from unittest.mock import AsyncMock, MagicMock

import pytest

from pykeycloak_cli.domain.clients import services as clients_services


@pytest.mark.asyncio
async def test_all_renders_clients(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    clients = [object(), object()]
    service.auth.client_login_async = AsyncMock()
    service.clients.get_clients_async = AsyncMock(return_value=clients)
    captured: dict[str, object] = {}
    monkeypatch.setattr(clients_services, "view_resource_list", lambda **kwargs: captured.update(kwargs) or "table")
    monkeypatch.setattr(clients_services.console, "print", MagicMock())

    await clients_services._all(service=service, fields="id", exclude=None)

    assert captured["resource_list"] == clients
    assert captured["resource_count"] == 2


@pytest.mark.asyncio
async def test_client_renders_single_client(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    client = object()
    service.auth.client_login_async = AsyncMock()
    service.clients.get_client_async = AsyncMock(return_value=client)
    captured: dict[str, object] = {}
    monkeypatch.setattr(clients_services, "view_resource_list", lambda **kwargs: captured.update(kwargs) or "table")

    await clients_services._client(service=service, fields=None, exclude=None)

    assert captured["resource_list"] == [client]
    assert captured["resource_count"] == 1
