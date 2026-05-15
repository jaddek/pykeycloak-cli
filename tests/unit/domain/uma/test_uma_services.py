from unittest.mock import AsyncMock, MagicMock

import pytest

from pykeycloak_cli.domain.uma import services as uma_services


@pytest.mark.asyncio
async def test_perms_async_calls_uma_and_prints(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    payload = object()
    perms = [{"rsname": "x"}]
    service.auth.client_login_async = AsyncMock()
    service.uma.get_uma_permissions_async = AsyncMock(return_value=perms)
    print_mock = MagicMock()
    monkeypatch.setattr(uma_services.console, "print", print_mock)

    await uma_services._perms_async(service=service, payload=payload)

    service.uma.get_uma_permissions_async.assert_awaited_once_with(payload=payload)
    print_mock.assert_called_once_with(perms)
