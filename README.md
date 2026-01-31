```sh

 make run ARGS="users all --realm otago"
```

```sh

make run ARGS="users subset --limit 1 --offset 10 --fields=email_verified --exclude-fields='email id enabled username' --realm otago"
```

```sh

 make run ARGS="users by-id --user_id=e33add52-05f8-4152-af17-a5815bfa6293 --realm otago"
```
