# Makefile for Network Security Project

.PHONY: install test lint run clean docker-build docker-run help

help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies"
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting"
	@echo "  run          - Run the FastAPI application"
	@echo "  train        - Train the model"
	@echo "  clean        - Clean up generated files"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Run Docker container"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v

lint:
	flake8 networksecurity/ --max-line-length=120 --ignore=E402,E501,W503

run:
	python app.py

train:
	python main.py

push-data:
	python push_data.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf dist build .pytest_cache .coverage htmlcov

docker-build:
	docker build -t networksecurity:latest .

docker-run:
	docker run -p 8000:8000 --env-file .env networksecurity:latest

docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down

format:
	black networksecurity/ tests/
	isort networksecurity/ tests/
