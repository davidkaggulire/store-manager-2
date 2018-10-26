"""sales_views.py"""

from flask import jsonify, request, make_response
from api import app
from api.models.user import User
from api.models.admin import Admin
from api.models.attendant import Attendant
from api.models.sales import Sales
from api.views.product_views import PRODUCT_LIST

SALES_LIST = [
        {
                "attendant_id": 1,
                "category": "guitars",
                "price": 700000,
                "product_name": "guitar",
                "quantity": 1,
                "sale_id": 2
        },
        {
                "attendant_id": 1,
                "category": "keyboards",
                "price": 1000000,
                "product_name": "piano",
                "quantity": 1,
                "sale_id": 1
        }
]

USER = User(1, username='attendant')
ADMIN_USER = Admin(1,username='admin')
ATTENDANT_USER = Attendant(1, 'attendant')

@app.route('/api/v1/sales', methods=['POST'])
def post_sales():
    """
    route to add a new sale
    """
    try:
        form_data = request.get_json(force=True)
        product_name = form_data['product_name']
        quantity = form_data['quantity']
        price = form_data['price']
        sale_id = len(SALES_LIST) + 1

        new_sale = Sales(sale_id=sale_id, product_name=product_name, quantity=quantity, price=price)
        attendant_id = ATTENDANT_USER.user_id
        valid_sale = new_sale.validate_sale()
        if product_name != '' and quantity != '' and price != '':
                if valid_sale is True:
                        save_sale = ATTENDANT_USER.add_sale(new_sale.sale_id, new_sale.quantity, new_sale.price, PRODUCT_LIST, SALES_LIST, attendant_id, new_sale.product_name)
                        if save_sale:
                                return make_response(jsonify({'message': save_sale}), 201)
                        else:
                                return make_response(jsonify({'message': 'Product not in store'}), 404)
                return valid_sale 
        else:
                return jsonify({'error': 'field missing'}), 400

    except Exception:
        return jsonify({'error': 'field missing'}), 400
      
@app.route('/api/v1/sales')
def get_all_sales():
    """route to retrieve all sales"""    
    get_sales = ADMIN_USER.get_all_sales(SALES_LIST)
    if get_sales:
        return make_response(jsonify(get_sales), 200)

@app.route('/api/v1/sales/<int:sale_id>')
def get_specific_sale(sale_id):
    """
    route to get specific sale.
    """
    specific_sale = User.get_single_sale(sale_id, ADMIN_USER.admin_status, USER.user_id, SALES_LIST)
    if specific_sale:
        return specific_sale  

@app.route('/api/v1/sales/<int:sale_id>', methods=['POST'])
def post_specific_sale(sale_id):
    """route to handle post sale to api"""
    if sale_id:
        return make_response(jsonify({'message': 'Unallowed route'}), 400)
