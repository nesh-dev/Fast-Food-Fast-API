
from flask_restful import Resource
from app.models import orders

class OrderListResource(Resource):
	"""
		return all the orders
	"""
	def get(self): 
		return {'orders':orders}

