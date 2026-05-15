from types import SimpleNamespace
from unittest.mock import MagicMock

from pykeycloak_cli.domain.users import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock(); registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def test_users_commands(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    for n in ["_subset_async","_all_async","_count_async","_by_id_async","_by_role_async","_create_async","_update_async","_enable_async","_disable_async","_delete_async","_update_password_async"]:
        monkeypatch.setattr(c, n, MagicMock(return_value=n))
    ctx = _ctx()
    c.subset(ctx, limit=1, offset=0)
    c.all(ctx)
    c.count(ctx)
    c.by_id(ctx, user_id="u1")
    c.by_role(ctx, role="r")
    c.create(ctx, username="u")
    c.update(ctx, user_id="u1", first_name="f", last_name="l")
    c.enable(ctx, user_id="u1")
    c.disable(ctx, user_id="u1")
    c.delete(ctx, user_id="u1")
    c.update_password(ctx, user_id="u1", pwd="p")
    assert c.asyncio.run.call_count == 11
