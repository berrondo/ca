tests:
	python manage.py test

test: tests

t: tests

run:
	python manage.py runserver

r: run

migrate:
	python manage.py migrate

makemi:
	python manage.py makemigrations