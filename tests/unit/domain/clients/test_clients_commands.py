from types import SimpleNamespace
from unittest.mock import MagicMock

from pykeycloak_cli.domain.clients import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock(); registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def test_clients_commands(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    monkeypatch.setattr(c, "_all", MagicMock(return_value="all"))
    monkeypatch.setattr(c, "_client", MagicMock(return_value="client"))
    ctx = _ctx()
    c.all(ctx); c.current(ctx)
    assert c.asyncio.run.call_count == 2
