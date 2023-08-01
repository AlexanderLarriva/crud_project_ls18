start:
	poetry run flask --app crud_create_flask_3107.app:app run

start-debug:
	poetry run flask --app crud_create_flask_3107.app --debug run --port 8000

test:
	poetry run flake8 .
	poetry run pytest