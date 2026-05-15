from unittest.mock import AsyncMock, MagicMock

import pytest

from pykeycloak_cli.domain.authz.settings import services as settings_services


@pytest.mark.asyncio
async def test_all_renders_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    settings = object()
    service.auth.client_login_async = AsyncMock()
    service.authz.get_client_authz_settings_async = AsyncMock(return_value=settings)
    captured: dict[str, object] = {}
    monkeypatch.setattr(settings_services, "view_resource", lambda **kwargs: captured.update(kwargs) or "table")

    await settings_services._all(service=service, fields="id", exclude=None)

    assert captured["resource"] is settings
    assert captured["fields"] == "id"
