.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo
	@echo "Targets:"
	@echo "  help    This help (default target)"
	@echo "  format  Format source code"
	@echo "  lint    Run lint checks"
	@echo "  test    Run tests"

.PHONY: format
format:	\
	format-isort \
	format-black

.PHONY: format-isort
format-isort:
	pipenv run isort --profile=black .

.PHONY: format-black
format-black:
	pipenv run black --line-length 100 .

.PHONY: lint
lint: \
	lint-isort \
	lint-black \
	lint-flake8 \
	lint-mypy

.PHONY: lint-isort
lint-isort:
	pipenv run isort --profile=black --check-only --diff .

.PHONY: lint-black
lint-black:
	pipenv run black --check --line-length 100 --diff .

.PHONY: lint-flake8
flake8:
	pipenv run flake8 --max-line-length 100 .

.PHONY: lint-mypy
lint-mypy:
	pipenv run mypy .

.PHONY: test
test:
	pipenv run pytest

.PHONY: run
run:
	pipenv run python run_scam_algo.py