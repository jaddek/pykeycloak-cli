from unittest.mock import AsyncMock, MagicMock

import pytest

from pykeycloak_cli.domain.auth import services as auth_services


@pytest.mark.asyncio
async def test_login_renders_token(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    payload = object()
    token = object()
    service.auth.client_login_async = AsyncMock()
    service.auth.user_login_async = AsyncMock(return_value=token)

    captured: dict[str, object] = {}
    monkeypatch.setattr(auth_services, "view_resource", lambda **kwargs: captured.update(kwargs) or "table")
    print_mock = MagicMock()
    monkeypatch.setattr(auth_services.console, "print", print_mock)

    await auth_services._login_async(service=service, payload=payload, fields="a", exclude="b")

    service.auth.client_login_async.assert_awaited_once()
    service.auth.user_login_async.assert_awaited_once_with(payload=payload)
    assert captured["resource"] is token
    assert captured["fields"] == "a"
    assert captured["exclude"] == "b"
    print_mock.assert_called_once_with("table")


@pytest.mark.asyncio
async def test_refresh_renders_token(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    payload = object()
    token = object()
    service.auth.client_login_async = AsyncMock()
    service.auth.refresh_token_async = AsyncMock(return_value=token)

    captured: dict[str, object] = {}
    monkeypatch.setattr(auth_services, "view_resource", lambda **kwargs: captured.update(kwargs) or "table")

    await auth_services._refresh_async(service=service, payload=payload, fields=None, exclude=None)

    service.auth.refresh_token_async.assert_awaited_once_with(payload=payload)
    assert captured["resource"] is token


@pytest.mark.asyncio
async def test_info_renders_user_info(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    info = object()
    service.auth.client_login_async = AsyncMock()
    service.auth.get_user_info_async = AsyncMock(return_value=info)

    captured: dict[str, object] = {}
    monkeypatch.setattr(auth_services, "view_resource", lambda **kwargs: captured.update(kwargs) or "table")

    await auth_services._info_async(service=service, access_token="abc", fields=None, exclude=None)

    service.auth.get_user_info_async.assert_awaited_once_with(access_token="abc")
    assert captured["resource"] is info


@pytest.mark.asyncio
async def test_introspect_renders_result(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    payload = object()
    introspect = object()
    service.auth.client_login_async = AsyncMock()
    service.auth.introspect_token_async = AsyncMock(return_value=introspect)

    captured: dict[str, object] = {}
    monkeypatch.setattr(auth_services, "view_resource", lambda **kwargs: captured.update(kwargs) or "table")

    await auth_services._introspect_async(service=service, payload=payload, fields=None, exclude=None)

    service.auth.introspect_token_async.assert_awaited_once_with(payload=payload)
    assert captured["resource"] is introspect


@pytest.mark.asyncio
async def test_logout_calls_auth_and_prints_ok(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.auth.logout_async = AsyncMock()
    print_mock = MagicMock()
    monkeypatch.setattr(auth_services.console, "print", print_mock)

    await auth_services._logout_async(service=service, refresh_token="rt")

    service.auth.logout_async.assert_awaited_once_with(refresh_token="rt")
    print_mock.assert_called_once_with("ok")


@pytest.mark.asyncio
async def test_revoke_calls_auth_and_prints_ok(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.auth.revoke_async = AsyncMock()
    print_mock = MagicMock()
    monkeypatch.setattr(auth_services.console, "print", print_mock)

    await auth_services._revoke_async(service=service, refresh_token="rt")

    service.auth.revoke_async.assert_awaited_once_with(refresh_token="rt")
    print_mock.assert_called_once_with("ok")


@pytest.mark.asyncio
async def test_certs_uses_well_known_service(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.well_known.get_certs_async = AsyncMock(return_value={"keys": []})
    print_mock = MagicMock()
    monkeypatch.setattr(auth_services.console, "print", print_mock)

    await auth_services._certs_async(service=service)

    service.auth.client_login_async.assert_awaited_once()
    service.well_known.get_certs_async.assert_awaited_once()
    print_mock.assert_called_once_with({"keys": []})
