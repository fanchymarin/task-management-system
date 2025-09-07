#!/bin/bash

DUMP_FILE=dump.sql.postgres

# Run migrations
python manage.py makemigrations --noinput
python manage.py migrate

# Load initial data
python manage.py dbshell < $DUMP_FILE

# Start server
python manage.py runserver 0.0.0.0:8000
