#!/usr/bin/env bash

do
    echo "Waiting for django volume..."
done

until python manage.py migrate --settings=config.settings.local
do
    echo "Waiting for postgres ready..."
    sleep 2
done

python manage.py runserver 0.0.0.0:8000 --settings=config.settings.local
