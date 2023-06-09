SHELL = /bin/bash
ENV ?= development
API_CONTAINER_NAME := credit_service_api_$(ENV)
DB_CONTAINER_NAME := credit_service_postgres_$(ENV)

.PHONY: run test clean api_container db_container makemigrations migrate

run:
	docker-compose --env-file ./.env up --build

test:
	poetry run pytest

clean:
	docker-compose --env-file ./.env down -v --rmi all

# shortcuts
api_container:
	docker exec -it $(API_CONTAINER_NAME) $(SHELL)

db_container:
	docker exec -it $(DB_CONTAINER_NAME) $(SHELL)

makemigrations:
	docker exec -it $(API_CONTAINER_NAME) $(SHELL) -c "python manage.py makemigrations"

migrate:
	docker exec -it $(API_CONTAINER_NAME) $(SHELL) -c "python manage.py migrate"
