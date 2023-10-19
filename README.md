## Create virtual env

python3 -m venv .venv

## Install packages
pip install -r requirements.txt

## Start django project
django-admin startproject music-beats

## Create app
django-admin startapp users

## Create superuser

- python manage.py migrate
- python manage.py createsuperuser

## Run server

python manage.py runserver
