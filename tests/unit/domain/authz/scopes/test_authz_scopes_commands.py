from types import SimpleNamespace
from unittest.mock import MagicMock

from pykeycloak_cli.domain.authz.scopes import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock(); registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def test_scopes_commands(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    monkeypatch.setattr(c, "_all", MagicMock(return_value="a"))
    c.all(_ctx())
    assert c.asyncio.run.call_count == 1
