from turtle import up
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel

parser = reqparse.RequestParser()

parser.add_argument('name',
                    type=str,
                    required=True,
                    help='This field cannot be left blank!'
                    )
parser.add_argument('price',
                    type=float,
                    required=True,
                    help='This field cannot be left blank!'
                    )
parser.add_argument('store_id',
                    type=int,
                    required=True,
                    help='Every item needs to be associated with a store'
                    )


class Item(Resource):
    @jwt_required()
    def get(self, id):
        item = ItemModel.find_by_id(id)
        if item:
            return item.json()
        return {'message': f"Item with id {id} was not found"}, 404

    def delete(self, id):
        item = ItemModel.find_by_id(id)
        if item:
            item.delete()
            return {'message': f"Item {id} deleted"}
        return {'message': f"Item with id {id} was not found"}, 404

    def put(self, id):
        data = parser.parse_args()
        print(f"put Item data: {data}")

        item = ItemModel.find_by_id(id)

        if item is None:
            item = ItemModel(data['name'], data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.upsert()

        return item.json()


class Items(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}

    def post(self):
        data = parser.parse_args()

        if ItemModel.find_by_name(data['name']):
            return {'message': f"An item with name {data['name']} already exists"}, 400

        item = ItemModel(data['name'], data['price'], data['store_id'])

        item.upsert()

        return item.json(), 201
