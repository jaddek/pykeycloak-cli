from types import SimpleNamespace
from unittest.mock import MagicMock

from pykeycloak_cli.domain.authz.policies import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock(); registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def test_policies_commands(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    monkeypatch.setattr(c, "_all", MagicMock(return_value="a"))
    monkeypatch.setattr(c, "_get_policy_by_name", MagicMock(return_value="p"))
    monkeypatch.setattr(c, "_get_policy_authorisation_scopes_async", MagicMock(return_value="s"))
    monkeypatch.setattr(c, "_get_associated_roles_async", MagicMock(return_value="r"))
    ctx = _ctx()
    c.all(ctx); c.policy(ctx, policy_name="p"); c.policy_auth_scopes(ctx, policy_id="x"); c.associated_roles(ctx, policy_id="x")
    assert c.asyncio.run.call_count == 4
