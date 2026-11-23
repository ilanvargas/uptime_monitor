
dev:

lint:
	cd app && uv run ruff check
	cd app && uv run ruff format --check

test:
	cd app && uv run pytest

.PHONY: dev lint test
