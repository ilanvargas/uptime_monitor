
dev:

lint:
	cd app && uv run ruff check --fix
	cd app && uv run ruff format

test:
	cd app && uv run pytest tests/

.PHONY: dev lint test
