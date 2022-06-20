# Flask with uWSGi behind Nginx: All Dockerized with Docker Compose

This repo is can be used as a starter project to stand-up a Flask REST API integrated with the uWSGI application server. This can be run locally with the use of Docker containers and Docker Compose.

Features:

- Utilizes Flask, Flask-RESTful, Flask-JWT, SQLAlchemy
- Basic REST API for a store having simple items
- SQLAlchemy ORM integrationwith simple SQLite DB
- Basic example of JWT protection around the REST API, simple User model
- Nginx reverse proxy in front of uWSGI
- Starter ini and conf files for uWSGI and Nginx
- Just works

## How to Run

```shell
# Have Docker installed already
git clone https://github.com/bobbrady/flask-uwsgi-nginx-dockerized.git
cd flask-uwsgi-nginx-dockerized.git
docker-compose up
# Test API with cURL or Postman
```
