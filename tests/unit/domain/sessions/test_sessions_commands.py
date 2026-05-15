from types import SimpleNamespace
from unittest.mock import MagicMock

from pykeycloak_cli.domain.sessions import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock()
    registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def test_sessions_commands(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    for name in [
        "_all_async",
        "_count_async",
        "_stats_async",
        "_offline_sessions_async",
        "_user_sessions_async",
        "_delete_session_by_id_async",
        "_delete_all_sessions_async",
        "_delete_users_sessions_async",
    ]:
        monkeypatch.setattr(c, name, MagicMock(return_value=name))

    ctx = _ctx()
    c.all(ctx)
    c.count(ctx)
    c.stats(ctx)
    c.offline(ctx, user_id="u1")
    c.user(ctx, user_id="u1")
    c.delete_by_id(ctx, session_id="s1")
    c.delete_all(ctx)
    c.delete_users_sessions(ctx, user_id="u1")

    assert c.asyncio.run.call_count == 8
