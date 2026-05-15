from types import SimpleNamespace
from unittest.mock import MagicMock

from pykeycloak_cli.domain.auth import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock()
    registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def _patch(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    for n in ["_login_async","_refresh_async","_info_async","_logout_async","_introspect_async","_certs_async","_revoke_async"]:
        monkeypatch.setattr(c, n, MagicMock(return_value=n))


def test_auth_commands(monkeypatch):
    _patch(monkeypatch)
    ctx = _ctx()
    c.login(ctx, username="u", password="p")
    c.refresh(ctx, refresh_token="rt")
    c.info(ctx, access_token="at")
    c.logout(ctx, refresh_token="rt")
    c.introspect_rtp(ctx, token="t")
    c.introspect_token(ctx, access_token="at")
    c.certs(ctx)
    c.revoke(ctx, refresh_token="rt")
    assert c.asyncio.run.call_count == 8
