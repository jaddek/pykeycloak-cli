# ========================
# Environment config
# ========================
SHELL := /bin/bash

APP_ENV_FILES :=
DOCKER_ENV_FILES :=
ARGS?=

ifneq ($(wildcard .env),)
  APP_ENV_FILES += .env
endif

ifneq ($(wildcard .env.local),)
  APP_ENV_FILES += .env.local
endif

ifneq ($(wildcard .env.kc),)
  APP_ENV_FILES +=  .env.kc
endif

ENV_FILE_OPTION := $(foreach f,$(APP_ENV_FILES),--env-file $f)

UV_RUN := make set-python-version;\
	PYTHONPATH=src uv run

DC := docker compose
PYTHON_VER := $(shell tr -d '\n' < .python-version)
CURRENT_VER := $(shell python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')

define load_env
	set -a; \
	for f in $(APP_ENV_FILES); do \
		[ -f "$$f" ] && . "$$f"; \
	done; \
	set +a
endef


# ========================
# PHONY Targets
# ========================
.PHONY: default help install clean run tests \
        pre-commit pre-commit-install pre-commit-update \
        script-% set-python-version format lint typecheck \
        build-package check-package publish-testpypi publish-pypi

default: help


# ========================
# Help
# ========================
help:
	@echo ""
	@echo "📦 Project Makefile Commands:"
	@echo "---------------------------------------------"
	@awk 'BEGIN {FS = ":.*?#"} /^[a-zA-Z_-]+:.*?#/ { printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

# ========================
# Project Setup
# ========================
install: ## Install dependencies and pre-commit hooks
	@make set-python-version
	@uv sync
	@uv run pre-commit install

clean: ## Remove .pyc files and pre-commit cache
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -exec rm -r {} +
	@uv run pre-commit clean

# ========================
# Run App
# ========================
run: ## Run app
	@$(load_env); $(UV_RUN) pykc.py $(ARGS)

# ========================
# Formatting & Linting
# ========================
format: ## Format code using Black and Ruff
	@uv run pre-commit run ruff-format --all-files
	@uv run pre-commit run ruff-check --all-files

lint: ## Lint code using Ruff
	@uv run pre-commit run ruff-check --all-files

typecheck: ## Type-check code using ty
	@$(load_env); $(UV_RUN) ty check src

# ========================
# Pre-commit
# ========================
pre-commit: ## Run all pre-commit hooks
	@uv run pre-commit run --all-files

pre-commit-install: ## Install pre-commit hooks
	@uv run pre-commit install

pre-commit-update: ## Update pre-commit hooks
	@uv run pre-commit autoupdate

# ========================
# Tests
# ========================
tests: ## Run all tests
	@$(load_env); $(UV_RUN) pytest tests -vv -s

test-unit: ## Run unit tests
	@$(load_env); $(UV_RUN) pytest tests/unit -vv -s

test-integration: ## Run integration tests
	@$(load_env); $(UV_RUN) pytest tests/integration -vv -s

test-functional: ## Run functional tests
	@$(load_env); $(UV_RUN) pytest tests/functional -vv -s

test-with-coverage: ## Run all tests with coverage
	@$(load_env); $(UV_RUN) pytest tests --cov=src --cov-report=html --cov-report=term -vv -s

build-package: ## Build sdist and wheel into dist/
	@uv build

check-package: build-package ## Validate built artifacts metadata
	@uvx twine check dist/*

publish-testpypi: check-package ## Upload package to TestPyPI (TWINE_USERNAME/TWINE_PASSWORD required)
	@uvx twine upload --repository testpypi dist/*

publish-pypi: check-package ## Upload package to PyPI (TWINE_USERNAME/TWINE_PASSWORD required)
	@uvx twine upload dist/*


release-bump: ## Sync pyproject version from GITHUB_REF_NAME (vX.Y.Z)
	@python3 bin/sync_version_from_tag.py

release-bump-tag: ## Sync pyproject version from TAG=vX.Y.Z
	@if [ -z "$(TAG)" ]; then \
		echo "TAG is required. Example: make release-bump-tag TAG=v0.7.4"; \
		exit 1; \
	fi
	@python3 bin/sync_version_from_tag.py --tag "$(TAG)"



# =========
# Helpers
# ==========

set-python-version:
	@if [ "$(CURRENT_VER)" != "$(PYTHON_VER)" ]; then \
	  	uv python pin $(PYTHON_VER); \
	 fi
