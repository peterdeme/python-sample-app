# FastAPI sample app

A sample Python webapp that intends to showcase best practises regarding:
- most importantly a great http server ([FastAPI](https://github.com/tiangolo/fastapi))
- project structure
- all-around asynchronous IO 
- config management
- dependency injection (provided by FastAPI)
- input validation (provided by FastAPI)
- unit and integration testing
- code style (flake8, isort)
- package management (Poetry)

# How to run the app

Clone the repo:
```shell
$ git clone https://github.com/peterdeme/python-sample-app.git
```
Install Poetry if you haven't already. This project requires 1.0 which is currently in beta as of November 2019.
```shell
$ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | POETRY_VERSION=1.0.0b4 python
```

Create your own configuration from the template:
```shell
$ cp .env-template .env
```

Setup the Postgresql connection string in `.env` file. The default connection string points to a local Dockerized instance which you can easily pull up with:
```shell
$ docker-compose up -d pgsql
```

Initialize the database schema:
```shell
$ poetry run alembic upgrade head
```

Finally, run the app:
```shell
$ poetry run python -m app.app
```

In another cmd window test if it works:
```shell
$ curl http://localhost:8000/api/v1/articles && echo
```

Or just open the above URL in a browser.

# Debug the app

Use the following interpeter in your IDE:

```shell
$ poetry run which python
```

Here's a sample debug config for VS Code users:

`.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch app",
            "type": "python",
            "request": "launch",
            "module": "app.app"
        }
    ]
}
```

# Production use case

In production you'll most probably want to run a webapp in Docker. This repository contains a Dockerfile which aims to be a good example for a production service. You can try it locally:
```shell
$ docker-compose up
```

As per the [official recommendation](https://fastapi.tiangolo.com/deployment/), the app uses [Gunicorn](https://pypi.org/project/gunicorn/) as a green "worker manager" which spawns [Uvicorn](https://www.uvicorn.org/) worker processes.

# Linting and testing

Type check:
```shell
$ poetry run mypy app --config-file tox.ini
```

Autofix flake8 issues with autopep8:
```shell
$ poetry run autopep8 -r -i .
```

Sort imports:
```shell
$ poetry run isort -rc .
```

Run tests:
```shell
$ poetry run pytest
```
