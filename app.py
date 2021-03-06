from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from datetime import timedelta
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, Stores
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret'
api = Api(app)

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth endpoint
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

api.add_resource(Store, "/stores/<int:id>")
api.add_resource(Stores, "/stores")
api.add_resource(Item, "/items/<int:id>")
api.add_resource(Items, "/items")
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
