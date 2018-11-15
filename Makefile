test:
	poetry run pytest --cov=cleanser -q tests/

lint:
	poetry run pylint cleanser

mypy:
	poetry run mypy cleanser