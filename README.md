# django-production-docker

Generic Dockerized REST Services for building other Microservices and React client

**Overview of App Architecture?**
* Django App, api, listens on port 8000 and manages user sessions
* Postgres DB listens on port 5432

## To Get Up and Running

* `$ git clone https://github.com/ahlusar1989/django-production-docker.git`
* `$ cd django-production-docker`

## Installation

* `$ docker-compose build`

## Start development

* `$ docker-compose up`
* browse to `localhost:8000` for testing out routes and API

## Stopping

To stop all Docker containers

* `$ docker-compose stop`

## Resetting

Stop Docker development server and remove containers, networks, volumes, and images created by initial build and initialization.

* `$ docker-compose down`

### Accessing a container

You can access shell in a container

* `$ docker exec -i -t <CONTAINER_NAME_OR_ID> /bin/bash`
