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

## Env

*optional usage*

Environment variables can be found as a list in .env and .env.local. It is NOT necessary TO USE ENVIRONMENT variables, as it is possible to initialize all components manually.

Located in .env|.env.local (according makefile)

To run the command it is possible to use just `python` OR `uv run` OR `make run`

- `sh bin/pykc.py`: Run the command using sh.
- `python pykc.py`: Run the command directly.
- `uv run pykc.py`: Run the command using uv.
- `make run`: Run the same with environment variables loaded from .env and .env.local. `(Dev mode)`


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

DATA_SANITIZER_EXTRA_SENSITIVE_KEYS=
DATA_SANITIZER_DEBUG=False
```

## Commands:

There are 2 ways how to run the commands:

1) Dev mode: to use .env | .env.local the easiest way to use `make run users all --realm otago`
2) For production way use `python pykc.py users all --realm otago`

### Users

```sh

python pykc.py users all --realm otago
make run ARGS="users all --realm otago"
```

```sh

python pykc.py users subset --limit 1 --offset 10 --fields=email_verified --exclude-fields='email id enabled username' --realm otago
make run ARGS="users subset --limit 1 --offset 10 --fields=email_verified --exclude-fields='email id enabled username' --realm otago"
```

```sh

python pykc.py users by-id --user_id=e33add52-05f8-4152-af17-a5815bfa6293 --realm otago
make run ARGS="users by-id --user_id=e33add52-05f8-4152-af17-a5815bfa6293 --realm otago"
```

```sh

python pykc.py users update-password --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago --pwd test
make run ARGS="users update-password --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago --pwd test"
```

```sh

python pykc.py users by-id --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago --fields enabled
make run ARGS="users by-id --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago --fields enabled"
```

```sh

python pykc.py users enable  --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago
make run ARGS="users enable  --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago"
```

```sh

python pykc.py users disable  --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago
make run ARGS="users disable  --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --realm otago"
```

```sh

python pykc.py users update --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --last-name 'hello' --first-name 'Kitty' --realm otago
make run ARGS="users update --user-id bcc23900-d840-47bd-aa4d-5e1e46646459 --last-name 'hello' --first-name 'Kitty' --realm otago"
```

```sh

python pykc.py users create --username 'cesar_the_third' --realm otago
make run ARGS="users create --username 'cesar_the_third' --realm otago"
```

### Clients

```sh

python pykc.py clients count --realm otago
make run ARGS="clients count --realm otago"
```

```sh

python pykc.py clients current --realm otago --fields 'name displayName'
make run ARGS="clients current --realm otago --fields 'name displayName'"
```

### Sessions

```sh

python pykc.py sessions stats  --realm otago
make run ARGS="sessions stats  --realm otago"
```

```sh

python pykc.py sessions delete-all --realm otago
make run ARGS="sessions delete-all --realm otago"
```

```sh

python pykc.py sessions delete-by-id --session-id e9c0a406-e9c0-72b7-8924-aedcd8e306e0  --realm otago
make run ARGS="sessions delete-by-id --session-id e9c0a406-e9c0-72b7-8924-aedcd8e306e0  --realm otago"
```

```sh

python pykc.py sessions stats  --realm otago --exclude-fields 'user_id useranme ip_address start remember_me'
make run ARGS="sessions stats  --realm otago --exclude-fields 'user_id useranme ip_address start remember_me'"
```

```sh

python pykc.py sessions user --realm otago --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c
make run ARGS="sessions user --realm otago --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c"
```

```sh

python pykc.py sessions offline  --realm otago --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c
make run ARGS="sessions offline  --realm otago --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c"
```

```sh

python pykc.py sessions delete_users_sessions  --realm otago --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c
make run ARGS="sessions delete_users_sessions  --realm otago --user-id b8b1a406-b8b1-78e6-a0e7-618f997aa57c"
```

### Auth

```sh

python pykc.py auth refresh --refresh-token ${refresh_token} --realm otago
make run ARGS="auth refresh --refresh-token ${refresh_token} --realm otago"
```

```sh

python pykc.py auth info --access-token ${access_token} --realm otago
make run ARGS="auth info --access-token ${access_token} --realm otago"
```

```sh

