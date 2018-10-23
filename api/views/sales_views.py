from api import app
from flask import jsonify, request, make_response
from api.models.products import Products
from api.models.sales import Sales
from api.models.user import User
from api.models.admin import Admin
from api.models.attendant import Attendant
from api.views.product_views import PRODUCT_LIST

SALES_LIST = []

user = User(1, username='attendant')
admin_user = Admin(1,username='admin')
attendant_user = Attendant(1, 'attendant')

@app.route('/api/v1/sales', methods=['POST'])
def post_sales():
    """
    route to add a new sale
    """
    form_data = request.get_json(force=True)
    product_name = form_data['product_name']
    sale_id = len(SALES_LIST) + 1

    attendant_id = attendant_user.user_id

    if product_name != "":
        save_sale = attendant_user.add_sale(sale_id, PRODUCT_LIST, SALES_LIST,attendant_id, product_name)
        if save_sale:
            return make_response(jsonify({'message': save_sale}), 201)
        else:
            return make_response(jsonify({'message': 'Product not in store'}), 404)
    else:
        return make_response(jsonify({'message': 'Product name missing'}), 400)

@app.route('/api/v1/sales')
def get_sales():            
    get_sales = admin_user.get_all_sales(SALES_LIST)
    if get_sales:
        return make_response(jsonify(get_sales), 200)

@app.route('/api/v1/sales/<int:sale_id>')
def get_specific_sale(sale_id):
    """
    route to get specific sale.
    """
    specific_sale = User.get_single_sale(sale_id, admin_user.admin_status, user.user_id, SALES_LIST)
    if specific_sale:
        return make_response(jsonify(specific_sale), 200)
    
@app.route('/api/v1/sales/<int:sale_id>', methods=['POST'])
def post_specific_sale(sale_id):    
    if sale_id:
        return make_response(jsonify({'message': 'Unallowed route'}), 400)