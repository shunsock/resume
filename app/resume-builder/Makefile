.PHONY: all formatting linter static-analysis test report

all: formatting linter static-analysis test report

formatting:
	rye run isort src/resume_builder
	rye run black src/resume_builder

linter:
	rye run ruff check src/resume_builder

static-analysis:
	rye run mypy src/resume_builder

test:
	rye run coverage run -m pytest --durations=10

report:
	rye run coverage report -m