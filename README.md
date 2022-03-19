# b2bit-mini-twitter

## Technologies

- [Python 3](https://www.python.org/);
- [Poetry](https://python-poetry.org/);
- [Django REST Framework](https://www.django-rest-framework.org/);
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/);

## Use cases

- CASE 1: User registration
  The actor registers in the system through the API. As a user, he must be able to register, so that he has access to Login. Use the fields you think are necessary for the user model definition.

- CASE 2: Authentication (Login)
  The actor must be authenticated in the system through a Token. As a user, he must be able to log in, so that he has access to the system. This token must have an expiration date.

- CASE 3: Make a publication
  The actor creates a post. This publication is persisted in the system. As a user, he must be able to create a publication, so that it can be seen by other users of the system.

- CASE 4: General feed
  The actor must receive, in JSON format, the feed of the last 10 posts.

## Env variables

Create a .env file on the project root folder, use example.env file as a base.

## Install dependencies

Before running the project, it is necessary to install the dependencies, to do that just run:

`$ poetry install`

## Start database

`$ docker-compose up -d`

## Run migrations

`$ poetry run python manage.py migrate`

## Run project

`$ poetry run python manage.py runserver`

## Run tests

`$ poetry run python manage.py test`
