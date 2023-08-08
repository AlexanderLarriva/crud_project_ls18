install:
	poetry install

start1:
	poetry run flask --app crud_project_ls18.app:app run

start-debug:
	poetry run flask --app crud_project_ls18.app --debug run --port 8000

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) crud_project_ls18.app:app
# poetry run gunicorn --workers=4 --bind=127.0.0.1:8000 crud_project_ls18.app:app

test:
	poetry run flake8 .
	poetry run pytest