# PyKeycloak CLI

The small library cli based on [pykeycloak](https://github.com/jaddek/pykeycloak) and Typer

## Env

Located in .env|.env.local (according makefile)

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
