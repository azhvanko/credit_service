#!/usr/bin/env bash

set -Eeuo pipefail

# wait for postgres
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  echo "Postgres is unavailable - sleeping"
  sleep 0.5
done

echo "Postgres is up"

# make and migrate db migrations
python manage.py makemigrations
python manage.py migrate
# collect static files in ./static/
python manage.py collectstatic --noinput
# create superuser with default credentials (declared in .env)
python manage.py createsuperuser --noinput || true

exec "$@"
