start:
	poetry run flask --app crud_project_ls18.app:app run

start-debug:
	poetry run flask --app crud_project_ls18.app --debug run --port 8000

start-guni:
	poetry run gunicorn --workers=4 --bind=127.0.0.1:8000 crud_project_ls18.app:app

test:
	poetry run flake8 .
	poetry run pytest