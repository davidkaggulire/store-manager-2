"""product_views.py"""

from flask import jsonify, request, make_response
from api import app
from api.models.products import Products
from api.models.user import User
from api.models.admin import Admin
from api.models.attendant import Attendant

PRODUCT_LIST = [
    {
        "product_name": "guitar",
        "category": "guitars",
        "price": 500000,
        "quantity": 10,
        "minimum_quantity": 2,
        "product_id": 2
    },
    {
        "product_name": "piano",
        "category": "keyboards",
        "price": 1000000,
        "quantity": 10,
        "minimum_quantity": 3,
        "product_id": 1
    }
]

USER = User(1, username='attendant')
ADMIN_USER = Admin(1, username='admin')
ATTENDANT_USER = Attendant(1, 'attendant')

@app.route('/')
def home():
    """Home route"""
    return make_response(jsonify({'message':'Welcome to Store Manager'}), 200)

@app.route('/api/v1/products', methods=['POST'])
def post_products():
    """
    method to handle post and get requests
    """
    try:
        product_id = len(PRODUCT_LIST) + 1
        form_data = request.get_json(force=True)
        product_name = form_data['product_name']
        category = form_data['category']
        price = form_data['price']
        quantity = form_data['quantity']
        minimum_quantity = form_data['minimum_quantity']
    
        product = Products(product_id=product_id, product_name=product_name, category=category,
        price=price, quantity=quantity, minimum_quantity=minimum_quantity)
        valid_product = product.validate_product()

        if valid_product == True:
            new_post = Admin.add_product(product, PRODUCT_LIST)
            return make_response(jsonify({"message": new_post}), 201)
        return valid_product
    except KeyError:
        return make_response(jsonify({'message': 'Missing input field'}), 400)
    
@app.route('/api/v1/products')
def get_products():
    """route to return all products"""
    new_get = Admin.get_products(PRODUCT_LIST)
    return new_get

@app.route('/api/v1/products/<int:product_id>')     
def get_product(product_id):
    """
    route to get specific product by Id
    """
    specific_product = Attendant.get_specific_product(product_id, PRODUCT_LIST)
    if specific_product:
        return specific_product

@app.route('/api/v1/products/<int:product_id>', methods=['POST'])
def post_product(product_id):
    """route to post a product to an Id"""
    return make_response(jsonify({'message': 'Unallowed route'}), 400)

@app.route('/api/v1/products/', methods=['POST'])
def post_wrong_url_products():
    """route to handle wrong url on post"""
    return make_response(jsonify({'message': 'Unallowed route'}), 400)
