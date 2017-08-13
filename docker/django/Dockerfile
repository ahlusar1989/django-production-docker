FROM python:3.4.3

ENV PYTHONUNBUFFERED 1

COPY ./docker/django/django-entrypoint.sh /
COPY ./requirements /django/requirements

WORKDIR /django

RUN pip install pip==9.0.1
RUN pip install -r requirements/local.txt
