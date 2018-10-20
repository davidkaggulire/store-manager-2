"""product_views.py"""

from api import app
from flask import jsonify, request, make_response
from api.models.products import Products
from api.models.user import User
from api.models.admin import Admin
from api.models.attendant import Attendant

PRODUCT_LIST = []

user = User(1, username='attendant')
admin_user = Admin(1,username='admin')
attendant_user = Attendant(1, 'attendant')

@app.route('/')
def home():
    """Home route"""
    return "Welcome to Store Manager"

@app.route('/api/v1/products', methods = ['GET', 'POST'])
def post_products():
    """
    method to handle post and get requests
    """
    if request.method == 'POST':
        product_id = len(PRODUCT_LIST) + 1
        form_data = request.get_json(force=True)
        product_name = form_data['product_name']
        category = form_data['category']
        price = form_data['price']
        quantity = form_data['quantity']
        minimum_quantity = form_data['minimum_quantity']

        if product_name != "" and category != "" and price != "" and quantity != "" and minimum_quantity != "" :
            product = Products(product_id=product_id, product_name=product_name, category=category,
        price=price, quantity=quantity, minimum_quantity=minimum_quantity)
            new_post = Admin.add_product(product, PRODUCT_LIST)
            return make_response(jsonify({"message": new_post}), 201)
        else:
            return make_response(jsonify({'message': 'Missing input fields'}), 406)

    elif request.method == 'GET':
        new_get = Admin.get_products(PRODUCT_LIST)
        return make_response(jsonify(new_get), 200)

@app.route('/api/v1/products/<int:product_id>', methods=['GET', 'POST'])     
def get_product(product_id):
    """
    route to get specific product by Id
    """
    if request.method == 'GET':
        specific_product = Attendant.get_specific_product(product_id, PRODUCT_LIST)
        if specific_product:
            return make_response(jsonify(specific_product), 200)
        else:
            return make_response(jsonify({'message': 'Product not found'}), 404)

    elif request.method == 'POST':
        return make_response(jsonify({'message': 'Unallowed route'}), 405)