.PHONY: all formatting linter static-analysis test report

all: formatting linter static-analysis test report

formatting:
	poetry run isort resumer tests
	poetry run black resumer tests

linter:
	poetry run ruff check resumer tests

static-analysis:
	poetry run mypy resumer

test:
	poetry run coverage run -m pytest -s --durations=10

report:
	poetry run coverage report -m