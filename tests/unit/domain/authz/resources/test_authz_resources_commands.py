from types import SimpleNamespace
from unittest.mock import MagicMock

from pykeycloak_cli.domain.authz.resources import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock()
    registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def test_resources_commands(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    monkeypatch.setattr(c, "_all", MagicMock(return_value="a"))
    monkeypatch.setattr(c, "_get_resource_by_id", MagicMock(return_value="r"))
    monkeypatch.setattr(c, "_get_resource_permissions_by_id", MagicMock(return_value="p"))
    ctx = _ctx()

    c.all(ctx)
    c.resource(ctx, resource_id="r1")
    c.resource_permissions(ctx, resource_id="r1")

    assert c.asyncio.run.call_count == 3
