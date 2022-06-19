from flask_restful import Resource, reqparse
from models.store import StoreModel

parser = reqparse.RequestParser()

parser.add_argument('name',
                    type=str,
                    required=True,
                    help='This field cannot be left blank!'
                    )


class Store(Resource):

    def get(self, id):
        store = StoreModel.find_by_id(id)
        if store:
            return store.json()
        else:
            return {'message': f"Store with id {id} not found"}, 404

    def delete(self, id):
        store = StoreModel.find_by_id(id)
        if store:
            store.delete()
            return {'message': f"Store with id {store.id} has been deleted"}
        else:
            return {'message', f"Store with name {store.id} does not exist"}, 404


class Stores(Resource):

    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}

    def post(self):
        data = parser.parse_args()

        if StoreModel.find_by_name(data['name']):
            return {'message', f"A store with name {data['name']} already exists"}, 400
        else:
            store = StoreModel(data['name'])
            try:
                store.upsert()
            except:
                return {'message', f"Error while creating store with name {data['name']}"}, 500
            return store.json(), 201
