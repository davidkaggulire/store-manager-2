"""product_views.py"""

from flask import jsonify, request, make_response
from api import app
from api.models.models import Database

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
        form_data = request.get_json(force=True)
        product_name = form_data['product_name']
        category = form_data['category']
        price = form_data['price']
        quantity = form_data['quantity']
        minimum_quantity = form_data['minimum_quantity']
    
        if product_name != '' and category != '' and price != '' and quantity != '' and minimum_quantity != '':
            pass
        else:
            return make_response(jsonify({'message': 'Missing input field'}), 400)
    except Exception:
        return make_response(jsonify({'message': 'Wrong input format'}), 400)

    
@app.route('/api/v1/products')
def get_products():
    """route to return all products"""
    pass

@app.route('/api/v1/products/<int:product_id>')     
def get_product(product_id):
    """
    route to get specific product by Id
    """
    pass

@app.route('/api/v1/products/<int:product_id>', methods=['POST'])
def post_product(product_id):
    """route to post a product to an Id"""
    pass 

@app.route('/api/v1/products/', methods=['POST'])
def post_wrong_url_products():
    """route to handle wrong url on post"""
    pass
