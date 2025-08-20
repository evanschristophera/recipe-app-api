# recipe-app-api
Recipe API project

## Linting

```
docker-compose run --rm app sh -c "flake8"
```

## Testing
- Django test suite
- Setup test per Django app
- Run tests through Docker Compose

```
docker compose run --rm app sh -c "python manage.py test"
```

## Create Project
```
    docker compose run --rm app sh -c "django-admin startproject app . "
```

## Progress

[Wed Aug 20 11:28:16 CDT 2025](https://www.udemy.com/course/django-python-advanced/learn/lecture/32238754#notes)