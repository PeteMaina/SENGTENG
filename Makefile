# Senteng Fashions - Makefile for automation

.PHONY: help build up down logs clean install-backend install-frontend test migrate seed

help: ## Show this help message
	@echo "Senteng Fashions - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Development
build: ## Build all Docker containers
	docker-compose build

up: ## Start all services
	docker-compose up -d
	@echo "🚀 Services started!"
	@echo "Frontend: http://localhost:3000"
	@echo "Backend API: http://localhost:8000"
	@echo "API Docs: http://localhost:8000/docs"
	@echo "MinIO Console: http://localhost:9001"

down: ## Stop all services
	docker-compose down

logs: ## View logs from all services
	docker-compose logs -f

logs-backend: ## View backend logs only
	docker-compose logs -f backend

logs-frontend: ## View frontend logs only
	docker-compose logs -f frontend

restart: ## Restart all services
	docker-compose restart

# Database
migrate: ## Run database migrations
	docker-compose exec backend alembic upgrade head

migrate-create: ## Create a new migration (use NAME=migration_name)
	docker-compose exec backend alembic revision --autogenerate -m "$(NAME)"

migrate-down: ## Rollback last migration
	docker-compose exec backend alembic downgrade -1

seed: ## Seed database with initial data
	docker-compose exec backend python scripts/seed_data.py

db-shell: ## Access PostgreSQL shell
	docker-compose exec db psql -U senteng -d senteng_db

# Testing
test-backend: ## Run backend tests
	docker-compose exec backend pytest

test-frontend: ## Run frontend tests
	docker-compose exec frontend npm test

test-all: ## Run all tests
	make test-backend
	make test-frontend

# Linting & Formatting
lint-backend: ## Lint backend code
	docker-compose exec backend ruff check .

format-backend: ## Format backend code
	docker-compose exec backend ruff format .

lint-frontend: ## Lint frontend code
	docker-compose exec frontend npm run lint

format-frontend: ## Format frontend code
	docker-compose exec frontend npm run format

# Installation
install-backend: ## Install backend dependencies
	cd backend && pip install -r requirements.txt

install-frontend: ## Install frontend dependencies
	cd frontend && npm install

# Cleanup
clean: ## Remove containers, volumes, and temp files
	docker-compose down -v
	@echo "Cleaned up all containers and volumes"

clean-all: clean ## Remove everything including images
	docker-compose down -v --rmi all
	@echo "Removed all containers, volumes, and images"

# Production
build-prod: ## Build production images
	docker-compose -f docker-compose.prod.yml build

deploy: ## Deploy to production (customize as needed)
	@echo "Deploying to production..."
	# Add your deployment commands here

# Development helpers
shell-backend: ## Access backend container shell
	docker-compose exec backend /bin/bash

shell-frontend: ## Access frontend container shell
	docker-compose exec frontend /bin/sh

shell-db: ## Access database container shell
	docker-compose exec db /bin/bash
