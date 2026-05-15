from unittest.mock import AsyncMock, MagicMock

import pytest

from pykeycloak_cli.domain.authz.scopes import services as scope_services


@pytest.mark.asyncio
async def test_all_renders_scopes(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    data = [object(), object()]
    service.auth.client_login_async = AsyncMock()
    service.authz_scope.get_client_authz_scopes_async = AsyncMock(return_value=data)
    captured: dict[str, object] = {}
    monkeypatch.setattr(scope_services, "view_resource_list", lambda **kwargs: captured.update(kwargs) or "table")

    await scope_services._all(service=service, fields="id", exclude=None)

    assert captured["resource_list"] == data
    assert captured["resource_count"] == 2
