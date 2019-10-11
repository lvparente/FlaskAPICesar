import sqlite3
from flask_restful import Resource, reqparse
from models.product import ProductModel

class Product(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('value',
		type=float,
		required=True,
		help="This field cannot be left blank!"
	)

	def get(self,code):
		product = ProductModel.find_by_code(code)

		if product:
			return product.json(), 200
		return {'message': 'Product not found'}, 404

	def post(self, code):

		if ProductModel.find_by_code(code):
			return {'message': "A product with code '{}' already exists.".format(code)}, 400
		
		data = Product.parser.parse_args()

		product = ProductModel(code, data["value"])

		try:
			product.save_to_db()
		except:
			return{"message": "An error ocorrued inserting the item."}, 500

		return product.json(), 201

class ProductList(Resource):
	def get(self):
		return {'products': [product.json() for product in ProductModel.query.all()]}, 200

