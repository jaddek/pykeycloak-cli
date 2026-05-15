from types import SimpleNamespace
from unittest.mock import MagicMock

from pykeycloak_cli.domain.authz.permissions import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock()
    registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def test_permissions_commands(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    monkeypatch.setattr(c, "_all_async", MagicMock(return_value="a"))
    monkeypatch.setattr(
        c,
        "_get_permission_based_on_resource_async",
        MagicMock(return_value="r"),
    )
    monkeypatch.setattr(c, "_get_permission_based_on_scope_async", MagicMock(return_value="s"))
    ctx = _ctx()

    c.all(ctx)
    c.permission_on_resource(ctx, permission_id="p1")
    c.permission_on_scope(ctx, permission_id="p2")

    assert c.asyncio.run.call_count == 3
