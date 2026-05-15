from unittest.mock import AsyncMock, MagicMock

import pytest

from pykeycloak_cli.domain.roles import services as roles_services


@pytest.mark.asyncio
async def test_read_paths(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    service.auth.client_login_async = AsyncMock()
    service.roles.get_client_roles_async = AsyncMock(return_value=[{"name": "r"}])
    service.roles.get_role_by_name_async = AsyncMock(return_value={"id": "1", "name": "r"})
    service.roles.get_composite_client_roles_of_user_async = AsyncMock(return_value=[])
    service.roles.get_available_client_roles_of_user_async = AsyncMock(return_value=[])
    service.roles.get_user_roles_async = AsyncMock(return_value=[])
    print_mock = MagicMock()
    monkeypatch.setattr(roles_services.console, "print", print_mock)

    await roles_services._client_roles_async(service, None, None)
    await roles_services._role_by_name_async(service, "r", None, None)
    await roles_services._user_composites_roles_async(service, "u1", None, None)
    await roles_services._user_available_roles_async(service, "u1", None, None)
    await roles_services._user_roles_async(service, "u1", None, None)

    service.roles.get_user_roles_async.assert_awaited_once_with(user_id="u1")
    print_mock.assert_any_call("Ok")


@pytest.mark.asyncio
async def test_write_paths_and_role_assignments(monkeypatch: pytest.MonkeyPatch) -> None:
    service = MagicMock()
    payload = object()
    service.auth.client_login_async = AsyncMock()
    service.roles.create_role_async = AsyncMock()
    service.roles.delete_role_by_id_async = AsyncMock()
    service.roles.delete_role_by_name_async = AsyncMock()
    service.roles.update_role_by_name_async = AsyncMock()
    service.roles.get_role_by_name_async = AsyncMock(return_value={"id": "rid", "name": "admin"})
    service.roles.assign_role_async = AsyncMock()
    service.roles.unassign_role_async = AsyncMock()
    monkeypatch.setattr(roles_services.console, "print", MagicMock())

    await roles_services._create_role_async(service, payload=payload, fields=None, exclude=None)
    await roles_services._delete_role_by_id_async(service, role_id="rid", fields=None, exclude=None)
    await roles_services._delete_role_by_name_async(service, role_name="admin", fields=None, exclude=None)
    await roles_services._update_role_by_name_async(
        service, role_name="admin", payload=payload, fields=None, exclude=None
    )
    await roles_services._assign_client_role_async(service, user_id="u1", role_name="admin", fields=None, exclude=None)
    await roles_services._unassign_client_role_async(service, user_id="u1", role_name="admin", fields=None, exclude=None)

    service.roles.create_role_async.assert_awaited_once_with(payload=payload)
    assigned_roles = service.roles.assign_role_async.await_args.kwargs["roles"]
    unassigned_roles = service.roles.unassign_role_async.await_args.kwargs["roles"]
    assert assigned_roles[0].id == "rid" and assigned_roles[0].name == "admin"
    assert unassigned_roles[0].id == "rid" and unassigned_roles[0].name == "admin"
