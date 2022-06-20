# Flask with uWSGi behind Nginx: All Dockerized with Docker Compose

This repo can be used as a starter project to stand-up a Flask REST API. It is integrated with the uWSGI application server. This can be run locally on a laptop with the use of Docker containers and Docker Compose. Deploying with Docker containers prevents the laptop system from being "polluted" with the required dependencies of the project.

Features:

- Utilizes Flask, Flask-RESTful, Flask-JWT, SQLAlchemy
- Basic REST API for a store having a simple inventory of items
- SQLAlchemy ORM integration with a SQLite DB
- Basic example of JWT authentication protection around the REST API, simple User model
- Nginx reverse proxy in front of the uWSGI app server
- Starter ini and conf files for uWSGI and Nginx
- Just works: clone repo and run `docker-compose up`

## How to Run

```shell
# Have Docker installed already
git clone https://github.com/bobbrady/flask-uwsgi-nginx-dockerized.git
cd flask-uwsgi-nginx-dockerized.git
docker-compose up
# Test API with cURL or Postman
```

## APP REST API

This project provides a simple Item Store schema to exercise JWT and the SQLAlchemy ORM.

**Model Entities**

- User: Stand-Alone for Auth to API only
- Store to Item: 1-to-Many, Lazy Loading

### Users and JWT

```shell
# Create a user
POST /register
{
    "username": "fubar",
    "password": "asdf"
}
```

```shell
# Authenticate with JWT and get a token
POST /auth
{
    "username": "fubar",
    "password": "asdf"
}
```

## Stores

```shell
# Create a Store
POST /stores
{
    "name": "store_name"
}

# Get a list of all Stores
GET /stores

# output
{
    "stores": [
        {
            "id": 1,
            "name": "store_name",
            "items": [
                {
                    "id": 1,
                    "name": "item_name",
                    "price": 10.99,
                    "store_id": 1
                }
            ]
        }
    ]
}

# Get a Store by ID
GET /stores/<int:id>

#output
{
    "id": 1,
    "name": "store_name",
    "items": [
        {
            "id": 1,
            "name": "item_name",
            "price": 15.99,
            "store_id": 1
        }
    ]
}

# Delete a Store by ID
DELETE /stores/<int:id>

```

## Items

```shell
# Create an Item
POST /items
{
    "name": "item_name",
    "price": 15.99,
    "store_id": 1
}

# Get a list of all Items
GET /items

# output
{
    "items": [
        {
            "id": 1,
            "name": "item_name",
            "price": 15.99,
            "store_id": 1
        }
    ]
}

# Get an Item by ID
GET /items/<int:id>

#output
{
    "id": 1,
    "name": "item_name",
    "price": 15.99,
    "store_id": 1
}


# Update an Item by ID
PUT /items/<int:id>
{
    "name": "item_name",
    "price": 10.99,
    "store_id": 1
}


# Delete an Item by ID
DELETE /items/<int:id>
```
