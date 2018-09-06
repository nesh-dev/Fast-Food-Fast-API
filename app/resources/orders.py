
from flask_restful import Resource, reqparse
from app.models import orders

class OrderListResource(Resource):
	def get(self): 
		return {'orders':orders}
	def post(self):
                inc_id = len(orders) + 1
                parser = reqparse.RequestParser()
                parser.add_argument("food",type=str,
                required=True)
                parser.add_argument("quantity",type=int,
                required=True)
                parser.add_argument("price",type=int,
                required=True)
                parser.add_argument("status",type=str,
                required=True)
                data = parser.parse_args()
                order = {
                'id': inc_id, 'food':data['food'],
                'quantity':data['quantity'],'price':data['price'],
                'status':data['status'] 
                }
                orders.append(order)
                return order, 201

class OrderResource(Resource): 
    
    def get(self,id):
        order = {'order': next(filter(lambda x:x['id'] == id, orders), None)}
        return order

    