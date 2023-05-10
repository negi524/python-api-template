main: log/ python_api_template/.env
	poetry run dev

test:
	poetry run pytest tests/

format:
	poetry run black python_api_template/ tests/

type-check:
	poetry run mypy python_api_template/
