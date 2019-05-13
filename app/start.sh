#!/bin/bash

# Setup application
python manage.py makemigrations
python manage.py migrate
python manage.py check
python manage.py collectstatic --no-input

# Start Gunicorn processes
exec gunicorn \
    --bind ":8000" \
    --workers "$GUNICORN_WORKER_THREADS" \
    --log-level "info" \
    --timeout "3600" \
    --error-logfile "-" \
    --access-logfile "-" \
    lab.wsgi:application