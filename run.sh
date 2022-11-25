#!/usr/bin/env bash
echo 'Applying migrations...'
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --noinput --settings='i2amparis.settings'

echo "Run Gunicorn"

gunicorn --workers=4 --limit-request-line 0 -b 0.0.0.0:8000 i2amparis.wsgi:application
