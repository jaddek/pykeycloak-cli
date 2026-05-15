from pykeycloak.services.representations import SessionRepresentation

from pykeycloak_cli.representations.console_utils import view_resource, view_resource_list


def test_view_resource_list_accepts_sequence() -> None:
    sessions = (
        SessionRepresentation(id="s1", user_id="u1"),
        SessionRepresentation(id="s2", user_id="u2"),
    )

    table = view_resource_list(
        resource_type=SessionRepresentation,
        resource_list=sessions,
        resource_count=len(sessions),
    )

    assert "Total: 2" in str(table.title)
    assert len(table.rows) == 2


def test_view_resource_applies_fields_and_exclude() -> None:
    resource = SessionRepresentation(id="s1", user_id="u1", username="name")

    table = view_resource(resource=resource, fields="username", exclude="clients")

    headers = list(table.columns[0]._cells[::2])
    assert any("id" in h for h in headers)
    assert any("user_id" in h for h in headers)
    assert any("username" in h for h in headers)
    assert all("clients" not in h for h in headers)
