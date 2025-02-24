install:
	poetry install

format:
	poetry run black . && poetry run isort .

type-check:
	poetry run mypy .

lint:
	poetry run black --check . && poetry run isort --check .

run:
	poetry run uvicorn main:app --reload

docker-build:
	docker build -t fastapi-template-app .

docker-run:
	docker run -p 8000:8000 fastapi-template-app