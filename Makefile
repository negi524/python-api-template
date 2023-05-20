main: log/ python_api_template/.env
	poetry run uvicorn python_api_template.main:app --reload

test:
	poetry run pytest tests/

format:
	poetry run black python_api_template/ tests/

type-check:
	poetry run mypy -p python_api_template
