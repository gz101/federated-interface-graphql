# Federated Interface GraphQL-FastAPI App

Simple app to try out federated interface types in Apollo Federation GraphQL and FastAPI using Ariadne.

## Install the app
```sh
pip install -r requirements.txt
```

## Run the app
```sh
uvicorn profile_service.main:app --reload
```

## Clear pycache
```sh
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
```

## Setup database
```sh
python -m profile_service.database.setup
```