python pykc.py auth introspect-rtp --access-token ${access_token} --realm otago
make run ARGS="auth introspect-rtp --access-token ${access_token} --realm otago"
```

```sh

python pykc.py auth introspect-token --access-token ${access_token} --realm otago
make run ARGS="auth introspect-token --access-token ${access_token} --realm otago"
```


```sh

python pykc.py auth certs  --realm otago
make run ARGS="auth certs  --realm otago"
```

```sh

python pykc.py auth login --username=admin --password=password --realm otago"
make run ARGS="auth login --username=admin --password=password --realm otago"
```


```sh

python pykc.py auth revoke --refresh-token=${__CLI_REFRESH} --realm otago
make run ARGS="auth revoke --refresh-token=${__CLI_REFRESH} --realm otago"
```


### UMA

```sh


python pykc.py uma perms --realm otago --access-token 'access-token' --response-mode permissions --permission-resource-format uri --permissions /otago/roles=view"
make run ARGS="uma perms --realm otago --access-token 'access-token' --response-mode permissions --permission-resource-format uri --permissions /otago/roles=view"
```

### Authz

#### Scopes

```sh
python pykc.py authz.scopes all --realm otago
make run ARGS="authz.scopes all --realm otago"
```

#### Policies

```sh
python pykc.py authz.policies all --realm otago
make run ARGS="authz.policies all --realm otago"
```

```sh
python pykc.py authz.policies policy --realm otago --policy-name my-policy
make run ARGS="authz.policies policy --realm otago --policy-name my-policy"
```

```sh
python pykc.py authz.policies policy-auth-scopes --realm otago --policy-id my-policy-id
make run ARGS="authz.policies policy-auth-scopes --realm otago --policy-id my-policy-id"
```

```sh
python pykc.py authz.policies associated-roles --realm otago --policy-id my-policy-id
make run ARGS="authz.policies associated-roles --realm otago --policy-id my-policy-id"
```

#### Resources

```sh
python pykc.py authz.resources all --realm otago
make run ARGS="authz.resources all --realm otago"
```

```sh
python pykc.py authz.resources resource --realm otago --resource-id my-resource-id
make run ARGS="authz.resources resource --realm otago --resource-id my-resource-id"
```

```sh
python pykc.py authz.resources resource-permissions --realm otago --resource-id my-resource-id
make run ARGS="authz.resources resource-permissions --realm otago --resource-id my-resource-id"
```

#### Permissions

```sh
python pykc.py authz.permissions all --realm otago
make run ARGS="authz.permissions all --realm otago"
```

```sh
python pykc.py authz.permissions permission-on-resource --realm otago --permission-id my-permission-id
make run ARGS="authz.permissions permission-on-resource --realm otago --permission-id my-permission-id"
```

```sh
python pykc.py authz.permissions permission-on-scope --realm otago --permission-id my-permission-id
make run ARGS="authz.permissions permission-on-scope --realm otago --permission-id my-permission-id"
```

#### Settings

```sh
python pykc.py authz settings all --realm otago
make run ARGS="authz.settings all --realm otago"
```


### Roles

```sh

 python pykc.py roles roles --realm otago
```

```sh

 python pykc.py roles roles --realm otago --role-name ${role_name}
```

```sh

 python pykc.py roles create --realm otago --role-name ${role_name} --description ${role_description}
```

```sh

 python pykc.py roles roles --realm otago --role-name ${role_name}
```

```sh

 python pykc.py roles update --realm otago --role-name ${role_name} --role-description ${role_description}
```

```sh

 python pykc.py roles delete-by-id --realm otago --role-id ${role_id}
```

```sh

 python pykc.py roles delete-by-name --realm otago --role-name ${role_name}
```

```sh

 python pykc.py roles user-roles --realm otago --user-id ${user_id}
```

```sh

 python pykc.py roles user-composites-roles --realm otago --user-id ${user_id}
```

```sh

 python pykc.py roles user-available-roles --realm otago --user-id ${user_id}
```


```sh

 python pykc.py roles assign --realm otago --user-id ${user_id} --role-name ${role_name}
```

```sh

 python pykc.py roles unassign --realm otago --user-id ${user_id} --role-name ${role_name}
```
