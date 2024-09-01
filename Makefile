all:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

mk:
	python manage.py makemigrations

migrate:
	python manage.py migrate

server:
	python manage.py runserver