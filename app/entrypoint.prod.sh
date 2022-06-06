#!/bin/sh

# Waiting database started

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Apply database migrations

echo "Apply database migrations"

python manage.py migrate

# Collect static files

echo "Collect static files"

python manage.py collectstatic --noinput

exec "$@"