setup:
	git clone git@github.com:berrondo/ca.git ca
	cd ca
	python -m venv env
	source env/bin/activate
	pip install -r requirements-dev.txt
	cp contrib/env_sample .env
	python manage.py migrate
	python manage.py createsuperuser --username admin --email a@a.com --no-input
	python manage.py test
	python manage.py runserver 0.0.0.0:8080

s: setup

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