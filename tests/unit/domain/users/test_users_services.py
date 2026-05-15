from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4

import pytest
from pykeycloak.services.representations import UserRepresentation

from pykeycloak_cli.domain.users import services as users_services


def _user() -> UserRepresentation:
    return UserRepresentation(id="u1", username="john")


def _capture_table(monkeypatch: pytest.MonkeyPatch) -> dict[str, object]:
    captured: dict[str, object] = {}

    def fake_view_resource_list(**kwargs: object) -> str:
        captured.update(kwargs)
        return "table"

    monkeypatch.setattr(users_services, "view_resource_list", fake_view_resource_list)
    monkeypatch.setattr(users_services.console, "print", MagicMock())
    return captured


@pytest.mark.asyncio
async def test_subset_async_calls_get_users(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.users.get_users_async = AsyncMock(return_value=([_user()], 1))
    captured = _capture_table(monkeypatch)

    await users_services._subset_async(service, limit=10, offset=2, fields="id", exclude=None)

    service.users.get_users_async.assert_awaited_once()
    query = service.users.get_users_async.await_args.args[0]
    assert query.max == 10
    assert query.first == 2
    assert captured["resource_type"] is UserRepresentation


@pytest.mark.asyncio
async def test_all_async(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.users.get_all_users_async = AsyncMock(return_value=([_user()], 1))
    captured = _capture_table(monkeypatch)

    await users_services._all_async(service, fields=None, exclude=None)

    service.users.get_all_users_async.assert_awaited_once()
    assert captured["resource_count"] == 1


@pytest.mark.asyncio
async def test_count_async(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.users.get_users_count_async = AsyncMock(return_value=42)
    print_mock = MagicMock()
    monkeypatch.setattr(users_services.console, "print", print_mock)

    await users_services._count_async(service)

    print_mock.assert_called_once_with(42)


@pytest.mark.asyncio
async def test_by_id_async(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    user = _user()
    service.auth.client_login_async = AsyncMock()
    service.users.get_user_async = AsyncMock(return_value=user)
    captured = _capture_table(monkeypatch)

    await users_services._by_id_async(service, user_id="u1", fields=None, exclude=None)

    service.users.get_user_async.assert_awaited_once_with(user_id="u1")
    assert captured["resource_list"] == [user]


@pytest.mark.asyncio
async def test_create_async(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    user = _user()
    service.auth.client_login_async = AsyncMock()
    service.users.create_user_async = AsyncMock(return_value="u1")
    service.users.get_user_async = AsyncMock(return_value=user)
    captured = _capture_table(monkeypatch)

    await users_services._create_async(service, username="john")

    service.users.create_user_async.assert_awaited_once()
    payload = service.users.create_user_async.await_args.kwargs["payload"]
    assert payload.username == "john"
    assert captured["resource_list"] == [user]


@pytest.mark.asyncio
async def test_update_async(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    user = _user()
    service.auth.client_login_async = AsyncMock()
    service.users.update_user_async = AsyncMock()
    service.users.get_user_async = AsyncMock(return_value=user)

    await users_services._update_async(service, user_id="u1", first_name="A", last_name="B")

    service.users.update_user_async.assert_awaited_once()
    kwargs = service.users.update_user_async.await_args.kwargs
    assert kwargs["user_id"] == "u1"
    assert kwargs["payload"].first_name == "A"
    assert kwargs["payload"].last_name == "B"


@pytest.mark.asyncio
async def test_enable_disable_delete_and_password(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    test_password = str(uuid4())
    service.auth.client_login_async = AsyncMock()
    service.users.enable_user_async = AsyncMock()
    service.users.get_user_async = AsyncMock(return_value=_user())
    service.users.delete_user_async = AsyncMock()
    service.users.update_user_password_async = AsyncMock()
    monkeypatch.setattr(users_services, "view_resource_list", lambda **kwargs: "table")
    monkeypatch.setattr(users_services.console, "print", MagicMock())

    await users_services._enable_async(service, user_id="u1")
    await users_services._disable_async(service, user_id="u1")
    await users_services._delete_async(service, user_id="u1")
    await users_services._update_password_async(
        service,
        user_id="u1",
        pwd=test_password,
    )

    enable_calls = service.users.enable_user_async.await_args_list
    assert enable_calls[0].kwargs["payload"].enabled is True
    assert enable_calls[1].kwargs["payload"].enabled is False
    service.users.delete_user_async.assert_awaited_once_with(user_id="u1")
    password_payload = service.users.update_user_password_async.await_args.kwargs["payload"]
    assert password_payload.credentials[0]["value"] == test_password
