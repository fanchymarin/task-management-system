#!/bin/bash

DUMP_FILE=dump.sql.postgres

# Run migrations
python manage.py makemigrations --noinput
python manage.py migrate
python manage.py dbshell < $DUMP_FILE

# Create users
python manage.py createsuperuser --noinput || true
python manage.py shell < create_users.py

# Start server
python manage.py runserver 0.0.0.0:8000
