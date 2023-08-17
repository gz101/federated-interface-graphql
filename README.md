# Federated Interface GraphQL-FastAPI App

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
