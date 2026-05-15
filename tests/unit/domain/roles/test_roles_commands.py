from types import SimpleNamespace
from unittest.mock import MagicMock

from pykeycloak_cli.domain.roles import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock(); registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def test_roles_commands(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    for n in ["_assign_client_role_async","_client_roles_async","_create_role_async","_delete_role_by_id_async","_delete_role_by_name_async","_role_by_name_async","_unassign_client_role_async","_update_role_by_name_async","_user_available_roles_async","_user_composites_roles_async","_user_roles_async"]:
        monkeypatch.setattr(c, n, MagicMock(return_value=n))
    ctx = _ctx()
    c.roles(ctx); c.role(ctx, role_name="r"); c.create(ctx, name="r"); c.update(ctx, role_name="r")
    c.delete_by_id(ctx, role_id="00000000-0000-0000-0000-000000000000"); c.delete_by_name(ctx, role_name="r")
    c.assign(ctx, user_id="u1", role_name="r"); c.user_roles(ctx, user_id="u1"); c.user_composites_roles(ctx, user_id="u1")
    c.user_available_roles(ctx, user_id="u1"); c.unassign(ctx, user_id="u1", role_name="r")
    assert c.asyncio.run.call_count == 11
