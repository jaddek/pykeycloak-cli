# PyKeycloak CLI

This is a lightweight CLI library built on [Pykeycloak](https://github.com/jaddek/pykeycloak) and [Typer](https://github.com/fastapi/typer).


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

## Env

To run the command iti is possible to use just `uv run` OR `make run`

- `uv run cli.py`: Run the command directly.
- `make run`: Run the same with environment variables loaded from .env and .env.local. `(Dev mode)`


Located in .env|.env.local (according makefile)

```sh
KEYCLOAK_ACCESS_TOKEN=
KEYCLOAK_REALM_NAME=
KEYCLOAK_REALM_CLIENT_UUID=
KEYCLOAK_REALM_CLIENT_ID=
KEYCLOAK_REALM_CLIENT_SECRET=
KEYCLOAK_BASE_URL=
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
KEYCLOAK_MAX_ROWS_QUERY_LIMIT=1000 # = max=1000(=limit=1000)

KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_VERIFY=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_CERT=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_TRUST_ENV=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_HTTP1=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_HTTP2=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_RETRIES=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_PROXY=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_UDS=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_LOCAL_ADDRESSES=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_MAX_CONNECTIONS=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_KEEPALIVE_EXPIRY=
KEYCLOAK_HTTPX_HTTP_TRANSPORT_HTTP_MAX_KEEPALIVE_CONNECTIONS=
```

## Commands:

### Users

```sh

make run ARGS="users all --realm otago"
```

```sh

make run ARGS="users subset --limit 1 --offset 10 --fields=email_verified --exclude-fields='email id enabled username' --realm otago"
```

```sh

make run ARGS="users by-id --user_id=e33add52-05f8-4152-af17-a5815bfa6293 --realm otago"
```

```sh

make run ARGS="users update-password --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago --pwd test"
```

```sh

make run ARGS="users by-id --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago --fields enabled
```

```sh

make run ARGS="users enable  --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago"
```

```sh

make run ARGS="users disable  --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago"
```

```sh

make run ARGS="users update --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --last-name 'hello' --first-name 'Kitty' --realm otago"
```

```sh
make run ARGS="users create --username 'cesar_the_third' --realm otago"
```

### Clients

```sh

make run ARGS="clients count --realm otago"
```

```sh

make run ARGS="clients current --realm otago --fields 'name displayName'
```
