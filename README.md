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

## APP REST API

This project provides a simple Item Store schema to exercise JWT and the SQLAlchemy ORM.

**Model Entities**

- Users: Stand-Alone for Auth to API only
- Stores to Item: 1-to-Many, lazy loading

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
