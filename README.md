# PyKeycloak CLI

This is a lightweight CLI library built
on the top of [Pykeycloak](https://github.com/jaddek/pykeycloak), Realm used from [Pykeycloak-realm](https://github.com/jaddek/pykeycloak-realm)
and [Typer](https://github.com/fastapi/typer).

- [Env](#env)
- [Commands](#commands)
    - [Users](#users)
    - [Clients](#clients)
    - [Sessions](#sessions)
    - [Roles](#roles)
    - [Auth](#auth)
    - [Uma](#uma)
    - [Authz](#authz)
        - [Scopes](#scopes)
        - [Policies](#policies)
        - [Resources](#resources)
        - [Permissions](#permissions)
        - [Settings](#settings)

## Env

*optional usage*

Environment variables can be found as a list in .env and .env.local. It is NOT necessary to use environment variables, as it is possible to initialize all components manually.

Located in .env|.env.local (according to Makefile)

To run the command it is possible to use just `python` OR `uv run` OR `make run`

- `python pykc.py`: Run the command directly.
- `uv run pykc.py`: Run the command using uv.
- `make run`: Run the same with environment variables loaded from .env and .env.local. `(Dev mode)`

```sh
KEYCLOAK_REALM=
KEYCLOAK_BASE_URL=

# Per-realm client config (replace <REALM_KEY> with the realm key in uppercase)
KEYCLOAK_REALM_<REALM_KEY>_REALM_NAME=
KEYCLOAK_REALM_<REALM_KEY>_CLIENT_UUID=
KEYCLOAK_REALM_<REALM_KEY>_CLIENT_ID=
KEYCLOAK_REALM_<REALM_KEY>_CLIENT_SECRET=

KEYCLOAK_HTTPX_CLIENT_PARAMS_HTTP1=
KEYCLOAK_HTTPX_CLIENT_PARAMS_HTTP2=
KEYCLOAK_HTTPX_CLIENT_PARAMS_FOLLOW_REDIRECTS=
KEYCLOAK_HTTPX_CLIENT_PARAMS_TRUST_ENV=
KEYCLOAK_HTTPX_CLIENT_CLIENT_PARAMS_TIMEOUT=
KEYCLOAK_HTTPX_CLIENT_PARAMS_MAX_CONNECTIONS=
KEYCLOAK_HTTPX_CLIENT_PARAMS_MAX_KEEPALIVE_CONNECTIONS=
KEYCLOAK_HTTPX_CLIENT_PARAMS_KEEPALIVE_EXPIRY=
KEYCLOAK_HTTPX_CLIENT_PARAMS_MAX_REDIRECTS=
KEYCLOAK_HTTPX_CLIENT_PARAMS_DEFAULT_ENCODING=utf-8

KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_VERIFY=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_CERT=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_TRUST_ENV=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_HTTP1=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_HTTP2=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_RETRIES=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_PROXY=

DATA_SANITIZER_EXTRA_SENSITIVE_KEYS=
DATA_SANITIZER_DEBUG=False
```

## Commands

`--realm` is a **global option** and must be placed before the subcommand name.
If `KEYCLOAK_REALM` env var is set, `--realm` can be omitted entirely.

```sh
# explicit
python pykc.py --realm otago_service <subcommand> [options]
make run ARGS="--realm otago_service <subcommand> [options]"

# via env var
export KEYCLOAK_REALM=otago_service
python pykc.py <subcommand> [options]
```

### Users

```sh
python pykc.py --realm otago_service users all
make run ARGS="--realm otago_service users all"
```

```sh
python pykc.py --realm otago_service users subset --limit 1 --offset 10 --fields=email_verified --exclude-fields='email id enabled username'
make run ARGS="--realm otago_service users subset --limit 1 --offset 10 --fields=email_verified --exclude-fields='email id enabled username'"
```

```sh
python pykc.py --realm otago_service users by-id --user-id e33add52-05f8-4152-af17-a5815bfa6293
make run ARGS="--realm otago_service users by-id --user-id e33add52-05f8-4152-af17-a5815bfa6293"
```

```sh
python pykc.py --realm otago_service users by-role --role my-role
make run ARGS="--realm otago_service users by-role --role my-role"
```

```sh
python pykc.py --realm otago_service users update-password --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --pwd test
make run ARGS="--realm otago_service users update-password --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --pwd test"
```

```sh
python pykc.py --realm otago_service users enable --user-id bcc23900-d840-47bd-aa4d-5e1e46646459
make run ARGS="--realm otago_service users enable --user-id bcc23900-d840-47bd-aa4d-5e1e46646459"
```

```sh
python pykc.py --realm otago_service users disable --user-id bcc23900-d840-47bd-aa4d-5e1e46646459
make run ARGS="--realm otago_service users disable --user-id bcc23900-d840-47bd-aa4d-5e1e46646459"
```

```sh
python pykc.py --realm otago_service users update --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --last-name 'hello' --first-name 'Kitty'
make run ARGS="--realm otago_service users update --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --last-name 'hello' --first-name 'Kitty'"
```

```sh
python pykc.py --realm otago_service users create --username 'cesar_the_third'
make run ARGS="--realm otago_service users create --username 'cesar_the_third'"
```

### Clients

```sh
python pykc.py --realm otago_service clients all
make run ARGS="--realm otago_service clients all"
```

```sh
python pykc.py --realm otago_service clients current --fields 'name displayName'
make run ARGS="--realm otago_service clients current --fields 'name displayName'"
```

### Sessions

```sh
python pykc.py --realm otago_service sessions all
make run ARGS="--realm otago_service sessions all"
```

```sh
python pykc.py --realm otago_service sessions count
make run ARGS="--realm otago_service sessions count"
```

```sh
python pykc.py --realm otago_service sessions stats
make run ARGS="--realm otago_service sessions stats"
```

```sh
python pykc.py --realm otago_service sessions stats --exclude-fields 'user_id username ip_address start remember_me'
make run ARGS="--realm otago_service sessions stats --exclude-fields 'user_id username ip_address start remember_me'"
```

```sh
python pykc.py --realm otago_service sessions user --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c
make run ARGS="--realm otago_service sessions user --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c"
```

```sh
python pykc.py --realm otago_service sessions offline --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c
make run ARGS="--realm otago_service sessions offline --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c"
```

```sh
python pykc.py --realm otago_service sessions delete-by-id --session-id e9c0a406-e9c0-72b7-8924-aedcd8e306e0
make run ARGS="--realm otago_service sessions delete-by-id --session-id e9c0a406-e9c0-72b7-8924-aedcd8e306e0"
```

```sh
python pykc.py --realm otago_service sessions delete-all
make run ARGS="--realm otago_service sessions delete-all"
```

```sh
python pykc.py --realm otago_service sessions delete-users-sessions --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c
make run ARGS="--realm otago_service sessions delete-users-sessions --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c"
```

### Auth

```sh
python pykc.py --realm otago_service auth login --username=admin --password=password
make run ARGS="--realm otago_service auth login --username=admin --password=password"
```

```sh
python pykc.py --realm otago_service auth refresh --refresh-token ${refresh_token}
make run ARGS="--realm otago_service auth refresh --refresh-token ${refresh_token}"
```

```sh
python pykc.py --realm otago_service auth revoke --refresh-token ${refresh_token}
make run ARGS="--realm otago_service auth revoke --refresh-token ${refresh_token}"
```

```sh
python pykc.py --realm otago_service auth info --access-token ${access_token}
make run ARGS="--realm otago_service auth info --access-token ${access_token}"
```

```sh
python pykc.py --realm otago_service auth introspect-rtp --token ${token}
make run ARGS="--realm otago_service auth introspect-rtp --token ${token}"
```

```sh
python pykc.py --realm otago_service auth introspect-token --access-token ${access_token}
make run ARGS="--realm otago_service auth introspect-token --access-token ${access_token}"
```

```sh
python pykc.py --realm otago_service auth certs
make run ARGS="--realm otago_service auth certs"
```

### UMA

Permissions are passed as `resource=scope1,scope2` and sent to Keycloak as `resource#scope1,scope2`.

```sh
python pykc.py --realm otago_service uma perms \
  --access-token ${access_token} \
  --audience otago_proxy_service_client \
  --response-mode permissions \
  --permission-resource-format uri \
  --permissions /otago/roles=view \
  --permissions /otago/users=update,view
make run ARGS="--realm otago_service uma perms --access-token ${access_token} --audience otago_proxy_service_client --response-mode permissions --permission-resource-format uri --permissions /otago/roles=view --permissions /otago/users=update,view"
```

### Authz

#### Scopes

```sh
python pykc.py --realm otago_service authz.scopes all
make run ARGS="--realm otago_service authz.scopes all"
```

#### Policies

```sh
python pykc.py --realm otago_service authz.policies all
make run ARGS="--realm otago_service authz.policies all"
```

```sh
python pykc.py --realm otago_service authz.policies policy --policy-name my-policy
make run ARGS="--realm otago_service authz.policies policy --policy-name my-policy"
```

```sh
python pykc.py --realm otago_service authz.policies policy-auth-scopes --policy-id my-policy-id
make run ARGS="--realm otago_service authz.policies policy-auth-scopes --policy-id my-policy-id"
```

```sh
python pykc.py --realm otago_service authz.policies associated-roles --policy-id my-policy-id
make run ARGS="--realm otago_service authz.policies associated-roles --policy-id my-policy-id"
```

#### Resources

```sh
python pykc.py --realm otago_service authz.resources all
make run ARGS="--realm otago_service authz.resources all"
```

```sh
python pykc.py --realm otago_service authz.resources resource --resource-id my-resource-id
make run ARGS="--realm otago_service authz.resources resource --resource-id my-resource-id"
```

```sh
python pykc.py --realm otago_service authz.resources resource-permissions --resource-id my-resource-id
make run ARGS="--realm otago_service authz.resources resource-permissions --resource-id my-resource-id"
```

#### Permissions

```sh
python pykc.py --realm otago_service authz.permissions all
make run ARGS="--realm otago_service authz.permissions all"
```

```sh
python pykc.py --realm otago_service authz.permissions permission-on-resource --permission-id my-permission-id
make run ARGS="--realm otago_service authz.permissions permission-on-resource --permission-id my-permission-id"
```

```sh
python pykc.py --realm otago_service authz.permissions permission-on-scope --permission-id my-permission-id
make run ARGS="--realm otago_service authz.permissions permission-on-scope --permission-id my-permission-id"
```

#### Settings

```sh
python pykc.py --realm otago_service authz.settings all
make run ARGS="--realm otago_service authz.settings all"
```

### Roles

```sh
python pykc.py --realm otago_service roles roles
make run ARGS="--realm otago_service roles roles"
```

```sh
python pykc.py --realm otago_service roles role --role-name ${role_name}
make run ARGS="--realm otago_service roles role --role-name ${role_name}"
```

```sh
python pykc.py --realm otago_service roles create --name ${role_name} --description ${role_description}
make run ARGS="--realm otago_service roles create --name ${role_name} --description ${role_description}"
```

```sh
python pykc.py --realm otago_service roles update --role-name ${role_name} --role-description ${role_description}
make run ARGS="--realm otago_service roles update --role-name ${role_name} --role-description ${role_description}"
```

```sh
python pykc.py --realm otago_service roles delete-by-id --role-id ${role_id}
make run ARGS="--realm otago_service roles delete-by-id --role-id ${role_id}"
```

```sh
python pykc.py --realm otago_service roles delete-by-name --role-name ${role_name}
make run ARGS="--realm otago_service roles delete-by-name --role-name ${role_name}"
```

```sh
python pykc.py --realm otago_service roles user-roles --user-id ${user_id}
make run ARGS="--realm otago_service roles user-roles --user-id ${user_id}"
```

```sh
python pykc.py --realm otago_service roles user-composites-roles --user-id ${user_id}
make run ARGS="--realm otago_service roles user-composites-roles --user-id ${user_id}"
```

```sh
python pykc.py --realm otago_service roles user-available-roles --user-id ${user_id}
make run ARGS="--realm otago_service roles user-available-roles --user-id ${user_id}"
```

```sh
python pykc.py --realm otago_service roles assign --user-id ${user_id} --role-name ${role_name}
make run ARGS="--realm otago_service roles assign --user-id ${user_id} --role-name ${role_name}"
```

```sh
python pykc.py --realm otago_service roles unassign --user-id ${user_id} --role-name ${role_name}
make run ARGS="--realm otago_service roles unassign --user-id ${user_id} --role-name ${role_name}"
```
