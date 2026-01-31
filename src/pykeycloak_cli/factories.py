from pykeycloak.core.realm import Realm, RealmClient
from pykeycloak.core.validator import KeycloakResponseValidator
from pykeycloak.dependancies import (
    get_headers_factory,
    get_keycloak_client_wrapper_from_env,
)
from pykeycloak.factories import KeycloakServiceFactory
from pykeycloak.providers.providers import KeycloakInMemoryProviderAsync


def service_factory(kc_realm: str) -> KeycloakServiceFactory:
    realm_client = RealmClient.from_env()
    realm = Realm(name=kc_realm)
    factory = KeycloakServiceFactory(
        provider=KeycloakInMemoryProviderAsync(
            realm=realm,
            realm_client=realm_client,
            headers=get_headers_factory(),
            wrapper=get_keycloak_client_wrapper_from_env(),
        ),
        validator=KeycloakResponseValidator(),
    )

    return factory
