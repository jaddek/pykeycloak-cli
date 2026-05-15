from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import uuid4

import pytest
import typer

from pykeycloak_cli.domain.uma import commands as c


def _ctx(service: object = object()) -> object:
    registry = MagicMock(); registry.get.return_value = service
    return SimpleNamespace(obj=SimpleNamespace(registry=registry, realm_key="realm"))


def test_parse_permissions_ok():
    assert c.parse_permissions(["res=read"]) == ["res#read"]


def test_parse_permissions_bad():
    with pytest.raises(typer.BadParameter):
        c.parse_permissions(["bad"])


def test_perms_command(monkeypatch):
    monkeypatch.setattr(c, "asyncio", SimpleNamespace(run=MagicMock()))
    monkeypatch.setattr(c, "_perms_async", MagicMock(return_value="ok"))
    ctx = _ctx()
    c.perms(
        ctx,
        audience="a",
        access_token=str(uuid4()),
        permissions=["r=s"],
    )
    assert c.asyncio.run.call_count == 1
