# Federated Interface GraphQL-FastAPI App

Simple app to try out federated interface types in Apollo Federation GraphQL and FastAPI using Ariadne.

## Install the app
```sh
pip install -r requirements.txt
```

## Setup database

Note that the DB initialization also populates the database with seed data.

For the profile-service app:

```sh
python -m profile_service.database.setup
```

For the content-service app:

```sh
python -m content_service.database.setup
```

## Run the app

For the profile-service app:

```sh
uvicorn profile_service.main:app --reload --host 127.0.0.1 --port 8000
```

For the content-service app:

```sh
uvicorn content_service.main:app --reload --host 127.0.0.1 --port 8001
```

## Clear pycache
```sh
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
```
