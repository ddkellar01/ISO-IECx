.PHONY: help build up down test clean

help:
	@echo "Makefile commands for ISO-IECx:"
	@echo "  make build  - Build Docker containers"
	@echo "  make up     - Start docker-compose services"
	@echo "  make down   - Stop docker-compose services"
	@echo "  make test   - Run test suites"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

test:
	pytest -v tests/
