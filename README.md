# FastAPI Template App

This is a basic FastAPI template app with Docker and Poetry support.

## Installation
```bash
poetry install
```

## Running Locally
```bash
poetry run uvicorn main:app --reload
```

## Formatting and Linting
```bash
poetry run black .
poetry run isort .
poetry run mypy .
```

## Docker
```bash
docker build -t fastapi-template-app .
docker run -p 8000:8000 fastapi-template-app
```
