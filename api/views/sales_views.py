"""sales_views.py"""

from flask import jsonify, request, make_response
from api import app
from api.models.user import User
from api.models.admin import Admin
from api.models.attendant import Attendant
from api.views.product_views import PRODUCT_LIST

SALES_LIST = [
        {
                "attendant_id": 1,
                "category": "guitars",
                "price": 500000,
                "product_id": 2,
                "product_name": "guitar",
                "quantity": 10,
                "sale_id": 2
        },
        {
                "attendant_id": 1,
                "category": "keyboards",
                "price": 30000,
                "product_id": 1,
                "product_name": "piano",
                "quantity": 10,
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
    form_data = request.get_json(force=True)
    product_name = form_data['product_name']
    sale_id = len(SALES_LIST) + 1

    attendant_id = ATTENDANT_USER.user_id

    if product_name != "":
        save_sale = ATTENDANT_USER.add_sale(sale_id, PRODUCT_LIST, SALES_LIST, attendant_id, product_name)
        if save_sale:
            return make_response(jsonify({'message': save_sale}), 201)
        else:
            return make_response(jsonify({'message': 'Product not in store'}), 404)
    else:
        return make_response(jsonify({'message': 'Product name missing'}), 400)

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
