from unittest.mock import AsyncMock, MagicMock

import pytest
from pykeycloak.services.representations import (
    SessionRepresentation,
    SessionsCountRepresentation,
    SessionsStatsRepresentation,
)

from pykeycloak_cli.domain.sessions import services as session_services


def _patch_table(monkeypatch: pytest.MonkeyPatch) -> dict[str, object]:
    captured: dict[str, object] = {}

    def fake_view_resource_list(**kwargs: object) -> str:
        captured.update(kwargs)
        return "table"

    monkeypatch.setattr(session_services, "view_resource_list", fake_view_resource_list)
    monkeypatch.setattr(session_services.console, "print", MagicMock())
    return captured


@pytest.mark.asyncio
async def test_all_async_uses_session_representation(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    sessions = [SessionRepresentation(id="s1", user_id="u1")]
    service.auth.client_login_async = AsyncMock()
    service.sessions.get_client_sessions_async = AsyncMock(return_value=sessions)
    captured = _patch_table(monkeypatch)

    await session_services._all_async(service=service, fields="id", exclude=None)

    assert captured["resource_type"] is SessionRepresentation
    assert captured["resource_list"] == sessions
    assert captured["resource_count"] == 1


@pytest.mark.asyncio
async def test_count_async_prints_count(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    count = SessionsCountRepresentation(count=7)
    service.auth.client_login_async = AsyncMock()
    service.sessions.get_client_sessions_count_async = AsyncMock(return_value=count)
    print_mock = MagicMock()
    monkeypatch.setattr(session_services.console, "print", print_mock)

    await session_services._count_async(service=service)

    service.sessions.get_client_sessions_count_async.assert_awaited_once()
    print_mock.assert_called_once_with(count)


@pytest.mark.asyncio
async def test_stats_uses_sessions_stats_representation(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    stats = [
        SessionsStatsRepresentation(
            id="s1", offline="false", client_id="client-a", active="1"
        )
    ]
    service.auth.client_login_async = AsyncMock()
    service.sessions.get_client_session_stats_async = AsyncMock(return_value=stats)
    captured = _patch_table(monkeypatch)

    await session_services._stats_async(service=service, fields=None, exclude=None)

    assert captured["resource_type"] is SessionsStatsRepresentation
    assert captured["resource_list"] == stats


@pytest.mark.asyncio
async def test_offline_sessions_wraps_single_session(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    session = SessionRepresentation(id="s1", user_id="u1")
    service.auth.client_login_async = AsyncMock()
    service.sessions.get_client_user_offline_sessions_async = AsyncMock(return_value=session)
    captured = _patch_table(monkeypatch)

    await session_services._offline_sessions_async(
        service=service, user_id="u1", fields=None, exclude=None
    )

    service.sessions.get_client_user_offline_sessions_async.assert_awaited_once_with(user_id="u1")
    assert captured["resource_type"] is SessionRepresentation
    assert captured["resource_list"] == [session]


@pytest.mark.asyncio
async def test_user_sessions_renders_list(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    sessions = [SessionRepresentation(id="s1", user_id="u1")]
    service.auth.client_login_async = AsyncMock()
    service.sessions.get_user_sessions_async = AsyncMock(return_value=sessions)
    captured = _patch_table(monkeypatch)

    await session_services._user_sessions_async(
        service=service, user_id="u1", fields=None, exclude=None
    )

    service.sessions.get_user_sessions_async.assert_awaited_once_with(user_id="u1")
    assert captured["resource_type"] is SessionRepresentation
    assert captured["resource_list"] == sessions


@pytest.mark.asyncio
async def test_delete_session_by_id_calls_service(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.sessions.delete_session_by_id_async = AsyncMock()
    print_mock = MagicMock()
    monkeypatch.setattr(session_services.console, "print", print_mock)

    await session_services._delete_session_by_id_async(
        service=service, session_id="sid", is_offline=True
    )

    service.sessions.delete_session_by_id_async.assert_awaited_once_with(
        session_id="sid", is_offline=True
    )
    print_mock.assert_called_once_with("ok")


@pytest.mark.asyncio
async def test_delete_all_sessions_calls_service(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.sessions.logout_all_users_async = AsyncMock()
    print_mock = MagicMock()
    monkeypatch.setattr(session_services.console, "print", print_mock)

    await session_services._delete_all_sessions_async(service=service)

    service.sessions.logout_all_users_async.assert_awaited_once()
    print_mock.assert_called_once_with("ok")


@pytest.mark.asyncio
async def test_delete_users_sessions_calls_service() -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.sessions.remove_user_sessions_raw_async = AsyncMock()

    await session_services._delete_users_sessions_async(service=service, user_id="u1")

    service.sessions.remove_user_sessions_raw_async.assert_awaited_once_with(user_id="u1")


@pytest.mark.asyncio
async def test_client_async_uses_session_representation(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    sessions = [SessionRepresentation(id="s1", user_id="u1")]
    service.auth.client_login_async = AsyncMock()
    service.sessions.get_client_sessions_async = AsyncMock(return_value=sessions)
    captured = _patch_table(monkeypatch)

    await session_services._client_async(service=service, fields=None, exclude=None)

    assert captured["resource_type"] is SessionRepresentation
    assert captured["resource_list"] == sessions
