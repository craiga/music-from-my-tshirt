# Music From My T-Shirt

[![CircleCI](https://img.shields.io/circleci/build/github/craiga/music-from-my-tshirt.svg)](https://app.circleci.com/github/craiga/music-from-my-tshirt/pipelines)

Share the music from your t-shirt!

## Running Web Site Locally

```
pipenv install
printf "DEBUG=1\n" > .env
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

## Running Tests and Code Quality Tools

```
pipenv install --dev
pipenv run isort --check-only
pipenv run black --check --diff .
find . -iname "*.py" | xargs pipenv run pylint
pipenv run pytest
```
